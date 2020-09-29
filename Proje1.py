import sys
from PyQt5.QtWidgets import QWidget , QToolTip , QPushButton,QApplication
from PyQt5.QtGui import QFont

class p_sinifi(QWidget):
    def __init__(self):
        super().__init__()
        self.ekran_tasarla()
    def ekran_tasarla(self):
        self.setToolTip("Bu bir penceredir")
        buton_01= QPushButton("Düğme_tıklanabilir",self)

        buton_01.clicked.connect(self.tiklandi)

        buton_01.move(250,250)
        buton_01.setToolTip("bu tıklanabilir bir butondur")

        self.show()

    def tiklandi(self):
        print("Butona tıklandı")
if __name__== '__main__':
    uygulama = QApplication(sys.argv)
    pencere = p_sinifi()
    sys.exit(uygulama.exec_())

