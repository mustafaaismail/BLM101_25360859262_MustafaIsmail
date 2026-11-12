# BLM101 Bilgisayar Mühendisliğine Giriş - Dönem Projesi

## Öğrenci Bilgileri
* **Ad Soyad:** Mustafa İsmail
* **Öğrenci Numarası:** 25360859262
* **Proje Konusu:** 3. Grup - Bilgisayar Mimarisi ve Bit Düzeyinde İşlemler (Bit Maskeleme Paneli)

## Kurulum ve Çalıştırma
Proje sadece temel Python kullanılarak yazılmıştır, ekstra bir kütüphane (modül) indirmeye gerek yoktur. 
Terminalde proje klasörüne girip şu komutla çalıştırabilirsiniz:
`python src/bit_maskeleme_paneli.py`

## Proje ve Algoritma Açıklaması
Bu projede 8 farklı cihazın (Güç, Wi-Fi, Bluetooth, Kamera vb.) açık/kapalı durumlarını ayrı ayrı değişkenlerde tutmak yerine, CPU yazmaç (register) mantığına uygun olarak tek bir 8-bitlik tamsayı (`durum_bayti`) içinde tuttum. 

Algoritmanın temel fonksiyonları ve çalışma mantığı şunlardır:
* **durumu_goster:** `for` döngüsü ve `1 << i` maskesi kullanarak baytın içindeki her bir biti `&` (AND) operatörüyle kontrol eder. Hangi bitin 1, hangisinin 0 olduğuna bakarak sonucu ekrana kutucuklar ve tablo halinde yazdırır.
* **ozellik_ac:** Seçilen cihazı açmak için `1 << no` ile oluşturulan maskeyi `|` (OR) operatörüyle ana bayta ekler ve sadece hedef biti 1 yapar.
* **ozellik_kapat:** Cihazı kapatmak için önce `~` (NOT) ile maskeyi ters çevirip ardından `&` (AND) operatörünü kullanarak o biti 0 yapar.
* **ozellik_tersle:** Cihaz açıksa kapatmak, kapalıysa açmak için hedef biti `^` (XOR) operatörüyle tersine çevirir.
