import random

kelimeler = ["python", "programlama", "oyun", "eğlence", "öğrenme"]

def kelime_ekle():
    while True:
        x = input("farklı kelimeler eklemek istiyorsanız kelimeyi giriniz. İstemiyorsanız enter'a basınız")
        if x != "":
            kelimeler.append(x)
            print("kelime havuza eklendi")
        else:
            break

def kelime_sec(kelimeler):
    return random.choice(kelimeler)

def oyunu_baslat():
    secilen_kelime = kelime_sec(kelimeler)
    tahmin_edilen_harfler = []
    tahmin_hakki = 6
    yanlis_tahmin_sayisi = 0

    print("Adam Asmaca oyununa hoş geldiniz!")

    while True:
        kelime_goruntusu = ""
        for harf in secilen_kelime:
            if harf in tahmin_edilen_harfler:
                kelime_goruntusu += harf
            else:
                kelime_goruntusu += "_"

        print("\nKelime: ", kelime_goruntusu)
        print("Tahmin hakkı: ", tahmin_hakki)

        if kelime_goruntusu == secilen_kelime:
            print("Tebrikler! Kelimeyi doğru tahmin ettiniz: ", secilen_kelime)
            break

        if tahmin_hakki == 0:
            print("Üzgünüz, deneme hakkınız tükendi. Doğru kelime: ", secilen_kelime)
            break

        tahmin = input("Bir harf tahmin edin: ").lower()

        if len(tahmin) != 1 or not tahmin.isalpha():
            print("Lütfen bir harf girin.")
            continue

        if tahmin in tahmin_edilen_harfler:
            print("Bu harfi zaten tahmin ettiniz.")
            continue

        tahmin_edilen_harfler.append(tahmin)

        if tahmin not in secilen_kelime:
            tahmin_hakki -= 1
            yanlis_tahmin_sayisi += 1
            print("Yanlış tahmin!")

            if yanlis_tahmin_sayisi == 1:
                print(" ______")
                print("|      |")
                print("|      O")
            elif yanlis_tahmin_sayisi == 2:
                print(" ______")
                print("|      |")
                print("|      O")
                print("|      |")
            elif yanlis_tahmin_sayisi == 3:
                print(" ______")
                print("|      |")
                print("|      O")
                print("|     /|")
            elif yanlis_tahmin_sayisi == 4:
                print(" ______")
                print("|      |")
                print("|      O")
                print("|     /|\\")
            elif yanlis_tahmin_sayisi == 5:
                print(" ______")
                print("|      |")
                print("|      O")
                print("|     /|\\")
                print("|     /")
            elif yanlis_tahmin_sayisi == 6:
                print(" ______")
                print("|      |")
                print("|      O")
                print("|     /|\\")
                print("|     / \\")
                print("Üzgünüz, oyunu kaybettiniz. Doğru kelime: ", secilen_kelime)


kelime_ekle()
oyunu_baslat()
