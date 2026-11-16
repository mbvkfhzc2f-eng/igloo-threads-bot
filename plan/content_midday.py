# -*- coding: utf-8 -*-
"""igloo Threads planı: 13:00 Öğle Arası. Her gün başka bir paylaşılabilir format (anket yok).
Her öğe: (metin, ilk yorum ya da None, konu etiketi)."""

# Pazartesi · Gayriresmî sektör sözlüğü
SOZLUK_MIZAH = [
    ("Gayriresmî sektör sözlüğü 😅\n\n\"Kısa bir video olsun\" = 3 gün çekim, 2 gün kurgu\n\"Doğal görünsün\" = 14. çekim\n"
     "\"Bütçemiz biraz kısıtlı\" = bütçe yok\n\"Hemen dönüyorum\" = cuma dönülecek\n\"Son bir şey daha\" = üç şey daha\n\n"
     "Eklemek istediğiniz var mı? 👇", None, "Sosyal Medya"),
    ("Gayriresmî sektör sözlüğü 😅 Bu hafta creator versiyonu:\n\n\"Bu hafta çekiyorum\" = pazar gecesi 23:40\n\"Doğal ışık kullandım\" "
     "= halka ışığın şarjı bitti\n\"Ham hali bu\" = 9. versiyon\n\"Algoritma beni sevmiyor\" = 3 gündür paylaşmadım\n\"Bir saatte "
     "hallederim\" = bir gün\n\nKendinizi hangisinde buldunuz? 👇", None, "İçerik Üreticisi"),
    ("Gayriresmî sektör sözlüğü 😅 Bu hafta ajans versiyonu, kendimize de gülelim:\n\n\"Hızlıca bir kontrol edelim\" = 4 kişilik "
     "toplantı\n\"Sıcak bir brief geldi\" = teslim yarın\n\"Ufak bir değişiklik var\" = tarih değişti\n\"Takvime bakıp dönüyorum\" = "
     "takvim çoktan dolu\n\nAjanslardan duyduğunuz başka bir cümle? 👇", None, "Sosyal Medya"),
    ("Gayriresmî sektör sözlüğü 😅 Bu hafta pazarlama ekibi versiyonu:\n\n\"Viral olsun yeter\" = brief bu kadar\n\"Rakibin yaptığı "
     "gibi ama farklı\" = aynısı\n\"Yönetim de bir görsün\" = 3 tur onay\n\"Bir de story ekleyelim mi?\" = ek kalem (fiyatıyla 😇)\n\n"
     "Marka tarafında bunu okuyup gülümseyen? 👇", None, "Influencer Marketing"),
    ("Gayriresmî sektör sözlüğü 😅 Bu hafta Aralık versiyonu:\n\n\"Yılbaşından önce yayına girsin\" = 3 gün içinde\n\"Ocak'ta "
     "konuşalım\" = şubat\n\"Bu yılın bütçesi bitti\" = gelecek yılın brief'i hazır\n\"Tatilde ufak bir şey çekerim\" = tatil iptal\n\n"
     "Aralık'ta en çok duyduğunuz cümle? 👇", None, "Sosyal Medya"),
    ("Gayriresmî sektör sözlüğü 😅 Yılın son versiyonu, sosyal medya:\n\n\"Organik büyüyorum\" = annem, teyzem ve 3 kuzenim\n\"Sadece "
     "kendim için paylaşıyorum\" = 10 dakikada bir istatistiğe bakıyorum\n\"Algoritma değişmiş\" = ben değiştim\n\"Bir ara Threads'e de "
     "bakarım\" = 6 aydır bakıyorum\n\nSizin sözlüğünüze eklenecek madde? 👇", None, "Sosyal Medya"),
]

