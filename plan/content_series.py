# -*- coding: utf-8 -*-
"""igloo Threads planı: 18:00 akşam serileri ve 21:00 Akşam Sohbeti."""
from content_notes import CTA_BRAND, CTA_CREATOR

# Pazartesi 18:00 · Marka Masası: (metin, ilk yorum)
MARKA = [
    ("Marka masası 🧊\n\nInfluencer kampanyasına başlamadan önce 3 soru:\n\n1. Amaç ne? Bilinirlik mi, satış mı, güven mi? Her biri farklı "
     "içerik üreticisi ve farklı ölçüm demek.\n2. Kime konuşuyoruz? Yaş, şehir, ilgi alanı.\n3. Neyle ölçeceğiz? Görüntülenme, tıklama, "
     "kod kullanımı...\n\nBu üçü netse içerik üreticisi seçimi yarı yarıya kolaylaşır.", CTA_BRAND),
    ("Marka masası 🧊\n\nDoğru içerik üreticisini seçmek için 4 filtre:\n\n1. Alan uyumu: Ürününüz onun içeriğinde doğal duruyor mu?\n"
     "2. Kitle uyumu: Takipçileri sizin müşteriniz mi?\n3. Ortalama performans: En iyi 3 gönderisi değil, son 10 gönderisinin "
     "ortalaması.\n4. Yorum kalitesi: Kitlesiyle gerçekten konuşuyor mu?\n\nTakipçi sayısı bu listede bilerek yok.",
     "Bir profili markaya önermeden önce takipçi kalitesine, etkileşim oranına ve hesabın büyüme geçmişine de bakıyoruz. Sahte takipçi "
     "denetimi bu sürecin bir parçası."),
    ("Marka masası 🧊\n\nBütçe sınırlıysa: önce test, sonra büyüt.\n\nBütçenin tamamını tek bir isme vermek yerine önce 3–5 küçük hesapla "
     "kısa bir deneme yapın. Hangi mesajın, hangi kitlenin, hangi formatın çalıştığını görün. Sonra bütçenin büyük kısmını işe yarayana "
     "aktarın.\n\nKampanya bittiğinde elinizde sadece sonuç değil, öğrenilmiş bir şey de kalır.", None),
    ("Marka masası 🧊\n\nİçerik onayını hızlandırmanın 3 yolu:\n\n1. Onayı tek kişi versin. Beş kişiden gelen beş ayrı yorum, içeriği "
     "kimsenin olmayan bir şeye çevirir.\n2. Geri bildirimi tek mesajda toplayın.\n3. Onay süresini baştan söyleyin: \"48 saat içinde "
     "döneriz.\"\n\nYayın tarihi kaymayan kampanya, planlandığı etkiyi yapar.", None),
    ("Marka masası 🧊\n\nKampanya raporunu okurken sırayla 3 soru sorun:\n\n1. Kaç kişiye ulaştı? (erişim, görüntülenme)\n2. "
     "İlgilendiler mi? (kaydetme, yorum, izlenme süresi)\n3. Harekete geçtiler mi? (tıklama, kod kullanımı, satış)\n\nBir kampanya ilk "
     "soruda zayıf, üçüncüde güçlü olabilir. Neyin hedeflendiğini hatırlamak raporun yarısıdır.", None),
    ("Marka masası 🧊\n\n2027 planı yapılırken influencer tarafı için 3 öneri:\n\n1. Tek seferlik iş birlikleri yerine birkaç uzun "
     "soluklu ilişki kurun.\n2. Her kampanyada bir şey test edin: yeni format, yeni kitle, yeni mesaj.\n3. Ölçümü takvime koyun: her "
     "kampanyadan 7 gün sonra kısa bir değerlendirme.\n\nYılın ilk brief'i şimdiden hazırsa Ocak boşa geçmez.",
     "2027 planınızı birlikte konuşmak isterseniz: iletisim@igloocollective.com 🧊"),
]

