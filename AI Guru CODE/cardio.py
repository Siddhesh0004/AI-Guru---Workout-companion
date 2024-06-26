# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Count2.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1178, 609)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, -10, 1181, 641))
        self.background.setAcceptDrops(False)
        self.background.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.background.setAutoFillBackground(True)
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap("CPENT-master\images\cardio_image.jpg"))
        self.background.setScaledContents(True)
        self.background.setOpenExternalLinks(False)
        self.background.setObjectName("background")
        
        self.view = QtWidgets.QLabel(self.centralwidget)
        self.view.setGeometry(QtCore.QRect(270, 130, 600, 450))
        self.view.setStyleSheet("background-color: rgb(157, 157, 157);")
        self.view.setText("")
        self.view.setObjectName("view")
        
        self.yoga = QtWidgets.QPushButton(self.centralwidget)
        self.yoga.setGeometry(QtCore.QRect(30, 280, 221, 151))
        
        self.yoga.setStyleSheet(u"background-color:#7689de;\n"
"color:#a9dce3;\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color:black;\n"
"font:bold 25px;\n"
"padding :6px;\n"
"min-width:10px;\n"
"")
        self.yoga.setObjectName("yoga")
        
        self.beginner = QtWidgets.QPushButton(self.centralwidget)
        self.beginner.setGeometry(QtCore.QRect(30, 160, 221, 91))
        self.beginner.setStyleSheet(u"background-color:#7689de;\n"
"color:#a9dce3;\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color:black;\n"
"font:bold 25px;\n"
"padding :6px;\n"
"min-width:10px;\n"
"")
        self.beginner.setObjectName("beginner")
        
        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(60, 490, 171, 51))
        self.back.setStyleSheet(u"background-color:#7689de;\n"
"color:#a9dce3;\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color:black;\n"
"font:bold 25px;\n"
"padding :6px;\n"
"min-width:10px;\n"
"")
        self.back.setObjectName("back")
        
        self.information = QtWidgets.QLabel(self.centralwidget)
        self.information.setGeometry(QtCore.QRect(890, 130, 261, 241))
        self.information.setStyleSheet("background-color: rgb(157, 157, 157);")
        self.information.setText("")
        self.information.setObjectName("information")
        
        self.start = QtWidgets.QPushButton(self.centralwidget)
        self.start.setGeometry(QtCore.QRect(890, 390, 91, 51))
        self.start.setStyleSheet(u"background-color:#7689de;\n"
"color:#a9dce3;\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color:black;\n"
"font:bold 25px;\n"
"padding :6px;\n"
"min-width:10px;\n"
"")
        self.start.setObjectName("start")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(1030, 450, 111, 91))
        self.lcdNumber.setObjectName("lcdNumber")
        
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(870, 470, 121, 61))
        self.label_2.setStyleSheet("border-color: rgb(255, 170, 0);\n"
"font: 45 48pt \"Calibri\";\n"
"color: rgb(255, 255, 255);\n"
"font:30pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        
        self.timeLabel = QtWidgets.QLabel(self.centralwidget)
        self.timeLabel.setGeometry(QtCore.QRect(1020, 380, 121, 61))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(25)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.timeLabel.setFont(font)
        self.timeLabel.setStyleSheet("color: rgb(255, 255, 255);\n"
"")
        self.timeLabel.setObjectName("timeLabel")
        
        
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))       
        self.yoga.setText(_translate("MainWindow", "INFO......"))
        self.beginner.setText(_translate("MainWindow", "BEGINNER"))
        
        self.back.setText(_translate("MainWindow", "BACK"))
        self.start.setText(_translate("MainWindow", "STOP"))
        
        
        self.timeLabel.setText(_translate("MainWindow", "00:00"))
        self.label_2.setText(_translate("MainWindow", "SETS"))
import yoga1_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
