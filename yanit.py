#!/usr/bin/env python3
"""igloo Threads yanıt sistemi: Mac ya da tarayıcı olmadan, resmi Threads API'siyle yanıt turları.

İki tür aday vardır:
  takip  igloo'nun kendi gönderilerine ve yanıtlarına gelen yorumlar. Meta onayı beklemeden çalışır
         (token'da threads_read_replies izni olmalı). Başkalarının gönderilerinin altındaki yorumlar onaydan sonra gelir.
  arama  anahtar kelimelerle bulunan yeni sohbetler. Meta threads_keyword_search iznini onaylayana kadar arama
         yalnızca igloo'nun kendi gönderilerini döndürür, bu yüzden bu tür aday onaydan sonra gelir.

Akış (README › Günlük yanıt turları):
  1. Claude'un "igloo Threads yanıt turu" görevi yanitlar/.ara dosyasını push eder. "Threads yanıt araması" iş akışı
     `bul` komutunu çalıştırır: yorumları ve aramayı tarar, eler, kalan adayları Claude'un açık anahtarıyla şifreleyip
     yanitlar/adaylar.enc.json'a, özeti yanitlar/durum.json'a yazar. Başkalarının metinleri herkese açık depoda düz
     metin olarak durmaz.
  2. Claude `adaylar` ile listeyi çözer, yanitlar/YAZIM_REHBERI.md'ye göre yanıtları yazar, `ekle` ile denetleyip
     yanitlar/kararlar.json'a kaydeder ve push eder. "Threads yanıt gönderimi" iş akışı `gonder` komutunu çalıştırır:
     yanıtları günlük sınır içinde, birkaç dakika arayla paylaşır ve sonucu yanitlar/gonderilen.json'a yazar.

Komutlar:
  python3 yanit.py bul
  python3 yanit.py gonder
  python3 yanit.py adaylar --anahtar OZEL_ANAHTAR.pem
  python3 yanit.py ekle KARARLAR.json --anahtar OZEL_ANAHTAR.pem

Ortam değişkenleri: THREADS_TOKEN; DENEME=true ise bul/gonder hiçbir şey kaydetmez ve göndermez, yalnızca gösterir.
Yalnızca Python standart kütüphanesi ve openssl komutu kullanılır.
"""
import argparse
import base64
import json
import os
import random
import re
import secrets
import subprocess
import sys
import time
import unicodedata
from datetime import datetime, timedelta, timezone
from pathlib import Path

from bot import ROOT, TZ, api, publish, report_error, threads_len

DIR = ROOT / 'yanitlar'
AYAR = DIR / 'ayar.json'
ISTEK = DIR / '.ara'
DURUM = DIR / 'durum.json'
ADAYLAR = DIR / 'adaylar.enc.json'
KARARLAR = DIR / 'kararlar.json'
GONDERILEN = DIR / 'gonderilen.json'
ACIK_ANAHTAR = DIR / 'claude_acik_anahtar.pem'

ALANLAR = 'id,text,media_type,permalink,timestamp,username,has_replies,is_quote_post,is_reply'
YORUM_ALANLARI = 'id,text,username,timestamp,permalink,replied_to,hide_status'
GIZLI = {'HIDDEN', 'COVERED', 'BLOCKED', 'RESTRICTED'}
VARSAYILAN = {
    'acik': True,
    'marka': 'igloo',
    'anahtar_kelimeler': [],
    'limit_yeni': 25,             # her kelime için en yeni gönderiler (RECENT)
    'limit_populer': 10,          # her kelime için öne çıkan gönderiler (TOP)
    'en_eski_saat': 48,           # bundan eski gönderiler aday olmaz
    'en_fazla_aday': 30,
    'en_kisa_metin': 25,
    'yasak_kelimeler': [],        # aramada bulunan gönderiyi baştan eler (yorumlara uygulanmaz)
    'gunluk_limit': 10,           # yorum cevapları dahil günlük toplam
    'tur_basina_yanit': 4,        # Claude'un bir turda yazabileceği en fazla yeni sohbet yanıtı
    'takip_acik': True,
    'takip_tur_basina': 2,        # bir turda en fazla yorum cevabı
    'takip_gun': 3,               # bu kadar gün içindeki gönderi ve yanıtlarımıza gelen yorumlara bakılır
    'takip_en_eski_saat': 48,     # bundan eski yorumlara cevap yazılmaz
    'takip_en_fazla_aday': 15,
    'tur_basina_gonderim': 6,     # gönderim iş akışının bir çalışmada atabileceği en fazla yanıt
    'yazar_araligi_gun': 14,      # aynı kişiye en erken bu kadar gün sonra tekrar yeni sohbet yanıtı
    'bekleme_saniye': [60, 150],  # iki yanıt arası bekleme (saniye, rastgele)
    'en_kisa_yanit': 150,
    'en_kisa_takip': 40,
    'en_uzun_yanit': 480,
    'en_fazla_emoji': 1,
    'marka_kelimeleri': ['igloo'],                     # yeni sohbet yanıtlarında geçemez
    'izinli_eposta': 'iletisim@igloocollective.com',   # yalnızca yorum cevaplarında yazılabilir
    'yasak_kaliplar': [],         # küçük harfli metinde aranan düzenli ifadeler (satış çağrısı, oran, tutar...)
}
LINK = re.compile(r'https?://|www\.|\b[\w-]+\.(com|net|org|io|app|co|me|ly|gl|tr)\b', re.I)
OAEP = ['-pkeyopt', 'rsa_padding_mode:oaep', '-pkeyopt', 'rsa_oaep_md:sha256']
AES = ['-aes-256-cbc', '-pbkdf2', '-iter', '100000', '-a', '-A', '-pass', 'env:YANIT_PAROLA']


