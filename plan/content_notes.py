# -*- coding: utf-8 -*-
"""igloo Threads planı: açılış, 09:00 Günün Notu ve 11:00 Sektör Sözlüğü içerikleri."""

CTA_CREATOR = "İş birliklerinizi tek yerden ve profesyonelce yürütmek isterseniz ağımıza başvurabilirsiniz: {LINK} 💙"
CTA_BRAND = "Markanız için doğru içerik üreticisini birlikte seçelim: iletisim@igloocollective.com 🧊"

INTRO = {
    "text": (
        "Threads'te yeniden aktifiz 🧊💙\n\n"
        "Biz igloo collective: markaları doğru içerik üreticileriyle buluşturan, içerik üreticilerinin de iş tarafını "
        "yöneten bir ajansız.\n\n"
        "Bundan sonra her gün buradayız:\n"
        "09:00 günün notu\n11:00 sektör sözlüğü\n13:00 öğle arası\n18:00 akşam serisi\n21:00 akşam sohbeti\n\n"
        "Creator'ın da markanın da sorusunu bekliyoruz 👇"
    ),
    "reply": "İlk soruyu biz soralım: Marka iş birliklerinde sizi en çok ne yoruyor? Fiyat konuşmak mı, brief mi, ödemeyi beklemek mi? 💬",
    "topic": "Influencer Marketing",
}

# 09:00 Günün Notu: içerik üreticileri (C) ve markalar (B) için sırayla
NOTES_C = [
    ("Medya kitiniz 10 sayfalık bir sunum olmak zorunda değil. Markanın ilk 30 saniyede görmek istediği şunlar: kim olduğunuz, "
     "kitlenizin kim olduğu, son 3 ayın ortalama görüntülenmesi ve 2–3 örnek iş.\n\nGerisini soran markaya ayrıca gönderirsiniz.", None),
    ("Teklif mesajı geldiğinde ilk cevabınız fiyat değil, soru olsun: Kaç içerik, hangi format, yayın tarihi ne, içerik reklamda "
     "kullanılacak mı, ödeme ne zaman?\n\nKapsam netleşmeden verilen fiyat ya çok düşük kalır ya da işi kaçırır.", None),
    ("Her kampanyadan sonra istatistiklerin ekran görüntüsünü alın: görüntülenme, kaydetme, paylaşım, link tıklaması. "
     "Biri 48. saatte, biri 7. günde.\n\nBir sonraki markaya \"çok ilgi gördü\" demek yerine göstermek bambaşka bir şey.", None),
    ("Marka ekipleri profilinize genelde birkaç saniye bakar. Kendinize 3 soru sorun:\n\nBio'da ne ürettiğiniz tek cümleyle "
     "yazıyor mu? İletişim e-postası görünüyor mu? Son 9 gönderi alanınızı anlatıyor mu?\n\nÜçü de \"evet\"se ilk eleme geçildi.", None),
    ("Brief geldiğinde okuyup \"tamam\" demek yerine anladığınızı 3 cümleyle geri yazın: \"Şu kitleye, şu mesajı, şu formatta "
     "anlatacağım.\"\n\nYanlış anlaşılma varsa daha kamerayı açmadan ortaya çıkar.", None),
    ("Teklif verirken revizyon sayısını baştan yazın: \"Fiyata 1 revizyon dahildir.\"\n\nYazılmayan revizyon sınırsız gibi "
     "algılanıyor ve işin en yorucu kısmı çoğu zaman orası oluyor.", None),
    ("Ödeme vadesini konuşmak ayıp değil. \"Yayından sonra 30 gün içinde\" mi, \"faturadan sonra 15 gün\" mü?\n\nTarihi yazıya "
     "dökün. Bir aksilik olursa elinizde bir referans olur, kimse kimseyi kovalamak zorunda kalmaz.", None),
    ("Her teklifi kabul etmek zorunda değilsiniz. Kitlenize uymayan bir ürünü tanıtmak kısa vadede para, uzun vadede güven "
     "kaybı.\n\nTakipçiniz \"bu da her şeyi tanıtıyor\" dediği an sonraki iş birliklerinin değeri düşer.", None),
    ("Marka içeriğinizi kendi hesabında ya da reklamlarında kullanmak isterse bu ayrı bir haktır ve genelde ayrıca fiyatlanır.\n\n"
     "Süreyi (ör. 3 ay) ve mecrayı (organik mi, reklam mı) teklifte açıkça yazın.", None),
    ("Videoda ürünü ilk 3 saniyede göstermek zorunda değilsiniz ama izleyiciyi ilk 3 saniyede tutmak zorundasınız.\n\nÖnce merak, "
     "sonra ürün. İş birliği içerikleri de bu kurala uyuyor.", None),
    ("Her konuda içerik üreten bir hesaptan çok, net bir alanı olan hesap markanın aklında kalır.\n\n\"Lifestyle\" geniş bir "
     "kelime. \"Kahve ve çalışma masası\" gibi dar bir alan, doğru markanın sizi bulmasını kolaylaştırır.", None),
    ("İş birliği içeriği yayınlandıktan sonraki ilk saat yorumlara cevap verin.\n\nMarkalar yorumlardaki sohbete de bakıyor. "
     "Kitlesiyle konuşan içerik üreticisi güven veriyor.", None),
    ("İlk iş birliğinden önce fatura tarafını netleştirin: Şahıs şirketi mi, istisna kapsamında mı, stopaj olacak mı?\n\n"
     "Bunu iş geldiğinde değil, önceden bir mali müşavirle konuşmak en hızlısı.", CTA_CREATOR),
    ("Brief'te \"yapılmaması gerekenler\" bölümü yoksa sorun: Rakip marka adı geçebilir mi, fiyat söylenebilir mi, kullanılmaması "
     "gereken kelimeler var mı?\n\nSonradan gelen \"bunu kaldıralım\" isteği çekimi baştan aldırabilir.", None),
    ("Markalar takipçi sayısının yanında görüntülenme ve kaydetme sayılarına da bakıyor.\n\nHer içeriği 30 bin kişiye ulaşan 10 bin "
     "takipçili bir hesap, 5 bin görüntülenen 100 bin takipçili bir hesaptan daha cazip olabilir.", None),
    ("Arka arkaya 3 reklam paylaşan profil, takipçide \"reklam hesabı\" algısı yaratabilir.\n\nBize göre güvenli denge: her iş "
     "birliği içeriğine en az 2–3 kendi içeriğiniz.", None),
    ("İş birlikleri için ayrı bir e-posta adresi açın ve bio'ya ekleyin.\n\nDM kutusunda kaybolan teklifler e-postada kaybolmaz. "
     "Marka ekipleri de resmî yazışmayı e-postadan yürütmeyi seviyor.", CTA_CREATOR),
    ("Fiyatınızı artırmanın en sağlam yolu rakamı değil kanıtı güncellemek: son kampanyanın sonuçları, kitlenizin değişen "
     "yapısı, yeni formatlar.\n\n\"Artık şu kadar\" derken yanında bir ekran görüntüsü olsun.", None),
    ("Kampanya bitince markaya kısa bir kapanış mesajı atın: yayın linkleri, 7 günlük sonuçlar ve bir teşekkür.\n\nBu 2 dakikalık "
     "mesaj, ikinci iş birliğinin en kısa yolu.", None),
    ("Bu hafta medya kitinizi açıp tek bir şeyi güncelleyin: son 3 ayın ortalama görüntülenmesi.\n\nMarkaya giden en eski rakam, "
     "profilinizi olduğundan zayıf gösteren rakamdır.", None),
]

