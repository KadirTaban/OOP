class sporcu():
    def __init__(self,ad,brans,altin,gumus,bronz):

        self.ad = ad
        self.brans = brans
        self.mbronz=bronz
        self._mgumus=gumus#yarı gizli
        self.__maltin = altin#tam gizli
    def atlet_bilgisi(self):
        return "ad:{} brans:{}".format(self.ad,self.brans)
    @property
    def a_yazdır(self):
        amadalya = self.__maltin
        return "altın madalya sayısı  {}".format(self.__maltin)
atlet1 =  sporcu("ali","100 metre",2,3,4)
print(atlet1.atlet_bilgisi())
print("bronz madalya sayısı",atlet1.mbronz)
print("gümüş madalya sayısı",atlet1._mgumus)
print(atlet1.a_yazdır)