# Salı · Tamamla
TAMAMLA = [
    ("Tamamla 👇\n\nİçerik üreticisi olduğumu ilk kez ___ anladım.",
     "Ajans tarafından bizim cevabımız: Bir kafede kahve beklerken \"bu mekân hangi içerik üreticisine yakışır\" diye düşündüğümüzde 😄",
     "İçerik Üreticisi"),
    ("Tamamla 👇\n\nBir markadan duyduğum en güzel cümle: \"___\"", "Bizim adayımız: \"Ödeme bugün yapıldı.\" 😄", "Marka İş Birliği"),
    ("Tamamla 👇\n\nİçerik üretmenin en sevdiğim yanı ___, en sevmediğim yanı ___.", None, "İçerik Üreticisi"),
    ("Tamamla 👇\n\nBir içeriğim beklemediğim kadar ilgi gördüğünde ilk yaptığım şey: ___", None, "İçerik Üreticisi"),
    ("Tamamla 👇\n\nBir çekim gününün olmazsa olmazı: ___", "Bizimki: Şarjı dolu bir yedek batarya ve bir termos çay ☕", "İçerik Üreticisi"),
    ("Tamamla 👇\n\nİlk iş birliğimden önce biri bana ___ söyleseydi keşke.",
     "Bizim adayımız: \"Fiyatı söylemeden önce kapsamı sor.\" 💙", "İçerik Üreticisi"),
    ("Tamamla 👇\n\nYeni yıl kararım: ___\n(ve büyük ihtimalle Ocak'ın ikinci haftasında bırakacağım 😅)", None, "Sosyal Medya"),
]

# Çarşamba · Kırmızı bayrak / yeşil bayrak
BAYRAK = [
    ("İş birliği teklifinde 🚩 ve 💚\n\n🚩 \"Bütçeye paylaşımdan sonra bakarız.\"\n🚩 Brief'te tarih var, bütçe yok.\n💚 Teslim kalemleri tek tek "
     "yazılmış.\n💚 Ödeme günü baştan söylenmiş.\n\nSizin listenize ne eklenir? 👇", None, "Marka İş Birliği"),
    ("Markalar için: İçerik üreticisi seçerken 🚩 ve 💚\n\n🚩 Bir gecede gelen 20 bin takipçi.\n🚩 Yorumların hepsi \"Süper 🔥\".\n💚 Son 10 "
     "gönderinin görüntülenmesi istikrarlı.\n💚 Medya kitinde güncel rakamlar var.\n\nSiz neye bakıyorsunuz? 👇", None, "Influencer Marketing"),
    ("Marka ile ilk görüşmede 🚩 ve 💚\n\n🚩 \"Fiyatı sonra konuşuruz.\"\n🚩 Onayı kimin vereceği belli değil.\n💚 Kampanyanın amacı net.\n💚 "
     "\"Sizin tarzınızı seviyoruz, öyle kalsın.\"\n\nİlk görüşmede sizi en çok ne rahatlatır? 👇", None, "Marka İş Birliği"),
    ("Ajans seçerken 🚩 ve 💚\n\n🚩 Size iş bulmak için sizden ücret istemek.\n🚩 Komisyonun kimden alındığını söylememek.\n💚 Koşulları "
     "yazılı paylaşmak.\n💚 Kitlenize uymayan teklifi size hiç getirmemek.\n\nEklemek istediğiniz? 👇", None, "İçerik Üreticisi"),
    ("Marka iletişiminde 🚩 ve 💚\n\n🚩 Haftalarca sessizlik, sonra \"yarın yayında olsun\".\n🚩 Brief'in her toplantıda değişmesi.\n💚 Tek "
     "bir iletişim kişisi.\n💚 Geri bildirimin tek mesajda gelmesi.\n\nHangisini en çok yaşadınız? 👇", None, "Marka İş Birliği"),
    ("İçerik üreticisinden markaya 🚩 ve 💚\n\n🚩 Teslim gününde \"biraz gecikeceğim\" mesajı.\n🚩 Reklam ifadesini \"unutmak\".\n💚 Brief'i kendi "
     "cümleleriyle geri yazmak.\n💚 Yayından sonra sonuçları kendiliğinden göndermek.\n\nMarkalar, sizin listeniz? 👇", None, "Influencer Marketing"),
    ("İş birliği bittikten sonra 🚩 ve 💚\n\n🚩 Ödeme için üçüncü hatırlatma.\n🚩 \"Rapor gerekmez\" deyip bir ay sonra rapor istemek.\n💚 "
     "Linkler, sonuçlar ve bir teşekkür.\n💚 \"Bir sonraki kampanyada yine çalışalım.\"\n\nYılın son bayrağını siz dikin 👇", None,
     "Marka İş Birliği"),
]

