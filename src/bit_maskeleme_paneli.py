# BLM101 Donem Projesi - Bit Maskeleme Paneli

cihazlar = ["Guc", "Wi-Fi", "Bluetooth", "Kamera", "Mikrofon", "GPS", "Ucak Modu", "Gece Modu"]

# bu fonksiyon mevcut durumu ikilik olarak ve tablo seklinde gosterir
def durumu_goster(durum):
    ikilik = format(durum, '08b')
    print("\nDurum Bayti:", ikilik, "-> Onluk:", durum)
    
    kutular = ""
    baslik = ""
    for i in range(7, -1, -1):
        baslik += f"B{i}   "
        kutular += f"[{ikilik[7-i]}]  "
        
    print(baslik)
    print(kutular)
    print("-----------------------------------")
    
    for i in range(8):
        # ilgili biti kontrol etmek icin maske olusturuyoruz
        maske = 1 << i
        if (durum & maske) != 0:
            sonuc = "ACIK"
        else:
            sonuc = "KAPALI"
        print(f"{i} - {cihazlar[i]:<12} : {sonuc}")


# bu fonksiyon OR (|) islemi ile secilen biti 1 yapar (ozelligi acar)
def ozellik_ac(durum, no):
    maske = 1 << no
    durum = durum | maske
    print(f"\n>> {cihazlar[no]} acildi.")
    return durum

# bu fonksiyon AND (&) ve NOT (~) ile biti 0 yapar (ozelligi kapatir)
def ozellik_kapat(durum, no):
    maske = ~(1 << no) & 255
    durum = durum & maske
    print(f"\n>> {cihazlar[no]} kapatildi.")
    return durum

# bu fonksiyon XOR (^) ile bitin durumunu tersine cevirir
def ozellik_tersle(durum, no):
    maske = 1 << no
    durum = durum ^ maske
    print(f"\n>> {cihazlar[no]} durumu tersine cevrildi.")
    return durum


# baslangicta hepsi kapali (00000000)
durum_bayti = 0

print("SANAL DONANIM DURUM PANELI")
durumu_goster(durum_bayti)

# ana menu dongusu
while True:
    print("\n1- Durumlari Gor")
    print("2- Bir Ozelligi Ac")
    print("3- Bir Ozelligi Kapat")
    print("4- Bir Ozelligi Tersine Cevir")
    print("0- Cikis")
    
    secim = input("Seciminiz: ")
    
    if secim == "1":
        durumu_goster(durum_bayti)
        
    elif secim == "2" or secim == "3" or secim == "4":
        print("\nCihazlar:")
        for i in range(8):
            print(f"{i}: {cihazlar[i]}")
            
        no = int(input("Cihaz numarasi girin (0-7): "))
        
        if no < 0 or no > 7:
            print("Hatali numara girdiniz! 0 ile 7 arasinda olmali.")
        else:
            if secim == "2":
                durum_bayti = ozellik_ac(durum_bayti, no)
            elif secim == "3":
                durum_bayti = ozellik_kapat(durum_bayti, no)
            elif secim == "4":
                durum_bayti = ozellik_tersle(durum_bayti, no)
                
            durumu_goster(durum_bayti)
            
    elif secim == "0":
        print("Cikis yapildi.")
        break
    else:
        print("Yanlis secim yaptiniz!")