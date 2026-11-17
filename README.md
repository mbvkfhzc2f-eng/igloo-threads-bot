# igloo collective Threads botu

@igloo.collective hesabının Threads planını kendi kendine paylaşır: **17 Kasım – 31 Aralık 2026**, her gün **09:00, 11:00, 13:00, 18:00 ve 21:00**'da (Türkiye saati) o saate düşen gönderi resmi Threads API ile atılır. Bilgisayarın açık olması gerekmez; bot GitHub'ın sunucularında ücretsiz çalışır.

- 226 gönderi: 09:00 günün notu, 11:00 sektör sözlüğü, 13:00 öğle arası (gayriresmî sözlük, tamamla, kırmızı bayrak/yeşil bayrak, popüler olmayan görüş, "sadece ... anlar" listeleri, POV, itiraf köşesi), 18:00 akşam serileri, 21:00 akşam sohbeti; 12 görsel kart; özel günler (Efsane Cuma, Öğretmenler Günü, 3 Aralık, yıl sonu)
- Gönderilerin bir kısmının altına bot kendisi ilk yorumu ekler (doğru mu yanlış mı cevabı, ek ipucu, igloo'nun kendi cevabı ya da site linki).
- Komisyon oranı hiçbir gönderide geçmez; yalnızca "komisyonu markadan alıyoruz" denir.
- Aynı gönderi iki kez gitmez. Saati 4 saatten fazla geçen gönderi atlanır. Bot geç kurulsa bile hesabın ilk gönderisi açılış gönderisi olur. 31 Aralık'tan sonra kendiliğinden durur.
- Token eklenene kadar bot hiçbir şey yapmaz ve hata e-postası göndermez.
- Claude'un **igloo Threads tetik** görevi her paylaşım saatinde botu tetikler. GitHub'ın kendi 15 dakikalık yoklaması yedektir.

## Kurulum (bir kerelik, ~10 dakika)

### 1. Threads'e Brave'den giriş
Claude uzantısının kurulu olduğu **Brave**'de [threads.com](https://www.threads.com)'a **igloo.collective** hesabıyla giriş yap. Token üretimi bu oturumu kullanır. Günlük yanıt turları tarayıcıya ihtiyaç duymaz.

### 2. Threads erişim token'ı
Lingoof'un Threads için kullandığı Meta uygulaması **LINGOOF Bot** (App ID 1133077682509852) igloo için de kullanılır. **İgloo App**'te Threads API kullanım durumu yok, o yüzden onu değil bunu seç:
1. [LINGOOF Bot › App roles › Roles](https://developers.facebook.com/apps/1133077682509852/roles/roles/) sayfasında **Add People › Threads Tester** yolunu izle ve `igloo.collective` kullanıcı adını ekle.
2. Threads'te igloo hesabındayken **Ayarlar › Hesap › Web sitesi izinleri › Davetler** bölümünden daveti kabul et.
3. Panele dön: **Use cases › Access the Threads API › Settings**. `igloo.collective`'in yanındaki **Generate Access Token** düğmesine bas, açılan pencerede izin ver ve `TH` ile başlayan token'ı kopyala.
   - Pencere lingoof hesabını gösterirse Brave'de Threads'e igloo ile giriş yapılmamıştır; 1. adıma dön.

### 3. Token'ı depoya ekle
Bu deponun **Settings › Secrets and variables › Actions › New repository secret** bölümüne git. Adı `THREADS_TOKEN`, değeri kopyaladığın token olsun. Token şifre gibidir; başka hiçbir yere yapıştırma.

### Kontrol
**Actions** sekmesinde **Threads paylaşımı › Run workflow** düğmesine bas. "Deneme" işaretli kalsın. Kayıtta `@igloo.collective` ve sıradaki gönderiyi görürsen her şey hazır. İlk gerçek paylaşım (açılış gönderisi) bir sonraki tetikte gider.

## Ayarlar
- `posts.json`: her gönderinin tarihi, saati, metni, ilk yorumu (`reply`), görseli (`img`, `alt`) ve konu etiketi (`topic`). İstenirse `poll` alanıyla anket de eklenebilir. GitHub üzerinden düzenleyebilirsin; `{LINK}` yazan yere site linki girer.
- `config.json`: `site_url` (link), `grace_hours` (kaç saat gecikmeye kadar paylaşılsın), `reply_delay_seconds` (ilk yorumdan önce bekleme).
- Durdurmak için: **Actions › Threads paylaşımı › ⋯ › Disable workflow**. Tekrar açınca o günün tarihinden devam eder.
- Bir çalışma hata verirse GitHub e-posta atar. Son hatanın metni `state.json` içindeki `last_error` alanında da durur. Aynı gönderi 3 kez hata verirse atlanır.

## İstatistikler
**Threads istatistikleri** iş akışı her sabah 07:37'de (GitHub'ın zamanlayıcısı çalışmazsa 09:11 tetiğiyle) paylaşılan her gönderinin görüntülenme, beğeni, yorum, repost, alıntı ve paylaşım sayılarını ve takipçi sayısını çeker:
- `insights.md`: seriye ve saate göre ortalamalar, en çok etkileşim alan 10 gönderi.
- `insights.json`: ham veri ve günlük takipçi sayısı.

Token'da `threads_manage_insights` izni olmalı (LINGOOF Bot'ta zaten açık). İzin yoksa iş akışı yalnızca uyarı verir, paylaşımlar etkilenmez.