# ---------- yardımcılar ----------

def oku(path, default):
    try:
        return json.loads(Path(path).read_text(encoding='utf-8'))
    except FileNotFoundError:
        return default


def yaz(path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')


def ayarlar():
    return {**VARSAYILAN, **oku(AYAR, {})}


def env_dogru(ad):
    return os.environ.get(ad, '').strip().lower() in ('1', 'true', 'yes')


def simdi():
    return datetime.now(timezone.utc).replace(microsecond=0)


def iso(dt):
    return dt.astimezone(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')


def zaman(s):
    """Threads (2026-10-29T08:07:01+0000) ya da bizim (…Z) zaman damgası → datetime; okunamazsa None."""
    if not s:
        return None
    s = str(s).strip().replace('Z', '+00:00')
    if re.search(r'[+-]\d{4}$', s):
        s = s[:-2] + ':' + s[-2:]
    try:
        z = datetime.fromisoformat(s)
    except ValueError:
        return None
    return z if z.tzinfo else z.replace(tzinfo=timezone.utc)


def kucuk(s):
    """Türkçeye uygun küçük harf: I → ı, İ → i."""
    return (s or '').replace('I', 'ı').replace('İ', 'i').lower()


def emoji_sayisi(s):
    return sum(1 for ch in s if unicodedata.category(ch) == 'So' and ord(ch) >= 0x2190)


def kaynak_of(k):
    return k.get('kaynak') or 'arama'


def metin_sorunu(metin, ayar, kaynak='arama'):
    """Yanıt metni kurallara uymuyorsa nedenini döndürür (Claude düzeltsin diye), uyuyorsa None."""
    if not metin:
        return 'yanıt boş'
    n = threads_len(metin)
    if n > 500:
        return f'çok uzun ({n} > 500, Threads sınırı)'
    if len(metin) > ayar['en_uzun_yanit']:
        return f'çok uzun ({len(metin)} karakter, en fazla {ayar["en_uzun_yanit"]})'
    en_kisa = ayar['en_kisa_takip'] if kaynak == 'takip' else ayar['en_kisa_yanit']
    if len(metin) < en_kisa:
        return f'çok kısa ({len(metin)} karakter, en az {en_kisa})'
    bakilan = metin
    eposta = (ayar.get('izinli_eposta') or '').strip()
    if kaynak == 'takip' and eposta:
        bakilan = re.sub(re.escape(eposta), ' ', bakilan, flags=re.I)
    if LINK.search(bakilan):
        return 'link içeremez' + (f' (yalnızca {eposta} yazılabilir)' if kaynak == 'takip' and eposta else '')
    if '@' in bakilan:
        return '@ ile kimse etiketlenemez'
    if '#' in metin:
        return 'hashtag içeremez'
    if '{' in metin or '}' in metin:
        return 'şablon işareti ({ }) içeremez'
    if '—' in metin:
        return 'uzun tire (—) yerine doğal noktalama kullan'
    k = kucuk(bakilan)
    for kalip in ayar['yasak_kaliplar']:
        if re.search(kalip, k):
            return f'yasak ifade ("{kalip}"): satış çağrısı, oran ya da tutar yazılmaz'
    if kaynak == 'arama' and any(kucuk(w) in k for w in ayar['marka_kelimeleri']):
        return 'yeni sohbet yanıtlarında marka adı geçmez'
    if emoji_sayisi(metin) > ayar['en_fazla_emoji']:
        return f'en fazla {ayar["en_fazla_emoji"]} emoji'
    return None


def hata_kodu(e):
    m = re.search(r'"code"\s*:\s*(\d+)', str(e))
    return int(m.group(1)) if m else None


def genel_hata(e):
    """Token, izin ya da hız sınırı hatası: tek bir gönderiye değil tüm çalışmaya ait, devam etmenin anlamı yok."""
    k = hata_kodu(e)
    return k in (4, 10, 17, 32, 190, 613) or (k is not None and 200 <= k <= 299)


def liste(path, params, token, yedek_alanlar=None):
    """Liste döndüren uç noktalar. Bir parametre reddedilirse (kod 100) `limit`/`since` olmadan ve varsa daha az alanla
    bir kez daha dener: bazı alanlar her uç noktada desteklenmeyebilir."""
    try:
        return api('GET', path, params, token).get('data', [])
    except RuntimeError as e:
        if hata_kodu(e) != 100:
            raise
        sade = {k: v for k, v in params.items() if k not in ('limit', 'since')}
        if yedek_alanlar:
            sade['fields'] = yedek_alanlar
        if sade == params:
            raise
        return api('GET', path, sade, token).get('data', [])


# ---------- şifreleme (openssl: RSA-OAEP ile sarılmış tek kullanımlık AES anahtarı) ----------

def _openssl(args, veri, parola=None):
    env = dict(os.environ)
    if parola is not None:
        env['YANIT_PAROLA'] = parola
    r = subprocess.run(['openssl', *args], input=veri, capture_output=True, env=env)
    if r.returncode != 0:
        raise RuntimeError(f'openssl {args[0]} başarısız: {r.stderr.decode(errors="replace").strip()[:300]}')
    return r.stdout


def sifrele(veri):
    parola = secrets.token_hex(32)
    govde = _openssl(['enc', '-salt', *AES], veri, parola).decode().strip()
    anahtar = _openssl(['pkeyutl', '-encrypt', '-pubin', '-inkey', str(ACIK_ANAHTAR), *OAEP], parola.encode())
    return {'anahtar': base64.b64encode(anahtar).decode(), 'veri': govde}


def coz(paket, ozel_anahtar):
    parola = _openssl(['pkeyutl', '-decrypt', '-inkey', str(ozel_anahtar), *OAEP],
                      base64.b64decode(paket['anahtar'])).decode()
    return _openssl(['enc', '-d', *AES], (paket['veri'] + '\n').encode(), parola)


def aday_listesi(ozel_anahtar):
    paket = oku(ADAYLAR, {})
    if not paket.get('veri'):
        return []
    return json.loads(coz(paket, ozel_anahtar))


# ---------- kayıtlar, kota ----------

def gonderildi(kayit):
    return kayit.get('durum') == 'gonderildi'


def bekliyor(pid, karar, gonderilen):
    """Karar 'yanıtla' ama yanıt henüz gitmedi ve vazgeçilmedi."""
    if karar.get('karar') != 'yanitla':
        return False
    k = gonderilen.get(pid)
    return k is None or k.get('durum') == 'hata'


def eskimis(karar, ayar, an):
    """Hedef o kadar eski ki yanıt artık tuhaf kaçar (arama/yorum penceresi + pay)."""
    z = zaman(karar.get('gonderi_zamani'))
    if z is None:
        return False
    saat = ayar['takip_en_eski_saat'] + 24 if kaynak_of(karar) == 'takip' else ayar['en_eski_saat'] + 12
    return an - z > timedelta(hours=saat)


def yakin_yazarlar(ayar, kararlar, gonderilen, an, bekleyenler_dahil=True):
    """Son `yazar_araligi_gun` günde yanıt verdiğimiz (ve istenirse yanıtı sırada bekleyen) kişiler, küçük harfle."""
    sinir = an - timedelta(days=ayar['yazar_araligi_gun'])
    adlar = {kucuk(k.get('kullanici')) for k in gonderilen.values()
             if gonderildi(k) and (zaman(k.get('zaman')) or sinir) > sinir}
    if bekleyenler_dahil:
        adlar |= {kucuk(k.get('kullanici')) for pid, k in kararlar.items() if bekliyor(pid, k, gonderilen)}
    return adlar - {''}


def kota(ayar, kararlar, gonderilen, an):
    bugun = an.astimezone(TZ).date()
    giden = sum(1 for k in gonderilen.values()
                if gonderildi(k) and zaman(k.get('zaman')) and zaman(k['zaman']).astimezone(TZ).date() == bugun)
    bekleyen = sum(1 for pid, k in kararlar.items() if bekliyor(pid, k, gonderilen) and not eskimis(k, ayar, an))
    kalan = max(0, ayar['gunluk_limit'] - giden - bekleyen)
    return {'bugun_gonderilen': giden, 'bekleyen': bekleyen, 'gunluk_limit': ayar['gunluk_limit'], 'kalan': kalan,
            'kalan_takip': min(ayar['takip_tur_basina'], kalan), 'kalan_arama': min(ayar['tur_basina_yanit'], kalan)}


def gonderilen_kaydi():
    kayit = oku(GONDERILEN, {})
    kayit.setdefault('yanitlar', {})
    return kayit


# ---------- bul (GitHub Actions) ----------

def elenme_nedeni(m, ayar, en_eski, kararlar, gonderilen, yakin):
    pid = str(m.get('id') or '')
    metin = (m.get('text') or '').strip()
    z = zaman(m.get('timestamp'))
    if not pid:
        return 'kimlik yok'
    if pid in kararlar or pid in gonderilen:
        return 'daha önce değerlendirildi'
    if m.get('is_reply'):
        return 'başka bir gönderiye yanıt'
    if len(metin) < ayar['en_kisa_metin']:
        return 'metin çok kısa'
    if z is None or z < en_eski:
        return 'eski'
    if LINK.search(metin):
        return 'link içeriyor'
    k = kucuk(metin)
    if any(kucuk(w) in k for w in ayar['yasak_kelimeler']):
        return 'yasaklı kelime'
    if kucuk(m.get('username')) in yakin:
        return 'bu kişiye yakın zamanda yanıt verildi'
    return None


def _arama(ayar, deneme, an, durum, token, ben, kararlar, gonderilen):
    yakin = yakin_yazarlar(ayar, kararlar, gonderilen, an)
    en_eski = an - timedelta(hours=ayar['en_eski_saat'])
    sorgular = [(k, t, n) for k in ayar['anahtar_kelimeler']
                for t, n in (('RECENT', ayar['limit_yeni']), ('TOP', ayar['limit_populer'])) if n]
    bulunan, hatalar = {}, []

    for kelime, tur, limit in sorgular:
        try:
            sonuc = api('GET', 'keyword_search', {'q': kelime, 'search_type': tur, 'fields': ALANLAR,
                                                  'since': int(en_eski.timestamp()), 'limit': limit}, token)
        except RuntimeError as e:
            hatalar.append(f'"{kelime}" ({tur}): {e}')
            if not durum['sorgu'] or genel_hata(e) or len(hatalar) >= 3:
                break                                   # ilk sorgu ya da izin/token hatası: kalanlar da başarısız olur
            continue
        durum['sorgu'] += 1
        for m in sonuc.get('data', []):
            durum['sonuc'] += 1
            ad = m.get('username') or ''
            kendi = kucuk(ad) == ben
            neden = 'kendi gönderimiz' if kendi else elenme_nedeni(m, ayar, en_eski, kararlar, gonderilen, yakin)
            durum['kendi_gonderisi'] += kendi
            if deneme:
                ozet = (m.get('text') or '').replace('\n', ' ')[:110]
                print(f'[{tur} · {kelime}] @{ad} · {m.get("timestamp", "")[:16]} · {neden or "ADAY"} · {ozet}')
            if neden:
                continue
            a = bulunan.get(str(m['id']))
            if a:
                if kelime not in a['kelimeler']:
                    a['kelimeler'].append(kelime)
                continue
            z = zaman(m.get('timestamp'))
            bulunan[str(m['id'])] = {
                'id': str(m['id']), 'kaynak': 'arama', 'kullanici': ad, 'metin': (m.get('text') or '').strip()[:700],
                'link': m.get('permalink'), 'zaman': iso(z), 'kac_saat_once': round((an - z).total_seconds() / 3600, 1),
                'yanitlari_var': bool(m.get('has_replies')), 'alinti': bool(m.get('is_quote_post')),
                'medya': m.get('media_type'), 'kelimeler': [kelime],
            }

    secilen, yazarlar = [], set()
    for a in sorted(bulunan.values(), key=lambda a: a['zaman'], reverse=True):
        if kucuk(a['kullanici']) not in yazarlar:      # bir kişiden yalnızca en yeni gönderisi
            yazarlar.add(kucuk(a['kullanici']))
            secilen.append(a)
    secilen = secilen[:ayar['en_fazla_aday']]

    durum['onay'] = durum['sonuc'] > durum['kendi_gonderisi']
    marka = ayar['marka']
    if hatalar:
        durum['hata'] = f'{len(hatalar)} sorgu başarısız. İlki: {hatalar[0]}'[:600]
    if not durum['sorgu'] and hatalar:
        durum['not'] = ('Anahtar kelime araması çalışmadı: token\'da threads_keyword_search izni yok. '
                        '"Threads yanıtları için Meta onayı" rehberinin 1. ve 2. adımlarını uygula.')
    elif durum['sonuc'] and not durum['onay']:
        durum['not'] = (f'Arama yalnızca {marka}\'nun kendi gönderilerini döndürdü: Meta threads_keyword_search iznini '
                        'henüz onaylamamış. Onay gelene kadar yalnızca kendi gönderilerimize gelen yorumlara cevap verilir.')
    elif not durum['sonuc'] and durum['sorgu']:
        durum['not'] = (f'Aramada hiç sonuç çıkmadı. İzin henüz onaylanmadıysa arama yalnızca {marka}\'nun kendi '
                        'gönderilerine bakar.')
    return secilen


def _takip(ayar, deneme, an, durum, token, ben, kararlar, gonderilen):
    """igloo'nun gönderilerine ve yanıtlarına gelen, henüz cevaplanmamış yorumlar."""
    alan = 'id,text,timestamp,permalink'
    since = int((an - timedelta(days=ayar['takip_gun'])).timestamp())
    gonderiler = liste('me/threads', {'fields': alan, 'since': since, 'limit': 50}, token)
    yanitlarim = liste('me/replies', {'fields': alan + ',replied_to,root_post',
                                      'since': since - 86400, 'limit': 100}, token)
    benim, cevaplanan = {}, set()
    kok_bizim = {str(g['id']) for g in gonderiler if g.get('id')}
    for g in gonderiler:
        benim[str(g['id'])] = {'tur': 'gönderimiz', 'metin': (g.get('text') or '')[:400], 'link': g.get('permalink'),
                               'kok_bizim': True}
    for y in yanitlarim:
        hedef = (y.get('replied_to') or {}).get('id')
        if hedef:
            cevaplanan.add(str(hedef))
        kok = str((y.get('root_post') or {}).get('id') or '')
        benim[str(y['id'])] = {'tur': 'yanıtımız', 'metin': (y.get('text') or '')[:400], 'link': y.get('permalink'),
                               'kok_bizim': kok in kok_bizim, 'zaman': y.get('timestamp')}
    cevaplanan |= {p for p, k in gonderilen.items() if gonderildi(k)}

    # Kendi gönderilerimizin altındaki bütün konuşma; başkalarının gönderisindeki yanıtlarımızın doğrudan altı
    # (orada cevap verebilmek Meta onayı ister, onay yokken bakılmaz).
    taranan, hatalar = [], []
    for gid in kok_bizim:
        taranan.append((gid, 'conversation'))
    if durum.get('onay'):
        sinir = an - timedelta(days=ayar['takip_gun'])
        for yid, b in benim.items():
            if b['tur'] == 'yanıtımız' and not b['kok_bizim'] and (zaman(b.get('zaman')) or sinir) >= sinir:
                taranan.append((yid, 'replies'))

    en_eski = an - timedelta(hours=ayar['takip_en_eski_saat'])
    adaylar = {}
    for mid, uc in taranan:
        try:
            yorumlar = liste(f'{mid}/{uc}', {'fields': YORUM_ALANLARI, 'limit': 100}, token,
                             yedek_alanlar='id,text,username,timestamp,permalink,replied_to')
        except RuntimeError as e:
            hatalar.append(f'{mid}/{uc}: {e}')
            if genel_hata(e):
                break
            continue
        durum['yorum'] += len(yorumlar)
        for c in yorumlar:
            pid = str(c.get('id') or '')
            ad = c.get('username') or ''
            hedef = str((c.get('replied_to') or {}).get('id') or mid)
            z = zaman(c.get('timestamp'))
            metin = (c.get('text') or '').strip()
            if not pid or kucuk(ad) == ben or hedef not in benim:
                continue                                 # kendi yorumumuz ya da başkalarının kendi arasındaki konuşması
            if pid in cevaplanan or pid in kararlar or pid in gonderilen:
                neden = 'cevaplanmış'
            elif c.get('hide_status') in GIZLI:
                neden = 'gizlenmiş'
            elif z is None or z < en_eski:
                neden = 'eski'
            elif not metin:
                neden = 'metin yok'
            else:
                neden = None
            if deneme:
                print(f'[yorum] @{ad} · {c.get("timestamp", "")[:16]} · {neden or "ADAY"} · {metin.replace(chr(10), " ")[:110]}')
            if neden:
                continue
            b = benim[hedef]
            adaylar[pid] = {
                'id': pid, 'kaynak': 'takip', 'kullanici': ad, 'metin': metin[:700], 'link': c.get('permalink'),
                'zaman': iso(z), 'kac_saat_once': round((an - z).total_seconds() / 3600, 1),
                'yanit_verdigi': {'tur': b['tur'], 'metin': b['metin'], 'link': b['link']},
                'kok_bizim': b['kok_bizim'],
            }
    if hatalar:
        durum['takip_hata'] = f'{len(hatalar)} istek başarısız. İlki: {hatalar[0]}'[:600]
    return sorted(adaylar.values(), key=lambda a: a['zaman'])[:ayar['takip_en_fazla_aday']]


def _bul(ayar, deneme, an, durum):
    if not ayar['acik']:
        durum['not'] = 'Yanıt sistemi kapalı (yanitlar/ayar.json › "acik": false).'
        return []
    token = os.environ.get('THREADS_TOKEN', '').strip()
    if not token:
        durum['hata'] = 'THREADS_TOKEN tanımlı değil.'
        return []
    ben = kucuk(api('GET', 'me', {'fields': 'id,username'}, token).get('username'))
    kararlar = oku(KARARLAR, {})
    gonderilen = gonderilen_kaydi()['yanitlar']
    arama = _arama(ayar, deneme, an, durum, token, ben, kararlar, gonderilen) if ayar['anahtar_kelimeler'] else []
    takip = []
    if ayar['takip_acik']:
        try:
            takip = _takip(ayar, deneme, an, durum, token, ben, kararlar, gonderilen)
        except RuntimeError as e:
            durum['takip_hata'] = str(e)[:600]
        if durum['takip_hata'] and hata_kodu(durum['takip_hata']) == 10:
            durum['takip_hata'] += (' · Token\'da threads_read_replies izni yok gibi görünüyor: rehberin 1. ve 2. '
                                    'adımlarıyla izni ekleyip yeni token üret.')
    durum['arama_aday'], durum['takip_aday'] = len(arama), len(takip)
    return takip + arama


def bul():
    ayar = ayarlar()
    deneme = env_dogru('DENEME')
    an = simdi()
    durum = {'istek': ISTEK.read_text(encoding='utf-8').strip() if ISTEK.exists() else '',
             'son_arama': iso(an), 'sorgu': 0, 'sonuc': 0, 'kendi_gonderisi': 0, 'onay': False, 'yorum': 0,
             'arama_aday': 0, 'takip_aday': 0, 'aday': 0, 'hata': None, 'takip_hata': None, 'not': None}
    adaylar = []
    try:
        adaylar = _bul(ayar, deneme, an, durum)
    except Exception as e:                              # durum.json her koşulda yazılsın: Claude'un turu beklemede kalmasın
        durum['hata'] = f'{type(e).__name__}: {e}'[:600]
    durum['aday'] = len(adaylar)
    print(f'{durum["sorgu"]} sorgu · {durum["sonuc"]} sonuç ({durum["kendi_gonderisi"]} kendi gönderimiz) · '
          f'{durum["yorum"]} yorum · {durum["takip_aday"]} yorum adayı · {durum["arama_aday"]} sohbet adayı')
    if durum['not']:
        print(f'Not: {durum["not"]}')
    for alan in ('hata', 'takip_hata'):
        if durum[alan]:
            print(f'::warning title=Yanıt araması::{durum[alan]}')
    if deneme:
        print('(Deneme) Hiçbir şey kaydedilmedi.')
        return
    paket = {'istek': durum['istek'], 'olusturuldu': durum['son_arama'], 'adet': len(adaylar)}
    try:
        paket.update(sifrele(json.dumps(adaylar, ensure_ascii=False).encode()))
    except Exception as e:
        paket['adet'] = durum['aday'] = 0
        durum['hata'] = f'Adaylar şifrelenemedi: {e}'[:600]
        print(f'::warning title=Yanıt araması::{durum["hata"]}')
    yaz(ADAYLAR, paket)
    yaz(DURUM, durum)


# ---------- adaylar / ekle (Claude) ----------

def son_yanitlar(kararlar, n=8):
    yanitlar = sorted((k for k in kararlar.values() if k.get('karar') == 'yanitla'), key=lambda k: k.get('zaman', ''))
    return [k['yanit'] for k in yanitlar[-n:]]


def guncel_adaylar(ozel_anahtar, ayar, kararlar, gonderilen, an):
    yakin = yakin_yazarlar(ayar, kararlar, gonderilen, an)
    return [a for a in aday_listesi(ozel_anahtar)
            if a['id'] not in kararlar and a['id'] not in gonderilen
            and (kaynak_of(a) == 'takip' or kucuk(a['kullanici']) not in yakin)]


def adaylar_komutu(ozel_anahtar):
    ayar, an = ayarlar(), simdi()
    kararlar, gonderilen = oku(KARARLAR, {}), gonderilen_kaydi()['yanitlar']
    durum = oku(DURUM, {})
    liste_ = guncel_adaylar(ozel_anahtar, ayar, kararlar, gonderilen, an)
    k = kota(ayar, kararlar, gonderilen, an)
    takip = sum(1 for a in liste_ if kaynak_of(a) == 'takip')
    if not liste_:
        ozet = durum.get('not') or durum.get('hata') or 'Cevap verilecek yeni yorum ya da gönderi yok.'
    elif not k['kalan']:
        ozet = f'Günlük yanıt sınırı ({ayar["gunluk_limit"]}) doldu.'
    else:
        ozet = (f'{takip} yorum, {len(liste_) - takip} sohbet adayı; bu turda en fazla {k["kalan_takip"]} yorum cevabı '
                f've {k["kalan_arama"]} sohbet yanıtı, toplam {k["kalan"]} yanıt yazılabilir.')
    print(json.dumps({'devam': bool(liste_ and k['kalan']), 'ozet': ozet, 'durum': durum, 'kota': k,
                      'son_yanitlarimiz': son_yanitlar(kararlar), 'adaylar': liste_}, ensure_ascii=False, indent=1))


def ekle_komutu(dosya, ozel_anahtar):
    ayar, an = ayarlar(), simdi()
    kararlar, gonderilen = oku(KARARLAR, {}), gonderilen_kaydi()['yanitlar']
    adaylar = {a['id']: a for a in guncel_adaylar(ozel_anahtar, ayar, kararlar, gonderilen, an)}
    girdi = json.loads(Path(dosya).read_text(encoding='utf-8'))
    if not isinstance(girdi, list):
        sys.exit('Kararlar bir JSON dizisi olmalı: [{"id": "...", "karar": "yanitla", "yanit": "..."}, ...]')

    sorunlar, yeni, yazarlar = [], {}, set()
    sayi = {'takip': 0, 'arama': 0}
    for i, k in enumerate(girdi, 1):
        pid, karar = str(k.get('id', '')), k.get('karar')
        a = adaylar.get(pid)
        if not a:
            sorunlar.append(f'{i}. kayıt: {pid} bu turun adayları arasında yok')
        elif pid in yeni:
            sorunlar.append(f'{i}. kayıt: {pid} iki kez yazılmış')
        elif karar == 'gec':
            yeni[pid] = {'karar': 'gec', 'kaynak': kaynak_of(a), 'zaman': iso(an)}
        elif karar != 'yanitla':
            sorunlar.append(f'{i}. kayıt: karar "yanitla" ya da "gec" olmalı')
        else:
            kaynak = kaynak_of(a)
            metin = (k.get('yanit') or '').strip()
            sorun = metin_sorunu(metin, ayar, kaynak)
            if sorun:
                sorunlar.append(f'@{a["kullanici"]} yanıtı: {sorun}')
                continue
            anahtar = (kaynak, kucuk(a['kullanici']))
            if anahtar in yazarlar:
                sorunlar.append(f'@{a["kullanici"]}: aynı kişiye bir turda tek yanıt')
                continue
            yazarlar.add(anahtar)
            sayi[kaynak] += 1
            yeni[pid] = {'karar': 'yanitla', 'kaynak': kaynak, 'kullanici': a['kullanici'], 'link': a.get('link'),
                         'gonderi_zamani': a.get('zaman'), 'yanit': metin, 'zaman': iso(an)}

    k = kota(ayar, kararlar, gonderilen, an)
    if sayi['takip'] > k['kalan_takip']:
        sorunlar.append(f'{sayi["takip"]} yorum cevabı yazılmış ama bu turda en fazla {k["kalan_takip"]} gidebilir')
    if sayi['arama'] > k['kalan_arama']:
        sorunlar.append(f'{sayi["arama"]} sohbet yanıtı yazılmış ama bu turda en fazla {k["kalan_arama"]} gidebilir')
    if sayi['takip'] + sayi['arama'] > k['kalan']:
        sorunlar.append(f'toplam {sayi["takip"] + sayi["arama"]} yanıt yazılmış ama bugün en fazla {k["kalan"]} '
                        'yanıt daha gidebilir')
    if sorunlar:
        print('Kaydedilmedi. Düzeltilmesi gerekenler:\n- ' + '\n- '.join(sorunlar))
        sys.exit(2)

    for pid, a in adaylar.items():                     # karar yazılmayan sohbet adayları geçilmiş sayılır; yorumlar
        if kaynak_of(a) == 'arama':                     # sınır yüzünden bu turda kalmış olabilir, sonraki turda yine gelir
            yeni.setdefault(pid, {'karar': 'gec', 'kaynak': 'arama', 'zaman': iso(an)})
    kararlar.update(yeni)
    sinir = iso(an - timedelta(days=7))                 # eski "geç" kayıtlarına gerek yok; yanıtlar kalıcı kayıttır
    kararlar = {p: k for p, k in kararlar.items() if k.get('karar') == 'yanitla' or k.get('zaman', '') >= sinir}
    yaz(KARARLAR, kararlar)
    toplam = sayi['takip'] + sayi['arama']
    print(f'Kaydedildi: {sayi["takip"]} yorum cevabı, {sayi["arama"]} sohbet yanıtı, {len(yeni) - toplam} geçildi.')


# ---------- gonder (GitHub Actions) ----------

def ozet_yaz(satirlar):
    yol = os.environ.get('GITHUB_STEP_SUMMARY')
    if yol and satirlar:
        with open(yol, 'a', encoding='utf-8') as f:
            f.write('### Yanıt gönderimi\n\n' + '\n'.join(satirlar) + '\n')


def zaten_cevaplanan(token, an):
    """Son günlerde hesabın attığı bütün yanıtların hedefleri (başka yoldan, ör. elle verilmiş cevaplar dahil)."""
    since = int((an - timedelta(days=4)).timestamp())
    try:
        yanitlar = liste('me/replies', {'fields': 'id,replied_to', 'since': since, 'limit': 100}, token)
    except RuntimeError as e:
        print(f'Son yanıtlar okunamadı, bu denetim atlandı: {e}')
        return set()
    return {str((y.get('replied_to') or {}).get('id')) for y in yanitlar if (y.get('replied_to') or {}).get('id')}


def gonder():
    ayar = ayarlar()
    deneme = env_dogru('DENEME')
    if not ayar['acik']:
        print('Yanıt sistemi kapalı (yanitlar/ayar.json › "acik": false).')
        return
    an = simdi()
    kayit = gonderilen_kaydi()
    gonderilen = kayit['yanitlar']
    kararlar = oku(KARARLAR, {})
    sira = sorted(((p, k) for p, k in kararlar.items() if bekliyor(p, k, gonderilen)),
                  key=lambda x: (kaynak_of(x[1]) != 'takip', x[1].get('zaman', '')))   # önce yorum cevapları
    if not sira:
        print('Gönderilecek yanıt yok.')
        return
    token = os.environ.get('THREADS_TOKEN', '').strip()
    if not token and not deneme:
        report_error('THREADS_TOKEN tanımlı değil.')
        sys.exit(1)

    hak = min(ayar['tur_basina_gonderim'], ayar['gunluk_limit'] - kota(ayar, kararlar, gonderilen, an)['bugun_gonderilen'])
    yakin = yakin_yazarlar(ayar, kararlar, gonderilen, an, bekleyenler_dahil=False)
    cevaplanan = zaten_cevaplanan(token, an) if token else set()
    giden, satirlar, genel = 0, [], None

    def kaydet():
        if not deneme:
            kayit['son_calisma'] = {'zaman': iso(simdi()), 'gonderilen': giden}
            yaz(GONDERILEN, kayit)

    for pid, k in sira:
        ad, kaynak = k.get('kullanici', ''), kaynak_of(k)
        iptal = metin_sorunu(k.get('yanit', ''), ayar, kaynak)
        if not iptal and pid in cevaplanan:
            iptal = 'bu yoruma ya da gönderiye zaten yanıt verilmiş'
        if not iptal and kaynak == 'arama' and kucuk(ad) in yakin:
            iptal = f'@{ad} kişisine son {ayar["yazar_araligi_gun"]} günde zaten yanıt verildi'
        if not iptal and eskimis(k, ayar, an):
            iptal = 'hedef artık çok eski'
        if iptal:
            print(f'Vazgeçildi: @{ad} ({iptal})')
            if not deneme:
                gonderilen[pid] = {'kullanici': ad, 'kaynak': kaynak, 'durum': 'iptal', 'neden': iptal,
                                   'zaman': iso(simdi())}
            continue
        if giden >= hak:
            print('Bu çalışmanın ya da günün sınırı doldu; kalan yanıtlar bir sonraki gönderimde.')
            break
        if deneme:
            print(f'(Deneme) [{kaynak}] @{ad} ← {k["yanit"]}')
            giden += 1
            continue
        if giden:
            time.sleep(random.randint(*ayar['bekleme_saniye']))
        try:
            yanit_id = publish(token, {'media_type': 'TEXT', 'text': k['yanit'], 'reply_to_id': pid})
        except RuntimeError as e:
            print(f'::warning title=Yanıt gönderilemedi::@{ad}: {e}')
            sayac = gonderilen.get(pid, {}).get('deneme', 0)
            if genel_hata(e):                           # token/izin/hız sınırı: gönderinin suçu değil, sonra yine denensin
                gonderilen[pid] = {'kullanici': ad, 'kaynak': kaynak, 'durum': 'hata', 'deneme': sayac,
                                   'neden': str(e)[:400], 'zaman': iso(simdi())}
                genel = e
                break
            sayac += 1                                  # hedefe özgü hata (silinmiş, yanıtlara kapalı...): bir kez daha denenir
            gonderilen[pid] = {'kullanici': ad, 'kaynak': kaynak, 'durum': 'hata' if sayac < 2 else 'iptal',
                               'deneme': sayac, 'neden': str(e)[:400], 'zaman': iso(simdi())}
            kaydet()
            continue
        try:
            link = api('GET', yanit_id, {'fields': 'permalink'}, token).get('permalink')
        except RuntimeError:
            link = None
        gonderilen[pid] = {'kullanici': ad, 'kaynak': kaynak, 'durum': 'gonderildi', 'yanit_id': yanit_id,
                           'yanit_link': link, 'link': k.get('link'), 'zaman': iso(simdi())}
        yakin.add(kucuk(ad))
        cevaplanan.add(pid)
        giden += 1
        kaydet()                                         # her yanıttan sonra: çalışma yarıda kesilse de aynı yanıt iki kez gitmez
        print(f'Gönderildi → [{kaynak}] @{ad}: {link or yanit_id}')
        satirlar.append(f'- {"Yorum cevabı" if kaynak == "takip" else "Sohbet"} · @{ad}: {link or yanit_id}')

    kaydet()
    ozet_yaz(satirlar)
    if genel:
        report_error(f'Yanıt gönderimi durdu (token ya da izin sorunu): {genel}')
        sys.exit(1)


def main():
    p = argparse.ArgumentParser(description='igloo Threads yanıt sistemi')
    alt = p.add_subparsers(dest='komut', required=True)
    alt.add_parser('bul')
    alt.add_parser('gonder')
    a = alt.add_parser('adaylar')
    a.add_argument('--anahtar', required=True)
    e = alt.add_parser('ekle')
    e.add_argument('dosya')
    e.add_argument('--anahtar', required=True)
    args = p.parse_args()
    if args.komut == 'bul':
        bul()
    elif args.komut == 'gonder':
        gonder()
    elif args.komut == 'adaylar':
        adaylar_komutu(args.anahtar)
    else:
        ekle_komutu(args.dosya, args.anahtar)


if __name__ == '__main__':
    main()
