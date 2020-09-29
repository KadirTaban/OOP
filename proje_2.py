from PyQt5.QtWidgets import *
import sys

class ana_pen(QWidget):
    def __init__(self):
        super().__init__()




ana_uygulaması= QApplication(sys.argv)

ana_penceresi= ana_pen()
ana_penceresi.show()
ana_uygulaması.exec_()