## Günlük yanıt turları
Claude'un **igloo Threads yanıt turu** görevi her gün 10:17, 15:17 ve 20:17'de (Türkiye saati) bulutta çalışır; Mac'in ya da tarayıcının açık olması gerekmez. Yanıtlar resmi Threads API'siyle bu depodaki iş akışlarından gider.
- Önce igloo'nun gönderilerine ve yanıtlarına son 48 saatte gelen yorumlara bakılır. Soru soranlara kısa cevap yazılır; şikâyet, tartışma ve iş birliği talepleri turun özetinde sana bildirilir.
- Sonra anahtar kelimelerle influencer pazarlaması, marka iş birlikleri ve içerik üreticiliği konuşan Türkçe gönderiler bulunur ve faydalı, satış yapmayan yanıtlar yazılır. **Bu kısım Meta onayı gerektiriyor** (aşağıda).
- Sınırlar: günde toplam en fazla 10 yanıt; bir turda en fazla 2 yorum cevabı ve 4 yeni sohbet yanıtı; aynı kişiye 14 günde en fazla bir yeni sohbet yanıtı; yanıtlar arasında 1–2,5 dakika. Link, hashtag, @etiket, oran, tutar ve "bize yazın" gibi çağrılar kodda da engellenir.
- Yazım kuralları `yanitlar/YAZIM_REHBERI.md` dosyasında. Kayıtlar: kararlar `yanitlar/kararlar.json`, gönderilenler ve linkleri `yanitlar/gonderilen.json`, son aramanın özeti `yanitlar/durum.json`. Başkalarının metinleri bu herkese açık depoda düz metin olarak durmasın diye `yanitlar/adaylar.enc.json` şifreli tutulur. Görev her turda yeni bir anahtar çifti üretir, açık anahtarı (`yanitlar/claude_acik_anahtar.pem`) aramayı başlatan commit'le birlikte gönderir; özel anahtar yalnızca o turun bulut oturumunda durur ve tur bitince silinir.

### Meta onayı
Threads, bir uygulamanın başkalarının gönderilerini aramasına ve onlara yanıt vermesine ancak Meta'nın uygulama incelemesinden (App Review) sonra izin veriyor. Onay gelene kadar arama yalnızca igloo'nun kendi gönderilerini döndürür ve sistem yalnızca yorumlara cevap verir. Ayrıntılı adımlar Claude'un hazırladığı "Threads yanıtları için Meta onayı" rehberinde:
1. LINGOOF Bot uygulamasına `threads_keyword_search`, `threads_manage_replies` ve `threads_read_replies` izinlerini ekle.
2. igloo için yeni token üret ve `THREADS_TOKEN` secret'ını güncelle (Kurulum › 2. adımdaki gibi).
3. `threads_keyword_search` ve `threads_manage_replies` için Advanced Access iste.

Onay gelince başka bir şey yapmana gerek yok: bir sonraki turda yeni sohbet yanıtları da kendiliğinden başlar.

### Ayarlar, deneme ve durdurma
- `yanitlar/ayar.json`: anahtar kelimeler, günlük sınır (`gunluk_limit`), tur başına sınırlar, aynı kişiye tekrar yanıt aralığı (`yazar_araligi_gun`), gönderiyi baştan eleyen kelimeler (`yasak_kelimeler`) ve yanıtlarda yasak ifadeler (`yasak_kaliplar`).
- Deneme: **Actions › Threads yanıt araması › Run workflow** ("Deneme" işaretli kalsın). Kayıtta bulunan yorumlar, gönderiler ve hangisinin neden elendiği görünür; hiçbir şey kaydedilmez.
- Durdurmak için `yanitlar/ayar.json` içinde `"acik": false` yap ya da Claude uygulamasında **igloo Threads yanıt turu** görevini duraklat.

## İsteğe bağlı: GH_PAT
Token yaklaşık 60 gün geçerli; plan 31 Aralık'ta bittiği için kurulumda üretilen token yeter. Planı uzatırsan GitHub › Settings › Developer settings › Fine-grained tokens yolundan yalnızca bu depoya **Secrets: Read and write** izniyle bir token üretip `GH_PAT` adıyla ekle; bot Threads token'ını kendisi yeniler.