# Salı 18:00 · Creator Masası
CREATOR = [
    ("Creator masası 💙\n\nİlk teklif mesajı geldi. Panik yok, sırayla:\n\n1. Markayı tanıyın: Ürün kitlenize gerçekten uyuyor mu?\n2. "
     "Kapsamı sorun: Kaç içerik, hangi format, hangi tarih?\n3. İçerik reklamda kullanılacak mı, sorun.\n4. Ödeme vadesini sorun.\n5. "
     "Sonra fiyat verin.\n\nKapsam netleşmeden verilen fiyat çoğu zaman eksik kalır.", None),
    ("Creator masası 💙\n\nFiyat belirlerken 3 şeye bakın:\n\n1. Emek: Fikir, çekim, kurgu, revizyon. Saat saat düşünün.\n2. Değer: "
     "Ortalama görüntülenmeniz ve kitlenizin kimlerden oluştuğu.\n3. Haklar: Kullanım hakkı, münhasırlık ve acil teslim fiyatı "
     "değiştirir.\n\nTakipçi sayısını bir rakamla çarpıp fiyat bulmak hızlı ama çoğu zaman sizi zarara sokar.", None),
    ("Creator masası 💙\n\nTek sayfalık medya kiti nasıl olur?\n\nÜstte: Adınız, alanınız, bir cümlelik tanıtım.\nOrtada: Takipçi, "
     "ortalama görüntülenme, kitlenin yaşı ve şehirleri.\nAltta: 2–3 iş birliği örneği ve sonuçları.\nEn altta: İletişim e-postası.\n\n"
     "Rakamları her ay güncelleyin. Eski rakamlar profilinizi olduğundan zayıf gösterebilir.",
     "Hızlı kontrol: tanıtım cümlesi, güncel rakamlar, kitle dağılımı, en iyi 3 içerik ve iletişim e-postası. Hepsi kitinizde var mı? ✅"),
    ("Creator masası 💙\n\nMarkayla ilk görüşmede sorulacak 5 soru:\n\n1. Bu kampanyayla neyi başarmak istiyorsunuz?\n2. Hedef kitle "
     "kim?\n3. Olmazsa olmaz mesajlar ve kaçınılacak ifadeler neler?\n4. İçerik onayını kim verecek, ne kadar sürede?\n5. Başarıyı neyle "
     "ölçeceğiz?\n\nSoru soran içerik üreticisi, markanın gözünde iş ortağına dönüşür.", None),
    ("Creator masası 💙\n\nYazılı anlaşmada bakılacak 6 madde:\n\n1. Teslim kalemleri ve tarihler\n2. Revizyon sayısı\n3. Kullanım hakkı: "
     "süre ve mecra\n4. Münhasırlık: kategori ve süre\n5. Ödeme tutarı ve vadesi\n6. İptal durumunda ne olacağı\n\nAnlamadığınız bir "
     "maddeyi imzalamadan sorun. Emin olamadığınızda bir hukukçuya danışmak her zaman iyi fikir.",
     "Sözleşmelerde sizi en çok düşündüren madde hangisi? Yorumlara yazın, bir sonraki creator masasında ele alalım."),
    ("Creator masası 💙\n\nYayından sonraki 7 gün, bir sonraki iş birliğini belirler:\n\n• İlk saat yorumlara cevap verin.\n• 48. saatte ve "
     "7. günde istatistiklerin ekran görüntüsünü alın.\n• Markaya linkleri ve sonuçları içeren kısa bir kapanış mesajı atın.\n• Öne "
     "çıkan yorumları da ekleyin.\n\nRaporu marka istemeden göndermek ikinci teklifin en kısa yolu.", None),
    ("Creator masası 💙\n\n2027 için kendinize 3 iş hedefi koyun:\n\n1. Fiyat hedefi: Ortalama iş birliği ücretinizi nereye taşımak "
     "istiyorsunuz?\n2. Marka hedefi: Çalışmak istediğiniz 5 markanın listesi.\n3. Düzen hedefi: Fatura, sözleşme, medya kiti... İş "
     "tarafını sistemli hale getirmek.\n\nİçerik hedefiniz zaten var. İş hedefiniz de olsun.", CTA_CREATOR),
]

