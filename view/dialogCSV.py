from PyQt5 import QtWidgets, QtCore

from view.dialogwindowCSV import Ui_Dialog


class DialogCSV(QtWidgets.QDialog, Ui_Dialog):

    finishedSignal = QtCore.pyqtSignal(int)

    def __init__(self):
        super(DialogCSV, self).__init__()
        self.setupUi(self)
        self.connectSignals()

    def connectSignals(self):
        self.buttonBox.accepted.connect(self.okClicked)

    def okClicked(self):
        self.finishedSignal.emit(self.spinBox.value())