# Perşembe · Popüler olmayan görüş
GORUS = [
    ("Popüler olmayan görüş 🔥\n\nHer içerik üreticisinin bir ajansa ihtiyacı yok.\n\nAyda bir iki iş birliği yapan ve iş tarafını rahatça "
     "yönetebilen biri için tek başına ilerlemek gayet mantıklı. Destek, işler büyüyüp vaktinizin çoğu iş tarafına gitmeye başlayınca "
     "anlam kazanıyor.\n\nKatılıyor musunuz? 👇", None, "İçerik Üreticisi"),
    ("Popüler olmayan görüş 🔥\n\n\"Mükemmel içerik\" beklemek, iyi içeriğin düşmanı.\n\nHer hafta paylaşılan üç iyi içerik, ayda bir "
     "gelen mükemmel içerikten çoğu zaman daha çok iş yapar. Kitle de algoritma da düzeni seviyor.\n\nKatılmayan var mı? 👇", None,
     "İçerik Üreticisi"),
    ("Popüler olmayan görüş 🔥\n\nTakipçi sayısı, fiyat konuşmasının en az önemli rakamı.\n\nMarka takipçilerinizi değil, içeriğinizi "
     "görecek kişileri satın alıyor. Ortalama görüntülenme ve kitle uyumu çok daha fazlasını anlatıyor.\n\nKatılıyor musunuz? 👇", None,
     "Influencer Marketing"),
    ("Popüler olmayan görüş 🔥\n\nKitlesine uymayan teklife \"hayır\" diyebilen içerik üreticisi, uzun vadede markalardan daha çok \"evet\" "
     "duyar.\n\nÇünkü takipçileri onun her önerisine güvenir. Markaların aradığı da tam olarak bu güven.\n\nSizce? 👇", None,
     "İçerik Üreticisi"),
    ("Popüler olmayan görüş 🔥\n\nThreads, markaların en çok hafife aldığı platform.\n\nBurada reklam değil sohbet işe yarıyor ve sohbeti "
     "iyi yapan marka sayısı henüz az. Erken gelenler için bu bir fırsat.\n\nBu yüzden buradayız. Siz Threads'i nasıl kullanıyorsunuz? 👇",
     None, "Sosyal Medya"),
    ("Popüler olmayan görüş 🔥\n\nBir içerik üreticisinin en değerli varlığı takipçi sayısı değil, yorum kısmı.\n\nYorumlarda gerçek "
     "sohbet varsa orada bir topluluk var demektir. Markaların ulaşmak istediği de tam olarak o topluluk.\n\nKatılıyor musunuz? 👇", None,
     "İçerik Üreticisi"),
    ("Popüler olmayan görüş 🔥\n\n2027'de en çok kazanan içerik üreticileri en çok paylaşanlar değil, en iyi soruları soranlar olacak.\n\n"
     "Kapsamı, kullanım hakkını, ödeme gününü soran içerik üreticisi hem daha az yorulur hem daha çok kazanır.\n\nYılın son tartışmasını "
     "açalım 👇", None, "İçerik Üreticisi"),
]