# Çarşamba 18:00 · Doğru mu Yanlış mı? (iddia, ilk yorumdaki cevap)
DYY = [
    ("Takipçi sayısı ne kadar yüksekse kampanya o kadar başarılı olur.",
     "Yanlış ❌\n\nTakipçi sayısı ulaşılabilecek kitleyi gösterir, ulaşılanı değil. Kampanyayı başarılı yapan; içerik üreticisinin alanının "
     "ürüne uyması, kitlesinin markanın müşterisi olması ve içeriğin gerçekten izlenmesi. Bazen 15 bin takipçili bir hesap, 500 bin "
     "takipçiliden daha çok iş çıkarır."),
    ("Barter iş birliği her zaman kötüdür.",
     "Yanlış ❌\n\nYeni başlayan bir hesap için kitlesine gerçekten uyan bir ürünle yapılan barter, portfolyonun ilk adımı olabilir. Sorun "
     "barter değil, belirsizlik: Kaç paylaşım, ne zaman, zorunlu mu? Bunlar yazılıysa barter da bir iş birliğidir. Ürün de bir menfaat "
     "olduğu için reklam ifadesi yine gerekir."),
    ("Ajansla çalışan içerik üreticisi, kazancının bir kısmını ajansa verir.",
     "Ajansa göre değişir 🤷\n\nBizim modelimizde komisyonu markadan alıyoruz; içerik üreticisinin kazancından kesinti yapmıyoruz. Hangi "
     "ajansla çalışırsanız çalışın, komisyonun kimden ve nasıl alındığını yazılı olarak sorun."),
    ("Reklam ifadesi koymak etkileşimi düşürür, en iyisi hiç koymamak.",
     "Yanlış ❌\n\n1 Ağustos 2026'dan beri menfaat karşılığı paylaşımlarda \"reklam\", \"iş birliği\" gibi açık bir ifade zaten zorunlu. "
     "Etkileşimi belirleyen de etiket değil, içeriğin kendisi. Kitleniz iş birliğini sizden saklamadığınızda size daha çok güvenir."),
    ("Mikro içerik üreticileri sadece küçük markalar içindir.",
     "Yanlış ❌\n\nBüyük markalar da birden çok mikro hesapla çalışmayı seçebiliyor: farklı şehirlere ve ilgi alanlarına aynı anda ulaşmak, "
     "hangi mesajın tuttuğunu görmek için. Küçük hesapların yakın topluluğu her bütçede değerli."),
    ("Viral olan iş birliği içeriği satış da getirir.",
     "Her zaman değil 🤏\n\nViral içerik çok kişiye ulaşır ama o kişiler ürünün müşterisi olmayabilir. Satış hedefli kampanyada doğru kitle, "
     "net bir neden (kod, teklif) ve kolay bir yol (link) gerekir. Bazen 20 bin doğru kişi, 2 milyon rastgele kişiden fazlasını yapar."),
    ("Bir markaya \"hayır\" demek ilişkiyi bozar.",
     "Yanlış ❌\n\nKibar ve gerekçeli bir \"hayır\" profesyonelliktir: \"Bu ürün kitleme uymuyor ama ileride şu kategoride çalışmak "
     "isterim.\" Uymayan işi kabul edip kötü sonuç almak ilişkiyi asıl o zaman bozar. Biz de kitlesine uymayan teklifleri içerik "
     "üreticilerimize iletmiyoruz."),
]

# Perşembe 18:00 · Sahne Arkası
SAHNE = [
    ("Sahne arkası 🧊\n\nBir marka bize ulaştığında süreç 3 adımda ilerliyor:\n\n1. Tanışma: Kısa bir form ve ilk görüşmeyle markayı ve "
     "beklentileri dinliyoruz.\n2. Profil seçimi: Sahte takipçi denetiminden geçmiş, markaya uygun içerik üreticilerini listeliyoruz.\n3. "
     "Kampanya: Fiyat ve kapsam netleşip teklif onaylanınca üretim başlıyor.\n\nSonrası mı? Raporlama.",
     "Markanız için ilk adımı atmak isterseniz: iletisim@igloocollective.com 💙"),
    ("Sahne arkası 🧊\n\nBir içerik üreticisini markaya önermeden önce neye bakıyoruz?\n\n• Takipçi kalitesi: Kitle gerçek mi?\n• "
     "Etkileşim oranı: Kitle içerikle ilgileniyor mu?\n• Büyüme geçmişi: Ani ve açıklanamayan sıçramalar var mı?\n• Alan ve kitle "
     "uyumu: Ürün bu profilde doğal duruyor mu?\n\nTakipçi sayısı listede en son geliyor.", None),
    ("Sahne arkası 🧊\n\nAğımıza başvuran bir içerik üreticisi için süreç şöyle: Başvuru formunu dolduruyorsunuz, profilinizi ortalama 3–5 "
     "iş günü içinde değerlendiriyoruz. Uygun bir kampanya geldiğinde profilinizi markaya öneriyoruz.\n\nDürüst olalım: Her öneri iş "
     "birliğine dönüşmüyor. Son kararı kampanyanın kriterleri, bütçesi ve markanın tercihi belirliyor.",
     "Başvuru formu: {LINK} 🧊"),
    ("Sahne arkası 🧊\n\nİletişim tarafında içerik üreticilerimiz için ne yapıyoruz?\n\nHer birine iş birlikleri için profesyonel bir "
     "e-posta adresi açıyoruz. DM'den ya da başka kanallardan gelen teklifleri bu adrese yönlendiriyor ve karşılıyoruz.\n\nAlanına ya da "
     "kitlesine uymayan teklifler içerik üreticisinin önüne gelmiyor. Hangi işi yapacağına yine kendisi karar veriyor.", None),
    ("Sahne arkası 🧊\n\nKomisyon tarafında nasıl çalışıyoruz?\n\nKomisyonumuzu markadan alıyoruz. İçerik üreticisinin kazancından kesinti "
     "yapmıyoruz. Koşulları da en baştan, yazılı olarak paylaşıyoruz.\n\nBizce bir iş birliği ilişkisinde en önemli şey, kimin neyi "
     "kazandığının en başta net olması.", None),
    ("Sahne arkası 🧊\n\nİşin bir de görünmeyen kısmı var: fatura ve vergi.\n\nŞahıs şirketi, esnaf muafiyeti, stopaj... İlk iş birliğinde "
     "en çok soru buradan geliyor. Bu süreçlerde içerik üreticilerimize destek oluyoruz.\n\nSözleşmelerimizde içerik üreticisini zor "
     "durumda bırakan ağır cezai şartlar da yok. İş birliği güvenle başlamalı.", CTA_CREATOR),
    ("Sahne arkası 🧊\n\n2026'nın son gününde kısa bir teşekkür.\n\nBu yıl bize başvuran, brief'ini paylaşan, mesajlarımıza dönen ve "
     "kampanyalarda emek veren herkese: İyi ki. Doğru eşleşmeleri ancak birlikte kurabiliyoruz.\n\n2027'de daha çok sohbet, daha net "
     "brief'ler ve daha adil iş birlikleri diliyoruz 💙🧊", None),
]

