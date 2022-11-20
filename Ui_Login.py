# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Login_Screen(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.setWindowModality(QtCore.Qt.WindowModal)
        Login.resize(517, 232)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Logos/logotrspisq.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Login.setWindowIcon(icon)
        Login.setLayoutDirection(QtCore.Qt.LeftToRight)
        Login.setModal(True)
        self.lineEdit_Username = QtWidgets.QLineEdit(Login)
        self.lineEdit_Username.setGeometry(QtCore.QRect(220, 40, 241, 22))
        self.lineEdit_Username.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_Username.setReadOnly(False)
        self.lineEdit_Username.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.lineEdit_Username.setObjectName("lineEdit_Username")
        self.lineEdit_Password = QtWidgets.QLineEdit(Login)
        self.lineEdit_Password.setGeometry(QtCore.QRect(220, 80, 241, 22))
        self.lineEdit_Password.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.lineEdit_Password.setObjectName("lineEdit_Password")
        self.pushButton_Login = QtWidgets.QPushButton(Login)
        self.pushButton_Login.setGeometry(QtCore.QRect(220, 170, 71, 28))
        self.pushButton_Login.setObjectName("pushButton_Login")
        self.pushButton_Reset = QtWidgets.QPushButton(Login)
        self.pushButton_Reset.setEnabled(True)
        self.pushButton_Reset.setGeometry(QtCore.QRect(300, 170, 93, 28))
        self.pushButton_Reset.setDefault(False)
        self.pushButton_Reset.setFlat(False)
        self.pushButton_Reset.setObjectName("pushButton_Reset")
        self.pushButton_SignUp = QtWidgets.QPushButton(Login)
        self.pushButton_SignUp.setGeometry(QtCore.QRect(400, 170, 71, 28))
        self.pushButton_SignUp.setObjectName("pushButton_SignUp")
        self.pushButton_Forgot_Password = QtWidgets.QPushButton(Login)
        self.pushButton_Forgot_Password.setGeometry(QtCore.QRect(350, 110, 111, 28))
        font = QtGui.QFont()
        font.setUnderline(True)
        self.pushButton_Forgot_Password.setFont(font)
        self.pushButton_Forgot_Password.setFlat(True)
        self.pushButton_Forgot_Password.setObjectName("pushButton_Forgot_Password")
        self.label_Logo = QtWidgets.QLabel(Login)
        self.label_Logo.setGeometry(QtCore.QRect(40, 10, 131, 151))
        self.label_Logo.setText("")
        self.label_Logo.setPixmap(QtGui.QPixmap("Logos/AppLogo128x128.ico"))
        self.label_Logo.setObjectName("label_Logo")

        self.retranslateUi(Login)
        self.pushButton_Reset.clicked.connect(self.lineEdit_Password.clear)
        self.pushButton_Reset.clicked.connect(self.lineEdit_Username.clear)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Login"))
        self.lineEdit_Username.setPlaceholderText(_translate("Login", "Username"))
        self.lineEdit_Password.setPlaceholderText(_translate("Login", "Password"))
        self.pushButton_Login.setText(_translate("Login", "LOGIN"))
        self.pushButton_Reset.setText(_translate("Login", "&RESET"))
        self.pushButton_Reset.setShortcut(_translate("Login", "Ctrl+R"))
        self.pushButton_SignUp.setText(_translate("Login", "SIGN UP"))
        self.pushButton_Forgot_Password.setText(_translate("Login", "Forgot Password"))
