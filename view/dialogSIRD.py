from PyQt5 import QtWidgets, QtCore

import pyqtgraph as pg
import resources.constants as constants

from view.dialogSIRDwindow import Ui_Dialog


class DialogSIRD(QtWidgets.QDialog, Ui_Dialog):

    finishedSignal = QtCore.pyqtSignal(int, int, float, float, float, int, Ui_Dialog)

    def __init__(self):
        """creates the gui of the SIRD-model calculation"""
        super(DialogSIRD, self).__init__()
        self.setupUi(self)
        self.connectSignals()
        self.data = None

        # initializie widgets
        self.spinBox_population.setMinimum(1)
        self.spinBox_population.setMaximum(1000000000)
        self.spinBox_initiallyInfected.setMinimum(1)
        self.spinBox_initiallyInfected.setMaximum(1000000000)
        self.spinBox_days.setMinimum(1)
        self.spinBox_days.setMaximum(10 * 365)

    def connectSignals(self):
        """this function connects the signals of this class"""
        self.pushButton.clicked.connect(self.okClicked)

    def okClicked(self):
        """this function is activated when starting the calculation of the SIRD-model"""
        self.graphWidget_SIRD.clear()
        self.finishedSignal.emit(self.spinBox_population.value(), self.spinBox_initiallyInfected.value(), self.spinBox_infectionRate.value(), self.spinBox_healthyRate.value(), self.spinBox_deathRate.value(), self.spinBox_days.value(), self)

    def showAlert(self, message):
        """this function shows an alert to the user
        Args:
            message: the message that should be show to the user
        """
        dlg = QtWidgets.QDialog(self)
        dlg.setWindowTitle(constants.ERROR)
        label = QtWidgets.QLabel(dlg)
        label.setText(message)
        label.adjustSize()
        label.move(100, 60)
        dlg.exec_()

    def updateData(self, data):
        """this function updates the data to later be drawn on the GUI
        Args:
            data: a data storage
            """
        t = data[0]
        r = data[1]
        self.graphWidget_SIRD.addLegend()
        self.graphWidget_SIRD.setLabel('left', constants.COUNT_OF_PARTICLES)
        self.graphWidget_SIRD.setLabel('bottom', constants.TIME_IN_WEEKS)
        self.plotHealthy = self.graphWidget_SIRD.plot(t, r[:,0],
                                                  pen=pg.mkPen(color=(0, 255, 0), width=3), name=constants.HEALTHY_NAME)
        self.plotInfected = self.graphWidget_SIRD.plot(t, r[:, 1],
                                                      pen=pg.mkPen(color=(255, 0, 0), width=3),
                                                      name=constants.INFECTED_NAME)
        self.plotImmune = self.graphWidget_SIRD.plot(t, r[:, 2],
                                                      pen=pg.mkPen(color=(255, 255, 0), width=3),
                                                      name=constants.IMMUNE_NAME)
        self.plotDead = self.graphWidget_SIRD.plot(t, r[:, 3],
                                                      pen=pg.mkPen(color=(255, 255, 255), width=3),
                                                      name=constants.DEAD_NAME)