# Cuma 18:00 · Teklif Kutusu
TEKLIF = [
    ("Teklif kutusu 📩\n\nİyi bir teklif mesajında olması gereken 5 şey:\n\n1. Markanın ve kampanyanın kısa tanıtımı\n2. Teslim kalemleri: "
     "kaç içerik, hangi format\n3. Tarihler: çekim, onay, yayın\n4. Kullanım hakkı var mı?\n5. Bütçe ya da bütçe aralığı\n\nBunların çoğu "
     "yoksa bu henüz bir teklif değil, ilk temas. Eksikleri sormak tamamen normal.", None),
    ("Teklif kutusu 📩\n\nBu dönem sık görülen bir teklif tipi: sadece satış payıyla çalışma.\n\nNe zaman mantıklı? Ürün kitlenize "
     "gerçekten uyuyorsa, kod ve link takibi şeffafsa, payın oranı ve ödeme günü yazılıysa.\n\nNe zaman dikkat? Çok sayıda içerik isteniyor "
     "ama sabit hiçbir ücret yoksa. O zaman riskin tamamını siz taşıyorsunuz.",
     "Hatırlatma: Kod üzerinden komisyon ya da ürün alıyorsanız bu da bir menfaat; paylaşımda \"reklam\" ya da \"iş birliği\" ifadesi "
     "gerekiyor."),
    ("Teklif kutusu 📩\n\nTeklifte kırmızı bayraklar 🚩\n\n• \"Önce paylaş, beğenirsek ödeme yaparız.\"\n• Ücret yok ama 5 Reels "
     "isteniyor.\n• Kullanım hakkı \"süresiz\" ve \"tüm mecralar\".\n• Size iş bulmak için sizden ücret isteyen yapılar.\n\nBunlardan biri "
     "varsa durun ve soru sorun. İkisi varsa geçin.", None),
    ("Teklif kutusu 📩\n\n\"Ücretsiz paylaşım yapar mısınız?\" mesajına kibar bir cevap örneği:\n\n\"Merhaba, düşündüğünüz için "
     "teşekkürler. İş birliklerimi ücretli olarak planlıyorum. Kapsamı ve tarihleri paylaşırsanız size bir teklif hazırlayabilirim.\"\n\n"
     "Kibar, net ve kapıyı kapatmıyor. Kaydedin, gerektiğinde kopyalayın 🔖", None),
    ("Teklif kutusu 📩\n\n\"Bir de story atar mısın?\" Kapsam kayması böyle başlar.\n\nKampanya sırasında gelen her ek istek, ek bir "
     "teslim kalemidir. Kibarca şöyle diyebilirsiniz:\n\n\"Tabii, bu anlaşmanın dışında bir kalem olduğu için ek ücretiyle birlikte "
     "planlayalım.\"\n\nİlk seferde söylemek, ikinciyi ve üçüncüyü önler.", None),
    ("Teklif kutusu 📩\n\nYıl sonu yaklaştı, son dakika teklifleri geliyor: \"Yarın yayında olabilir mi?\"\n\nAcil işlerde 3 şeye "
     "dikkat:\n1. Takviminiz gerçekten uygun mu?\n2. Onay süreci de aynı hızda olacak mı?\n3. Acil teslimin bir ek ücreti var mı?\n\nHızlı "
     "iş bir hizmettir ve fiyatı vardır.", None),
]

