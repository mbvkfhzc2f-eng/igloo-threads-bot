# -*- coding: utf-8 -*-
"""igloo Threads planını kurar: posts.json + görsel kartlar (img/) + doğrulama raporu."""
import json
import re
import sys
import unicodedata
from datetime import date, timedelta
from pathlib import Path

from content_notes import INTRO, NOTES_C, NOTES_B, NOTE_SPECIAL, SOZLUK
from content_midday import MIDDAY
from content_series import MARKA, CREATOR, DYY, SAHNE, TEKLIF, KAYDET, PAZAR, AKSAM, OZET_REPLIES

BOT = Path('/home/claude/igloo-threads-bot')
IMG = BOT / 'img'
START, END = date(2026, 11, 17), date(2026, 12, 31)
YEAR_END = {'2026-12-28', '2026-12-29', '2026-12-30', '2026-12-31'}
TOPIC_C, TOPIC_B = 'İçerik Üreticisi', 'Influencer Marketing'


def threads_len(text):
    n = 0
    for ch in text:
        if ord(ch) > 0xFFFF or (ord(ch) >= 0x2000 and unicodedata.category(ch) in ('So', 'Sk', 'Mn', 'Cf')):
            n += len(ch.encode('utf-8'))
        else:
            n += 1
    return n


def short(term):
    return re.sub(r'\s*\(.*?\)', '', term).strip()


def slug(s):
    tr = str.maketrans('çğıöşüÇĞİÖŞÜ', 'cgiosuCGIOSU')
    return re.sub(r'[^a-z0-9]+', '_', s.translate(tr).lower()).strip('_')[:30]


posts, cards = [], []


def add(d, time, series, text, reply=None, topic=None, poll=None, img=None, alt=None):
    t = text + (reply or '')
    posts.append({'n': len(posts), 'date': d, 'time': time, 'series': series, 'cta': ('{LINK}' in t or 'iletisim@' in t),
                  'img': img, 'alt': alt, 'poll': poll, 'text': text, 'reply': reply, 'topic': topic})


add('2026-11-16', '21:00', 'Açılış', INTRO['text'], INTRO['reply'], INTRO['topic'])

it_c, it_b = iter(NOTES_C), iter(NOTES_B)
it_mid = {wd: (name, iter(items)) for wd, (name, items) in MIDDAY.items()}
it = {k: iter(v) for k, v in dict(MARKA=MARKA, CREATOR=CREATOR, DYY=DYY, SAHNE=SAHNE, TEKLIF=TEKLIF, KAYDET=KAYDET, PAZAR=PAZAR).items()}
aksam = {d: (t, r, tp) for d, t, r, tp in AKSAM}
it_ozet = iter(OZET_REPLIES)
use_c = True
week_terms = []
kaydet_no = ozet_no = 0

