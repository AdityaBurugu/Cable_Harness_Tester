# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Pin_to_Pin_Automatic.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_Pin_to_PinAutomatic(object):
    def setupUi(self, Dialog_Pin_to_PinAutomatic):
        Dialog_Pin_to_PinAutomatic.setObjectName("Dialog_Pin_to_PinAutomatic")
        Dialog_Pin_to_PinAutomatic.resize(1030, 642)
        self.tableWidget = QtWidgets.QTableWidget(Dialog_Pin_to_PinAutomatic)
        self.tableWidget.setGeometry(QtCore.QRect(10, 41, 1011, 521))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        self.pushButton_Measure = QtWidgets.QPushButton(Dialog_Pin_to_PinAutomatic)
        self.pushButton_Measure.setGeometry(QtCore.QRect(210, 590, 93, 28))
        self.pushButton_Measure.setObjectName("pushButton_Measure")
        self.pushButton_Save = QtWidgets.QPushButton(Dialog_Pin_to_PinAutomatic)
        self.pushButton_Save.setGeometry(QtCore.QRect(310, 590, 93, 28))
        self.pushButton_Save.setObjectName("pushButton_Save")
        self.pushButton_Abort = QtWidgets.QPushButton(Dialog_Pin_to_PinAutomatic)
        self.pushButton_Abort.setGeometry(QtCore.QRect(420, 590, 93, 28))
        self.pushButton_Abort.setObjectName("pushButton_Abort")
        self.pushButton_Back = QtWidgets.QPushButton(Dialog_Pin_to_PinAutomatic)
        self.pushButton_Back.setGeometry(QtCore.QRect(530, 590, 93, 28))
        self.pushButton_Back.setObjectName("pushButton_Back")
        self.progressBar = QtWidgets.QProgressBar(Dialog_Pin_to_PinAutomatic)
        self.progressBar.setGeometry(QtCore.QRect(630, 590, 401, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.label_Units = QtWidgets.QLabel(Dialog_Pin_to_PinAutomatic)
        self.label_Units.setGeometry(QtCore.QRect(20, 590, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_Units.setFont(font)
        self.label_Units.setObjectName("label_Units")
        self.comboBox = QtWidgets.QComboBox(Dialog_Pin_to_PinAutomatic)
        self.comboBox.setGeometry(QtCore.QRect(80, 590, 111, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.label_Elapsedtime = QtWidgets.QLabel(Dialog_Pin_to_PinAutomatic)
        self.label_Elapsedtime.setGeometry(QtCore.QRect(780, 10, 91, 21))
        self.label_Elapsedtime.setObjectName("label_Elapsedtime")
        self.timeEdit_ElapsedTime = QtWidgets.QTimeEdit(Dialog_Pin_to_PinAutomatic)
        self.timeEdit_ElapsedTime.setGeometry(QtCore.QRect(870, 10, 118, 22))
        self.timeEdit_ElapsedTime.setReadOnly(True)
        self.timeEdit_ElapsedTime.setObjectName("timeEdit_ElapsedTime")

        self.retranslateUi(Dialog_Pin_to_PinAutomatic)
        QtCore.QMetaObject.connectSlotsByName(Dialog_Pin_to_PinAutomatic)

    def retranslateUi(self, Dialog_Pin_to_PinAutomatic):
        _translate = QtCore.QCoreApplication.translate
        Dialog_Pin_to_PinAutomatic.setWindowTitle(_translate("Dialog_Pin_to_PinAutomatic", "Pin to Pin Automatic"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog_Pin_to_PinAutomatic", "S.No"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog_Pin_to_PinAutomatic", "Line X"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog_Pin_to_PinAutomatic", "LineY"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog_Pin_to_PinAutomatic", "Min"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Dialog_Pin_to_PinAutomatic", "Measured Value"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Dialog_Pin_to_PinAutomatic", "Max"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Dialog_Pin_to_PinAutomatic", "Units"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Dialog_Pin_to_PinAutomatic", "Results"))
        self.pushButton_Measure.setText(_translate("Dialog_Pin_to_PinAutomatic", "Measure"))
        self.pushButton_Save.setText(_translate("Dialog_Pin_to_PinAutomatic", "Save"))
        self.pushButton_Abort.setText(_translate("Dialog_Pin_to_PinAutomatic", "Abort"))
        self.pushButton_Back.setText(_translate("Dialog_Pin_to_PinAutomatic", "Back"))
        self.label_Units.setText(_translate("Dialog_Pin_to_PinAutomatic", "Units:"))
        self.comboBox.setItemText(0, _translate("Dialog_Pin_to_PinAutomatic", "Ohms"))
        self.label_Elapsedtime.setText(_translate("Dialog_Pin_to_PinAutomatic", "Elapsed Time:"))
        self.timeEdit_ElapsedTime.setDisplayFormat(_translate("Dialog_Pin_to_PinAutomatic", "HH:mm:ss"))