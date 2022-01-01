#Bu uygulama banka simulasyonunu 2 dil seçeneği ile yapmayı amaçlayan ve sqlite3 veritabanını kullanan bir yazılımdır.
#Bu uygulama Murtaza SARITÜRK tarafından kodlanmıştır.


#Gerekli olan modüller
import os
from sqlite3.dbapi2 import Cursor
import sys
import time
import sqlite3
import platform
import datetime

#gerekli olan değişkenler:
bugun = datetime.datetime.today()
bilgisayar = platform.platform()
metin_listesi = list()
musteri_giris = False
deneme_hakki = 3
musteri = list()
dil = "tr"


#Müşteriden hangi dili kullanmak istediğini soruyorum:
print("""Lütfen kullanmak istediğini dilin numarasını yazınız:
 Please enter number of the language your want to use:
 
 1- Türkçe
 2- English""")

#olası hatalı girişlere karşı önlemimi try:except ile alıyorum
try: 
    dil_secimi = int(input())
    #kullanıcının girdiği sayıya göre dili ayarlama:
    #Dil türkçe olarak seçilirse:
    if dil_secimi == 1:
        print("Türkçe olarak devam edilecek. Lütfne giriş menüsüne yönlendirilirken lütfen bekleyiniz...")
        
        dil = "tr"
        
        #dil dosyasından verilerimi çekiyorum.
        file = open("tr.dil", "r", encoding="utf-8")

        #for döngüsü ile verileri liste haline getiriyorum. Bu sayede listeden istediğim veriyi istediğim şekilde kullanacağım.
        for i in file:
            i = i[:-1]
            i = i.strip("\n")
            metin_listesi.append(i)
        time.sleep(3)

    #dil ingilizce olarak seçilirse:
    elif dil_secimi == 2:
        print("You choosed English. Please wait when you redirecting to login screen...")

        dil = "en"
        file = open("en.dil", "r", encoding="utf-8")

        for i in file:
            i = i[:-1]
            i = i.strip("\n")
            metin_listesi.append(i)
        time.sleep(3)
    
    #Yanlış girdileri önlemek için ek kod:
    else:
        print("""Yanlış karakter girişi yaptığınız için program kendini kapatacaktır. İyi günler dileriz
        You inserted now allowed characters. Application will be closed in 5 seconds.
        """)
        time.sleep(5)
        sys.exit()

#Sayı yerine farklı karakterler girilirse:
except:
    print("""Yanlış karakter girişi yaptığınız için program kendini kapatacaktır. İyi günler dileriz
    You inserted now allowed characters. Application will be closed in 5 seconds.
    """)
    time.sleep(5)
    sys.exit()

#Günün tarihini ve girilen cihazı bilgi amaçlı yazdırma:
print(metin_listesi[0].format(bugun))
print(metin_listesi[1].format(bilgisayar))

#işlemler sonrası görüntü kirliliğini önlemek amaçlı ekranı temizle fonksiyonu:
def ekrani_temizle():

    if os.name == 'nt':
        _ = os.system('cls')
    