d = START
day = 0
while d <= END:
    ds, wd = d.isoformat(), d.weekday()          # 0 = pazartesi
    # 09:00 Günün Notu
    if ds in NOTE_SPECIAL:
        text, reply, topic = NOTE_SPECIAL[ds]
        add(ds, '09:00', 'Yıl Sonu Notu' if ds in YEAR_END else 'Özel Gün', text, reply, topic)
    else:
        if use_c:
            body, reply = next(it_c)
            add(ds, '09:00', 'Günün Notu', f'Günün notu · içerik üreticileri için 💙\n\n{body}', reply, TOPIC_C)
        else:
            body, reply = next(it_b)
            add(ds, '09:00', 'Günün Notu', f'Günün notu · markalar için 🧊\n\n{body}', reply, TOPIC_B)
        use_c = not use_c
    # 11:00 Sektör Sözlüğü
    term, body, card_def = SOZLUK[day]
    week_terms.append((term, card_def))
    add(ds, '11:00', 'Sektör Sözlüğü', f'Sektör sözlüğü 📖\n\n{term}\n{body}', None, 'Dijital Pazarlama')
    # 13:00 Öğle Arası: her gün başka bir paylaşılabilir format (anket yok)
    name, gen = it_mid[wd]
    text, reply, topic = next(gen)
    add(ds, '13:00', name, text, reply, topic)
    # 18:00 akşam serisi
    if wd == 0:
        text, reply = next(it['MARKA']); add(ds, '18:00', 'Marka Masası', text, reply, TOPIC_B)
    elif wd == 1:
        text, reply = next(it['CREATOR']); add(ds, '18:00', 'Creator Masası', text, reply, TOPIC_C)
    elif wd == 2:
        claim, reply = next(it['DYY'])
        add(ds, '18:00', 'Doğru mu Yanlış mı?', f'Doğru mu, yanlış mı? 🤔\n\n"{claim}"\n\nCevabımız ilk yorumda 👇', reply, TOPIC_B)
    elif wd == 3:
        text, reply = next(it['SAHNE']); add(ds, '18:00', 'Sahne Arkası', text, reply, 'Marka İş Birliği')
    elif wd == 4:
        text, reply = next(it['TEKLIF']); add(ds, '18:00', 'Teklif Kutusu', text, reply, 'Marka İş Birliği')
    elif wd == 5:
        title, items, text, reply, topic = next(it['KAYDET'])
        kaydet_no += 1
        fn = f'kaydet_{kaydet_no:02d}_{slug(title)}.jpg'
        alt = f'igloo collective bilgi kartı. {title}: ' + '; '.join(f'{i}) {x}' for i, x in enumerate(items, 1)) + '.'
        cards.append({'file': fn, 'kind': 'kaydet', 'label': 'Kaydet listesi', 'title': title, 'items': [(x, None) for x in items]})
        add(ds, '18:00', 'Kaydet Listesi', text, reply, topic, img=fn, alt=alt)
    else:
        add(ds, '18:00', 'Pazar Okuması', next(it['PAZAR']), None, TOPIC_B)
    # 21:00 Akşam Sohbeti / Haftanın Özeti
    if wd == 6:
        ozet_no += 1
        names = [short(t) for t, _ in week_terms]
        first = (d - timedelta(days=len(week_terms) - 1))
        rng = f'{first.day}–{d.day} {"Kasım" if d.month == 11 and first.month == 11 else "Aralık" if first.month == 12 else "Kasım–Aralık"}'
        if first.month != d.month:
            rng = f'{first.day} Kasım – {d.day} Aralık'
        fn = f'ozet_{ozet_no:02d}_sozluk.jpg'
        text = (f'Haftanın özeti 📖\n\nBu hafta sektör sözlüğüne {len(names)} terim girdi: {", ".join(names)}.\n\n'
                'Hepsi kısa tanımlarıyla görselde. Kaydedin, bir teklif ya da brief geldiğinde açarsınız 🔖')
        alt = (f'igloo collective bilgi kartı. Haftanın sözlüğü, {rng}: ' +
               '; '.join(f'{short(t)}: {c}' for t, c in week_terms) + '.')
        cards.append({'file': fn, 'kind': 'ozet', 'label': 'Haftanın sözlüğü', 'title': 'Bu haftanın 7 terimi' if len(names) == 7 else f'Bu haftanın {len(names)} terimi',
                      'sub': rng, 'items': [(short(t), c) for t, c in week_terms]})
        add(ds, '21:00', 'Haftanın Özeti', text, next(it_ozet), 'Dijital Pazarlama', img=fn, alt=alt[:1000])
        week_terms = []
    else:
        text, reply, topic = aksam[ds]
        add(ds, '21:00', 'Akşam Sohbeti', text, reply, topic)
    d += timedelta(days=1)
    day += 1

# Her şey tükendi mi?
for name, gen in [('NOTES_C', it_c), ('NOTES_B', it_b), ('OZET', it_ozet)] + list(it.items()) + [(n, g) for n, g in it_mid.values()]:
    left = list(gen)
    if left:
        print(f'UYARI: {name} içinde kullanılmayan {len(left)} öğe var', file=sys.stderr)

# Doğrulama
problems = []
for p in posts:
    for field in ('text', 'reply'):
        v = p.get(field)
        if v:
            L = threads_len(v.replace('{LINK}', 'https://igloocollective.com'))
            if L > 490:
                problems.append(f"#{p['n']} {p['date']} {p['time']} {field} çok uzun: {L}")
            if '—' in v:
                problems.append(f"#{p['n']} {field} uzun tire içeriyor")
    if p['poll']:
        if not (2 <= len(p['poll']) <= 4):
            problems.append(f"#{p['n']} anket seçenek sayısı {len(p['poll'])}")
        for o in p['poll']:
            if len(o.encode('utf-8')) > 25:
                problems.append(f"#{p['n']} anket seçeneği 25 baytı aşıyor: {o} ({len(o.encode('utf-8'))})")
    t = p['topic']
    if t and (len(t) > 50 or '.' in t or '&' in t):
        problems.append(f"#{p['n']} konu etiketi geçersiz: {t}")
    if p['alt'] and len(p['alt']) > 1000:
        problems.append(f"#{p['n']} alt metin uzun")

slots = [(p['date'], p['time']) for p in posts]
assert len(slots) == len(set(slots)), 'aynı saate iki gönderi düşmüş'
json.dump(posts, open(BOT / 'posts.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump(cards, open('/home/claude/igloo/cards.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

from collections import Counter
print(len(posts), 'gönderi ·', posts[1]['date'], '→', posts[-1]['date'])
print('seriler:', dict(Counter(p['series'] for p in posts)))
print('saatler:', dict(Counter(p['time'] for p in posts)))
print('anket:', sum(1 for p in posts if p['poll']), '· görsel:', sum(1 for p in posts if p['img']),
      '· ilk yorum:', sum(1 for p in posts if p['reply']), '· CTA:', sum(1 for p in posts if p['cta']))
print('en uzun metin:', max(threads_len(p['text']) for p in posts), '· en uzun yorum:',
      max(threads_len(p['reply'].replace('{LINK}', 'https://igloocollective.com')) for p in posts if p['reply']))
print('SORUNLAR:' if problems else 'Sorun yok.')
for x in problems:
    print(' -', x)
