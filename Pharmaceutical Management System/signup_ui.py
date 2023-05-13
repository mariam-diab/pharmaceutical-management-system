# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signup.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1301, 843)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(420, 90, 471, 191))
        font = QtGui.QFont()
        font.setFamily("PMingLiU-ExtB")
        font.setPointSize(48)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pass_label = QtWidgets.QLabel(Dialog)
        self.pass_label.setGeometry(QtCore.QRect(420, 380, 111, 61))
        font = QtGui.QFont()
        font.setFamily("PMingLiU-ExtB")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pass_label.setFont(font)
        self.pass_label.setObjectName("pass_label")
        self.u_name_label = QtWidgets.QLabel(Dialog)
        self.u_name_label.setGeometry(QtCore.QRect(420, 310, 121, 41))
        font = QtGui.QFont()
        font.setFamily("PMingLiU-ExtB")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.u_name_label.setFont(font)
        self.u_name_label.setObjectName("u_name_label")
        self.signup_button = QtWidgets.QPushButton(Dialog)
        self.signup_button.setGeometry(QtCore.QRect(590, 550, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.signup_button.setFont(font)
        self.signup_button.setObjectName("signup_button")
        self.uname_line = QtWidgets.QLineEdit(Dialog)
        self.uname_line.setGeometry(QtCore.QRect(570, 300, 311, 51))
        self.uname_line.setStyleSheet("QLineEdit{\n"
"    border:2px solid;\n"
"    border-radius: 20px;\n"
"    color: rgb(108, 112, 125);\n"
"}")
        self.uname_line.setObjectName("uname_line")
        self.email_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.email_lineEdit.setGeometry(QtCore.QRect(570, 380, 311, 51))
        self.email_lineEdit.setStyleSheet("QLineEdit{\n"
"    border:2px solid;\n"
"    border-radius: 20px;\n"
"    color: rgb(108, 112, 125);\n"
"}")
        self.email_lineEdit.setObjectName("email_lineEdit")
        self.pass_label_2 = QtWidgets.QLabel(Dialog)
        self.pass_label_2.setGeometry(QtCore.QRect(420, 450, 111, 61))
        font = QtGui.QFont()
        font.setFamily("PMingLiU-ExtB")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pass_label_2.setFont(font)
        self.pass_label_2.setObjectName("pass_label_2")
        self.password_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.password_lineEdit.setGeometry(QtCore.QRect(570, 460, 311, 51))
        self.password_lineEdit.setStyleSheet("QLineEdit{\n"
"    border:2px solid;\n"
"    border-radius: 20px;\n"
"    color: rgb(108, 112, 125);\n"
"}")
        self.password_lineEdit.setObjectName("password_lineEdit")
        self.signup_button_3 = QtWidgets.QPushButton(Dialog)
        self.signup_button_3.setGeometry(QtCore.QRect(750, 550, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.signup_button_3.setFont(font)
        self.signup_button_3.setObjectName("signup_button_3")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 1311, 861))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/newPrefix/start.jpg"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_3.raise_()
        self.label.raise_()
        self.pass_label.raise_()
        self.u_name_label.raise_()
        self.signup_button.raise_()
        self.uname_line.raise_()
        self.email_lineEdit.raise_()
        self.pass_label_2.raise_()
        self.password_lineEdit.raise_()
        self.signup_button_3.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ffffff;\">Create account</span></p></body></html>"))
        self.pass_label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ffffff;\">Email</span></p></body></html>"))
        self.u_name_label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ffffff;\">Username</span></p></body></html>"))
        self.signup_button.setText(_translate("Dialog", "Signup"))
        self.pass_label_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ffffff;\">Password</span></p></body></html>"))
        self.signup_button_3.setText(_translate("Dialog", "Sign in"))
import image_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
