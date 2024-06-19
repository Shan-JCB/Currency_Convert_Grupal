import sys
import os

from PyQt6.QtWidgets import QApplication,QDialog
from PyQt6 import uic
from tkinter import messagebox

class Dialogo(QDialog):
    #AusInUS = 2
    #UKInUS = 0.5
    AusInUS = 3
    UKInUS = 1.5
    def __init__(self):
        ruta = os.path.dirname ( os.path.abspath ( __file__ ) ) + r"\..\vista\CurrencyConvert.ui"
        QDialog.__init__(self)
        uic.loadUi(ruta,self)

        self.pbConvert.clicked.connect(self.calculate_convert)
        self.pbExit.clicked.connect(self.exit_app)

    def calculate_convert( self ):
        converted = 0.0
        initial = 0.0

        initial = float(self.ltAmount.text())
        converted=initial
        if self.brFromUK.isChecked():
            converted = initial / self.UKInUS
        elif self.brFromAUS.isChecked():
            converted = initial / self.AusInUS

        if self.brToUK.isChecked():
            converted = converted * self.UKInUS
        elif self.brToAUS.isChecked():
            converted = converted * self.AusInUS
        self.lbResult.setText(converted.__str__())

    def exit_app( self ):
        resultado = messagebox.askquestion("Salir","¿Está seguro que desea salir?")
        if resultado == "yes":
            #exit(0)
            quit(0)

if __name__ == '__main__':
    app=QApplication(sys.argv)
    dialogo=Dialogo()
    dialogo.show()
    app.exec()
