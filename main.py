#Banka yazılımı v0.8 
import platform
from sqlite3.dbapi2 import Cursor
import time
import datetime
import sqlite3
import sys
import os

#Bu yazılım ekstra bir database.db adlı sqlite ile oluşturulmuş bir veritabanına ihtiyaç duymaktadır.

#Ekran temizleme Fonksiyonu
def ClearScreen():

    if os.name == 'nt':
        _ = os.system('cls')
    
#Gerekli Bazı Değişken Tanımları
ItsDate = datetime.datetime.now()


User = []
UserLogIn = False

#Girilen Cihaz Bilgileri
OS_System = platform.system()
Platform = platform.platform()

print(" Girilen Cihaz : {} {}".format(OS_System, Platform))
time.sleep(1)

DatabaseList = []
print("Banka Yazılımı Alpha Sürümüne Hoş Geldiniz. Tarih: {}. Giriş ekranına yönlendirliyorsunuz. Lütfen Bekleyiniz.".format(ItsDate))
time.sleep(1)

def LoginScreen():

    global User
    global UserLogIn
    global DatabaseList

    baglanti = sqlite3.connect("database.db")

    cursor = baglanti.cursor()

    cursor.execute("SELECT * FROM CUSTOMERS")
    DatabaseList = cursor.fetchall()

    print("Lütfen TC Kimlik Numaranızı Giriniz:")
    UserID = int(input())

    print("Lütfen Şifrenizi Giriniz:")
    Password = int(input())

    for i in DatabaseList:
        if (i[2] == UserID):
            if (i[8] == Password):
                User = list(i)
                UserLogIn = True
                print("Hoşgeldiniz Sayın {}. Başarılı Bir Şekilde Giriş Yaptınız ve Ana Menüye Yönlendiriliyorsunuz. Lütfen Bekleyiniz.".format(User[3]))
                time.sleep(3)
                return UserLogIn
    
    if UserLogIn == False:
        print("TC Kimlik Numaranız Veya Şifreniz Yanlış. Lütfen Tekrar Deneyiniz.")
        time.sleep(3)
    baglanti.close()


