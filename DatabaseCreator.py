#Veritabanı Oluşturucu by Murtaza SARITÜRK
#Sürüm Numarası 0.1 Debug Derleme 1


try:

    while True:
        print("Var Olan Kişi VeriTabanı Dosyası Üzerinden İşlem Yapmak Mı İstiyorsanız Yeni Dosya Üzerinden Mi? 1 - Var Olan Dosya 2 - Hayır, Yeni Dosya Oluştur - 0 Çıkış")
        
        ddm = int(input())

        if (ddm == 1):
            print("Var Olan Kişi VeriTabanı Dosyası Üzerinden İşlem Yapmayı Seçtiniz. Lütfen Dosya Adını Giriniz:")
            FileLocation = input()

            try:

                print("Dosyanız Aranıyor Lütfen Bekleyiniz.")
                File = open(FileLocation, "a", encoding="utf-8")
                print("Dosyanız Bulundu. İşlemler Başlatılıyor. Lütfen Bekleyiniz.")
                print("Dosyanız Üzerinde Yapmak İstediğiniz İşlemi Seçiniz.")
                print("1 - Dosyadaki verileri ekrana yazdır.")
                print("2 - DOsyaya Veri Ekle")
                print("0 - Çıkış")

                

                try:

                    islem = int(input())

                    if islem == 1:

                        print("Dosyadaki Veriler Ekrana Yazılıyor. Lütfen Bekleyiniz.")

                        FileRead = open(FileLocation, encoding="utf-8")

                        for i in FileRead:
                            print(i)

                        FileRead.close()


                    elif islem == 2:

                        print("Dosya Eklemek İstediğiniz Kişinin Önce Adını Ve Soyadınız Giriniz.")
                        adSoyad = input()

                        print("Şimdi İste Doğum Tarihini Giriniz. ÖRNEK ŞEKİL: 09.09.1999")
                        dogumTarihi = input()

                        print("Şimdi İse Telefon Numarasını Giriniz. Örnek: 5679873219")
                        tlfNo = int(input())

                        print("Şimdi İse Adresini Giriniz. (Zorunlu Değil) - Örnek: Zafer Mah. 1.Sokak. 13.Cadde ONİKİŞUBAT K.Maraş")
                        adres = input()

                        print("Verileriniz Dosyaya Yazdırılıyorken Lütfen Bekleyiniz.")

                        File.write("İsim-Soyisim: {}\nDoğum Tarihi: {}\nTelefon Numarası: {}\nAdres: {}\n".format(adSoyad, dogumTarihi, str(tlfNo), adres))

                        print("İşleminiz Tamamlanmıştır.")

                except ValueError:
                    print("")
            
            except FileNotFoundError:
                print("")


except:
    print("")

finally:
    File.close()
