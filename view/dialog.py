from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import Qt, QRectF
from PyQt5.QtGui import QPen, QBrush
from PyQt5.QtWidgets import QSlider
import numpy as np

from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg

from view.dialogwindow import Ui_Dialog


class Dialog(QtWidgets.QDialog, Ui_Dialog):

    finishedSignal = QtCore.pyqtSignal(int)

    def __init__(self):
        super(Dialog, self).__init__()
        self.setupUi(self)
        self.buttonBox.accepted.connect(self.okClicked)

    def okClicked(self):
        self.finishedSignal.emit(self.spinBox.value())
