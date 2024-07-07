#Parolayı al
parola = input("Parolayi girin :: ")

#Parola uzunluğu
parola_len = len(parola)

#Karakterleri listele
karakterler = list(parola)

özel_karakterler = "!@#$%^&*()-_+=<>?/|\\{[]~}`"


def kontrol_et(parola):
    if not any(char.isupper() for char in parola):
        return "Parola güçlü değil. Büyük harf kullan."
    
    if not any(char.islower() for char in parola):
        return "Parola güçlü değil. Küçük harf kullan."
    
    if not any(char.isdigit() for char in parola):
        return "Parola güçlü değil. Sayi kullan."
    
    if not any(char in özel_karakterler for char in parola):
        return "Parola güçlü değil. Özel karakter kullan."
    
    return "Güçlü parola."
            
if parola_len >= 8:
    print("Parola  uzunluğu ideal.")  
    kontrol = kontrol_et(parola)      
    print(kontrol)  
else:
    print("Dikkat parola 8 ya da daha fazla karakterden oluşmali! ")
    
 