NOTES_B = [
    ("İyi bir brief tek sayfaya sığar: amaç (bilinirlik mi satış mı), hedef kitle, ana mesaj, olmazsa olmazlar, yapılmaması "
     "gerekenler, teslim tarihleri ve bütçe aralığı.\n\nBütçe aralığı yazılmayan brief iki tarafın da vaktini alır.", None),
    ("Takipçi sayısına bakmadan önce takipçi kalitesine bakın: Yorumlar gerçek mi, kitle hangi şehir ve ülkelerden, büyüme "
     "grafiğinde açıklanamayan sıçramalar var mı?\n\nBir gecede gelen 20 bin takipçi genelde iyi haber değildir.", CTA_BRAND),
    ("Satış odaklı kampanyalarda tek büyük isim yerine birkaç nano ve mikro içerik üreticisiyle çalışmak riski dağıtır.\n\n"
     "Üstelik hangi kitlenin, hangi mesajın işe yaradığını da görürsünüz.", None),
    ("İçerik üreticisine metni kelime kelime yazıp vermek içeriği reklama çevirir.\n\nAna mesajı ve kırmızı çizgileri verin, "
     "anlatımı ona bırakın. Kitlesi onu kendi diliyle tanıyor.", None),
    ("Kampanya bitince \"ne kadar işe yaradı?\" sorusu havada kalmasın diye ölçümü en başta konuşun: hangi metrik, hangi süre, "
     "ekran görüntüleri ne zaman.\n\nKişiye özel indirim kodu ve UTM'li link takibi kolaylaştırır.", None),
    ("İçerik üreticisinden onay için 24 saatte dönüş bekliyorsanız siz de 24 saatte dönün.\n\nOnay süreci uzadıkça yayın tarihi "
     "kayar, içerik güncelliğini kaybeder.", None),
    ("İçeriği reklamlarda kullanmayı düşünüyorsanız bunu teklif aşamasında söyleyin.\n\nSonradan istenen kullanım hakkı hem "
     "pazarlığı zorlaştırır hem de bütçeyi şaşırtır.", None),
    ("Ürün göndermek bir iş birliği teklifi değildir. Paylaşım bekliyorsanız bunu ve karşılığını açıkça yazın; beklemiyorsanız "
     "\"paylaşım zorunluluğu yok\" deyin.\n\nBelirsizlik iki tarafı da zor durumda bırakıyor.", None),
    ("Reklam ifadesi yalnızca içerik üreticisinin sorumluluğu gibi görülmesin. 1 Ağustos 2026'dan beri menfaat karşılığı "
     "paylaşımlarda \"reklam\" ya da \"iş birliği\" gibi açık bir ifade zorunlu.\n\nBunu brief'e yazmak markayı da korur.", None),
    ("İçerik üreticisi seçerken en popüler 3 gönderisine değil, son 10 gönderisine bakın.\n\nOrtalama performans, kampanyada "
     "alacağınız sonuca en yakın tahmindir.", None),
    ("Influencer kampanyasını tek güne sıkıştırmayın. Teaser, lansman ve lansman sonrası deneyim içerikleriyle 2–3 haftaya "
     "yayılan plan, tek günlük bir patlamadan daha uzun yaşar.", CTA_BRAND),
    ("İçerik üreticileri de birer işletme. Ödemeyi söz verilen sürede yapan markalar, bir sonraki kampanyada doğru isimleri "
     "çok daha kolay bulur.\n\nVade yazılı olsun ve ona uyulsun.", None),
    ("Basit bir yazılı anlaşma bile çok şey kurtarır: teslim kalemleri, yayın tarihleri, revizyon sayısı, kullanım hakkı, "
     "ödeme vadesi ve iptal durumu.\n\nSözleşme güvensizlik değil, netlik demek.", None),
    ("Kampanya yayına girdiğinde yorumları da raporun parçası sayın.\n\n\"Nereden alabilirim?\", \"Fiyatı ne?\" gibi sorular "
     "gerçek ilginin en net işareti. Sayılardan önce bunlara bakın.", None),
    ("UGC ile influencer içeriği aynı şey değil. UGC'de içerik üreticisi içeriği kendi hesabında paylaşmaz; marka kendi "
     "kanallarında kullanır.\n\nErişim değil, içerik satın alıyorsunuz. Fiyatlama da buna göre değişir.", None),
    ("Reklamlarda yeniden kurgulamak için ham görüntü istiyorsanız bunu teklifte belirtin.\n\nHam görüntü ayrı bir teslim "
     "kalemidir ve kurgulanmış videodan farklı fiyatlanır.", None),
    ("Münhasırlık istiyorsanız kapsamını ve süresini net yazın: Hangi kategori, kaç ay?\n\nUzun ve geniş münhasırlık içerik "
     "üreticisinin gelirini kısıtlar. Bunun bir karşılığı olması da bu yüzden.", None),
    ("Yılbaşı ve özel gün kampanyalarında içerik üreticilerinin takvimi erken doluyor.\n\nŞubat'taki özel günler için konuşmaya "
     "Aralık'ta başlamak erken sayılmaz.", CTA_BRAND),
    ("Marka kitlesiyle içerik üreticisinin kitlesi örtüşüyor mu? Yaş, şehir, ilgi alanı.\n\nBunun için istatistik ekran "
     "görüntüsü istemek gayet normal. İyi içerik üreticileri bunu zaten hazır tutar.", None),
]

