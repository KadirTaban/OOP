class futbolcu():
    kosu = "koşabilir"
    depar = "depar atar"
    maas= 800
    pass
    def __init__(self,ayak ="sağ"):
        self.mevki = "orta"
        self.ayak=ayak
        mevki = ""
class basketbolcu ():
    turnike="turnike atar"
    ucluk="ucluk atar"
    maas = 950
    def __init__(self):
        self.bolge = "ileri"

    pass

class multisporcu(futbolcu,basketbolcu):
    def __init__(self,ayak):
        basketbolcu.__init__(self)
        futbolcu.__init__(self,ayak)


    pass

mahmut = multisporcu("sol")
print(mahmut.turnike)
print(mahmut.kosu)
print(mahmut.maas)
print(mahmut.mevki)
print(mahmut.ayak)
print(mahmut.bolge)