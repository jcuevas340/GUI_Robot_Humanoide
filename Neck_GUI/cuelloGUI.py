from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget
from cuelloGUI_ui import *

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kargs)
        self.setupUi(self)

        self.cuelloHorizontalSlider.valueChanged.connect(self.actualizarLabelHorizontal)
        self.cuelloVerticalSlider.valueChanged.connect(self.actualizarLabelVertical)

    def actualizarLabelHorizontal(self, valor):
        self.cuelloHorizontalLabel.setText(str(valor))

    def actualizarLabelVertical(self, valor):
        self.cuelloVerticalLabel.setText(str(valor))

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()