# Cumartesi 18:00 · Kaydet Listesi (görsel kartlı): (kart başlığı, kart maddeleri, metin, ilk yorum, konu)
KAYDET = [
    ("Medya kiti kontrol listesi",
     ["Bir cümlelik tanıtım: kimsiniz, ne üretiyorsunuz", "Takipçi ve ortalama görüntülenme (son 3 ay)",
      "Kitle: yaş, cinsiyet, şehir dağılımı", "En iyi 3 içerik ve linkleri", "Geçmiş iş birlikleri ve sonuçları",
      "Ürettiğiniz içerik türleri: Reels, story, UGC...", "İletişim e-postası"],
     "Kaydet listesi 🔖\n\nMedya kitinizi göndermeden önce kontrol edin: 7 madde görselde.\n\nEn sık unutulanlar güncel rakamlar ve "
     "iletişim e-postası. Sizde hangisi eksikti? 👇", None, "İçerik Üreticisi"),
    ("Teklife cevap vermeden önce sorun",
     ["Kaç içerik ve hangi formatta?", "Çekim, onay ve yayın tarihleri ne?", "İçerik onayı kimde, ne kadar sürede?",
      "Kullanım hakkı var mı? Süre ve mecra?", "Münhasırlık isteniyor mu?", "Ödeme ne zaman ve nasıl yapılacak?"],
     "Kaydet listesi 🔖\n\nTeklif geldi, fiyat vermeden önce bu 6 soruyu sorun. Hepsi görselde.\n\nCevaplar netleşince doğru fiyatı "
     "vermek çok daha kolay.", None, "Marka İş Birliği"),
    ("Marka brief'i kontrol listesi",
     ["Kampanya amacı: bilinirlik, satış ya da güven", "Hedef kitle: yaş, şehir, ilgi alanı", "Ana mesaj ve olmazsa olmazlar",
      "Yapılmaması gerekenler", "Teslim kalemleri ve tarihler", "Kullanım hakkı ve münhasırlık", "Bütçe aralığı ve ölçüm yöntemi"],
     "Kaydet listesi 🔖\n\nMarkalar için: Brief'i göndermeden önce bu 7 maddeyi kontrol edin. Görselde.\n\nİyi brief, iyi içeriğin "
     "yarısıdır.", CTA_BRAND, "Influencer Marketing"),
    ("Yayın günü kontrol listesi",
     ["\"Reklam\" ya da \"iş birliği\" ifadesi ilk bakışta görünüyor", "Marka etiketi ve hesap adı doğru",
      "Link ya da kod çalışıyor", "Yayın saati takvimle aynı", "İlk saat yorumlara cevap verildi", "48. saat ekran görüntüsü alındı",
      "7. gün ekran görüntüsü ve kapanış mesajı"],
     "Kaydet listesi 🔖\n\nİş birliği içeriğinin yayın günü için 7 adımlık kontrol listesi görselde.\n\nEn kritik olanı ilk madde: 1 "
     "Ağustos 2026'dan beri zorunlu.", None, "İçerik Üreticisi"),
    ("Kampanya raporu şablonu",
     ["Yayın linkleri ve tarihleri", "Erişim ve görüntülenme", "Etkileşim: beğeni, yorum, kaydetme, paylaşım",
      "İzlenme süresi (videolar için)", "Link tıklaması ve kod kullanımı", "Öne çıkan yorumlar", "Bir sonraki kampanya için 2 öneri"],
     "Kaydet listesi 🔖\n\nKampanya bitti, rapor zamanı. 7 başlıklı şablon görselde.\n\nİçerik üreticisi için portfolyo, marka için "
     "öğrenme belgesi. İkisi için de bir sonraki işin referansı.", None, "Influencer Marketing"),
    ("2027'ye hazırlık listesi",
     ["Medya kitindeki rakamları güncelleyin", "Fiyat kartınızı gözden geçirin", "2026'nın en iyi 5 işini portfolyoya ekleyin",
      "Fatura ve gider düzeninizi kurun", "Çalışmak istediğiniz 5 markayı yazın", "İş birlikleri için ayrı bir e-posta açın",
      "Yeni bir format denemek için tarih koyun"],
     "Kaydet listesi 🔖\n\nYeni yıla girmeden önce içerik üreticileri için 7 maddelik hazırlık listesi görselde.\n\nHangisini bu hafta "
     "yapacaksınız? 👇", CTA_CREATOR, "İçerik Üreticisi"),
]

