# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\pandemieSchoen3dialogSimulation.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(901, 1148)
        Dialog.setStyleSheet("/*\n"
"    Copyright 2013 Emanuel Claesson\n"
"\n"
"    Licensed under the Apache License, Version 2.0 (the \"License\");\n"
"    you may not use this file except in compliance with the License.\n"
"    You may obtain a copy of the License at\n"
"\n"
"        http://www.apache.org/licenses/LICENSE-2.0\n"
"\n"
"    Unless required by applicable law or agreed to in writing, software\n"
"    distributed under the License is distributed on an \"AS IS\" BASIS,\n"
"    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n"
"    See the License for the specific language governing permissions and\n"
"    limitations under the License.\n"
"*/\n"
"\n"
"/*\n"
"    COLOR_DARK     = #191919\n"
"    COLOR_MEDIUM   = #353535\n"
"    COLOR_MEDLIGHT = #5A5A5A\n"
"    COLOR_LIGHT    = #DDDDDD\n"
"    COLOR_ACCENT   = #3D7848\n"
"*/\n"
"\n"
"* {\n"
"    background: #191919;\n"
"    color: #DDDDDD;\n"
"    border: 1px solid #5A5A5A;\n"
"}\n"
"\n"
"QWidget::item:selected {\n"
"    background: #3D7848;\n"
"}\n"
"\n"
"QCheckBox, QRadioButton {\n"
"    border: none;\n"
"}\n"
"\n"
"QRadioButton::indicator, QCheckBox::indicator {\n"
"    width: 13px;\n"
"    height: 13px;\n"
"}\n"
"\n"
"QRadioButton::indicator::unchecked, QCheckBox::indicator::unchecked {\n"
"    border: 1px solid #5A5A5A;\n"
"    background: none;\n"
"}\n"
"\n"
"QRadioButton::indicator::checked, QCheckBox::indicator::checked {\n"
"    border: 1px solid #5A5A5A;\n"
"    background: #3D7848;\n"
"}\n"
"\n"
"QGroupBox {\n"
"    margin-top: 6px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    top: -7px;\n"
"    left: 7px;\n"
"}\n"
"\n"
"QScrollBar {\n"
"    border: 1px solid #5A5A5A;\n"
"    background: #191919;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"    height: 15px;\n"
"    margin: 0px 0px 0px 32px;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    width: 15px;\n"
"    margin: 32px 0px 0px 0px;\n"
"}\n"
"\n"
"QScrollBar::handle {\n"
"    background: #353535;\n"
"    border: 1px solid #5A5A5A;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    border-width: 0px 1px 0px 1px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    border-width: 1px 0px 1px 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    min-width: 20px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    min-height: 20px;\n"
"}\n"
"\n"
"QScrollBar::add-line, QScrollBar::sub-line {\n"
"    background:#353535;\n"
"    border: 1px solid #5A5A5A;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line {\n"
"    position: absolute;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"    width: 15px;\n"
"    subcontrol-position: left;\n"
"    left: 15px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    height: 15px;\n"
"    subcontrol-position: top;\n"
"    top: 15px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"    width: 15px;\n"
"    subcontrol-position: top left;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    height: 15px;\n"
"    subcontrol-position: top;\n"
"}\n"
"\n"
"QScrollBar:left-arrow, QScrollBar::right-arrow, QScrollBar::up-arrow, QScrollBar::down-arrow {\n"
"    border: 1px solid #5A5A5A;\n"
"    width: 3px;\n"
"    height: 3px;\n"
"}\n"
"\n"
"QScrollBar::add-page, QScrollBar::sub-page {\n"
"    background: none;\n"
"}\n"
"\n"
"QAbstractButton:hover {\n"
"    background: #353535;\n"
"}\n"
"\n"
"QAbstractButton:pressed {\n"
"    background: #5A5A5A;\n"
"}\n"
"\n"
"QAbstractItemView {\n"
"    show-decoration-selected: 1;\n"
"    selection-background-color: #3D7848;\n"
"    selection-color: #DDDDDD;\n"
"    alternate-background-color: #353535;\n"
"}\n"
"\n"
"QHeaderView {\n"
"    border: 1px solid #5A5A5A;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background: #191919;\n"
"    border: 1px solid #5A5A5A;\n"
"    padding: 4px;\n"
"}\n"
"\n"
"QHeaderView::section:selected, QHeaderView::section::checked {\n"
"    background: #353535;\n"
"}\n"
"\n"
"QTableView {\n"
"    gridline-color: #5A5A5A;\n"
"}\n"
"\n"
"QTabBar {\n"
"    margin-left: 2px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    border-radius: 0px;\n"
"    padding: 4px;\n"
"    margin: 4px;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background: #353535;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    border: 1px solid #5A5A5A;\n"
"    background: #353535;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    border: 1px solid #5A5A5A;\n"
"    background: #353535;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    width: 3px;\n"
"    height: 3px;\n"
"    border: 1px solid #5A5A5A;\n"
"}\n"
"\n"
"QAbstractSpinBox {\n"
"    padding-right: 15px;\n"
"}\n"
"\n"
"QAbstractSpinBox::up-button, QAbstractSpinBox::down-button {\n"
"    border: 1px solid #5A5A5A;\n"
"    background: #353535;\n"
"    subcontrol-origin: border;\n"
"}\n"
"\n"
"QAbstractSpinBox::up-arrow, QAbstractSpinBox::down-arrow {\n"
"    width: 3px;\n"
"    height: 3px;\n"
"    border: 1px solid #5A5A5A;\n"
"}\n"
"\n"
"QSlider {\n"
"    border: none;\n"
"}\n"
"\n"
"QSlider::groove:horizontal {\n"
"    height: 5px;\n"
"    margin: 4px 0px 4px 0px;\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    width: 5px;\n"
"    margin: 0px 4px 0px 4px;\n"
"}\n"
"\n"
"QSlider::handle {\n"
"    border: 1px solid #5A5A5A;\n"
"    background: #808080;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    width: 15px;\n"
"    margin: -4px 0px -4px 0px;\n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"    height: 15px;\n"
"    margin: 0px -4px 0px -4px;\n"
"}\n"
"\n"
"QSlider::add-page:vertical, QSlider::sub-page:horizontal {\n"
"    background: #3D7848;\n"
"}\n"
"\n"
"QSlider::sub-page:vertical, QSlider::add-page:horizontal {\n"
"    background: #808080;\n"
"}\n"
"\n"
"QLabel {\n"
"    border: none;\n"
"}\n"
"\n"
"QProgressBar {\n"
"    text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    width: 1px;\n"
"    background-color: #3D7848;\n"
"}\n"
"\n"
"QMenu::separator {\n"
"    background: #353535;\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        self.groupBox_4 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.graphWidget_2 = PlotWidget(self.groupBox_4)
        self.graphWidget_2.setMinimumSize(QtCore.QSize(300, 300))
        self.graphWidget_2.setObjectName("graphWidget_2")
        self.verticalLayout_5.addWidget(self.graphWidget_2)
        self.gridLayout.addLayout(self.verticalLayout_5, 0, 0, 1, 1)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.graphWidget_3 = PlotWidget(self.groupBox_4)
        self.graphWidget_3.setMinimumSize(QtCore.QSize(300, 300))
        self.graphWidget_3.setObjectName("graphWidget_3")
        self.verticalLayout_6.addWidget(self.graphWidget_3)
        self.gridLayout.addLayout(self.verticalLayout_6, 0, 1, 1, 1)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.graphWidget_4 = PlotWidget(self.groupBox_4)
        self.graphWidget_4.setMinimumSize(QtCore.QSize(300, 300))
        self.graphWidget_4.setObjectName("graphWidget_4")
        self.verticalLayout_7.addWidget(self.graphWidget_4)
        self.gridLayout.addLayout(self.verticalLayout_7, 1, 0, 1, 1)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.graphWidget_5 = PlotWidget(self.groupBox_4)
        self.graphWidget_5.setMinimumSize(QtCore.QSize(300, 300))
        self.graphWidget_5.setObjectName("graphWidget_5")
        self.verticalLayout_8.addWidget(self.graphWidget_5)
        self.gridLayout.addLayout(self.verticalLayout_8, 1, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_4)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.spinBox = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout_2.addWidget(self.spinBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.spinBox_2 = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_2.setObjectName("spinBox_2")
        self.horizontalLayout_3.addWidget(self.spinBox_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.spinBox_3 = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_3.setObjectName("spinBox_3")
        self.horizontalLayout.addWidget(self.spinBox_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.spinBox_4 = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_4.setObjectName("spinBox_4")
        self.horizontalLayout_4.addWidget(self.spinBox_4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_5.addWidget(self.label_9)
        self.spinBox_8 = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBox_8.setObjectName("spinBox_8")
        self.horizontalLayout_5.addWidget(self.spinBox_8)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_10 = QtWidgets.QLabel(self.groupBox_2)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_6.addWidget(self.label_10)
        self.spinBox_9 = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBox_9.setObjectName("spinBox_9")
        self.horizontalLayout_6.addWidget(self.spinBox_9)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_11 = QtWidgets.QLabel(self.groupBox_2)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_7.addWidget(self.label_11)
        self.spinBox_10 = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBox_10.setObjectName("spinBox_10")
        self.horizontalLayout_7.addWidget(self.spinBox_10)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_12 = QtWidgets.QLabel(self.groupBox_2)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_8.addWidget(self.label_12)
        self.spinBox_11 = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBox_11.setObjectName("spinBox_11")
        self.horizontalLayout_8.addWidget(self.spinBox_11)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_13 = QtWidgets.QLabel(self.groupBox_2)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_9.addWidget(self.label_13)
        self.spinBox_12 = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBox_12.setObjectName("spinBox_12")
        self.horizontalLayout_9.addWidget(self.spinBox_12)
        self.verticalLayout_3.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_10.addWidget(self.label_6)
        self.spinBox_5 = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBox_5.setObjectName("spinBox_5")
        self.horizontalLayout_10.addWidget(self.spinBox_5)
        self.verticalLayout_3.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_11.addWidget(self.label_7)
        self.spinBox_6 = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBox_6.setObjectName("spinBox_6")
        self.horizontalLayout_11.addWidget(self.spinBox_6)
        self.verticalLayout_3.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_12.addWidget(self.label_8)
        self.spinBox_7 = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBox_7.setObjectName("spinBox_7")
        self.horizontalLayout_12.addWidget(self.spinBox_7)
        self.verticalLayout_3.addLayout(self.horizontalLayout_12)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_14 = QtWidgets.QLabel(self.groupBox_3)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_13.addWidget(self.label_14)
        self.spinBox_13 = QtWidgets.QSpinBox(self.groupBox_3)
        self.spinBox_13.setObjectName("spinBox_13")
        self.horizontalLayout_13.addWidget(self.spinBox_13)
        self.verticalLayout_4.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_15 = QtWidgets.QLabel(self.groupBox_3)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_14.addWidget(self.label_15)
        self.spinBox_14 = QtWidgets.QSpinBox(self.groupBox_3)
        self.spinBox_14.setObjectName("spinBox_14")
        self.horizontalLayout_14.addWidget(self.spinBox_14)
        self.verticalLayout_4.addLayout(self.horizontalLayout_14)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Führe mehrere Simulationen gleichzeitig aus!"))
        self.groupBox_4.setTitle(_translate("Dialog", "GroupBox"))
        self.groupBox.setTitle(_translate("Dialog", "Allgemeine Einstellungen:"))
        self.label_2.setText(_translate("Dialog", "Anzahl paralleler Simulationen:"))
        self.label_3.setText(_translate("Dialog", "Dauer der Simulationen (in Tagen):"))
        self.label_4.setText(_translate("Dialog", "Anzahl der Partikel:"))
        self.label_5.setText(_translate("Dialog", "Anzahl der bereits kranken Partikel:"))
        self.groupBox_2.setTitle(_translate("Dialog", "Infektionsbezogene Einstellungen"))
        self.label_9.setText(_translate("Dialog", "Infektionsrate (in Prozent):"))
        self.label_10.setText(_translate("Dialog", "Infektionsradius:"))
        self.label_11.setText(_translate("Dialog", "Sterberate (in Prozent):"))
        self.label_12.setText(_translate("Dialog", "minimale Infektionsdauer (in Tagen):"))
        self.label_13.setText(_translate("Dialog", "maximale Infektionsdauer (in Tagen):"))
        self.label_6.setText(_translate("Dialog", "Anteil der Immunen nach Genesung (in Prozent):"))
        self.label_7.setText(_translate("Dialog", "minimale Dauer der Immunität (in Tagen):"))
        self.label_8.setText(_translate("Dialog", "maximale Dauer der Immunität (in Tagen):"))
        self.groupBox_3.setTitle(_translate("Dialog", "Bewegungsbezogene Einstellungen"))
        self.label_14.setText(_translate("Dialog", "Eingehaltener Abstandsradius:"))
        self.label_15.setText(_translate("Dialog", "Anteil der Quarantäneeinhaltung (in Prozent):"))
        self.pushButton.setText(_translate("Dialog", "Start"))

from pyqtgraph import PlotWidget