# Cuma · Tanıdık gelecek listeler
TANIDIK = [
    ("Sadece içerik üreticilerinin anlayacağı 5 şey 😅\n\n1. \"Bir dakikalık\" video için 47 dakikalık kayıt\n2. Arkadaki tek dağınıklık "
     "yüzünden çekimi baştan almak\n3. Paylaştıktan sonra ilk 10 dakika telefonu bırakamamak\n4. Market poşetini açarken \"bunu çekeyim mi\" "
     "diye düşünmek\n5. \"Sen tam olarak ne iş yapıyorsun?\" sorusu\n\n6. maddeyi siz yazın 👇", None, "İçerik Üreticisi"),
    ("Sadece Efsane Cuma haftasında çalışan pazarlamacıların anlayacağı 5 şey 😅\n\n1. Güne \"kod çalışmıyor\" mesajıyla başlamak\n2. Aynı "
     "indirimi 6 farklı cümleyle anlatmak\n3. \"Stok bitti\" ile \"stok geldi\" arasındaki 40 dakika\n4. Cumartesi sabahı raporu açmaya "
     "korkmak\n5. Pazartesi \"peki şimdi ne yapıyoruz?\" toplantısı\n\nBu hafta hangisini yaşadınız? 👇", None, "Influencer Marketing"),
    ("Sadece marka iş birliği yapanların anlayacağı 5 şey 😅\n\n1. Brief'i 3 kez okuyup yine bir soru bulmak\n2. \"Onaylandı\" mesajını "
     "görünce alınan derin nefes\n3. Ürün ışıkta güzel durmayınca başlayan kriz yönetimi\n4. Fatura kesmeyi hep \"sonraya\" bırakmak\n5. Yayın "
     "saatinde bildirimleri açıp kapatıp yeniden açmak\n\nListeye ne eklersiniz? 👇", None, "Marka İş Birliği"),
    ("Sadece ajans çalışanlarının anlayacağı 5 şey (evet, kendimize gülüyoruz 😅)\n\n1. Aynı anda 4 grupta \"birazdan dönüyorum\" yazmak\n2. "
     "Takvime \"öğle arası\" yazıp o saate toplantı koymak\n3. İçerik üreticisi \"tamamdır\" deyince içten içe dans etmek\n4. \"Acil\" işin hep "
     "cuma 18:00'de gelmesi\n5. Her kafede \"bu mekân hangi profile yakışır\" diye düşünmek\n\nAjans dostlarımız, 6. madde? 👇", None,
     "Sosyal Medya"),
    ("Sadece kışın içerik üretenlerin anlayacağı 5 şey 🥶\n\n1. Saat 16:30'da \"ışık gitti\" paniği\n2. Dışarıda üç kat giyinip kadrajda tek "
     "kat görünmek\n3. Her video için cam kenarı savaşı\n4. Titreyen elle \"doğal\" görünmeye çalışmak\n5. Yılbaşı süsleri yüzünden her kareye "
     "bir parıltı sızması\n\nKış çekimi itirafınız? 👇", None, "İçerik Üreticisi"),
    ("Sadece yıl sonu yoğunluğunu yaşayanların anlayacağı 5 şey 😅\n\n1. \"Yeni yıldan önce bitirelim\" cümlesini günde 6 kez duymak\n2. "
     "Ocak'ın ilk haftasına 9 toplantı\n3. Yıl özeti çekerken yılın yarısını hatırlamamak\n4. \"Bu yıl çok hızlı geçti\" demeyi bırakamamak\n"
     "5. Tatil planını bile içerik takvimine göre yapmak\n\nSiz hangisindesiniz? 👇", None, "Sosyal Medya"),
]