NOTE_SPECIAL = {
    "2026-11-27": ("Efsane Cuma notu 🛍️\n\nİndirim kodlu iş birliklerinde iki küçük hatırlatma:\n\n1. Kodun geçerlilik tarihini "
                   "içerikte yazın.\n2. Kod üzerinden komisyon ya da ürün alıyorsanız bu da bir menfaat; paylaşımda \"reklam\" ya da "
                   "\"iş birliği\" ifadesi ilk bakışta görünsün.\n\nBol satışlı bir gün dileriz 💙", None, "Influencer Marketing"),
    "2026-12-03": ("Bugün Dünya Engelliler Günü.\n\nİçerikleri daha çok kişiye ulaştırmanın en kolay iki yolu: videolara altyazı "
                   "eklemek ve görsellere alternatif metin yazmak.\n\nSesi kapalı izleyen herkes de altyazıdan faydalanıyor. Bir sonraki "
                   "iş birliği içeriğinde deneyin.", None, "Sosyal Medya"),
    "2026-12-28": ("Yıl sonu notları 1/4 📌\n\n2026, influencer paylaşımlarında \"reklam\" ifadesinin zorunlu olduğu yıl oldu.\n\n"
                   "Bize göre bu, sektör için iyi bir adım. Şeffaf iş birliği uzun vadede hem içerik üreticisine hem markaya "
                   "kazandırıyor.", None, "Influencer Marketing"),
    "2026-12-29": ("Yıl sonu notları 2/4 📌\n\nTakipçi sayısının tek başına çok şey söylemediğini daha çok kişi görüyor.\n\n"
                   "2027'de bize göre asıl konuşulacak olanlar görüntülenme, kaydetme, izlenme süresi ve gerçek yorumlar.", None,
                   "Influencer Marketing"),
    "2026-12-30": ("Yıl sonu notları 3/4 📌\n\nThreads Haziran'da Türkiye'ye geri döndü.\n\nYayından çok sohbetin öne çıktığı bir "
                   "platform. Burada konuşmayı bilen markalar ve içerik üreticileri için 2027 ilginç geçecek gibi görünüyor.", None,
                   "Sosyal Medya"),
    "2026-12-31": ("Yıl sonu notları 4/4 📌\n\nBu yıl bize en çok şunu öğretti: Her şeyden önce doğru eşleşme geliyor.\n\nDoğru "
                   "içerik üretici, gerçek sonuç. 2027'de görüşmek üzere 💙🧊", None, "Influencer Marketing"),
}