# Pazar 18:00 · Pazar Okuması
PAZAR = [
    "Pazar okuması ☕\n\nNeden \"doğru içerik üretici\" diyoruz?\n\nÇünkü bir iş birliğini çoğu zaman bütçe ya da takipçi sayısı değil, "
    "eşleşme kurtarıyor: Ürünü gerçekten kullanacak bir kitle, ürünü kendi diliyle anlatabilen bir içerik üretici ve bunu bekleyen bir "
    "marka.\n\nBu üçü buluştuğunda reklam reklam gibi durmuyor. Sonuç da gerçek oluyor.",
    "Pazar okuması ☕\n\nKüçük hesapların gücü üzerine.\n\n5 bin takipçili bir hesabın yorumlarında herkes birbirini tanıyormuş gibi "
    "konuşur. Öneri bir arkadaştan geliyormuş gibi algılanır.\n\nBüyük hesaplar çok kişiye ulaşır, küçük hesaplar yakınlık kurar. İyi bir "
    "kampanya planı ikisinin de nerede işe yaradığını bilir.",
    "Pazar okuması ☕\n\nBir iş birliğinin en uzun kısmı yayın değil, hazırlık.\n\nYayın birkaç saniyede olur. Öncesinde brief, eşleşme, "
    "teklif, fikir, çekim, onay ve revizyon var. Sonrasında da rapor.\n\nİçerik iyi görünüyorsa arkasında genelde iyi hazırlanmış bir süreç "
    "vardır. Görünmeyen kısım, görüneni belirliyor.",
    "Pazar okuması ☕\n\nGüven etiketle başlar.\n\n\"Reklam\" yazmak bir zamanlar çekinilen bir şeydi. Bugün hem zorunlu hem de bizce bir "
    "güven işareti: \"Bunu sizden saklamıyorum ve yine de öneriyorum.\"\n\nKitle, iş birliği yaptığını açıkça söyleyen içerik üreticisinin "
    "diğer önerilerine de daha çok inanır.",
    "Pazar okuması ☕\n\nSohbet eden markalar üzerine.\n\nThreads, yayın yapmaktan çok konuşmanın platformu. Burada öne çıkan markalar "
    "genelde en çok paylaşım yapanlar değil; yorumlara cevap veren, soru soran ve kendine gülebilenler.\n\nBiz de bu yüzden buradayız: "
    "sorularınızı cevaplamak ve sizinkileri öğrenmek için 💙",
    "Pazar okuması ☕\n\nYılın son pazarı.\n\nBu yıl birçok içerik üreticisi ilk iş birliğini yaptı, birçok marka ilk kez bir içerik "
    "üreticisiyle çalıştı. İlkler hep biraz karışık olur: fiyatlar, brief'ler, takvimler.\n\nİkinciler daha iyi geçer. 2027 ikinciler yılı "
    "olsun 🧊",
]

