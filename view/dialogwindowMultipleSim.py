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
        Dialog.resize(1234, 982)
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
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        self.groupBox_4 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.graphWidget_Immune = PlotWidget(self.groupBox_4)
        self.graphWidget_Immune.setMinimumSize(QtCore.QSize(300, 300))
        self.graphWidget_Immune.setObjectName("graphWidget_Immune")
        self.verticalLayout_7.addWidget(self.graphWidget_Immune)
        self.gridLayout.addLayout(self.verticalLayout_7, 1, 0, 1, 1)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.graphWidget_Dead = PlotWidget(self.groupBox_4)
        self.graphWidget_Dead.setMinimumSize(QtCore.QSize(300, 300))
        self.graphWidget_Dead.setObjectName("graphWidget_Dead")
        self.verticalLayout_8.addWidget(self.graphWidget_Dead)
        self.gridLayout.addLayout(self.verticalLayout_8, 1, 1, 1, 1)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.graphWidget_Infected = PlotWidget(self.groupBox_4)
        self.graphWidget_Infected.setMinimumSize(QtCore.QSize(300, 300))
        self.graphWidget_Infected.setObjectName("graphWidget_Infected")
        self.verticalLayout_6.addWidget(self.graphWidget_Infected)
        self.gridLayout.addLayout(self.verticalLayout_6, 0, 1, 1, 1)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.graphWidget_Healthy = PlotWidget(self.groupBox_4)
        self.graphWidget_Healthy.setMinimumSize(QtCore.QSize(300, 300))
        self.graphWidget_Healthy.setObjectName("graphWidget_Healthy")
        self.verticalLayout_5.addWidget(self.graphWidget_Healthy)
        self.gridLayout.addLayout(self.verticalLayout_5, 0, 0, 1, 1)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.graphWidget_Vaccinated = PlotWidget(self.groupBox_4)
        self.graphWidget_Vaccinated.setMinimumSize(QtCore.QSize(300, 300))
        self.graphWidget_Vaccinated.setObjectName("graphWidget_Vaccinated")
        self.horizontalLayout_15.addWidget(self.graphWidget_Vaccinated)
        self.gridLayout.addLayout(self.horizontalLayout_15, 0, 2, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_4)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_countSim = QtWidgets.QLabel(self.groupBox)
        self.label_countSim.setObjectName("label_countSim")
        self.horizontalLayout_2.addWidget(self.label_countSim)
        self.spinBox_countSim = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_countSim.setObjectName("spinBox_countSim")
        self.horizontalLayout_2.addWidget(self.spinBox_countSim)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_simDuration = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_simDuration.setFont(font)
        self.label_simDuration.setObjectName("label_simDuration")
        self.horizontalLayout_3.addWidget(self.label_simDuration)
        self.spinBox_simDuration = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_simDuration.setObjectName("spinBox_simDuration")
        self.horizontalLayout_3.addWidget(self.spinBox_simDuration)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_countParticles = QtWidgets.QLabel(self.groupBox)
        self.label_countParticles.setObjectName("label_countParticles")
        self.horizontalLayout.addWidget(self.label_countParticles)
        self.spinBox_countParticles = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_countParticles.setObjectName("spinBox_countParticles")
        self.horizontalLayout.addWidget(self.spinBox_countParticles)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_countInfectedParticles = QtWidgets.QLabel(self.groupBox)
        self.label_countInfectedParticles.setObjectName("label_countInfectedParticles")
        self.horizontalLayout_4.addWidget(self.label_countInfectedParticles)
        self.spinBox_countInfectedParticles = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_countInfectedParticles.setObjectName("spinBox_countInfectedParticles")
        self.horizontalLayout_4.addWidget(self.spinBox_countInfectedParticles)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_18.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_infectionRate = QtWidgets.QLabel(self.groupBox_2)
        self.label_infectionRate.setObjectName("label_infectionRate")
        self.horizontalLayout_5.addWidget(self.label_infectionRate)
        self.spinBox_infectionRate = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBox_infectionRate.setObjectName("spinBox_infectionRate")
        self.horizontalLayout_5.addWidget(self.spinBox_infectionRate)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_infectionRadius = QtWidgets.QLabel(self.groupBox_2)
        self.label_infectionRadius.setObjectName("label_infectionRadius")
        self.horizontalLayout_6.addWidget(self.label_infectionRadius)
        self.spinBox_infectionRadius = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBox_infectionRadius.setObjectName("spinBox_infectionRadius")
        self.horizontalLayout_6.addWidget(self.spinBox_infectionRadius)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_deathRate = QtWidgets.QLabel(self.groupBox_2)
        self.label_deathRate.setObjectName("label_deathRate")
        self.horizontalLayout_7.addWidget(self.label_deathRate)
        self.spinBox_deathRate = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBox_deathRate.setObjectName("spinBox_deathRate")
        self.horizontalLayout_7.addWidget(self.spinBox_deathRate)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_minInfectionDays = QtWidgets.QLabel(self.groupBox_2)
        self.label_minInfectionDays.setObjectName("label_minInfectionDays")
        self.horizontalLayout_8.addWidget(self.label_minInfectionDays)
        self.spinBox_minInfectionDays = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBox_minInfectionDays.setObjectName("spinBox_minInfectionDays")
        self.horizontalLayout_8.addWidget(self.spinBox_minInfectionDays)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_maxInfectionDays = QtWidgets.QLabel(self.groupBox_2)
        self.label_maxInfectionDays.setObjectName("label_maxInfectionDays")
        self.horizontalLayout_9.addWidget(self.label_maxInfectionDays)
        self.spinBox_maxInfectionDays = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBox_maxInfectionDays.setObjectName("spinBox_maxInfectionDays")
        self.horizontalLayout_9.addWidget(self.spinBox_maxInfectionDays)
        self.verticalLayout_3.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_ImmunePercentage = QtWidgets.QLabel(self.groupBox_2)
        self.label_ImmunePercentage.setObjectName("label_ImmunePercentage")
        self.horizontalLayout_10.addWidget(self.label_ImmunePercentage)
        self.spinBox_ImmunePercentage = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBox_ImmunePercentage.setObjectName("spinBox_ImmunePercentage")
        self.horizontalLayout_10.addWidget(self.spinBox_ImmunePercentage)
        self.verticalLayout_3.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_minImmuneDays = QtWidgets.QLabel(self.groupBox_2)
        self.label_minImmuneDays.setObjectName("label_minImmuneDays")
        self.horizontalLayout_11.addWidget(self.label_minImmuneDays)
        self.spinBox_minImmuneDays = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBox_minImmuneDays.setObjectName("spinBox_minImmuneDays")
        self.horizontalLayout_11.addWidget(self.spinBox_minImmuneDays)
        self.verticalLayout_3.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_maxImmuneDays = QtWidgets.QLabel(self.groupBox_2)
        self.label_maxImmuneDays.setObjectName("label_maxImmuneDays")
        self.horizontalLayout_12.addWidget(self.label_maxImmuneDays)
        self.spinBox_maxImmuneDays = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBox_maxImmuneDays.setObjectName("spinBox_maxImmuneDays")
        self.horizontalLayout_12.addWidget(self.spinBox_maxImmuneDays)
        self.verticalLayout_3.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_18.addWidget(self.groupBox_2)
        self.groupBox_5 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.checkBox_activateVaccination = QtWidgets.QCheckBox(self.groupBox_5)
        self.checkBox_activateVaccination.setObjectName("checkBox_activateVaccination")
        self.horizontalLayout_19.addWidget(self.checkBox_activateVaccination)
        self.verticalLayout_9.addLayout(self.horizontalLayout_19)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_dateForVaccine = QtWidgets.QLabel(self.groupBox_5)
        self.label_dateForVaccine.setObjectName("label_dateForVaccine")
        self.horizontalLayout_16.addWidget(self.label_dateForVaccine)
        self.spinBox_dateForVaccine = QtWidgets.QSpinBox(self.groupBox_5)
        self.spinBox_dateForVaccine.setObjectName("spinBox_dateForVaccine")
        self.horizontalLayout_16.addWidget(self.spinBox_dateForVaccine)
        self.verticalLayout_9.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_vaccineSpeed = QtWidgets.QLabel(self.groupBox_5)
        self.label_vaccineSpeed.setObjectName("label_vaccineSpeed")
        self.horizontalLayout_17.addWidget(self.label_vaccineSpeed)
        self.spinBox_vaccineSpeed = QtWidgets.QSpinBox(self.groupBox_5)
        self.spinBox_vaccineSpeed.setObjectName("spinBox_vaccineSpeed")
        self.horizontalLayout_17.addWidget(self.spinBox_vaccineSpeed)
        self.verticalLayout_9.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.checkBox_healthyFirstVaccinated = QtWidgets.QCheckBox(self.groupBox_5)
        self.checkBox_healthyFirstVaccinated.setObjectName("checkBox_healthyFirstVaccinated")
        self.horizontalLayout_20.addWidget(self.checkBox_healthyFirstVaccinated)
        self.verticalLayout_9.addLayout(self.horizontalLayout_20)
        self.horizontalLayout_18.addWidget(self.groupBox_5)
        self.groupBox_3 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_distanceRadius = QtWidgets.QLabel(self.groupBox_3)
        self.label_distanceRadius.setObjectName("label_distanceRadius")
        self.horizontalLayout_13.addWidget(self.label_distanceRadius)
        self.spinBox_distanceRadius = QtWidgets.QSpinBox(self.groupBox_3)
        self.spinBox_distanceRadius.setObjectName("spinBox_distanceRadius")
        self.horizontalLayout_13.addWidget(self.spinBox_distanceRadius)
        self.verticalLayout_4.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_quarantinePercentage = QtWidgets.QLabel(self.groupBox_3)
        self.label_quarantinePercentage.setObjectName("label_quarantinePercentage")
        self.horizontalLayout_14.addWidget(self.label_quarantinePercentage)
        self.spinBox_quarantinePercentage = QtWidgets.QSpinBox(self.groupBox_3)
        self.spinBox_quarantinePercentage.setObjectName("spinBox_quarantinePercentage")
        self.horizontalLayout_14.addWidget(self.spinBox_quarantinePercentage)
        self.verticalLayout_4.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_18.addWidget(self.groupBox_3)
        self.verticalLayout.addLayout(self.horizontalLayout_18)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Führe mehrere Simulationen gleichzeitig aus!\n"
