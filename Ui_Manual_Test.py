# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ManualTest.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_Manual_Test(object):
    def setupUi(self, Dialog_Manual_Test):
        Dialog_Manual_Test.setObjectName("Dialog_Manual_Test")
        Dialog_Manual_Test.resize(446, 303)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Logos/logotrspisq.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog_Manual_Test.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(Dialog_Manual_Test)
        self.label.setGeometry(QtCore.QRect(50, 70, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.comboBox_line1 = QtWidgets.QComboBox(Dialog_Manual_Test)
        self.comboBox_line1.setGeometry(QtCore.QRect(20, 110, 101, 31))
        self.comboBox_line1.setObjectName("comboBox_line1")
        self.label_2 = QtWidgets.QLabel(Dialog_Manual_Test)
        self.label_2.setGeometry(QtCore.QRect(200, 70, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.comboBox_Line2 = QtWidgets.QComboBox(Dialog_Manual_Test)
        self.comboBox_Line2.setGeometry(QtCore.QRect(170, 110, 101, 31))
        self.comboBox_Line2.setObjectName("comboBox_Line2")
        self.label_3 = QtWidgets.QLabel(Dialog_Manual_Test)
        self.label_3.setGeometry(QtCore.QRect(330, 70, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.comboBox_Units = QtWidgets.QComboBox(Dialog_Manual_Test)
        self.comboBox_Units.setGeometry(QtCore.QRect(310, 110, 101, 31))
        self.comboBox_Units.setObjectName("comboBox_Units")
        self.comboBox_Units.addItem("Ohms")
        self.label_4 = QtWidgets.QLabel(Dialog_Manual_Test)
        self.label_4.setGeometry(QtCore.QRect(20, 190, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit_VFDMM = QtWidgets.QLineEdit(Dialog_Manual_Test)
        self.lineEdit_VFDMM.setGeometry(QtCore.QRect(150, 190, 221, 22))
        self.lineEdit_VFDMM.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_VFDMM.setObjectName("lineEdit_VFDMM")
        self.pushButton_Measure = QtWidgets.QPushButton(Dialog_Manual_Test)
        self.pushButton_Measure.setGeometry(QtCore.QRect(170, 250, 111, 31))
        self.pushButton_Measure.setObjectName("pushButton_Measure")

        self.retranslateUi(Dialog_Manual_Test)
        QtCore.QMetaObject.connectSlotsByName(Dialog_Manual_Test)

    def retranslateUi(self, Dialog_Manual_Test):
        _translate = QtCore.QCoreApplication.translate
        Dialog_Manual_Test.setWindowTitle(_translate("Dialog_Manual_Test", "Manual Test"))
        self.label.setText(_translate("Dialog_Manual_Test", "Line"))
        self.label_2.setText(_translate("Dialog_Manual_Test", "Line"))
        self.label_3.setText(_translate("Dialog_Manual_Test", "Units"))
        self.comboBox_Units.setItemText(0, _translate("Dialog_Manual_Test", "Ohms"))
        self.label_4.setText(_translate("Dialog_Manual_Test", "Value from DMM"))
        self.lineEdit_VFDMM.setText(_translate("Dialog_Manual_Test", "2.01"))
        self.pushButton_Measure.setText(_translate("Dialog_Manual_Test", "Measure"))