#İşlemlerin seçilip gerçekleştirileceği yer:
def ana_ekran():

    #gerekli değişkenler:
    global metin_listesi
    global musteri
    global bugun

    #İşlem yazıları
    print(metin_listesi[9].format(musteri[3]))
    print(metin_listesi[10])
    print(metin_listesi[11])
    print(metin_listesi[12])
    print(metin_listesi[13])
    print(metin_listesi[14])

    #İşlemin girilmesi ve yine olası hataları önleme amaçlı try:except komutları
    try:
        islem = int(input())
    
    except:
        print(metin_listesi[17])
        time.sleep(5)
        sys.exit()

    #Çıkış işlemi
    if islem == 0:   
        print(metin_listesi[15])
        time.sleep(5)
        sys.exit()

    #bakiye işlemi
    elif islem == 1:
        print(metin_listesi[16].format(musteri[3],bugun,musteri[6]))
        time.sleep(5)
        ekrani_temizle()

    #Hesaba para gönderme işlemi:
    elif islem == 2:
        print(metin_listesi[18])

        #Gönderilecek hesabın ve tutarın kullanıcıdan istenmesi ve olası hataları önlemek için yine try:except komutları
        try:
            gonderilecek_hesap = int(input())
            print(metin_listesi[19])
            gonderilecek_tutar = int(input())

        except:
            print(metin_listesi[17])
            time.sleep(5)
            sys.exit()

        print(metin_listesi[20])

        #Gerekli kontroller:
        if ((gonderilecek_tutar + 2) < musteri[6]):

            if (gonderilecek_hesap != musteri[1]):

                #veritabanına bağlanma
                baglan = sqlite3.connect("database.db")
                cursor = baglan.cursor()
                cursor.execute("SELECT * FROM CUSTOMERS")
                musteriler = cursor.fetchall()

                #For döngüsü ile paranın gönderileceği hesabı bulma:
                for i in musteriler:
                    if i[1] == gonderilecek_hesap:
                        para_gond_hesap = list(i)

                        #Listelerin Güncellenmesi:
                        musteri[6] = musteri[6] - (gonderilecek_tutar + 2)
                        para_gond_hesap[6] = para_gond_hesap[6] + (gonderilecek_tutar)

                        #Veritabanı güncellenmesi
                        cursor.execute("UPDATE CUSTOMERS SET HesapBakiyesi = ? WHERE HesapNumarasi = ?",(musteri[6],musteri[1]))
                        baglan.commit()
                        cursor.execute("UPDATE CUSTOMERS SET HesapBakiyesi = ? WHERE HesapNumarasi = ?",(para_gond_hesap[6],para_gond_hesap[1]))
                        baglan.commit()
                        baglan.close()

                        #Gerekli metinlerin yazdırılması:
                        print(metin_listesi[21].format(musteri[6]))
                        time.sleep(1)
                        print(metin_listesi[22])
                        time.sleep(4) 
                        ekrani_temizle()

            else:
                
                #Müşterinin kendi hesap numarasını yazma ihtimaline karşı önlemin uyarısı:
                print(metin_listesi[23])
                time.sleep(4)
                ekrani_temizle()
        else:
            
            #Gerekli Olan Ekstra Bakiye:
            goeb = -(musteri[6]) - (gonderilecek_tutar + 2)
            print(metin_listesi[24].format(goeb))     
            time.sleep(4)
            ekrani_temizle()


    #Telefon numarası değiştirme işlemi:
    elif islem == 3:

        print(metin_listesi[25])

        #Olası girdi hatalarına karşı önlem:
        try:

            #Eski telefon numarasının karşı taraftan istenmesi ve bu telefon numarasının doğru olup olmadığının
            #kontrolünün ardından telefon numarası uzunluğu kontrolü daha sonra ise şifre istenip onun kontrolü
            telefon_no = int(input())

            if telefon_no == musteri[4]:

                #Yeni telefon numarasını kullanıcıdan isteme:
                print(metin_listesi[26])
                yeni_telefonNo =  int(input())

                #yeni telefon numarasının kontrolü:
                if len(str(yeni_telefonNo)) == 10:

                    print(metin_listesi[27])

                    sifre_kontrol = int(input())

                    #Şifre ve şifre kontrolü:
                    if sifre_kontrol == musteri[8]:

                        musteri[4] = yeni_telefonNo

                        #Veritabanı güncellenmesi:
                        baglan = sqlite3.connect("database.db")
                        cursor = baglan.cursor()
                        cursor.execute("UPDATE CUSTOMERS SET TelefonNo = ? Where HesapNumarasi = ?",(musteri[4],musteri[1]))
                        baglan.commit()
                        baglan.close()

                        #Gerekli çıktılar:
                        print(metin_listesi[28])
                        time.sleep(4)
                        ekrani_temizle()

                    else:

                        #Şifre yanlış ise gösterilecek mesajlar:
                        print(metin_listesi[29])
                        time.sleep(4)
                else:

                    #yeni telefon numarasının uzunluğu yanlış olursa:
                    print(metin_listesi[30])
                    time.sleep(4)
                    ekrani_temizle()
            else:

                #Telefon numarasının yanlış girilmesi durumunda:
                print(metin_listesi[31])
                time.sleep(4)
                ekrani_temizle()
        except:

            #Olası girdi hataları oluşması durumunda:
            print(metin_listesi[17])
            time.sleep(4)
            ekrani_temizle()
    elif islem == 4:
        
        #Şifreyi değiştirme:

        print(metin_listesi[32])
        
        try:
            sifre = int(input())

            if sifre == musteri[8]:

                #Eğer girilen şifre doğru ise kullanıcıdan yeni şifre isteme:
                print(metin_listesi[33])

                yeni_sifre = int(input())

                #Yeni şifre kontrolü:
                if len(str(yeni_sifre)) == 6:
                    print(metin_listesi[34])
                    time.sleep(1)

                    #Güncelleme işlemleri:

                    deneme_hakki = 3
                    musteri[8] = yeni_sifre

                    #Veritabanı güncelleme:

                    baglan = sqlite3.connect("database.db")
                    cursor = baglan.cursor()
                    cursor.execute("UPDATE CUSTOMERS SET Sifre = ? WHERE HesapNumarasi = ?",(musteri[8],musteri[1]))
                    baglan.commit()
                    baglan.close()

                    #Gerekli son işlemler (Yazılar, kullanıcı çıkışı vs.):
                    print(metin_listesi[35])
                    musteri_giris = False
                    time.sleep(4)
                    ekrani_temizle()
                
                else:

                    #Yeni şifeniz gereksinimleri karşılayamaması durumunda:
                    print(metin_listesi[36])
                    time.sleep(4)
                    ekrani_temizle()
            else:

                #Mevcut şifrenin yanlış girilmesi durumunda:
                print(metin_listesi[37])
                time.sleep(4)
                ekrani_temizle()
        except:

            #Olası girdiğ hatası durumunda:
            print(metin_listesi[17])
            time.sleep(4)
            ekrani_temizle()
    else:

        #Mevcut işlemler dışında başka bir işlemin girilmesi durumunda:
        print(metin_listesi[38])
        time.sleep(4)
        ekrani_temizle()

