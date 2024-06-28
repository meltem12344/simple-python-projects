import sys
import os

def sayi_gir():
    ilk_sayi = float(input("İlk sayiyi girin: "))
    ikinci_sayi = float(input("İkinci sayiyi girin: "))
    return ilk_sayi, ikinci_sayi

while True:
    print("----------------------------------")
    print("1-toplama")
    print("2-çikartma")
    print("3-bölme")
    print("4-çarpma")
    print("5-çik")
    print("6-geçmiş..","\n")

    seçme = input("Hangi işlemi yapmak istersiniz? : ")


    if seçme == '5':
        sys.exit("Çikiş yapildi!")
    elif seçme == '6':
        with open("geçmis.txt", "r") as dosya:
            dosya_ici = dosya.read()
        print(dosya_ici)
    elif seçme in ['1', '2', '3', '4']:
        try:
            a, b = sayi_gir()
            if seçme == '4':
                sonuç = a * b
                with open("geçmis.txt", "a") as dosya:
                    dosya.write(f"{a} * {b} = {sonuç}" + "\n")
            elif seçme == '3':
                if b != 0:
                    sonuç = a / b
                    with open("geçmis.txt", "a") as dosya:
                        dosya.write(f"{a} / {b} = {sonuç}" + "\n")
                else:
                    sonuç = "Payda sifir olamaz! "
            elif seçme == '2':
                sonuç = a - b
                with open("geçmis.txt", "a") as dosya:
                    dosya.write(f"{a} - {b} = {sonuç}" + "\n")
            elif seçme == '1':
                sonuç = a + b
                with open("geçmis.txt", "a") as dosya:
                    dosya.write(f"{a} + {b} = {sonuç}" + "\n")
            print("İŞLEMİNİZİN SONUCU :: ", sonuç, "\n")
        except ValueError:
            print("Geçersiz seçim! Geçerli bir işlem numarasi girin.\n")
    else:
        print("Geçersiz seçim! Geçerli bir işlem numarasi girin.\n")

    print("----------------------------------")

