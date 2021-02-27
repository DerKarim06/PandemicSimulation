from PyQt5 import QtWidgets, QtCore

from view.dialogwindowCSV import Ui_Dialog


class DialogCSV(QtWidgets.QDialog, Ui_Dialog):

    finishedSignal = QtCore.pyqtSignal(int)

    def __init__(self):
        """this is the constructor of the CSV dialog to enter a specific granularity"""
        super(DialogCSV, self).__init__()
        self.setupUi(self)
        self.connectSignals()

    def connectSignals(self):
        """this function is used to connect the signals"""
        self.buttonBox.accepted.connect(self.okClicked)

    def okClicked(self):
        """this function is called to sent the granularity data with the finishedSignal"""
        self.finishedSignal.emit(self.spinBox.value())
