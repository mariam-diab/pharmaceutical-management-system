# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'welcome.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1278, 836)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.Welcome = QtWidgets.QLabel(Dialog)
        self.Welcome.setGeometry(QtCore.QRect(430, 160, 481, 141))
        font = QtGui.QFont()
        font.setFamily("PMingLiU-ExtB")
        font.setPointSize(48)
        self.Welcome.setFont(font)
        self.Welcome.setObjectName("Welcome")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(580, 360, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
"    border:2px solidrgb(99, 99, 99)\n"
"    border -radius: 20px    \n"
"\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(580, 490, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"    border:2px solidrgb(99, 99, 99)\n"
"    border -radius: 20px    \n"
"\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.Welcome_2 = QtWidgets.QLabel(Dialog)
        self.Welcome_2.setGeometry(QtCore.QRect(530, 440, 101, 51))
        font = QtGui.QFont()
        font.setFamily("PMingLiU-ExtB")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.Welcome_2.setFont(font)
        self.Welcome_2.setObjectName("Welcome_2")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 1291, 851))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/newPrefix/start.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_2.raise_()
        self.Welcome.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.Welcome_2.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.Welcome.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:72pt; color:#ffffff;\">Welcome</span></p></body></html>"))
        self.pushButton.setText(_translate("Dialog", "Sign in"))
        self.pushButton_2.setText(_translate("Dialog", "Sign up"))
        self.Welcome_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt; color:#ffffff;\">New user?</span></p></body></html>"))
import image_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
