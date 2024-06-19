import sys
import os
from PyQt6.QtWidgets import QApplication, QDialog, QMessageBox
from PyQt6 import uic

class Dialogo(QDialog):
    AusInUS = 3
    UKInUS = 1.5
    SOLInUS = 0.27  # Añadir la tasa de conversión de SOL a USD (1 SOL ≈ 0.27 USD)

    def __init__(self):
        ruta = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'vista', 'CurrencyConvert.ui')
        QDialog.__init__(self)
        uic.loadUi(ruta, self)

        self.pbConvert.clicked.connect(self.calculate_convert)
        self.pbExit.clicked.connect(self.exit_app)

    def calculate_convert(self):
        try:
            initial = float(self.ltAmount.text())
        except ValueError:
            QMessageBox.warning(self, "Error", "Por favor, ingrese un número válido.")
            return

        converted = initial
        if self.brFromUK.isChecked():
            converted = initial * self.UKInUS
        elif self.brFromAUS.isChecked():
            converted = initial * self.AusInUS
        elif self.brFromSOL.isChecked():
            converted = initial * self.SOLInUS

        if self.brToUK.isChecked():
            converted = converted / self.UKInUS
        elif self.brToAUS.isChecked():
            converted = converted / self.AusInUS
        elif self.brToSOL.isChecked():
            converted = converted / self.SOLInUS

        self.lbResult.setText(f"{converted:.2f}")

    def exit_app(self):
        resultado = QMessageBox.question(self, "Salir", "¿Está seguro que desea salir?",
                                         QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if resultado == QMessageBox.StandardButton.Yes:
            sys.exit(0)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialogo = Dialogo()
    dialogo.show()
    app.exec()