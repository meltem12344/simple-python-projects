import random

def dosyadan_rastgele_kelime_sec(dosya_adi):
    with open(dosya_adi, "r", encoding="utf-8") as dosya:
        kelimeler = dosya.read().splitlines()
    rastgele_kelime = random.choice(kelimeler)
    return rastgele_kelime

def kelime_sec(harf_sayisi):
    if harf_sayisi == "3":
        dosya_adi = "üçHarfli.txt"
    elif harf_sayisi == "4":
        dosya_adi = "dörtHarfli.txt"
    elif harf_sayisi == "5":
        dosya_adi = "beşHarfli.txt"
    else:
        print("Geçersiz seçim! 3, 4 veya 5 girin.")
        return None

    rastgele_kelime = dosyadan_rastgele_kelime_sec(dosya_adi)
    return list(rastgele_kelime)

while True:
    harf_sayisi = input("Kaç harfli kelime tahmin etmek istersiniz? (3-5): ")
    can_sayisi = 5
    tamamlanma = 0

    if harf_sayisi in ["3", "4", "5"]:
        kelime = kelime_sec(harf_sayisi)
        if kelime:
            print("---------------------------------------------------")
            print(f"{harf_sayisi} harfli kelime tahmini yapacaksiniz.")
            print("Toplam ",can_sayisi," hakkiniz var.")
            while can_sayisi > 0 and tamamlanma < int(harf_sayisi):
                try:
                    index = int(input(f"Kaçinci harfi tahmin etmek istersiniz? (1-{harf_sayisi}) :: "))
                    if 1 <= index <= int(harf_sayisi):
                        girilen_harf = input("Harfi girin :: ").lower()
                        if kelime[index-1] == girilen_harf:
                            print("Girdiğiniz harf doğru. Tebrikler.")
                            tamamlanma += 1
                            if tamamlanma == int(harf_sayisi):
                                print("Kelimeyi buldunuz!!")
                                break
                            else:
                                print("Bir harfi buldunuz.")
                        else:
                            can_sayisi -= 1
                            print("Yanliş harf! ", can_sayisi, "caniniz kaldi.")
                            if can_sayisi == 0:
                                print("Hakkiniz bitti!.","Seçilen kelime :: ", ''.join(kelime))
                                break
                            else:
                                continue
                    else:
                        print(f"Geçersiz sayi. 1-{harf_sayisi} arasinda bir sayi girin!")
                except ValueError:
                    print(f"Geçersiz giriş. 1-{harf_sayisi} arasinda bir sayi girin!")
        else:
            continue
    else:
        print("Geçersiz giriş! Lütfen 3, 4 veya 5 giriniz.")

#Harfi girin :: kısmında boş gönderdiğinde yine can gidiyor onu düzelt.