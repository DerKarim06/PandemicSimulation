# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\pandemieSchoen4.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1392, 1110)
        MainWindow.setStyleSheet("/*\n"
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
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setContentsMargins(-1, -1, 250, -1)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.label_logo = QtWidgets.QLabel(self.centralwidget)
        self.label_logo.setText("")
        self.label_logo.setPixmap(QtGui.QPixmap("resources/icons8-virus-100.png"))
        self.label_logo.setScaledContents(False)
        self.label_logo.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_logo.setObjectName("label_logo")
        self.horizontalLayout_19.addWidget(self.label_logo)
        self.label_header = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_header.setFont(font)
        self.label_header.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_header.setObjectName("label_header")
        self.horizontalLayout_19.addWidget(self.label_header)
        self.verticalLayout.addLayout(self.horizontalLayout_19)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setStyleSheet("")
        self.graphicsView.setObjectName("graphicsView")
        self.horizontalLayout.addWidget(self.graphicsView)
        self.graphWidget = PlotWidget(self.centralwidget)
        self.graphWidget.setObjectName("graphWidget")
        self.horizontalLayout.addWidget(self.graphWidget)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_particlesAmount = QtWidgets.QLabel(self.groupBox)
        self.label_particlesAmount.setObjectName("label_particlesAmount")
        self.horizontalLayout_9.addWidget(self.label_particlesAmount)
        self.spinBox_particlesAmount = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_particlesAmount.setMaximum(500)
        self.spinBox_particlesAmount.setObjectName("spinBox_particlesAmount")
        self.horizontalLayout_9.addWidget(self.spinBox_particlesAmount)
        self.verticalLayout_3.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_initiallyInfected = QtWidgets.QLabel(self.groupBox)
        self.label_initiallyInfected.setObjectName("label_initiallyInfected")
        self.horizontalLayout_10.addWidget(self.label_initiallyInfected)
        self.spinBox_initiallyInfected = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_initiallyInfected.setObjectName("spinBox_initiallyInfected")
        self.horizontalLayout_10.addWidget(self.spinBox_initiallyInfected)
        self.verticalLayout_3.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_speed = QtWidgets.QLabel(self.groupBox)
        self.label_speed.setObjectName("label_speed")
        self.horizontalLayout_15.addWidget(self.label_speed)
        self.label_speedFactor = QtWidgets.QLabel(self.groupBox)
        self.label_speedFactor.setObjectName("label_speedFactor")
        self.horizontalLayout_15.addWidget(self.label_speedFactor)
        self.horizontalSlider = QtWidgets.QSlider(self.groupBox)
        self.horizontalSlider.setMinimum(30)
        self.horizontalSlider.setMaximum(300)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.horizontalSlider.setTickInterval(0)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalLayout_15.addWidget(self.horizontalSlider)
        self.verticalLayout_3.addLayout(self.horizontalLayout_15)
        self.verticalLayout_7.addLayout(self.verticalLayout_3)
        self.horizontalLayout_4.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_infectionRate = QtWidgets.QLabel(self.groupBox_2)
        self.label_infectionRate.setObjectName("label_infectionRate")
        self.horizontalLayout_11.addWidget(self.label_infectionRate)
        self.spinBox_infectionRate = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBox_infectionRate.setMaximum(100)
        self.spinBox_infectionRate.setObjectName("spinBox_infectionRate")
        self.horizontalLayout_11.addWidget(self.spinBox_infectionRate)
        self.verticalLayout_4.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_infectionRadius = QtWidgets.QLabel(self.groupBox_2)
        self.label_infectionRadius.setObjectName("label_infectionRadius")
        self.horizontalLayout_13.addWidget(self.label_infectionRadius)
        self.spinBox_infectionRadius = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBox_infectionRadius.setMaximum(100)
        self.spinBox_infectionRadius.setObjectName("spinBox_infectionRadius")
        self.horizontalLayout_13.addWidget(self.spinBox_infectionRadius)
        self.verticalLayout_4.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_deathRate = QtWidgets.QLabel(self.groupBox_2)
        self.label_deathRate.setObjectName("label_deathRate")
        self.horizontalLayout_12.addWidget(self.label_deathRate)
        self.spinBox_deathRate = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBox_deathRate.setMaximum(100)
        self.spinBox_deathRate.setObjectName("spinBox_deathRate")
        self.horizontalLayout_12.addWidget(self.spinBox_deathRate)
        self.verticalLayout_4.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.label_minInfectionDuration = QtWidgets.QLabel(self.groupBox_2)
        self.label_minInfectionDuration.setObjectName("label_minInfectionDuration")
        self.horizontalLayout_20.addWidget(self.label_minInfectionDuration)
        self.spinBox_minInfectionDuration = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBox_minInfectionDuration.setObjectName("spinBox_minInfectionDuration")
        self.horizontalLayout_20.addWidget(self.spinBox_minInfectionDuration)
        self.verticalLayout_4.addLayout(self.horizontalLayout_20)
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.label_maxInfectionDuration = QtWidgets.QLabel(self.groupBox_2)
        self.label_maxInfectionDuration.setObjectName("label_maxInfectionDuration")
        self.horizontalLayout_21.addWidget(self.label_maxInfectionDuration)
        self.spinBox_maxInfectionDuration = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBox_maxInfectionDuration.setObjectName("spinBox_maxInfectionDuration")
        self.horizontalLayout_21.addWidget(self.spinBox_maxInfectionDuration)
        self.verticalLayout_4.addLayout(self.horizontalLayout_21)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_percentageImmune = QtWidgets.QLabel(self.groupBox_2)
        self.label_percentageImmune.setObjectName("label_percentageImmune")
        self.horizontalLayout_3.addWidget(self.label_percentageImmune)
        self.spinBox_percentageImmune = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBox_percentageImmune.setObjectName("spinBox_percentageImmune")
        self.horizontalLayout_3.addWidget(self.spinBox_percentageImmune)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_minImmuneDuration = QtWidgets.QLabel(self.groupBox_2)
        self.label_minImmuneDuration.setObjectName("label_minImmuneDuration")
        self.horizontalLayout_5.addWidget(self.label_minImmuneDuration)
        self.spinBox_minImmuneDuration = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBox_minImmuneDuration.setObjectName("spinBox_minImmuneDuration")
        self.horizontalLayout_5.addWidget(self.spinBox_minImmuneDuration)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_maxImmuneDuration = QtWidgets.QLabel(self.groupBox_2)
        self.label_maxImmuneDuration.setObjectName("label_maxImmuneDuration")
        self.horizontalLayout_6.addWidget(self.label_maxImmuneDuration)
        self.spinBox_maxImmuneDuration = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBox_maxImmuneDuration.setObjectName("spinBox_maxImmuneDuration")
        self.horizontalLayout_6.addWidget(self.spinBox_maxImmuneDuration)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.verticalLayout_8.addLayout(self.verticalLayout_4)
        self.horizontalLayout_4.addWidget(self.groupBox_2)
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.checkBox_activateVaccination = QtWidgets.QCheckBox(self.groupBox_4)
        self.checkBox_activateVaccination.setObjectName("checkBox_activateVaccination")
        self.horizontalLayout_22.addWidget(self.checkBox_activateVaccination)
        self.verticalLayout_6.addLayout(self.horizontalLayout_22)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_dateForVaccine = QtWidgets.QLabel(self.groupBox_4)
        self.label_dateForVaccine.setObjectName("label_dateForVaccine")
        self.horizontalLayout_7.addWidget(self.label_dateForVaccine)
        self.spinBox_dateForVaccine = QtWidgets.QSpinBox(self.groupBox_4)
        self.spinBox_dateForVaccine.setObjectName("spinBox_dateForVaccine")
        self.horizontalLayout_7.addWidget(self.spinBox_dateForVaccine)
        self.verticalLayout_6.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_vaccineSpeed = QtWidgets.QLabel(self.groupBox_4)
        self.label_vaccineSpeed.setObjectName("label_vaccineSpeed")
        self.horizontalLayout_8.addWidget(self.label_vaccineSpeed)
        self.spinBox_vaccineSpeed = QtWidgets.QSpinBox(self.groupBox_4)
        self.spinBox_vaccineSpeed.setObjectName("spinBox_vaccineSpeed")
        self.horizontalLayout_8.addWidget(self.spinBox_vaccineSpeed)
        self.verticalLayout_6.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.checkBox_healthyFirstVaccinated = QtWidgets.QCheckBox(self.groupBox_4)
        self.checkBox_healthyFirstVaccinated.setObjectName("checkBox_healthyFirstVaccinated")
        self.horizontalLayout_14.addWidget(self.checkBox_healthyFirstVaccinated)
        self.verticalLayout_6.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_4.addWidget(self.groupBox_4)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.checkBox_peopleStayAtHome = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox_peopleStayAtHome.setEnabled(True)
        self.checkBox_peopleStayAtHome.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkBox_peopleStayAtHome.setStyleSheet("QCheckBox::indicator {\n"
"color: black;\n"
"}\n"
"QCheckBox::indicator {\n"
"background: url(...);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"background: url(...);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"background: #3D7848;\n"
"}\n"
"QCheckBox::indicator:pressed {\n"
"background: url(...);\n"
"}\n"
"\n"
"QCheckBox::indicator:hover:checked {\n"
"background: url(...);\n"
"}")
        self.checkBox_peopleStayAtHome.setChecked(False)
        self.checkBox_peopleStayAtHome.setObjectName("checkBox_peopleStayAtHome")
        self.horizontalLayout_16.addWidget(self.checkBox_peopleStayAtHome)
        self.verticalLayout_5.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_distanceRadius = QtWidgets.QLabel(self.groupBox_3)
        self.label_distanceRadius.setObjectName("label_distanceRadius")
        self.horizontalLayout_17.addWidget(self.label_distanceRadius)
        self.spinBox_distanceRadius = QtWidgets.QSpinBox(self.groupBox_3)
        self.spinBox_distanceRadius.setObjectName("spinBox_distanceRadius")
        self.horizontalLayout_17.addWidget(self.spinBox_distanceRadius)
        self.verticalLayout_5.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.label_quarantinePercentage = QtWidgets.QLabel(self.groupBox_3)
        self.label_quarantinePercentage.setObjectName("label_quarantinePercentage")
        self.horizontalLayout_18.addWidget(self.label_quarantinePercentage)
        self.spinBox_quarantinePercentage = QtWidgets.QSpinBox(self.groupBox_3)
        self.spinBox_quarantinePercentage.setObjectName("spinBox_quarantinePercentage")
        self.horizontalLayout_18.addWidget(self.spinBox_quarantinePercentage)
        self.verticalLayout_5.addLayout(self.horizontalLayout_18)
        self.verticalLayout_9.addLayout(self.verticalLayout_5)
        self.horizontalLayout_4.addWidget(self.groupBox_3)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.startSimButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startSimButton.sizePolicy().hasHeightForWidth())
        self.startSimButton.setSizePolicy(sizePolicy)
        self.startSimButton.setMinimumSize(QtCore.QSize(300, 50))
        self.startSimButton.setObjectName("startSimButton")
        self.horizontalLayout_2.addWidget(self.startSimButton)
        self.pauseSimButton = QtWidgets.QPushButton(self.centralwidget)
        self.pauseSimButton.setMinimumSize(QtCore.QSize(300, 50))
        self.pauseSimButton.setObjectName("pauseSimButton")
        self.horizontalLayout_2.addWidget(self.pauseSimButton)
        self.resetSimButton = QtWidgets.QPushButton(self.centralwidget)
        self.resetSimButton.setMinimumSize(QtCore.QSize(300, 50))
        self.resetSimButton.setObjectName("resetSimButton")
        self.horizontalLayout_2.addWidget(self.resetSimButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1392, 23))
        self.menubar.setObjectName("menubar")
        self.menuExport_CSV = QtWidgets.QMenu(self.menubar)
        self.menuExport_CSV.setObjectName("menuExport_CSV")
        self.menuSimulation = QtWidgets.QMenu(self.menubar)
        self.menuSimulation.setObjectName("menuSimulation")
        self.menuDEBUG = QtWidgets.QMenu(self.menubar)
        self.menuDEBUG.setObjectName("menuDEBUG")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExport_CSV = QtWidgets.QAction(MainWindow)
        self.actionExport_CSV.setObjectName("actionExport_CSV")
        self.actionMehrere_Simulationen_ausf_hren = QtWidgets.QAction(MainWindow)
        self.actionMehrere_Simulationen_ausf_hren.setObjectName("actionMehrere_Simulationen_ausf_hren")
        self.actionShow_InfectionRadius = QtWidgets.QAction(MainWindow)
        self.actionShow_InfectionRadius.setCheckable(True)
        self.actionShow_InfectionRadius.setObjectName("actionShow_InfectionRadius")
        self.actionShow_DistanceRadius = QtWidgets.QAction(MainWindow)
        self.actionShow_DistanceRadius.setCheckable(True)
        self.actionShow_DistanceRadius.setObjectName("actionShow_DistanceRadius")
        self.actionSIRD_Modell = QtWidgets.QAction(MainWindow)
        self.actionSIRD_Modell.setObjectName("actionSIRD_Modell")
        self.actionSIRD_Modell_2 = QtWidgets.QAction(MainWindow)
        self.actionSIRD_Modell_2.setObjectName("actionSIRD_Modell_2")
        self.menuExport_CSV.addAction(self.actionExport_CSV)
        self.menuSimulation.addAction(self.actionMehrere_Simulationen_ausf_hren)
        self.menuSimulation.addAction(self.actionSIRD_Modell_2)
        self.menuDEBUG.addAction(self.actionShow_InfectionRadius)
        self.menuDEBUG.addAction(self.actionShow_DistanceRadius)
        self.menubar.addAction(self.menuExport_CSV.menuAction())
        self.menubar.addAction(self.menuSimulation.menuAction())
        self.menubar.addAction(self.menuDEBUG.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_header.setText(_translate("MainWindow", "<html><head/><body><p>Pandemiesimulator</p></body></html>"))
        self.groupBox.setTitle(_translate("MainWindow", "Allgemeine Einstellungen"))
        self.label_particlesAmount.setText(_translate("MainWindow", "Anzahl der Partikel:"))
        self.label_initiallyInfected.setText(_translate("MainWindow", "Anzahl der bereits kranken Partikel:"))
        self.label_speed.setText(_translate("MainWindow", "Geschwindigkeit:"))
        self.label_speedFactor.setText(_translate("MainWindow", "x1"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Infektionsbezogene Einstellungen"))
        self.label_infectionRate.setText(_translate("MainWindow", "Infektionsrate (in Prozent):"))
        self.label_infectionRadius.setText(_translate("MainWindow", "Infektionsradius:"))
        self.label_deathRate.setText(_translate("MainWindow", "Sterberate (in Prozent):"))
        self.label_minInfectionDuration.setText(_translate("MainWindow", "minimale Infektionsdauer (in Tagen):"))
        self.label_maxInfectionDuration.setText(_translate("MainWindow", "maximale Infektionsdauer (in Tagen):"))
        self.label_percentageImmune.setText(_translate("MainWindow", "Anteil der Immunen nach Genesung (in Prozent):"))
        self.label_minImmuneDuration.setText(_translate("MainWindow", "minimale Dauer der Immunität (in Tagen):"))
        self.label_maxImmuneDuration.setText(_translate("MainWindow", "maximale Dauer der Immunität (in Tagen):"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Impfbezogene Einstellungen"))
        self.checkBox_activateVaccination.setToolTip(_translate("MainWindow", "<html><head/><body><p>Aktiviere den Einsatz eines Impfstoffes (Es wird davon ausgegangen, dass geimpfte permanent immun sind)</p></body></html>"))
        self.checkBox_activateVaccination.setText(_translate("MainWindow", "Impfstoff aktivieren"))
        self.label_dateForVaccine.setText(_translate("MainWindow", "Ab diesem Zeitpunkt steht\n"
"ein Impfstoff zu Verfügung:"))
        self.label_vaccineSpeed.setText(_translate("MainWindow", "Impfgeschwindigkeit (Partikel pro Tag):"))
        self.checkBox_healthyFirstVaccinated.setText(_translate("MainWindow", "Gesunde werden vor den Immunen geimpft"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Bewegungsbezogene Einstellungen"))
        self.checkBox_peopleStayAtHome.setText(_translate("MainWindow", "Menschen bleiben zuhause"))
        self.label_distanceRadius.setText(_translate("MainWindow", "Eingehaltener Abstandsradius:"))
        self.label_quarantinePercentage.setText(_translate("MainWindow", "Anteil der Quarantäneeinhaltung (in Prozent):"))
        self.startSimButton.setText(_translate("MainWindow", "Start"))
        self.pauseSimButton.setText(_translate("MainWindow", "Pause"))
        self.resetSimButton.setText(_translate("MainWindow", "Reset"))
        self.menuExport_CSV.setTitle(_translate("MainWindow", "Datei"))
        self.menuSimulation.setTitle(_translate("MainWindow", "Simulation"))
        self.menuDEBUG.setTitle(_translate("MainWindow", "DEBUG"))
        self.actionExport_CSV.setText(_translate("MainWindow", "CSV exportieren"))
        self.actionMehrere_Simulationen_ausf_hren.setText(_translate("MainWindow", "Mehrere Simulationen ausführen"))
        self.actionShow_InfectionRadius.setText(_translate("MainWindow", "Zeige Infektionsradius (Rot)"))
        self.actionShow_DistanceRadius.setText(_translate("MainWindow", "Zeige Abstandsradius (Magenta)"))
        self.actionSIRD_Modell.setText(_translate("MainWindow", "SIRD-Modell"))
        self.actionSIRD_Modell_2.setText(_translate("MainWindow", "SIRD-Modell"))

from pyqtgraph import PlotWidget