#Gerekli Modüller:
import time
from pytube import YouTube


#Gerekli fonksiyonlar
def video_indir(link):

    icerik = YouTube(link) 
    print("İndireceğiniz Videonun Adı: {}".format(icerik.title))

    indir = icerik.streams.get_highest_resolution() #En yüksek çözünürlüğü seçtim. Siz get_by_resolution() ile istediğiniz çözünürlüğü kullanabilirsiniz.

    basla = indir.download("indirilenler/") #indirme klasörünü ekledim. Eğer yoksa otomatik oluşturacaktır.
    print("İndirme Başarıyla Tamamlanmıştır. Dosya Adı {}, İndirilen Yer: {}".format(icerik.title,"İndirilenler"))
    time.sleep(4)

def ses_indir(link):

    icerik = YouTube(link)
    print("İndireceğiniz Sesin Adı: {}".format(icerik.title))
    

    indir = icerik.streams.get_audio_only()

    basla = indir.download("indirilenler/",icerik.title + ".mp3")
    print("İndirme Başarıyla Tamamlanmıştır. Dosya Adı {}, İndirilen Yer: {}".format(icerik.title,"İndirilenler"))
    time.sleep(4)

#Ana ekran fonksiyonları çağırmak için yazılan fonksiyon görevini üstleniyor.
def ana_ekran():
    print("Hoşgeldiniz. Lütfen İndirmek İstediğiniz Videonun Linkini Giriniz:")
    link = input()

    print("Lütfen Video İçin V, Ses İçin S tuşuna Basınız:")
    dosya_turu = input()

    if dosya_turu == "V":
        print("Videonuz İndiriliyor... Lütfen Bekleyiniz...")
        video_indir(link)
    elif dosya_turu == "S":
        print("Ses Dosyanız indiriliyor.. Lütfen Bekleyiniz..")
        ses_indir(link)
    else:
        print("Yanlış Giriş Yaptınız. Lütfen Tekrar Deneyiniz.")
        time.sleep(4)

#Sonsuz döngü ile kullanıcı istediği kadar video veya ses indirebiliyor.
while True:
    ana_ekran()







