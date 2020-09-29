


class an:

    def __init__(self,ad,soyad,puan):#initialization 'kısaltmasıdır.değişkenler için başlatma objesidir.

        self.ad=ad#self metodu ile düzen sağlanır bir nesne için girilen veriyi nesne için kılar.
        self.soyad=soyad
        self.puan = puan

    def tamad(self):
        return "adı:{} soyadı:{} puanı:{}".format(self.ad,self.soyad,self.puan)

personel1=an("kadir","taban",150)
personel2 = an("ali","mahmut",50)

print (an.tamad(personel1))
print("****")
print(an.tamad(personel2))










# Aşağıdaki kısım dersin ilk bölümünde anlatılan kısım


# print(personel1)
# print(personel1.ad,personel1.soyad,personel1.eposta)
# print(personel1.tamad())
#
# print(personel2)
# print(personel2.ad,personel2.soyad)
# print(personel2.eposta)



# class an:
#     def __init__(self,ad,soyad,maas):
#         pass
#
# personel1 = an("ali","demir",2500)
# personel1.ad = "ali"
# personel1.soyad = "demir"
# personel1.maas = 2500
#
# personel2 = an ()
# personel2.ad = "kerim"
# personel2.soyad = "bakir"
# personel2.maas = 1950
#
#
# print(personel1)
# print(personel1.ad,personel1.soyad)
#
# print(personel2)
# print(personel2.ad,personel2.soyad)