"(Je nach Konfiguration kann der Prozess einige Zeit dauern! Bitte haben Sie Geduld.)"))
        self.groupBox_4.setTitle(_translate("Dialog", "Graphen"))
        self.groupBox.setTitle(_translate("Dialog", "Allgemeine Einstellungen:"))
        self.label_countSim.setText(_translate("Dialog", "Anzahl paralleler Simulationen:"))
        self.label_simDuration.setText(_translate("Dialog", "Dauer der Simulationen (in Tagen):"))
        self.label_countParticles.setText(_translate("Dialog", "Anzahl der Partikel:"))
        self.label_countInfectedParticles.setText(_translate("Dialog", "Anzahl der bereits kranken Partikel:"))
        self.groupBox_2.setTitle(_translate("Dialog", "Infektionsbezogene Einstellungen"))
        self.label_infectionRate.setText(_translate("Dialog", "Infektionsrate (in Prozent):"))
        self.label_infectionRadius.setText(_translate("Dialog", "Infektionsradius:"))
        self.label_deathRate.setText(_translate("Dialog", "Sterberate (in Prozent):"))
        self.label_minInfectionDays.setText(_translate("Dialog", "minimale Infektionsdauer (in Tagen):"))
        self.label_maxInfectionDays.setText(_translate("Dialog", "maximale Infektionsdauer (in Tagen):"))
        self.label_ImmunePercentage.setText(_translate("Dialog", "Anteil der Immunen nach Genesung (in Prozent):"))
        self.label_minImmuneDays.setText(_translate("Dialog", "minimale Dauer der Immunität (in Tagen):"))
        self.label_maxImmuneDays.setText(_translate("Dialog", "maximale Dauer der Immunität (in Tagen):"))
        self.groupBox_5.setTitle(_translate("Dialog", "Impfbezogene Einstellungen"))
        self.checkBox_activateVaccination.setText(_translate("Dialog", "Impfstoff aktivieren"))
        self.label_dateForVaccine.setText(_translate("Dialog", "Ab diesem Zeitpunkt steht ein Impfstoff zu Verfügung:"))
        self.label_vaccineSpeed.setText(_translate("Dialog", "Impfgeschwindigkeit (Partikel pro Tag):"))
        self.checkBox_healthyFirstVaccinated.setText(_translate("Dialog", "Gesunde werden vor den Immunen geimpft"))
        self.groupBox_3.setTitle(_translate("Dialog", "Bewegungsbezogene Einstellungen"))
        self.label_distanceRadius.setText(_translate("Dialog", "Eingehaltener Abstandsradius:"))
        self.label_quarantinePercentage.setText(_translate("Dialog", "Anteil der Quarantäneeinhaltung (in Prozent):"))
        self.pushButton.setText(_translate("Dialog", "Start"))

from pyqtgraph import PlotWidget