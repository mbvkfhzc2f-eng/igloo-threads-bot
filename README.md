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
Claude uzantısının kurulu olduğu **Brave**'de [threads.com](https://www.threads.com)'a **igloo.collective** hesabıyla giriş yap. Hem token üretimi hem de günlük yanıt turları bu oturumu kullanır.

### 2. Threads erişim token'ı
Lingoof için kullandığın Meta uygulaması (**lingoof.app**) igloo için de kullanılabilir:
1. [developers.facebook.com](https://developers.facebook.com) › **My Apps** › **lingoof.app** › **App roles › Roles › Add People › Threads Tester** yolunu izle ve `igloo.collective` kullanıcı adını ekle.
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
**Threads istatistikleri** iş akışı her sabah 07:37'de paylaşılan her gönderinin görüntülenme, beğeni, yorum, repost, alıntı ve paylaşım sayılarını ve takipçi sayısını çeker:
- `insights.md`: seriye ve saate göre ortalamalar, en çok etkileşim alan 10 gönderi.
- `insights.json`: ham veri ve günlük takipçi sayısı.

Token'da `threads_manage_insights` izni olmalı (lingoof.app'te zaten açık). İzin yoksa iş akışı yalnızca uyarı verir, paylaşımlar etkilenmez.

## Günlük yanıt turları (Claude görevi, bu depoda değil)
Claude'un **igloo Threads yanıtları** görevi her gün 10:47, 15:47 ve 20:47'de Brave'deki igloo oturumuyla çalışır:
- Influencer pazarlaması, marka iş birlikleri ve içerik üreticiliği konuşan Türkçe gönderileri anahtar kelimelerle bulur ve faydalı, satış yapmayan yanıtlar yazar.
- Günde toplam en fazla 10 yanıt (10:47'de en fazla 4, diğer turlarda en fazla 3). Önce igloo'ya yazan kişilere cevap verilir.
- Link, @etiket, fiyat, komisyon ya da "bize yazın" çağrısı yok. Şikâyet, tartışma ve hassas konulara girilmez; böyle durumlar özetle sana bildirilir.
- Mac açık, Brave çalışıyor ve Claude uzantısı bağlı olmalı. Değilse tur bir satırlık notla kendini atlar.
- Durdurmak için Claude uygulamasında **igloo Threads yanıtları** görevini duraklat.

## İsteğe bağlı: GH_PAT
Token yaklaşık 60 gün geçerli; plan 31 Aralık'ta bittiği için kurulumda üretilen token yeter. Planı uzatırsan GitHub › Settings › Developer settings › Fine-grained tokens yolundan yalnızca bu depoya **Secrets: Read and write** izniyle bir token üretip `GH_PAT` adıyla ekle; bot Threads token'ını kendisi yeniler.
