# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'appWindowDesign.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 611)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frameMainButtons = QtWidgets.QFrame(self.centralwidget)
        self.frameMainButtons.setGeometry(QtCore.QRect(-1, 0, 901, 51))
        self.frameMainButtons.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameMainButtons.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameMainButtons.setObjectName("frameMainButtons")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.frameMainButtons)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 901, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.toolButtonHome = QtWidgets.QToolButton(self.horizontalLayoutWidget)
        self.toolButtonHome.setAutoRepeat(False)
        self.toolButtonHome.setAutoExclusive(True)
        self.toolButtonHome.setAutoRaise(False)
        self.toolButtonHome.setObjectName("toolButtonHome")
        self.horizontalLayout.addWidget(self.toolButtonHome)
        self.toolButtonCP = QtWidgets.QToolButton(self.horizontalLayoutWidget)
        self.toolButtonCP.setAutoExclusive(True)
        self.toolButtonCP.setObjectName("toolButtonCP")
        self.horizontalLayout.addWidget(self.toolButtonCP)
        self.toolButtonHP = QtWidgets.QToolButton(self.horizontalLayoutWidget)
        self.toolButtonHP.setAutoExclusive(True)
        self.toolButtonHP.setObjectName("toolButtonHP")
        self.horizontalLayout.addWidget(self.toolButtonHP)
        self.toolButtonTS = QtWidgets.QToolButton(self.horizontalLayoutWidget)
        self.toolButtonTS.setAutoExclusive(True)
        self.toolButtonTS.setObjectName("toolButtonTS")
        self.horizontalLayout.addWidget(self.toolButtonTS)
        self.toolButtonMS = QtWidgets.QToolButton(self.horizontalLayoutWidget)
        self.toolButtonMS.setAutoExclusive(True)
        self.toolButtonMS.setObjectName("toolButtonMS")
        self.horizontalLayout.addWidget(self.toolButtonMS)
        self.toolButtonArt = QtWidgets.QToolButton(self.horizontalLayoutWidget)
        self.toolButtonArt.setAutoExclusive(True)
        self.toolButtonArt.setObjectName("toolButtonArt")
        self.horizontalLayout.addWidget(self.toolButtonArt)
        self.stackedWidgetAllPages = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidgetAllPages.setGeometry(QtCore.QRect(-1, 49, 901, 541))
        self.stackedWidgetAllPages.setObjectName("stackedWidgetAllPages")
        self.pageWelcomeHome = QtWidgets.QWidget()
        self.pageWelcomeHome.setObjectName("pageWelcomeHome")
        self.textWelcome = QtWidgets.QTextBrowser(self.pageWelcomeHome)
        self.textWelcome.setGeometry(QtCore.QRect(200, 130, 511, 201))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(211, 168, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(211, 168, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(211, 168, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(211, 168, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.textWelcome.setPalette(palette)
        self.textWelcome.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textWelcome.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textWelcome.setLineWidth(1)
        self.textWelcome.setMidLineWidth(0)
        self.textWelcome.setAcceptRichText(True)
        self.textWelcome.setObjectName("textWelcome")
        self.stackedWidgetAllPages.addWidget(self.pageWelcomeHome)
        self.pageCP = QtWidgets.QWidget()
        self.pageCP.setObjectName("pageCP")
        self.tabsIn_pageCP = QtWidgets.QTabWidget(self.pageCP)
        self.tabsIn_pageCP.setGeometry(QtCore.QRect(0, 0, 901, 21))
        self.tabsIn_pageCP.setObjectName("tabsIn_pageCP")
        self.tabCPSteinerGrids = QtWidgets.QWidget()
        self.tabCPSteinerGrids.setObjectName("tabCPSteinerGrids")
        self.tabsIn_pageCP.addTab(self.tabCPSteinerGrids, "")
        self.tabCPMobiusTransformations = QtWidgets.QWidget()
        self.tabCPMobiusTransformations.setObjectName("tabCPMobiusTransformations")
        self.tabsIn_pageCP.addTab(self.tabCPMobiusTransformations, "")
        self.mplWidgetIn_pageCP = MplWidget(self.pageCP)
        self.mplWidgetIn_pageCP.setGeometry(QtCore.QRect(0, 20, 621, 491))
        self.mplWidgetIn_pageCP.setObjectName("mplWidgetIn_pageCP")
        self.lineEditCPSGComplexNumber1 = QtWidgets.QLineEdit(self.pageCP)
        self.lineEditCPSGComplexNumber1.setGeometry(QtCore.QRect(630, 50, 71, 21))
        self.lineEditCPSGComplexNumber1.setText("")
        self.lineEditCPSGComplexNumber1.setObjectName("lineEditCPSGComplexNumber1")
        self.pushButtonCPSGCommon = QtWidgets.QPushButton(self.pageCP)
        self.pushButtonCPSGCommon.setGeometry(QtCore.QRect(630, 80, 113, 32))
        self.pushButtonCPSGCommon.setObjectName("pushButtonCPSGCommon")
        self.lineEditCPSGComplexNumber2 = QtWidgets.QLineEdit(self.pageCP)
        self.lineEditCPSGComplexNumber2.setGeometry(QtCore.QRect(720, 50, 71, 21))
        self.lineEditCPSGComplexNumber2.setObjectName("lineEditCPSGComplexNumber2")
        self.stackedWidgetAllPages.addWidget(self.pageCP)
        self.pageHP = QtWidgets.QWidget()
        self.pageHP.setObjectName("pageHP")
        self.tabsIn_pageHP = QtWidgets.QTabWidget(self.pageHP)
        self.tabsIn_pageHP.setGeometry(QtCore.QRect(0, 0, 901, 541))
        self.tabsIn_pageHP.setStatusTip("")
        self.tabsIn_pageHP.setObjectName("tabsIn_pageHP")
        self.tabUHP = QtWidgets.QWidget()
        self.tabUHP.setObjectName("tabUHP")
        self.tabsIn_tabUHP = QtWidgets.QTabWidget(self.tabUHP)
        self.tabsIn_tabUHP.setGeometry(QtCore.QRect(0, 0, 901, 21))
        self.tabsIn_tabUHP.setObjectName("tabsIn_tabUHP")
        self.tabUHPBasicConstructions = QtWidgets.QWidget()
        self.tabUHPBasicConstructions.setObjectName("tabUHPBasicConstructions")
        self.tabsIn_tabUHP.addTab(self.tabUHPBasicConstructions, "")
        self.tabUHPGeodesicMotion = QtWidgets.QWidget()
        self.tabUHPGeodesicMotion.setObjectName("tabUHPGeodesicMotion")
        self.tabsIn_tabUHP.addTab(self.tabUHPGeodesicMotion, "")
        self.tabUHPCircularMotion = QtWidgets.QWidget()
        self.tabUHPCircularMotion.setObjectName("tabUHPCircularMotion")
        self.tabsIn_tabUHP.addTab(self.tabUHPCircularMotion, "")
        self.tabUHPIsometries = QtWidgets.QWidget()
        self.tabUHPIsometries.setObjectName("tabUHPIsometries")
        self.tabsIn_tabUHP.addTab(self.tabUHPIsometries, "")
        self.mplWidgetIn_tabUHP = MplWidget(self.tabUHP)
        self.mplWidgetIn_tabUHP.setGeometry(QtCore.QRect(0, 20, 621, 491))
        self.mplWidgetIn_tabUHP.setObjectName("mplWidgetIn_tabUHP")
        self.tabsIn_pageHP.addTab(self.tabUHP, "")
        self.tabPD = QtWidgets.QWidget()
        self.tabPD.setObjectName("tabPD")
        self.tabsIn_tabPD = QtWidgets.QTabWidget(self.tabPD)
        self.tabsIn_tabPD.setGeometry(QtCore.QRect(0, 0, 901, 21))
        self.tabsIn_tabPD.setObjectName("tabsIn_tabPD")
        self.tabPDBasicConstructions = QtWidgets.QWidget()
        self.tabPDBasicConstructions.setObjectName("tabPDBasicConstructions")
        self.tabsIn_tabPD.addTab(self.tabPDBasicConstructions, "")
        self.tabPDGeodesicMotion = QtWidgets.QWidget()
        self.tabPDGeodesicMotion.setObjectName("tabPDGeodesicMotion")
        self.tabsIn_tabPD.addTab(self.tabPDGeodesicMotion, "")
        self.tabPDCircularMotion = QtWidgets.QWidget()
        self.tabPDCircularMotion.setObjectName("tabPDCircularMotion")
        self.tabsIn_tabPD.addTab(self.tabPDCircularMotion, "")
        self.tabPDIsometries = QtWidgets.QWidget()
        self.tabPDIsometries.setObjectName("tabPDIsometries")
        self.tabsIn_tabPD.addTab(self.tabPDIsometries, "")
        self.mplWidgetIn_tabPD = MplWidget(self.tabPD)
        self.mplWidgetIn_tabPD.setGeometry(QtCore.QRect(0, 20, 621, 491))
        self.mplWidgetIn_tabPD.setObjectName("mplWidgetIn_tabPD")
        self.tabsIn_pageHP.addTab(self.tabPD, "")
        self.tabHyper = QtWidgets.QWidget()
        self.tabHyper.setObjectName("tabHyper")
        self.tabsIn_tabHyper = QtWidgets.QTabWidget(self.tabHyper)
        self.tabsIn_tabHyper.setGeometry(QtCore.QRect(0, 0, 901, 21))
        self.tabsIn_tabHyper.setObjectName("tabsIn_tabHyper")
        self.tabHyperBasicConstructions = QtWidgets.QWidget()
        self.tabHyperBasicConstructions.setObjectName("tabHyperBasicConstructions")
        self.tabsIn_tabHyper.addTab(self.tabHyperBasicConstructions, "")
        self.tabHyperGeodesicMotion = QtWidgets.QWidget()
        self.tabHyperGeodesicMotion.setObjectName("tabHyperGeodesicMotion")
        self.tabsIn_tabHyper.addTab(self.tabHyperGeodesicMotion, "")
        self.tabHyperCircularMotion = QtWidgets.QWidget()
        self.tabHyperCircularMotion.setObjectName("tabHyperCircularMotion")
        self.tabsIn_tabHyper.addTab(self.tabHyperCircularMotion, "")
        self.tabHyperIsometries = QtWidgets.QWidget()
        self.tabHyperIsometries.setObjectName("tabHyperIsometries")
        self.tabsIn_tabHyper.addTab(self.tabHyperIsometries, "")
        self.mplWidgetIn_tabHyper = MplWidget(self.tabHyper)
        self.mplWidgetIn_tabHyper.setGeometry(QtCore.QRect(0, 20, 621, 491))
        self.mplWidgetIn_tabHyper.setObjectName("mplWidgetIn_tabHyper")
        self.tabsIn_pageHP.addTab(self.tabHyper, "")
        self.tabUHPandPD = QtWidgets.QWidget()
        self.tabUHPandPD.setObjectName("tabUHPandPD")
        self.tabsIn_tabUHPandPD = QtWidgets.QTabWidget(self.tabUHPandPD)
        self.tabsIn_tabUHPandPD.setGeometry(QtCore.QRect(0, 0, 901, 21))
        self.tabsIn_tabUHPandPD.setObjectName("tabsIn_tabUHPandPD")
        self.tabUHPandPDBasicConstructions = QtWidgets.QWidget()
        self.tabUHPandPDBasicConstructions.setObjectName("tabUHPandPDBasicConstructions")
        self.tabsIn_tabUHPandPD.addTab(self.tabUHPandPDBasicConstructions, "")
        self.tabUHPandPDGeodesicMotion = QtWidgets.QWidget()
        self.tabUHPandPDGeodesicMotion.setObjectName("tabUHPandPDGeodesicMotion")
        self.tabsIn_tabUHPandPD.addTab(self.tabUHPandPDGeodesicMotion, "")
        self.tabUHPandPDCircularMotion = QtWidgets.QWidget()
        self.tabUHPandPDCircularMotion.setObjectName("tabUHPandPDCircularMotion")
        self.tabsIn_tabUHPandPD.addTab(self.tabUHPandPDCircularMotion, "")
        self.tabUHPandPDIsometries = QtWidgets.QWidget()
        self.tabUHPandPDIsometries.setObjectName("tabUHPandPDIsometries")
        self.tabsIn_tabUHPandPD.addTab(self.tabUHPandPDIsometries, "")
        self.mplWidgetIn_tabUHPandPD_Upper = MplWidget(self.tabUHPandPD)
        self.mplWidgetIn_tabUHPandPD_Upper.setGeometry(QtCore.QRect(0, 20, 441, 351))
        self.mplWidgetIn_tabUHPandPD_Upper.setObjectName("mplWidgetIn_tabUHPandPD_Upper")
        self.mplWidgetIn_tabUHPandPD_Poincare = MplWidget(self.tabUHPandPD)
        self.mplWidgetIn_tabUHPandPD_Poincare.setGeometry(QtCore.QRect(450, 20, 441, 351))
        self.mplWidgetIn_tabUHPandPD_Poincare.setObjectName("mplWidgetIn_tabUHPandPD_Poincare")
        self.tabsIn_pageHP.addTab(self.tabUHPandPD, "")
        self.tabUHPandHyper = QtWidgets.QWidget()
        self.tabUHPandHyper.setObjectName("tabUHPandHyper")
        self.tabsIn_tabUHPandHyper = QtWidgets.QTabWidget(self.tabUHPandHyper)
        self.tabsIn_tabUHPandHyper.setGeometry(QtCore.QRect(0, 0, 901, 21))
        self.tabsIn_tabUHPandHyper.setObjectName("tabsIn_tabUHPandHyper")
        self.tabUHPandHyperBasicConstructions = QtWidgets.QWidget()
        self.tabUHPandHyperBasicConstructions.setObjectName("tabUHPandHyperBasicConstructions")
        self.tabsIn_tabUHPandHyper.addTab(self.tabUHPandHyperBasicConstructions, "")
        self.tabUHPandHyperGeodesicMotion = QtWidgets.QWidget()
        self.tabUHPandHyperGeodesicMotion.setObjectName("tabUHPandHyperGeodesicMotion")
        self.tabsIn_tabUHPandHyper.addTab(self.tabUHPandHyperGeodesicMotion, "")
        self.tabUHPandHyperCircularMotion = QtWidgets.QWidget()
        self.tabUHPandHyperCircularMotion.setObjectName("tabUHPandHyperCircularMotion")
        self.tabsIn_tabUHPandHyper.addTab(self.tabUHPandHyperCircularMotion, "")
        self.tabUHPandHyperIsometries = QtWidgets.QWidget()
        self.tabUHPandHyperIsometries.setObjectName("tabUHPandHyperIsometries")
        self.tabsIn_tabUHPandHyper.addTab(self.tabUHPandHyperIsometries, "")
        self.mplWidgetIn_tabUHPandHyper_Upper = MplWidget(self.tabUHPandHyper)
        self.mplWidgetIn_tabUHPandHyper_Upper.setGeometry(QtCore.QRect(0, 20, 441, 351))
        self.mplWidgetIn_tabUHPandHyper_Upper.setObjectName("mplWidgetIn_tabUHPandHyper_Upper")
        self.mplWidgetIn_tabUHPandHyper_Hyper = MplWidget(self.tabUHPandHyper)
        self.mplWidgetIn_tabUHPandHyper_Hyper.setGeometry(QtCore.QRect(450, 20, 441, 351))
        self.mplWidgetIn_tabUHPandHyper_Hyper.setObjectName("mplWidgetIn_tabUHPandHyper_Hyper")
        self.tabsIn_pageHP.addTab(self.tabUHPandHyper, "")
        self.tabPDandHyper = QtWidgets.QWidget()
        self.tabPDandHyper.setObjectName("tabPDandHyper")
        self.tabsIn_tabPDandHyper = QtWidgets.QTabWidget(self.tabPDandHyper)
        self.tabsIn_tabPDandHyper.setGeometry(QtCore.QRect(0, 0, 901, 21))
        self.tabsIn_tabPDandHyper.setObjectName("tabsIn_tabPDandHyper")
        self.tabPDandHyperBasicConstructions = QtWidgets.QWidget()
        self.tabPDandHyperBasicConstructions.setObjectName("tabPDandHyperBasicConstructions")
        self.tabsIn_tabPDandHyper.addTab(self.tabPDandHyperBasicConstructions, "")
        self.tabPDandHyperGeodesicMotion = QtWidgets.QWidget()
        self.tabPDandHyperGeodesicMotion.setObjectName("tabPDandHyperGeodesicMotion")
        self.tabsIn_tabPDandHyper.addTab(self.tabPDandHyperGeodesicMotion, "")
        self.tabPDandHyperCircularMotion = QtWidgets.QWidget()
        self.tabPDandHyperCircularMotion.setObjectName("tabPDandHyperCircularMotion")
        self.tabsIn_tabPDandHyper.addTab(self.tabPDandHyperCircularMotion, "")
        self.tabPDandHyperIsometries = QtWidgets.QWidget()
        self.tabPDandHyperIsometries.setObjectName("tabPDandHyperIsometries")
        self.tabsIn_tabPDandHyper.addTab(self.tabPDandHyperIsometries, "")
        self.mplWidgetIn_tabPDandHyper_Poincare = MplWidget(self.tabPDandHyper)
        self.mplWidgetIn_tabPDandHyper_Poincare.setGeometry(QtCore.QRect(0, 20, 441, 351))
        self.mplWidgetIn_tabPDandHyper_Poincare.setObjectName("mplWidgetIn_tabPDandHyper_Poincare")
        self.mplWidgetIn_tabPDandHyper_Hyper = MplWidget(self.tabPDandHyper)
        self.mplWidgetIn_tabPDandHyper_Hyper.setGeometry(QtCore.QRect(450, 20, 441, 351))
        self.mplWidgetIn_tabPDandHyper_Hyper.setObjectName("mplWidgetIn_tabPDandHyper_Hyper")
        self.tabsIn_pageHP.addTab(self.tabPDandHyper, "")
        self.tabThreeModels = QtWidgets.QWidget()
        self.tabThreeModels.setObjectName("tabThreeModels")
        self.tabsIn_tabThreeModels = QtWidgets.QTabWidget(self.tabThreeModels)
        self.tabsIn_tabThreeModels.setGeometry(QtCore.QRect(0, 0, 901, 21))
        self.tabsIn_tabThreeModels.setObjectName("tabsIn_tabThreeModels")
        self.tabThreeModelsBasicConstructions = QtWidgets.QWidget()
        self.tabThreeModelsBasicConstructions.setObjectName("tabThreeModelsBasicConstructions")
        self.tabsIn_tabThreeModels.addTab(self.tabThreeModelsBasicConstructions, "")
        self.tabThreeModelsGeodesicMotion = QtWidgets.QWidget()
        self.tabThreeModelsGeodesicMotion.setObjectName("tabThreeModelsGeodesicMotion")
        self.tabsIn_tabThreeModels.addTab(self.tabThreeModelsGeodesicMotion, "")
        self.tabThreeModelsCircularMotion = QtWidgets.QWidget()
        self.tabThreeModelsCircularMotion.setObjectName("tabThreeModelsCircularMotion")
        self.tabsIn_tabThreeModels.addTab(self.tabThreeModelsCircularMotion, "")
        self.tabThreeModelsIsometries = QtWidgets.QWidget()
        self.tabThreeModelsIsometries.setObjectName("tabThreeModelsIsometries")
        self.tabsIn_tabThreeModels.addTab(self.tabThreeModelsIsometries, "")
        self.mplWidgetIn_tabThreeModels_Upper = MplWidget(self.tabThreeModels)
        self.mplWidgetIn_tabThreeModels_Upper.setGeometry(QtCore.QRect(0, 20, 291, 271))
        self.mplWidgetIn_tabThreeModels_Upper.setObjectName("mplWidgetIn_tabThreeModels_Upper")
        self.mplWidgetIn_tabThreeModels_Hyper = MplWidget(self.tabThreeModels)
        self.mplWidgetIn_tabThreeModels_Hyper.setGeometry(QtCore.QRect(600, 20, 291, 271))
        self.mplWidgetIn_tabThreeModels_Hyper.setObjectName("mplWidgetIn_tabThreeModels_Hyper")
        self.mplWidgetIn_tabThreeModels_Poincare = MplWidget(self.tabThreeModels)
        self.mplWidgetIn_tabThreeModels_Poincare.setGeometry(QtCore.QRect(300, 20, 291, 271))
        self.mplWidgetIn_tabThreeModels_Poincare.setObjectName("mplWidgetIn_tabThreeModels_Poincare")
        self.tabsIn_pageHP.addTab(self.tabThreeModels, "")
        self.stackedWidgetAllPages.addWidget(self.pageHP)
        self.pageTS = QtWidgets.QWidget()
        self.pageTS.setObjectName("pageTS")
        self.stackedWidgetAllPages.addWidget(self.pageTS)
        self.pageMS = QtWidgets.QWidget()
        self.pageMS.setObjectName("pageMS")
        self.stackedWidgetAllPages.addWidget(self.pageMS)
        self.pageArt = QtWidgets.QWidget()
        self.pageArt.setObjectName("pageArt")
        self.stackedWidgetAllPages.addWidget(self.pageArt)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidgetAllPages.setCurrentIndex(0)
        self.tabsIn_pageCP.setCurrentIndex(0)
        self.tabsIn_pageHP.setCurrentIndex(6)
        self.tabsIn_tabUHP.setCurrentIndex(0)
        self.tabsIn_tabPD.setCurrentIndex(0)
        self.tabsIn_tabHyper.setCurrentIndex(0)
        self.tabsIn_tabUHPandPD.setCurrentIndex(0)
        self.tabsIn_tabUHPandHyper.setCurrentIndex(0)
        self.tabsIn_tabPDandHyper.setCurrentIndex(0)
        self.tabsIn_tabThreeModels.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.toolButtonHome, self.toolButtonHP)
        MainWindow.setTabOrder(self.toolButtonHP, self.toolButtonTS)
        MainWindow.setTabOrder(self.toolButtonTS, self.toolButtonMS)
        MainWindow.setTabOrder(self.toolButtonMS, self.toolButtonArt)
        MainWindow.setTabOrder(self.toolButtonArt, self.tabsIn_pageHP)
        MainWindow.setTabOrder(self.tabsIn_pageHP, self.tabsIn_pageCP)
        MainWindow.setTabOrder(self.tabsIn_pageCP, self.tabsIn_tabUHP)
        MainWindow.setTabOrder(self.tabsIn_tabUHP, self.tabsIn_tabPD)
        MainWindow.setTabOrder(self.tabsIn_tabPD, self.tabsIn_tabHyper)
        MainWindow.setTabOrder(self.tabsIn_tabHyper, self.textWelcome)
        MainWindow.setTabOrder(self.textWelcome, self.tabsIn_tabUHPandPD)
        MainWindow.setTabOrder(self.tabsIn_tabUHPandPD, self.tabsIn_tabUHPandHyper)
        MainWindow.setTabOrder(self.tabsIn_tabUHPandHyper, self.tabsIn_tabPDandHyper)
        MainWindow.setTabOrder(self.tabsIn_tabPDandHyper, self.tabsIn_tabThreeModels)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "HG App"))
        self.toolButtonHome.setText(_translate("MainWindow", "Home"))
        self.toolButtonCP.setText(_translate("MainWindow", "Complex Plane"))
        self.toolButtonHP.setText(_translate("MainWindow", "Hyperbolic Plane"))
        self.toolButtonTS.setText(_translate("MainWindow", "Teichmüller Spaces"))
        self.toolButtonMS.setText(_translate("MainWindow", "Moduli Spaces"))
        self.toolButtonArt.setText(_translate("MainWindow", "Art"))
        self.textWelcome.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:36pt;\">Welcome to HG APP!</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:24pt;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">This app is designed to help you visualize properties of the Hyperbolic Plane in its three models -the upper half plane, the Poincaré disc and the hyperboloid.</span></p></body></html>"))
        self.tabsIn_pageCP.setTabText(self.tabsIn_pageCP.indexOf(self.tabCPSteinerGrids), _translate("MainWindow", "Steiner grids"))
        self.tabsIn_pageCP.setTabText(self.tabsIn_pageCP.indexOf(self.tabCPMobiusTransformations), _translate("MainWindow", "Möbius transformations"))
        self.lineEditCPSGComplexNumber1.setPlaceholderText(_translate("MainWindow", "a+bj"))
        self.pushButtonCPSGCommon.setText(_translate("MainWindow", "Show!"))
        self.lineEditCPSGComplexNumber2.setPlaceholderText(_translate("MainWindow", "c+dj"))
        self.tabsIn_tabUHP.setTabText(self.tabsIn_tabUHP.indexOf(self.tabUHPBasicConstructions), _translate("MainWindow", "Basic Constructions"))
        self.tabsIn_tabUHP.setTabText(self.tabsIn_tabUHP.indexOf(self.tabUHPGeodesicMotion), _translate("MainWindow", "Geodesic Motion"))
        self.tabsIn_tabUHP.setTabText(self.tabsIn_tabUHP.indexOf(self.tabUHPCircularMotion), _translate("MainWindow", "Circular Motion"))
        self.tabsIn_tabUHP.setTabText(self.tabsIn_tabUHP.indexOf(self.tabUHPIsometries), _translate("MainWindow", "Isometries"))
        self.tabsIn_pageHP.setTabText(self.tabsIn_pageHP.indexOf(self.tabUHP), _translate("MainWindow", "Upper half plane"))
        self.tabsIn_tabPD.setTabText(self.tabsIn_tabPD.indexOf(self.tabPDBasicConstructions), _translate("MainWindow", "Basic Constructions"))
        self.tabsIn_tabPD.setTabText(self.tabsIn_tabPD.indexOf(self.tabPDGeodesicMotion), _translate("MainWindow", "Geodesic Motion"))
        self.tabsIn_tabPD.setTabText(self.tabsIn_tabPD.indexOf(self.tabPDCircularMotion), _translate("MainWindow", "Circular Motion"))
        self.tabsIn_tabPD.setTabText(self.tabsIn_tabPD.indexOf(self.tabPDIsometries), _translate("MainWindow", "Isometries"))
        self.tabsIn_pageHP.setTabText(self.tabsIn_pageHP.indexOf(self.tabPD), _translate("MainWindow", "Poincaré Disc"))
        self.tabsIn_tabHyper.setTabText(self.tabsIn_tabHyper.indexOf(self.tabHyperBasicConstructions), _translate("MainWindow", "Basic Constructions"))
        self.tabsIn_tabHyper.setTabText(self.tabsIn_tabHyper.indexOf(self.tabHyperGeodesicMotion), _translate("MainWindow", "Geodesic Motion"))
        self.tabsIn_tabHyper.setTabText(self.tabsIn_tabHyper.indexOf(self.tabHyperCircularMotion), _translate("MainWindow", "Circular Motion"))
        self.tabsIn_tabHyper.setTabText(self.tabsIn_tabHyper.indexOf(self.tabHyperIsometries), _translate("MainWindow", "Isometries"))
        self.tabsIn_pageHP.setTabText(self.tabsIn_pageHP.indexOf(self.tabHyper), _translate("MainWindow", "Hyperboloid"))
        self.tabsIn_tabUHPandPD.setTabText(self.tabsIn_tabUHPandPD.indexOf(self.tabUHPandPDBasicConstructions), _translate("MainWindow", "Basic Constructions"))
        self.tabsIn_tabUHPandPD.setTabText(self.tabsIn_tabUHPandPD.indexOf(self.tabUHPandPDGeodesicMotion), _translate("MainWindow", "Geodesic Motion"))
        self.tabsIn_tabUHPandPD.setTabText(self.tabsIn_tabUHPandPD.indexOf(self.tabUHPandPDCircularMotion), _translate("MainWindow", "Circular Motion"))
        self.tabsIn_tabUHPandPD.setTabText(self.tabsIn_tabUHPandPD.indexOf(self.tabUHPandPDIsometries), _translate("MainWindow", "Isometries"))
        self.tabsIn_pageHP.setTabText(self.tabsIn_pageHP.indexOf(self.tabUHPandPD), _translate("MainWindow", "UHP/PD"))
        self.tabsIn_tabUHPandHyper.setTabText(self.tabsIn_tabUHPandHyper.indexOf(self.tabUHPandHyperBasicConstructions), _translate("MainWindow", "Basic Constructions"))
        self.tabsIn_tabUHPandHyper.setTabText(self.tabsIn_tabUHPandHyper.indexOf(self.tabUHPandHyperGeodesicMotion), _translate("MainWindow", "Geodesic Motion"))
        self.tabsIn_tabUHPandHyper.setTabText(self.tabsIn_tabUHPandHyper.indexOf(self.tabUHPandHyperCircularMotion), _translate("MainWindow", "Circular Motion"))
        self.tabsIn_tabUHPandHyper.setTabText(self.tabsIn_tabUHPandHyper.indexOf(self.tabUHPandHyperIsometries), _translate("MainWindow", "Isometries"))
        self.tabsIn_pageHP.setTabText(self.tabsIn_pageHP.indexOf(self.tabUHPandHyper), _translate("MainWindow", "UHP/Hyperboloid"))
        self.tabsIn_tabPDandHyper.setTabText(self.tabsIn_tabPDandHyper.indexOf(self.tabPDandHyperBasicConstructions), _translate("MainWindow", "Basic Constructions"))
        self.tabsIn_tabPDandHyper.setTabText(self.tabsIn_tabPDandHyper.indexOf(self.tabPDandHyperGeodesicMotion), _translate("MainWindow", "Geodesic Motion"))
        self.tabsIn_tabPDandHyper.setTabText(self.tabsIn_tabPDandHyper.indexOf(self.tabPDandHyperCircularMotion), _translate("MainWindow", "Circular Motion"))
        self.tabsIn_tabPDandHyper.setTabText(self.tabsIn_tabPDandHyper.indexOf(self.tabPDandHyperIsometries), _translate("MainWindow", "Isometries"))
        self.tabsIn_pageHP.setTabText(self.tabsIn_pageHP.indexOf(self.tabPDandHyper), _translate("MainWindow", "PD/Hyperboloid"))
        self.tabsIn_tabThreeModels.setTabText(self.tabsIn_tabThreeModels.indexOf(self.tabThreeModelsBasicConstructions), _translate("MainWindow", "Basic Constructions"))
        self.tabsIn_tabThreeModels.setTabText(self.tabsIn_tabThreeModels.indexOf(self.tabThreeModelsGeodesicMotion), _translate("MainWindow", "Geodesic Motion"))
        self.tabsIn_tabThreeModels.setTabText(self.tabsIn_tabThreeModels.indexOf(self.tabThreeModelsCircularMotion), _translate("MainWindow", "Circular Motion"))
        self.tabsIn_tabThreeModels.setTabText(self.tabsIn_tabThreeModels.indexOf(self.tabThreeModelsIsometries), _translate("MainWindow", "Isometries"))
        self.tabsIn_pageHP.setTabText(self.tabsIn_pageHP.indexOf(self.tabThreeModels), _translate("MainWindow", "All three models"))

from mplwidget import MplWidget

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

