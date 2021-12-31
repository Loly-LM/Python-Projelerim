# Fonksiyonu Kullanan Hesap Makinesi
import time

def toplama(sayi1, sayi2):
    sonuc = sayi1 + sayi2
    print("İşlem Sonucu: {}".format(sonuc))
    time.sleep(1)
    print("Yeniden İşlem Seçiniz\n")
    time.sleep(1)
    if (sonuc == 31 or sonuc == 69 or sonuc == 52):
        print("DLKASDLKJASLIJLKSLKDJASLKJDLKASLKLKD")
        time.sleep(1)

def cikarma(sayi1, sayi2):
    sonuc = sayi1 - sayi2
    print("İşlem Sonucu: {}".format(sonuc))
    time.sleep(1)
    print("Yeniden İşlem Seçiniz\n")
    time.sleep(1)
    if (sonuc == 31 or sonuc == 69 or sonuc == 52):
        print("DLKASDLKJASLIJLKSLKDJASLKJDLKASLKLKD")
        time.sleep(1)

def carpma(sayi1, sayi2):
    sonuc = sayi2 * sayi1
    print("İşlem Sonucu: {}".format(sonuc))
    time.sleep(1)
    print("Yeniden İşlem Seçiniz\n")
    time.sleep(1)
    if (sonuc == 31 or sonuc == 69 or sonuc == 52):
        print("DLKASDLKJASLIJLKSLKDJASLKJDLKASLKLKD")
        time.sleep(1)

def bolme(sayi1, sayi2):
    sonuc = sayi1 / sayi2
    print("İşlem Sonucu: {}".format(sonuc))
    time.sleep(1)
    print("Yeniden İşlem Seçiniz\n")
    time.sleep(1)
    if (sonuc == 31 or sonuc == 69 or sonuc == 52):
        print("DLKASDLKJASLIJLKSLKDJASLKJDLKASLKLKD")
        time.sleep(1)

def kalaniBulma(sayi1,sayi2):
    sonuc = sayi1 % sayi2
    print("İşlem Sonucu: {}".format(sonuc))
    time.sleep(1)
    print("Yeniden İşlem Seçiniz\n")
    time.sleep(1)
    if (sonuc == 31 or sonuc == 69 or sonuc == 52):
        print("DLKASDLKJASLIJLKSLKDJASLKJDLKASLKLKD")
        time.sleep(1)

def tamSayiBolmesi(sayi1,sayi2):
    sonuc = sayi1 // sayi2
    print("İşlem Sonucu: {}".format(sonuc))
    time.sleep(1)
    print("Yeniden İşlem Seçiniz\n")
    time.sleep(1)
    if (sonuc == 31 or sonuc == 69 or sonuc == 52):
        print("DLKASDLKJASLIJLKSLKDJASLKJDLKASLKLKD")
        time.sleep(1)

print(
    """
    *************************************************************************
                Fonksiyonları Kullanan Hesap Makinesi v0.2'e Hoşgeldiniz!
                Lütfen Bir İşlem Seçiniz;
                1 - Toplama
                2 - Çıkarma
                3 - Çarpma
                4 - Bölme
                5 - Bölmeden Kalanı Bulma
                6 - Tam Sayı Bölme İşlemi
                0 - Çıkış
                Not: İşleminiz bittikten sonra Yeniden İşlem Seçebilirsiniz.
    *************************************************************************
    """
)
while True:

    try:
        islem = int(input())
        if (islem == 1):
            print("Toplama İşlemini Seçtiniz. Lütfen iki adet sayı giriniz.")
            sayi1 = int(input())
            sayi2 = int(input())
            toplama(sayi1, sayi2)
        elif (islem == 2):
            print("Çıkarma İşlemini Seçtiniz. Lütfen İki Tane Sayı Giriniz.")
            sayi1 = int(input())
            sayi2 = int(input())
            cikarma(sayi1, sayi2)
        elif (islem == 3):
            print("Çarpma İşlemini Seçtiniz. Lütfen İki Adet Sayı Giriniz.")
            sayi1 = int(input())
            sayi2 = int(input())
            carpma(sayi1, sayi2)
        elif (islem == 4):
            print("Bölme İşlemini Seçtiniz. Lütfen İki Adet Sayı Giriniz.")
            sayi1 = int(input())
            sayi2 = int(input())
            bolme(sayi1, sayi2)    
        elif (islem == 5):
            print("Bölümden Kalanı Bulma İşlemini Seçtiniz. Lütfen İki Adet Sayı Giriniz.")
            sayi1 = int(input())
            sayi2 = int(input())
            kalaniBulma(sayi1, sayi2)
        elif (islem == 6):
            print("Tam Sayı Bölme İşlemini Seçtiniz. Lütfen İki Adet Sayı Giriniz.")
            sayi1 = int(input())
            sayi2 = int(input())
            tamSayiBolmesi(sayi1, sayi2)
        elif (islem == 0):
            print("Çıkmayı Tercih Ettiniz. İyi Günler Dilerim :)")
            time.sleep(2)
            break
        
    except:
        print("Hata Oluştu! Sayı Girmediğiniz İçin İşlemler Yürütülemiyor.")
        time.sleep(2)
        break