#Giriş yapma ekranı:
def giris_ekrani():

    #Gerekli olan değişkenler:
    global bugun
    global musteri
    global deneme_hakki
    global musteri_giris
    global metin_listesi
    
    print(metin_listesi[2])

    #Olası karakter hatalarını önlemek için try:except kullanımı:
    try:
        
        #Kimlik numarası:
        tc_kimlik = int(input())

        #Şifre isteme:
        print(metin_listesi[3])
        sifre = int(input())

        print(metin_listesi[7])

        #Veritabanından tüm kullanıcıların çekilmesi ve bunların geçici olarak bir listeye aktarılması:
        baglan = sqlite3.connect("database.db")
        cursor = baglan.cursor()
        cursor.execute("SELECT * FROM CUSTOMERS")
        musteriler = cursor.fetchall()

        #For döngüsü ile geçicic değişkendeki verilerin girilen verilerle karşılaştırılması ve eşleşme halinde kullanıcının girişinin yapılması:
        for i in musteriler:
            if i[2] == tc_kimlik and i[8] == sifre:

                musteri = list(i)
                musteri_giris = True
        
        #Kullanıcı girişi başarılı ile yaptıysa:
        if musteri_giris == True:
            print(metin_listesi[8].format(musteri[3]))
            time.sleep(5)
            ekrani_temizle()

        #Giriş yapamadıysa:
        else:
            print(metin_listesi[4])
            time.sleep(1)

            print(metin_listesi[5].format(deneme_hakki))
            time.sleep(3)
            ekrani_temizle()
    
    #Olası yanlış girilen karakterlere karşı önlem:
    except:
        print(metin_listesi(17))
        time.sleep(5)
        sys.exit()

#Kullanıcının ilk girişi:
while musteri_giris == False:
    deneme_hakki = deneme_hakki - 1
    print(metin_listesi[5].format(deneme_hakki))
    time.sleep(2)
    giris_ekrani()

    #Kullanıcının deneme hakkının kalmaması durumunda uygulamayı kapatmak için:
    if deneme_hakki == 0:
        print(metin_listesi[6])
        time.sleep(4)
        sys.exit()

#Kullanıcı eğer başarılı bir şekilde giriş yaptıysa sonsuz döngü ile kullanıcı çıkıncaya kadar işlem yapma:
while musteri_giris == True:
    ana_ekran()

#Kullanıcı eğer şifreyi değiştirdiyse çalışacak olan kodlar:
while musteri_giris == False:
    deneme_hakki = deneme_hakki - 1
    print(metin_listesi[5].format(deneme_hakki))
    time.sleep(2)

    #Deneme hakkının bitmesi durumunda programı kapatacak kodlar:
    if deneme_hakki == 0:
        print(metin_listesi[6])
        time.sleep(4)
        break