# 21:00 · Akşam Sohbeti (pazartesi–cumartesi), tarih sırasıyla: (tarih, metin, ilk yorum, konu)
AKSAM = [
    ("2026-11-17", "Akşam sohbeti 💬\n\nBir markadan gelen en tuhaf iş birliği teklifi neydi? İsim vermeden anlatın, yorumlarda birlikte gülelim 😅",
     "Bizden başlasın: Bize gelen başvuruların bir kısmı \"Ürünlerinizi uzun zamandır kullanıyorum\" diye başlıyor. Ürünümüz yok 😭💙", "Sosyal Medya"),
    ("2026-11-18", "Akşam sohbeti 💬\n\nİçerik üretmeye ne zaman başladınız? İlk videonuzu hâlâ izleyebiliyor musunuz, yoksa arşivde mi saklanıyor? 🙈",
     None, "İçerik Üreticisi"),
    ("2026-11-19", "Akşam sohbeti 💬\n\n\"Bunu kim izler ki\" deyip paylaştığınız ama en çok izlenen içeriğiniz hangisiydi?", None, "İçerik Üreticisi"),
    ("2026-11-20", "Akşam sohbeti 💬\n\nCuma akşamı sorusu: Markalara tek bir cümle söyleme hakkınız olsa ne söylerdiniz?",
     "Bizimki: \"Brief'e bütçe aralığını da yazın, herkesin hayatı kolaylaşacak.\" 😄", "İçerik Üreticisi"),
    ("2026-11-21", "Akşam sohbeti 💬\n\nİçerik fikirleri aklınıza en çok nerede geliyor? Duşta, yolda, gece 3'te? 🌙", None, "İçerik Üreticisi"),
    ("2026-11-23", "Akşam sohbeti 💬\n\nMarkalar, sıra sizde: İçerik üreticilerine tek bir cümle söyleme hakkınız olsa ne söylerdiniz?",
     "Bizimki: \"Medya kitinizi güncel tutun, gerisini birlikte konuşuruz.\" 💙", "Influencer Marketing"),
    ("2026-11-24", "Bugün Öğretmenler Günü 💙\n\nİçerik üretmeyi size kim öğretti? Bir öğretmen, bir arkadaş, YouTube'da izlediğiniz biri... "
     "Etiketleyin, birlikte teşekkür edelim.", None, "İçerik Üreticisi"),
    ("2026-11-25", "Akşam sohbeti 💬\n\nİçerik üreticiliğinin kimsenin bahsetmediği zor yanı ne sizce?", None, "İçerik Üreticisi"),
    ("2026-11-26", "Akşam sohbeti 💬\n\nBir iş birliğinden sonra aldığınız ve sizi en çok sevindiren takipçi yorumu neydi?", None, "İçerik Üreticisi"),
    ("2026-11-27", "Akşam sohbeti 💬\n\nEfsane Cuma itirafı: İçerik üretmek için alıp hiç kullanmadığınız bir ekipman var mı? 😄", None, "Sosyal Medya"),
    ("2026-11-28", "Akşam sohbeti 💬\n\nHaftada kaç saatinizi içerik üretmeye ayırıyorsunuz? Dürüst olun: çekim, kurgu ve \"fikir düşünme\" dahil 😄",
     None, "İçerik Üreticisi"),
    ("2026-11-30", "Akşam sohbeti 💬\n\nTelefonunuzdaki en vazgeçilmez içerik uygulaması hangisi? Kurgu, fotoğraf, planlama... Önerin, listeyi büyütelim 📱",
     None, "İçerik Üreticisi"),
    ("2026-12-01", "Akşam sohbeti 💬\n\nÇöpe attığınız bir içerik fikrini sonradan çekip \"iyi ki\" dediğiniz oldu mu?", None, "İçerik Üreticisi"),
    ("2026-12-02", "Akşam sohbeti 💬\n\nVerdiğiniz bir \"hayır\" cevabı sonradan iyi ki dedirtti mi? Hikâyesi varsa merak ediyoruz.", None, "İçerik Üreticisi"),
    ("2026-12-03", "Akşam sohbeti 💬\n\nİçerik üretirken en çok zamanınızı ne alıyor: fikir, çekim, kurgu yoksa açıklama metni? ✍️", None, "İçerik Üreticisi"),
    ("2026-12-04", "Akşam sohbeti 💬\n\nKendi alanınızda takip etmeyi önerdiğiniz bir içerik üreticisi var mı? Etiketleyin, birlikte keşfedelim 💙",
     None, "İçerik Üreticisi"),
    ("2026-12-05", "Akşam sohbeti 💬\n\nİçerik üreticisi olmasaydınız şu an ne iş yapıyor olurdunuz?", None, "Sosyal Medya"),
    ("2026-12-07", "Akşam sohbeti 💬\n\nMarkalar: Bu yıl denediğiniz ve iyi ki dediğiniz bir pazarlama fikri neydi?", None, "Influencer Marketing"),
    ("2026-12-08", "Akşam sohbeti 💬\n\nSize en çok emek veren ama en az ilgi gören içeriğiniz hangisiydi? Bazen en sevdiğimiz içerik algoritmanın en "
     "sevmediği oluyor 🙃", None, "İçerik Üreticisi"),
    ("2026-12-09", "Akşam sohbeti 💬\n\nBugünün mini itirafı: Bir teslim tarihini son dakikaya bıraktığınız oldu mu? 🙈", None, "İçerik Üreticisi"),
    ("2026-12-10", "Akşam sohbeti 💬\n\nAjans, menajer, yönetim... Sizce bir içerik üreticisi iş tarafında ne zaman desteğe ihtiyaç duyar?", None,
     "İçerik Üreticisi"),
    ("2026-12-11", "Akşam sohbeti 💬\n\nKendi içeriğinizde asla yapmayacağınız bir şey ne?", None, "İçerik Üreticisi"),
    ("2026-12-12", "Akşam sohbeti 💬\n\nBir kampanyada en çok eğlendiğiniz çekim hangisiydi? Hikâyesi varsa anlatın 🎬", None,
     "Marka İş Birliği"),
    ("2026-12-14", "Akşam sohbeti 💬\n\nGün ışığı mı, halka ışık mı? Çekim ışığı tartışmasında tarafınızı seçin ☀️", None, "İçerik Üreticisi"),
    ("2026-12-15", "Akşam sohbeti 💬\n\nBaşka bir içerik üreticisinden öğrendiğiniz ve hâlâ kullandığınız en iyi şey ne?", None, "İçerik Üreticisi"),
    ("2026-12-16", "Akşam sohbeti 💬\n\nMarkalar: Bir içerik üreticisiyle çalışmaya karar verirken sizi en çok ne etkiliyor?", None, "Influencer Marketing"),
    ("2026-12-17", "Akşam sohbeti 💬\n\nKışın içerik üretmek sizin için daha mı zor, daha mı kolay? Erken kararan akşamlar ışığı da etkiliyor 🌥️", None,
     "İçerik Üreticisi"),
    ("2026-12-18", "Akşam sohbeti 💬\n\nYıl bitmeden çekmek istediğiniz bir içerik var mı? Yazın, söz vermiş olun 😄", None, "İçerik Üreticisi"),
    ("2026-12-19", "Akşam sohbeti 💬\n\nTakipçilerinizden aldığınız en tatlı mesaj neydi? 💌", None, "İçerik Üreticisi"),
    ("2026-12-21", "Akşam sohbeti 💬\n\nBu gece yılın en uzun gecesi. Uzun bir gece için öneriniz ne: izlenecek, okunacak ya da dinlenecek bir şey 🌙",
     None, "Sosyal Medya"),
    ("2026-12-22", "Akşam sohbeti 💬\n\n2026'da en çok gurur duyduğunuz iş hangisiydi? Anlatın, birlikte sevinelim 💙", None, "İçerik Üreticisi"),
    ("2026-12-23", "Akşam sohbeti 💬\n\n2027'de denemek istediğiniz yeni bir format var mı? Uzun video, canlı yayın, podcast, Threads serisi...", None,
     "İçerik Üreticisi"),
    ("2026-12-24", "Akşam sohbeti 💬\n\nBu yıl takip etmeye başladığınız ve iyi ki dediğiniz bir hesap var mı? Etiketleyin 💙", None, "Sosyal Medya"),
    ("2026-12-25", "Akşam sohbeti 💬\n\nYılbaşı kampanyası içeriği çeken var mı? En çok hangi tema geliyor: hediye, sofra, parti? 🎁", None,
     "İçerik Üreticisi"),
    ("2026-12-26", "Akşam sohbeti 💬\n\nBu yıl bir markayla çalışırken öğrendiğiniz en önemli ders neydi?", None, "Marka İş Birliği"),
    ("2026-12-28", "Akşam sohbeti 💬\n\nYıl sonu sorusu: 2026'yı tek bir içerik başlığıyla özetleseniz ne olurdu? 🎬", None, "Sosyal Medya"),
    ("2026-12-29", "Akşam sohbeti 💬\n\nYılbaşında çalışan var mı? 😄 Hangi işler son dakikaya kaldı?", None, "İçerik Üreticisi"),
    ("2026-12-30", "Akşam sohbeti 💬\n\n2027 için tek bir dilek: İçerik üreticisi ya da marka olarak sektörde neyin değişmesini isterdiniz?", None,
     "Influencer Marketing"),
    ("2026-12-31", "Mutlu yıllar 💙🧊\n\n2027'de doğru eşleşmeler, adil iş birlikleri ve bol ilham diliyoruz. Bu yıl bizimle konuşan, soru soran, "
     "cevap veren herkese teşekkürler.\n\nYeni yılda da buradayız.", None, "Sosyal Medya"),
]

# Pazar 21:00 · Haftanın Özeti (o haftanın sözlük terimleri görselde) için ilk yorumlar
OZET_REPLIES = [CTA_CREATOR, CTA_BRAND, None, CTA_CREATOR, CTA_BRAND, None]
