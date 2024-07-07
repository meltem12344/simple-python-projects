import random

rastgele_sayi = int(random.randint(1, 100))  
while True:
    print("-------------------------------------------------")
    print("1 ile 100 arasinda bir sayi tahmini yapacaksiniz.")
    
    can_sayisi = 10
    print(can_sayisi , " hakkiniz var.")

    while can_sayisi > 0:
        tahmin = int(input("Tahmin ettiğiniz sayi nedir? :: "))
        if rastgele_sayi != tahmin:
            can_sayisi -= 1
            if can_sayisi == 0:
                print("Hakkiniz bitti!.","Seçilen sayi::",rastgele_sayi)
                break
            else:
                if rastgele_sayi < tahmin:
                    print("Girdiğin sayiyi azaltmalisin.")
                else:
                    print("Girdiğin sayiyi artirmalisin.")
                print(can_sayisi," hakkiniz kaldi.")
        else:
            print("Sayiyi buldunuz. Tebrikler!")
            break

#Tahmin ettiğiniz sayi nedir? ::   burda aralıkta olup olmadıgını kontrol et