# Cumartesi · POV
POV = [
    ("POV 🎬\n\nMarka \"küçük bir revizyon\" dedi.\nRevizyon: müzik, ışık, metin, kıyafet ve mekân değişiyor.\nSen: \"Tabii, hemen "
     "bakıyorum\" 🙂\n\nBu sahneyi yaşayan? 👇",
     "Ufak not: Revizyonun sayısı ve kapsamı teklifte yazılıysa bu sahne çok daha kısa sürüyor 💙", "İçerik Üreticisi"),
    ("POV 🎬\n\nİlk marka iş birliği teklifin geldi.\nMesajı 5 kez okudun, ekran görüntüsünü 3 arkadaşına attın, cevabı 40 dakikada "
     "yazdın.\nSonra fark ettin: Fiyatı sormayı unutmuşsun 😅\n\nSizin ilk teklif hikâyeniz? 👇", None, "İçerik Üreticisi"),
    ("POV 🎬\n\nPazarlama ekibisin. 20 içerik üreticisinin profiline baktın.\nHepsinin medya kitinde \"yüksek etkileşim\" yazıyor.\n"
     "Hiçbirinde rakam yok 🫠\n\nMarkalar, tanıdık mı? 👇",
     "İçerik üreticileri için not: Medya kitine son 3 ayın ortalama görüntülenmesini yazın, \"yüksek etkileşim\"i rakamlar anlatsın 💙",
     "Influencer Marketing"),
    ("POV 🎬\n\nYayın saati 20:00.\n19:58 Son kontrol.\n19:59 Reklam ifadesi yerinde mi? ✅\n20:00 Paylaş.\n20:01 İstatistiklere bakmaya "
     "başladın.\n20:02 Hâlâ bakıyorsun 👀\n\nKaç dakikada bırakabiliyorsunuz? 👇", None, "İçerik Üreticisi"),
    ("POV 🎬\n\nAralık'ın son haftaları.\nBir marka: \"Yılbaşı kampanyası için yarın çekebilir misiniz?\"\nTakvimin: \"Hayır.\"\nSen: "
     "\"Bakalım, bir yolunu buluruz\" 😅\n\nSon dakika işlere \"evet\" diyenler el kaldırsın 🙋", None, "İçerik Üreticisi"),
    ("POV 🎬\n\nYılın sonu. Galeriye girdin, 2026'nın en iyi içeriklerini seçeceksin.\n4.218 fotoğraf. 612 video. \"Bunu sonra çekerim\" "
     "notlu 37 ekran görüntüsü.\n\nSizin galeri kaç fotoğraf? 👇", None, "Sosyal Medya"),
]

# Pazar · İtiraf köşesi
ITIRAF = [
    ("İtiraf köşesi 🤫\n\nBizden başlayalım: Bir brief'i üç kez okuyup yine de soru sormaktan hiç çekinmiyoruz. Bize göre soru sormak iyi "
     "işin yarısı.\n\nSektörle ilgili sizin itirafınız? 👇", None, "Sosyal Medya"),
    ("İtiraf köşesi 🤫\n\nİçerik üreticileri: Bir iş birliği içeriğini paylaştıktan sonra silip yeniden paylaştığınız oldu mu? Neden? 😄",
     None, "İçerik Üreticisi"),
    ("İtiraf köşesi 🤫\n\nMarkalar: Bir içerik üreticisinin profilini incelerken takip etmeye başlayıp kampanyayı unuttuğunuz oldu mu? 😄",
     None, "Influencer Marketing"),
    ("İtiraf köşesi 🤫\n\nHiç çekmediğiniz ama \"bir gün kesin çekeceğim\" dediğiniz içerik fikri ne? Burada saklayalım, belki bir marka "
     "görür 👀", None, "İçerik Üreticisi"),
    ("İtiraf köşesi 🤫\n\nBir markanın ürününü iş birliği bittikten sonra da kullanmaya devam ettiğiniz oldu mu?\n\nBize göre en iyi iş "
     "birlikleri tam olarak bunlardan çıkıyor 💙", None, "Marka İş Birliği"),
    ("İtiraf köşesi 🤫\n\nYılın son itirafı: 2026'da yaptığınız ve artık gülerek anlattığınız bir içerik hatası? 😅", None, "Sosyal Medya"),
]

# Haftanın gününe göre (0 = pazartesi): (seri adı, liste)
MIDDAY = {
    0: ('Gayriresmî Sözlük', SOZLUK_MIZAH),
    1: ('Tamamla', TAMAMLA),
    2: ('Kırmızı Bayrak', BAYRAK),
    3: ('Popüler Olmayan Görüş', GORUS),
    4: ('Tanıdık Gelecek', TANIDIK),
    5: ('POV', POV),
    6: ('İtiraf Köşesi', ITIRAF),
}
