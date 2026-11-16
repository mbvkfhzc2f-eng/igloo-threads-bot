# Planın kaynağı

`posts.json` ve `img/` klasöründeki kartlar bu dosyalardan üretildi. Bot bu klasörü kullanmaz; yalnızca planı düzenlemek ya da uzatmak için duruyor.

- `content_notes.py`: açılış, 09:00 günün notu, 11:00 sektör sözlüğü
- `content_midday.py`: 13:00 öğle arası serileri
- `content_series.py`: 18:00 akşam serileri ve 21:00 akşam sohbeti
- `build.py`: takvimi kurar, metin uzunluklarını ve konu etiketlerini denetler, `posts.json` yazar
- `cards.py`: kartları 1080×1350 JPEG olarak çizer