# 11:00 Sektör Sözlüğü: (terim, gönderi gövdesi, karttaki kısa tanım)
SOZLUK = [
    ("Brief",
     "Markanın kampanya için içerik üreticisine verdiği yol haritası: amaç, hedef kitle, ana mesaj, teslim kalemleri, tarihler ve "
     "yapılmaması gerekenler.\n\nÖrnek: \"18–25 yaş, kampüs hayatı, 1 Reels + 2 story, rakip marka adı geçmeyecek.\"\n\nİyi brief soruları "
     "azaltır. Okuduktan sonra hâlâ 5 sorunuz varsa eksik olan brief'tir, siz değil.",
     "Kampanyanın yol haritası: amaç, kitle, mesaj, kalemler, tarihler."),
    ("Teslim kalemi (deliverable)",
     "Kampanyada üretilecek ve ücrete dahil olan her bir içerik.\n\nÖrnek: 1 Reels + 3 story + 1 Threads gönderisi = 3 kalem.\n\n"
     "Teklifte kalemleri tek tek yazmak, sonradan gelen \"bir story daha atsak?\" isteğinin ücretli bir ek iş olduğunu baştan netleştirir.",
     "Ücrete dahil her içerik: 1 Reels, 3 story gibi."),
    ("Kullanım hakkı",
     "Markanın, içerik üreticisinin ürettiği içeriği kendi hesabında, sitesinde ya da reklamlarında kullanma izni.\n\nÖrnek: \"Video 3 ay "
     "boyunca markanın Instagram reklamlarında kullanılabilir.\"\n\nSüre ve mecra yazılmazsa tartışma çıkar. Kullanım hakkı ayrı bir "
     "değerdir ve genelde ayrıca fiyatlanır.",
     "İçeriğin markanın kanallarında ve reklamlarında kullanım izni."),
    ("Münhasırlık (exclusivity)",
     "İçerik üreticisinin belli bir süre rakip markalarla çalışmama şartı.\n\nÖrnek: \"Kampanya sonrası 2 ay boyunca başka bir kahve "
     "markasıyla iş birliği yapılmaz.\"\n\nKategori ve süre ne kadar genişse içerik üreticisi o kadar teklif kaçırır. Bu yüzden "
     "münhasırlığın da bir bedeli vardır.",
     "Belli bir süre rakip markalarla çalışmama şartı."),
    ("UGC (user generated content)",
     "İçerik üreticisinin marka için ürettiği ama kendi hesabında paylaşmadığı içerik. Marka bunu kendi hesabında ya da reklamlarında "
     "kullanır.\n\nÖrnek: Bir cilt bakım markasının reklamında gördüğünüz \"gerçek kullanıcı\" videosu.\n\nUGC'de satın alınan şey erişim "
     "değil, içeriğin kendisi. Fiyatlama da buna göre değişir.",
     "Marka için üretilen, markanın kendi kanallarında kullandığı içerik."),
    ("Medya kiti",
     "İçerik üreticisinin markalara gönderdiği tanıtım dosyası: kim olduğu, kitlesi, temel istatistikleri, örnek işleri ve iletişim "
     "bilgisi.\n\nÖrnek: Tek sayfalık bir PDF ya da bir link.\n\nKısa ve güncel olanı kazanır. 6 ay önceki rakamlarla gönderilen medya "
     "kiti, iyi bir profili olduğundan zayıf gösterebilir.",
     "Kitle, istatistik ve örnek işlerin olduğu tanıtım dosyası."),
    ("Etkileşim oranı",
     "Beğeni, yorum, kaydetme ve paylaşım toplamının erişime (bazı raporlarda takipçiye) bölünüp 100 ile çarpılması.\n\nÖrnek: 10.000 "
     "kişiye ulaşan ve 600 etkileşim alan gönderi: %6.\n\nHangi formülü kullandığınızı raporda yazın. Erişime göre ve takipçiye göre "
     "hesaplanan oranlar birbiriyle kıyaslanmaz.",
     "Etkileşimlerin erişime (ya da takipçiye) oranı."),
    ("Erişim (reach)",
     "İçeriği en az bir kez gören tekil kişi sayısı.\n\nÖrnek: Aynı kişi videoyu 3 kez izlese de erişim 1 artar.\n\nKampanyanın kaç "
     "kişiye ulaştığını erişim söyler. Gösterimle karıştırılmasın; yarın onu anlatıyoruz.",
     "İçeriği en az bir kez gören tekil kişi sayısı."),
    ("Gösterim (impression)",
     "İçeriğin ekranlarda kaç kez görüntülendiği. Aynı kişinin tekrar tekrar görmesi de sayılır. Bazı platformlar bunu "
     "\"görüntülenme\" olarak gösteriyor.\n\nÖrnek: 1 kişi videoyu 3 kez izlerse erişim 1, gösterim 3.\n\nGösterim erişimden belirgin "
     "şekilde büyükse içerik tekrar izleniyor demektir.",
     "İçeriğin ekranda görülme sayısı, tekrarlar dahil."),
    ("CPM (cost per mille)",
     "Bin gösterim başına maliyet.\n\nÖrnek: 10.000 TL'lik bir kampanya 500.000 gösterim aldıysa CPM = 20 TL.\n\nFarklı içerik "
     "üreticilerini ya da kampanyaları aynı terazide tartmanın en basit yolu. Tek başına yetmez ama iyi bir başlangıç.",
     "Bin gösterim başına maliyet."),
    ("Barter",
     "Ücret yerine ürün ya da hizmet karşılığında yapılan iş birliği.\n\nÖrnek: Bir restoranın akşam yemeği karşılığında story "
     "paylaşımı istemesi.\n\nBarter yanlış değil ama kapsamı net olmalı: Kaç paylaşım, ne zaman, zorunlu mu? Ürün de bir menfaat "
     "sayıldığı için reklam ifadesi burada da gerekiyor.",
     "Ücret yerine ürün ya da hizmet karşılığı iş birliği."),
    ("Marka elçisi (ambassador)",
     "Markayla tek seferlik değil, aylar süren düzenli bir iş birliği.\n\nÖrnek: 6 ay boyunca her ay 1 video + 2 story.\n\nKitle "
     "markayı aynı yüzle defalarca görünce güven oluşur. Uzun sürdüğü için münhasırlık ve ödeme takvimi daha da önemli hale gelir.",
     "Markayla aylar süren düzenli iş birliği."),
    ("PR paketi (seeding)",
     "Markanın, paylaşım şartı koymadan içerik üreticilerine ürün göndermesi.\n\nÖrnek: Yeni çıkan bir parfümün hediye kutusuyla 30 "
     "içerik üreticisine gönderilmesi.\n\nŞart yoksa paylaşmak zorunda değilsiniz. Paylaşırsanız da hediye bir menfaat; içerikte "
     "bunu belirtmek gerekiyor.",
     "Paylaşım şartı olmadan gönderilen ürün kutusu."),
    ("Mood board",
     "İçeriğin rengini, ışığını, havasını anlatan örnek görsellerden oluşan pano.\n\nÖrnek: \"Sıcak tonlar, gün ışığı, ev ortamı\" "
     "diye seçilmiş 8 örnek kare.\n\nUzun açıklamalardan daha hızlı anlaşılır. Marka beklentisini, içerik üreticisi de kendi tarzını "
     "tek bakışta gösterebilir.",
     "İçeriğin görsel havasını anlatan örnek pano."),
    ("Senaryo onayı",
     "Çekime geçmeden önce fikrin, akışın ya da metnin markaya onaylatılması.\n\nÖrnek: \"Açılış sahnesi, ürünün göründüğü an, "
     "kapanış cümlesi\" diye üç satırlık bir taslak.\n\nÇekimden sonra gelen \"bunu baştan alalım\" cümlesini çoğu zaman bu küçük "
     "adım önler. Kısa tutun, roman yazmayın.",
     "Çekimden önce fikrin ve akışın onaylatılması."),
    ("Revizyon hakkı",
     "Markanın teslim edilen içerikte isteyebileceği, ücrete dahil düzeltme sayısı.\n\nÖrnek: \"Fiyata 1 revizyon dahildir; "
     "sonrakiler ek ücrete tabidir.\"\n\nRevizyon içeriği düzeltmektir, yeniden çekmek değil. Bu farkı teklifte yazmak iki tarafı da "
     "korur.",
     "Ücrete dahil düzeltme sayısı; yeniden çekim değil."),
    ("Yayın takvimi",
     "Kampanyadaki her içeriğin hangi gün ve saatte yayına gireceğini gösteren plan.\n\nÖrnek: Teaser 3 Aralık 19:00, ana video 5 "
     "Aralık 20:00, hatırlatma story'si 7 Aralık.\n\nBirden çok içerik üreticisiyle çalışırken takvim hayat kurtarır. Aynı saatte "
     "çıkan 10 benzer içerik, kitleye kampanya değil gürültü gibi görünür.",
     "Her içeriğin hangi gün ve saatte yayınlanacağı."),
    ("Ödeme vadesi",
     "Ödemenin hangi tarihte yapılacağı. Genelde yayından ya da faturadan sonra belli bir gün sayısıyla yazılır.\n\nÖrnek: \"Ödeme, "
     "fatura tarihinden itibaren 30 gün içinde yapılır.\"\n\nVade baştan yazılırsa kimse kimseyi kovalamak zorunda kalmaz.",
     "Ödemenin ne zaman yapılacağı: faturadan sonra X gün gibi."),
    ("Hook (kanca)",
     "İzleyiciyi videonun ilk saniyelerinde ya da gönderinin ilk cümlesinde yakalayan açılış.\n\nÖrnek: \"Bu kahveyi 3 haftadır "
     "içiyorum ve bir şeyi kimse söylemiyor...\"\n\nİş birliği içeriğinde de kanca, ürünü öne koymaktan önce gelir. Önce merak, sonra "
     "ürün.",
     "İzleyiciyi ilk saniyelerde tutan açılış."),
    ("İzlenme süresi (retention)",
     "İzleyicilerin videoda ortalama ne kadar kaldığı ya da videonun yüzde kaçını izlediği.\n\nÖrnek: 30 saniyelik videoda "
     "ortalama 21 saniye izlenme = %70.\n\nGörüntülenme \"kaç kişi açtı\"yı, izlenme süresi \"kaç kişi kaldı\"yı söyler. İyi bir rapor "
     "ikisini birlikte gösterir.",
     "İzleyicinin videoda kaldığı ortalama süre ya da oran."),
    ("Kaydetme (save)",
     "Kullanıcının içeriği daha sonra bakmak üzere kaydetmesi.\n\nÖrnek: Bir tarif videosunu \"hafta sonu yaparım\" diye "
     "kaydetmek.\n\nBeğeni anlık bir tepki, kaydetme ise \"bu bana lazım olacak\" demek. Bilgi veren iş birliği içeriklerinde kaydetme "
     "sayısı çoğu zaman beğeniden daha anlamlı.",
     "İçeriğin sonra bakmak için kaydedilmesi."),
    ("Sahte takipçi",
     "Gerçek bir kişiye ait olmayan, satın alınmış ya da bot hesaplardan gelen takipçiler.\n\nİşaretleri: Bir gecede gelen binlerce "
     "takipçi, ilgisiz ülkelerden gelen kitle, kopyala yapıştır yorumlar.\n\nBir içerik üreticisini markaya önermeden önce bu denetimi "
     "yapıyoruz. Sahte kitleye yapılan reklam kimseye ulaşmaz.",
     "Satın alınmış ya da bot hesaplardan gelen takipçi."),
    ("Kitle demografisi",
     "Takipçilerin yaş, cinsiyet ve şehir/ülke dağılımı.\n\nÖrnek: Kitlenin %70'i 18–34 yaş; en çok İstanbul, İzmir ve "
     "Ankara.\n\nMarka için takipçi sayısından önce şu soru gelir: \"Benim müşterim burada mı?\" İstatistik ekran görüntüsünü medya "
     "kitinde hazır tutmak işi hızlandırır.",
     "Takipçilerin yaş, cinsiyet ve konum dağılımı."),
    ("Marka güvenliği (brand safety)",
     "Markanın adının, değerleriyle çelişen içeriklerle yan yana gelmemesi.\n\nÖrnek: Çocuklara yönelik bir markanın, küfürlü "
     "içerikler üreten bir hesapla çalışmaması.\n\nMarkalar içerik üreticisinin son gönderilerine bu gözle de bakar. Bu bir yargılama "
     "değil, uyum meselesi.",
     "Markanın değerleriyle çelişen içeriklerden uzak durması."),
    ("Dönüşüm (conversion)",
     "İzleyicinin kampanyada hedeflenen eylemi yapması: satın alma, kayıt, uygulama indirme gibi.\n\nÖrnek: Linke tıklayan 1.000 "
     "kişiden 30'unun satın alması = %3 dönüşüm.\n\nHer kampanyanın amacı dönüşüm değildir. Bilinirlik kampanyasını yalnızca satışla "
     "ölçmek, maratoncuyu 100 metrede yarıştırmaya benzer.",
     "İzleyicinin satın alma, kayıt gibi hedef eylemi yapması."),
    ("ROAS (return on ad spend)",
     "Reklama harcanan her 1 TL'nin geri getirdiği gelir.\n\nÖrnek: 20.000 TL harcanan kampanya 60.000 TL satış getirdiyse ROAS = "
     "3.\n\nSatış odaklı influencer kampanyalarında bakılan temel oranlardan biri. Ölçebilmek için kişiye özel indirim kodu ya da "
     "takip linki şart.",
     "Harcanan her 1 TL'nin getirdiği gelir."),
    ("UTM",
     "Linkin sonuna eklenen ve ziyaretin nereden geldiğini gösteren küçük etiketler.\n\nÖrnek: Linkin sonuna eklenen ?utm_source=threads&"
     "utm_campaign=aralik ifadesi.\n\nHer içerik üreticisine ayrı UTM vermek, hangi iş birliğinin siteye kaç kişi getirdiğini analiz "
     "araçlarında ayrı ayrı görmeyi sağlar.",
     "Ziyaretin kaynağını gösteren link etiketi."),
    ("İndirim kodu",
     "İçerik üreticisine özel tanımlanan ve takipçilere indirim sağlayan kod.\n\nÖrnek: AYSE15 ile %15 indirim.\n\nHem takipçiye bir "
     "neden verir hem de markaya hangi içerik üreticisinin kaç satış getirdiğini gösterir. Kodun bitiş tarihini içerikte yazmayı "
     "unutmayın.",
     "İçerik üreticisine özel, satışı izlenebilir indirim kodu."),
    ("Satış ortaklığı (affiliate)",
     "İçerik üreticisinin, kendi linki ya da kodu üzerinden gelen her satıştan pay aldığı model.\n\nÖrnek: Kodla gelen her satışın "
     "%10'u.\n\nRiskin tamamı içerik üreticisinde olduğu için tek başına her zaman adil değil. Sabit ücret ve satış payı karması iki "
     "tarafı da dengeler.",
     "Link ya da kodla gelen satıştan pay alma modeli."),
    ("Ortak gönderi (collab)",
     "Instagram'da iki hesabın birlikte paylaştığı ve iki profilde de görünen gönderi. Beğeni ve yorumlar ortak toplanır.\n\n"
     "Örnek: Gönderinin üstünde içerik üreticisinin ve markanın adının birlikte yazması.\n\nMarkanın takipçileri içerik üreticisini, "
     "içerik üreticisinin kitlesi markayı görür. Teklifte collab olup olmayacağını yazmak iyi olur.",
     "İki hesabın birlikte paylaştığı, iki profilde görünen gönderi."),
    ("Ücretli ortaklık etiketi",
     "Instagram'da iş birliği gönderilerinin üstünde görünen \"Ücretli ortaklık\" ibaresi; marka adı da yanında çıkar.\n\nTürkiye'de 1 "
     "Ağustos 2026'dan beri menfaat karşılığı paylaşımlarda \"reklam\", \"iş birliği\" gibi açık bir ifade zorunlu. Platform etiketini "
     "kullanmak şeffaflığı güçlendirir; açıklamadaki ifadeyi de unutmayın.",
     "Instagram'daki \"Ücretli ortaklık\" ibaresi."),
    ("Ortaklık reklamı (partnership ads)",
     "Markanın, içerik üreticisinin gönderisini onun izniyle reklam olarak yayınlaması. Reklamda iki isim birlikte görünür.\n\n"
     "Örnek: Akışta içerik üreticisinin ve markanın adıyla çıkan sponsorlu bir video.\n\nİçerik üreticisinin adı reklamda kullanıldığı "
     "için bu da bir kullanım hakkıdır: süresi ve ücreti ayrıca konuşulur.",
     "Creator gönderisinin, onun adıyla reklam olarak yayınlanması."),
    ("Nano, mikro, mid-tier",
     "İçerik üreticilerini takipçi sayısına göre ayıran yaygın bir sınıflandırma. Sınırlar kaynağa göre değişir; sık kullanılan "
     "aralıklar:\nnano: 1–10 bin\nmikro: 10–100 bin\nmid-tier: 100–500 bin\n\nKüçük hesapların genelde daha yakın bir topluluğu olur. "
     "Kampanyalarımızda en çok bu üç grupla çalışıyoruz.",
     "Takipçiye göre gruplar: 1–10 bin, 10–100 bin, 100–500 bin."),
    ("Ham görüntü (raw footage)",
     "Kurgulanmamış, olduğu gibi teslim edilen video kayıtları.\n\nÖrnek: Ürünün kutudan çıkışının kesintisiz 4 dakikalık "
     "çekimi.\n\nMarka bunları kendi reklamları için yeniden kurgulamak ister. Ham görüntü ayrı bir teslim kalemidir; teklifte ayrıca "
     "yazılıp fiyatlanması gerekir.",
     "Kurgulanmamış video kayıtları; ayrı bir teslim kalemi."),
    ("Hesap devri (takeover)",
     "İçerik üreticisinin belli bir süre markanın hesabında içerik yayınlaması.\n\nÖrnek: Bir festival günü boyunca markanın "
     "story'lerini içerik üreticisinin hazırlaması.\n\nMarka yeni bir ses kazanır, içerik üreticisi yeni bir kitleyle tanışır. Şifre "
     "paylaşmak yerine içerikleri marka ekibine teslim etmek daha güvenli.",
     "İçerik üreticisinin markanın hesabında içerik yayınlaması."),
    ("Kampanya raporu",
     "Kampanya bittiğinde sonuçları özetleyen belge: yayın linkleri, erişim, görüntülenme, etkileşim, link tıklamaları ve öne çıkan "
     "yorumlar.\n\nÖrnek: Her içerik için 48. saat ve 7. gün ekran görüntüleri.\n\nRapor, bir sonraki kampanyanın en güçlü referansı. "
     "İçerik üreticisi için portfolyo, marka için öğrenme belgesi.",
     "Kampanya sonuçlarını özetleyen belge."),
    ("CTA (call to action)",
     "İzleyiciden istenen net eylem.\n\nÖrnek: \"Linke tıkla\", \"Kaydet, sonra dene\", \"Hangisini seçerdin? Yoruma yaz.\"\n\nİş "
     "birliği içeriğinde tek ve net bir CTA, üç ayrı istekten daha iyi çalışır. Kampanyanın amacına göre seçilir: bilinirlikte "
     "yorum, satışta tıklama.",
     "İzleyiciden istenen tek ve net eylem."),
    ("Konu etiketi",
     "Threads'te gönderiyi bir konuya bağlayan etiket. Gönderi o konunun akışında, konuyla ilgilenen kişilere de gösterilebilir.\n\n"
     "Örnek: Bu gönderinin \"Dijital Pazarlama\" etiketi.\n\nHashtag kalabalığı yerine gönderiyle gerçekten ilgili tek bir konu seçmek "
     "daha etkili. Threads da konu etiketli gönderilerin genelde daha çok görüntülendiğini söylüyor.",
     "Threads'te gönderiyi bir konunun akışına bağlayan etiket."),
    ("Organik ve ücretli erişim",
     "Organik: İçeriğin reklam bütçesi olmadan, takipçiler ve öneri akışları üzerinden ulaştığı kitle. Ücretli: Reklamla ulaşılan "
     "kitle.\n\nÖrnek: Bir Reels'in ilk 3 günde kendiliğinden ulaştığı 40 bin kişi organiktir.\n\nİyi performans gösteren organik "
     "içeriği reklamla desteklemek çoğu zaman sıfırdan reklam üretmekten daha verimli.",
     "Reklamsız ulaşılan ve reklamla ulaşılan kitle."),
    ("A/B testi",
     "Aynı içeriğin iki versiyonunu karşılaştırıp hangisinin daha iyi çalıştığını ölçmek.\n\nÖrnek: Aynı videonun iki farklı açılış "
     "cümlesiyle reklamda yarıştırılması.\n\nInfluencer kampanyalarında da işe yarar: Farklı içerik üreticileri farklı mesajları "
     "denediğinde hangi mesajın kitleye ulaştığı netleşir.",
     "İki versiyonu karşılaştırıp kazananı ölçmek."),
    ("Link çıkartması",
     "Instagram story'lerinde izleyicinin dokunup bir siteye gitmesini sağlayan çıkartma.\n\nÖrnek: \"Ürünü incele\" yazan bir "
     "link çıkartması.\n\nSatış ya da kayıt hedefli kampanyalarda story'nin en değerli parçası. Link UTM'li olursa kaç kişinin "
     "geldiği de ölçülür.",
     "Story'de siteye götüren çıkartma."),
    ("Teaser",
     "Lansmandan önce, ne geleceğini tam söylemeden merak uyandıran içerik.\n\nÖrnek: \"Cuma günü masamda yeni bir şey olacak 👀\" "
     "diye kutunun yalnızca bir köşesinin göründüğü story.\n\nTeaser'lı kampanyalarda lansman günü kitle zaten bekliyor oluyor. Tek "
     "bir içerikten çok küçük bir hikâye kurulur.",
     "Lansmandan önce merak uyandıran ipucu içerik."),
    ("Lansman",
     "Ürünün ya da kampanyanın resmî olarak duyurulduğu an.\n\nÖrnek: Yeni koleksiyonun aynı akşam 10 içerik üreticisinin "
     "paylaşımıyla tanıtılması.\n\nLansman günü yoğun geçer ama hikâye orada bitmez. Sonraki günlerde gelen deneyim içerikleri "
     "ilgiyi canlı tutar.",
     "Ürünün ya da kampanyanın resmî çıkış anı."),
    ("İptal bedeli (kill fee)",
     "İş başladıktan sonra marka kampanyayı iptal ederse, harcanan emeğin karşılığı olarak ödenen bedel.\n\nÖrnek: \"Çekim "
     "sonrası iptalde ücretin %50'si ödenir.\"\n\nNadiren gerekir ama yazılı olması iki tarafı da rahatlatır. Hazırlık, çekim ve "
     "kurgu zaman demek; zaman da emek.",
     "Marka işi yarıda iptal ederse ödenen bedel."),
    ("Fiyat kartı (rate card)",
     "İçerik üreticisinin içerik türlerine göre başlangıç fiyatlarını gösteren liste.\n\nÖrnek: Reels, story seti, Threads gönderisi "
     "ve UGC video için ayrı ayrı başlangıç fiyatı.\n\n\"Başlangıç\" kelimesi önemli: Kullanım hakkı, münhasırlık ve acil teslim "
     "fiyatı değiştirir. Kartı yılda en az iki kez güncelleyin.",
     "İçerik türlerine göre başlangıç fiyatları listesi."),
]
