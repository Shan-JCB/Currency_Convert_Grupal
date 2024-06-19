import sys
from PyQt6.QtWidgets import QApplication
from src.currencyconvert.logica.CurrentConvert import Dialogo

if __name__ == '__main__':
    app=QApplication(sys.argv)
    dialogo=Dialogo()
    dialogo.show()
    app.exec()