def MainMenu():
    global User
    global UserLogIn
    

    print("Ana Menüye Hoşgeldiniz Sayın {}. Bugün Tarih: {} ".format(User[3], ItsDate))
    print("""Lütfen Aşağıdaki İşlemlerden Birini Seçiniz.
    
    0 - Çıkış
    1 - Bakiye Öğrenme
    2 - Para Gönderme
    3 - Kredi Kartı Borcu Ödeme
    4 - Ehliyet Harcı Ödeme
    5 - Telefon Faturası Ödeme
    6 - Elektrik Faturası Ödeme
    7 - Su Faturası Ödeme
    8 - Sınav Ödemeleri
    9 - KYK Yurt Ödemeleri
    
    
    Not: Lütfen Bu Yazılan İşlemlerin Sadece Başındaki Sayıyı Giriniz. Aksi Takdirde İşleminiz Gerçekleşmeyecek Ve Yazılım Kapatılacaktır.
    """)
    
    try:

        Proccess = int(input())

    except:
    
        print("İşlem Girme Hatası Yaptığınız İçin Çıkışınız Gerçekleştiriliyor...")
        Proccess = 0

    if Proccess == 0:
        print("Bizi Tercih Ettiğiniz İçin Teşekkürler Sayın {}. İyi Günler Dileriz.".format(User[3]))
        time.sleep(3)
        sys.exit()
        
    elif Proccess == 1:

        print("Sayın {}, {} Tarihiyle Bakiyeniz: {} TL".format(User[3],ItsDate,User[6]))
        time.sleep(3)

        
    elif Proccess == 2:

        print("Sayın {}, Lütfen Para Göndermek İstediğiniz Hesabın Numarasını Yazınız.".format(User[3]))
        
        try:
            MoneyTransferID = int(input())

        except:

            print("Hesap Numarası Kısmına Kabul Edilmeyen Karakter Girdiğiniz için İşleminiz İptal Edilmiştir....")
            time.sleep(3)
            
            print("Olası Güvenlik Problemlerinden Dolayı Uygulamadan Çıkış Yapıyorsunuz.. Lütfen Bekleyiniz...")
            time.sleep(3)
            
            UserLogIn = False


        print("Sayın {}, Lütfen Göndermek İstediğiniz Tutarı Yazınız. (İşlem Ücreti 2 TL'dir)".format(User[3]))
        
        try:
            MoneyTransferCash = int(input())

        except:

            print("Göndermek İstedeiğiniz Tutar Bölümüne Kabul Edilmeyen Karakter Girdiğiniz İçin İşleminiz İptal Edilmiştir.")
            time.sleep(3)

            print("Olası Güvenlik Problemlerinden Dolayı Uygulamadan Çıkış Yapıyorsunuz... Lütfen Bekleyiniz...")
            time.sleep(3)
            
            UserLogIn = False
            
        print("Lütfen Bekleyin. Kontroller Yapılıyor....")

        print(User)

        bakiye = User[6]
        FindNewCustomer = False
        

        if MoneyTransferCash <= (bakiye - 2):

            if MoneyTransferID != User[1]:

                baglanti = sqlite3.connect("database.db")

                cursor = baglanti.cursor()

                cursor.execute("SELECT * FROM CUSTOMERS")
                TargetCustomer = cursor.fetchall()

                klm = True

                for i in TargetCustomer:
                    if i[1] == MoneyTransferID:
                        NewCustomer = list(i)
                        FindNewCustomer = True
                    
                    
            else:
                print("Kendi Kendinize Para Gönderemezsiniz!")
                klm = False
                time.sleep(3)



            if FindNewCustomer == True:
                A1Bakiye = NewCustomer[6]
                bakiye = bakiye - MoneyTransferCash - 2
                A1Bakiye = A1Bakiye + MoneyTransferCash

                cursor.execute("UPDATE CUSTOMERS SET HesapBakiyesi = ? WHERE HesapNumarasi = ?",(bakiye,User[1]))
                baglanti.commit()
                cursor.execute("UPDATE CUSTOMERS SET HesapBakiyesi = ? WHERE HesapNumarasi = ?",(A1Bakiye,NewCustomer[1]))
                baglanti.commit()
                baglanti.close()
                print("Para Gönderme İşleminiz Başarıyla Tamamlanmıştır. Kalan Bakiyeniz: {} TL".format(bakiye))
                time.sleep(3)
            elif klm == True:
                print("Girdiğiniz Hesap Numarasına Ait Birisi Bulunamamaıştır.")    
                time.sleep(4)
        else:
            print("Hesabınızda Yeterli Bakiye Bulunamamıştır.")
            time.sleep(3)
            print("Ana Menüye Yönlendiriliyorsunuz. Lütfen Bekleyiniz...")
            time.sleep(3)


    elif Proccess == 3:
        print("Şu An ki Kredi Kartı Borcunuz: {} TL".format(User[7]))
        Borc = User[7]

        print("Şu an ki Bakiyeniz ise: {} TL".format(User[6]))
        time.sleep(1)


        print("\n Lütfen Ödemek İstediğiniz Tutarı Yazınız.")

        try:
            odenecekBorc = int(input())

        except:
            print("Kabul Edilmeyen Karakter Girmenizden Dolayı İşleminiz İptal Edilmiştir.Olası Güvenlik Problemlerinden Dolayı Uygulamadan Çıkış Yapıyorsunuz.....")
            time.sleep(3)
            
            UserLogIn = False


        if odenecekBorc <= User[6]:
             
            if odenecekBorc <= User[7]:

                print("Ödeme İşleminiz Başlamıştır. Lütfen Bekleyiniz...")

                Bakiye = User[6] - odenecekBorc
                NewBorc = Borc - odenecekBorc

                baglanti = sqlite3.connect("database.db")

                cursor = baglanti.cursor()

                cursor.execute("UPDATE CUSTOMERS SET HesapBakiyesi = ? AND KrediKartiBorcu = ? WHERE HesapNumarasi = ?",(Bakiye,NewBorc,User[1]))
                
                baglanti.commit()
                baglanti.close()
                User[6] = Bakiye
                User[7] = NewBorc



                print("Ödeme İşleminiz Başarıyla Tamamlanmıştır.")
                time.sleep(3)

    elif Proccess == 4:

        if User[10] == 1000:

            print("B Sınıfı (B-B1-F-M) Ehliyet Harcı Ödemeniz Bulunmaktadır Ve Toplamda Sizden Tahsil Edilecek Tutar 1000 TL'dir.")
            time.sleep(3)

            print("Bakiye KontrolÜ Yapılıyor Lütfen Bekleyiniz...")
            time.sleep(2)


            if User[6] < 1000:
                print("Ödemek İçin Yeterli Bakiyeniz Bulunamamıştır.")
                time.sleep(3)
            
            else:
                print("Yeterli Bakiye Hesabınızda Bulunmaktadır. Ödeme Yapmak İster Misiniz? (1 - Evet, 2 - Hayır)")

                try:
                    OdemeOnay = int(input())
                except:
                    print("Ödeme Onay İşleminize Gerekli Cevabı Vermediğiniz İçin İşleminiz İptal Edilmiştir..")
                    time.sleep(3)

                    print("Olası Güvenlik Problemlerinden Dolayı Uygulamadan Çıkış Yapıyorsunuz... Lütfen Bekleyiniz...")
                    time.sleep(3)
                    UserLogIn = False


                if OdemeOnay == 1:
                    print("Ödeme İşleminiz Sürüyor... Lütfen Bekleyiniz...")


                    GeciciBakiye = User[6] - User[10]
                    User[6] = GeciciBakiye
                    User[10] = 0



                    baglanti = sqlite3.connect("database.db")
                    cursor = baglanti.cursor()

                    cursor.execute("UPDATE SET CUSTOMERS HesapBakiyesi = ? AND EhliyetHarci = ? WHERE TC_NO = ?",(User[6],0,User[2]))
                    baglanti.commit()
                    baglanti.close()

                    print("Ödeme İşleminiz Başarıyla Tamamlanmıştır. Kalan Bakiyeniz: {} TL".format(User[6]))
                    time.sleep(2)

                    print("Ana Menüye Yönlendiriliyorsunuz. Lütfen Bekleyiniz...")
                    time.sleep(2)
                
                elif OdemeOnay == 2:
                    print("İşlem İptalini Seçtiniz. Ana Menüye Yönlendirilirken Lütfen Bekleyiniz...")
                    time.sleep(3)
                    

                else:
                    print("İşlem İptali Gerçekleştiriliyor... Lütfen Bekleyiniz...")
                    time.sleep(3)

                    
        elif User[10] == 600:
            print("Motosiklet Sınıfı Ehliyet Harcı Ödemeniz Bulunmaktadır Ve Toplamda Sizden Tahsil Edilecek Tutar 600 TL'dir.")
            time.sleep(3)

            print("Bakiye KontrolÜ Yapılıyor Lütfen Bekleyiniz...")
            time.sleep(2)


            if User[6] < 600:
                print("Ödemek İçin Yeterli Bakiyeniz Bulunamamıştır.")
                time.sleep(3)
            
            else:
                print("Yeterli Bakiye Hesabınızda Bulunmaktadır. Ödeme Yapmak İster Misiniz? (1 - Evet, 2 - Hayır)")

                try:
                    OdemeOnay = int(input())
                except:
                    print("Ödeme Onay İşleminize Gerekli Cevabı Vermediğiniz İçin İşleminiz İptal Edilmiştir..")
                    time.sleep(3)

                    print("Olası Güvenlik Problemlerinden Dolayı Uygulamadan Çıkış Yapıyorsunuz... Lütfen Bekleyiniz...")
                    time.sleep(3)
                    UserLogIn = False


                if OdemeOnay == 1:
                    print("Ödeme İşleminiz Sürüyor... Lütfen Bekleyiniz...")


                    GeciciBakiye = User[6] - User[10]
                    User[6] = GeciciBakiye
                    User[10] = 0



                    baglanti = sqlite3.connect("database.db")
                    cursor = baglanti.cursor()

                    cursor.execute("UPDATE SET CUSTOMERS HesapBakiyesi = ? AND EhliyetHarci = ? WHERE TC_NO = ?",(User[6],0,User[2]))
                    baglanti.commit()
                    baglanti.close()

                    print("Ödeme İşleminiz Başarıyla Tamamlanmıştır. Kalan Bakiyeniz: {} TL".format(User[6]))
                    time.sleep(2)

                    print("Ana Menüye Yönlendiriliyorsunuz. Lütfen Bekleyiniz...")
                    time.sleep(2)
                
                elif OdemeOnay == 2:
                    print("İşlem İptalini Seçtiniz. Ana Menüye Yönlendirilirken Lütfen Bekleyiniz...")
                    time.sleep(3)
                    

                else:
                    print("İşlem İptali Gerçekleştiriliyor... Lütfen Bekleyiniz...")
                    time.sleep(3)
        elif User[6] == 1200:
            print("Ağır İş Makinaları Sınıfı Ehliyet Harcı Ödemeniz Bulunmaktadır Ve Toplamda Sizden Tahsil Edilecek Tutar 1200 TL'dir.")
            time.sleep(3)

            print("Bakiye KontrolÜ Yapılıyor Lütfen Bekleyiniz...")
            time.sleep(2)


            if User[6] < 1200:
                print("Ödemek İçin Yeterli Bakiyeniz Bulunamamıştır.")
                time.sleep(3)
            
            else:
                print("Yeterli Bakiye Hesabınızda Bulunmaktadır. Ödeme Yapmak İster Misiniz? (1 - Evet, 2 - Hayır)")

                try:
                    OdemeOnay = int(input())
                except:
                    print("Ödeme Onay İşleminize Gerekli Cevabı Vermediğiniz İçin İşleminiz İptal Edilmiştir..")
                    time.sleep(3)

                    print("Olası Güvenlik Problemlerinden Dolayı Uygulamadan Çıkış Yapıyorsunuz... Lütfen Bekleyiniz...")
                    time.sleep(3)
                    
                    UserLogIn = False



                if OdemeOnay == 1:
                    print("Ödeme İşleminiz Sürüyor... Lütfen Bekleyiniz...")


                    GeciciBakiye = User[6] - User[10]
                    User[6] = GeciciBakiye
                    User[10] = 0



                    baglanti = sqlite3.connect("database.db")
                    cursor = baglanti.cursor()

                    cursor.execute("UPDATE SET CUSTOMERS HesapBakiyesi = ? AND EhliyetHarci = ? WHERE TC_NO = ?",(User[6],0,User[2]))
                    baglanti.commit()
                    baglanti.close()

                    print("Ödeme İşleminiz Başarıyla Tamamlanmıştır. Kalan Bakiyeniz: {} TL".format(User[6]))
                    time.sleep(2)

                    print("Ana Menüye Yönlendiriliyorsunuz. Lütfen Bekleyiniz...")
                    time.sleep(2)
                
                elif OdemeOnay == 2:
                    print("İşlem İptalini Seçtiniz. Ana Menüye Yönlendirilirken Lütfen Bekleyiniz...")
                    time.sleep(3)
                    

                else:
                    print("İşlem İptali Gerçekleştiriliyor... Lütfen Bekleyiniz...")
                    time.sleep(3)
           

        elif User[6] == 0:
            print("Herhangi Bir Ehliyet Harcı Borcunuz Bulunmamaktadır. Başka İşlem Yapmak İster Misiniz? (1 - Evet, 2 - Hayır)")

            try:
                BaskaIslem = int(input())

            except:

                print("Kabul Edilmeyen Karakter Girdiğiniz İçin İşleminiz İptal Edilmiştir...")

                print("Olası Güvenlik Problemlerinden Dolayı Uygulamadan Çıkış Yapıyorsunuz... Lütfen Bekleyiniz...")
                time.sleep(3)
                UserLogIn = False
                 

            if BaskaIslem == 1:
                MainMenu()
            elif BaskaIslem == 2:
                print("İyi Günler Dileriz. Bizi Tercih Ettiğiniz İçin Teşekkürler...")

                time.sleep(4)
                UserLogIn = False

            else:
                print("İyi Günler Dileriz. Bizi Tercih Ettiğiniz İçin Teşekkürler...")

                time.sleep(4)
                UserLogIn = False

    elif Proccess == 5:
        print("Telefon Faturanız Var Mı Diye Kontrol Ediyoruz... Lütfen Bekleyiniz...")

        if User[9] > 0:
            print("{} TL Değerinde Telefon Faturası Borcunuz Bulunmaktadır. Ödemek İster Misiniz? (1 - Evet 2 - Hayır)")

            try:
                OdemeOnay = int(input())

            except:
                print("Kabul Edilmeyen Karakter Girdiniz.")
                time.sleep(2)

                print("Olası Güvenlik Problemlerinden Dolayı Uygulamadan Çıkış Yapıyorsunuz... Lütfen Bekleyiniz...")
                time.sleep(3)
                UserLogIn = False
            
            if OdemeOnay == 1:
                print("Ödeme İşlemi Başlatıldı. Lütfen Bekleyiniz...")

                if User[9] > User[6]:

                    print("Hesabınızda Yeterli Bakiye Bulunmadığından Dolayı İşleminiz İptal Edilmiştir.")
                    time.sleep(2)

                    print("Ana Menüye Yönlendriliyorsunuz. Lütfen Bekleyiniz...")

                    time.sleep(2)
                else:
                    time.sleep(1)
                    print("Ödeme İşlemi Devam Ediyor. Lütfen Bekleyiniz..")

                    GeciciBakiye = User[6] - User[9]
                    User[9] = 0


                    baglanti = sqlite3.connect("database.db")

                    cursor = baglanti.cursor()

                    cursor.execute("UPDATE SET CUSTOMERS HesapBakiyesi = ? AND TelefonFaturasi = ? WHERE TC_NO = ?",(GeciciBakiye,0,User[2]))
                    
                    print("Ödeme İşleminiz Başarıyla Tamamlanmıştır. Kalan Bakiyeniz: {} TL'dir.".format(User[6]))
                    time.sleep(3)

                    print("Ana Menüye Yönlendiriliyorsunuz. Lütfen Bekleyiniz...")

                    time.sleep(3)
            elif OdemeOnay == 2:

                print("Ödeme İşlemini İptal Ettiniz. Başka Bir İşlem Yapmak İster Misiniz? (1- Evet, 2 - Hayır)")

                try:
                    BaskaIslem = int(input())

                    if BaskaIslem == 1:
                        print("Ana Menüye Yönlendiriliyorsunuz. Lütfen bekleyiniz...")
                        time.sleep(3)

                    elif BaskaIslem == 2:

                        print("Çıkış Yapıyorsunuz. Bizi Tercih Ettiğiniz İçin Teşekkürler!")
                        time.sleep(3)
                        
                        UserLogIn = False
                    
                    else:

                        print("Hatalı Giriş Yaptığınız İçin Çıkış Yapıyorsunuz. Lütfen Bekleyiniz...")
                        time.sleep(3)

                        UserLogIn = False

                except:

                    print("Hatalı Giriş yaptınız. Çıkışınız Yapılıyor Lütfen Bekleyiniz...")
                    time.sleep(3)
                    UserLogIn == False
            else:

               print("Hatalı Giriş Yapmanızdan Ötürü GÜvenlik Amacıyla Çıkışınız Yapılıyor. Lütfen Bekleyiniz...")
               time.sleep(3)

               UserLogIn = False
        else:

            print("Herhangi Bir Telefon Faturası Borcunuz Bulunmamaktadır. Başka İşlem yapmak İstediğinizden Emin Misiniz?")

            try:
                BaskaIslem = int(input())

            except:

                print("Yanlış Karakter Girdiğinizden Dolayı Çıkış Yapılıyor. Lütfen Bekleyiniz...")

                UserLogIn = False

                time.sleep(4)
    if Proccess == 6:
        print("Adınıza Kayıtlı elektrik faturası var mı diye kontrol ediliyor... Lütfen bekleyiniz...")

        if User[11] > 0:
            print("Adınıza Kayıtlı aboneliğinize ait {} TL Borcunuz bulunmaktadır. Ödemek ister misiniz? (1 - Evet, 2 - Hayır)".format(User[11]))

            try:
                IslemOnay = int(input())

                if IslemOnay == 1:
                    print("Ödeme İşleminiz Başlatıldı. Lütfen Bekleyiniz.")

                    baglanti = sqlite3.connect("database.db")
                    cursor = baglanti.cursor()

                    GeciciBakiye = User[6] - User[11]

                    User[11] = 0
                    User[6] = GeciciBakiye



                    cursor.execute("UPDATE SET CUSTOMERS ElektrikFaturasi = ? AND HesapBakiyesi = ? WHERE TC_NO",(0,User[6],User[2]))

                    baglanti.cursor()

                    baglanti.close()

                    print("Ödeme İşleminiz Tamamlanmıştır. Kalan Bakiyeniz: {} TL'dir".format(User[6]))


            except:
                print("Hatalı Girdi Yaptığınız İçin İşleminiz İptal Edilmiştir. Ana Menüye Yönlendiriliyorsunuz. Lütfen bekleyiniz...")
                time.sleep(3)
                
                            
        else:

            print("Adınıza Kayıtlı Bir Elektrik Faturası Bulunmamaktadır. Ana Menüye Yönlendirilirken Lütfen Bekleyiniz...")
            time.sleep(3)



DenemeHakki = 3


while UserLogIn == False:
    LoginScreen()
    if UserLogIn == False:

        DenemeHakki = DenemeHakki - 1
        print("Kalan Deneme Hakkınız: {}".format(DenemeHakki))
        if DenemeHakki == 0:
            print("Deneme Hakkınız Kalmamıştır. Lütfen Daha Sonra Tekrar Deneyiniz...")
        
        break
    else:
        break

while UserLogIn==True:
    ClearScreen()
    MainMenu()

