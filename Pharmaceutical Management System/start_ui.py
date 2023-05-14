# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'start.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1275, 834)
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(-10, 0, 1290, 861))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("tabWidget{\n"
"font-color: rgb(255, 28, 244);\n"
"}")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.Welcome = QtWidgets.QLabel(self.tab)
        self.Welcome.setGeometry(QtCore.QRect(389, 10, 261, 81))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(48)
        self.Welcome.setFont(font)
        self.Welcome.setAlignment(QtCore.Qt.AlignCenter)
        self.Welcome.setObjectName("Welcome")
        self.Welcome_3 = QtWidgets.QLabel(self.tab)
        self.Welcome_3.setGeometry(QtCore.QRect(30, 670, 141, 61))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(48)
        self.Welcome_3.setFont(font)
        self.Welcome_3.setAlignment(QtCore.Qt.AlignCenter)
        self.Welcome_3.setObjectName("Welcome_3")
        self.Welcome_7 = QtWidgets.QLabel(self.tab)
        self.Welcome_7.setGeometry(QtCore.QRect(40, 110, 391, 81))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.Welcome_7.setFont(font)
        self.Welcome_7.setAlignment(QtCore.Qt.AlignCenter)
        self.Welcome_7.setObjectName("Welcome_7")
        self.Signout = QtWidgets.QPushButton(self.tab)
        self.Signout.setGeometry(QtCore.QRect(1100, 660, 151, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.Signout.setFont(font)
        self.Signout.setObjectName("Signout")
        self.today = QtWidgets.QTableWidget(self.tab)
        self.today.setGeometry(QtCore.QRect(40, 190, 601, 451))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.today.sizePolicy().hasHeightForWidth())
        self.today.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        self.today.setFont(font)
        self.today.setFocusPolicy(QtCore.Qt.NoFocus)
        self.today.setStyleSheet("QTableWidget {\n"
"    border: 1px solid black;\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #f0f0f0;\n"
"    border: 1px solid rgb(15, 12, 107);\n"
"    font-weight: bold;\n"
"    font-size: 18px;\n"
"    color: black;\n"
"}\n"
"")
        self.today.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.today.setObjectName("today")
        self.today.setColumnCount(3)
        self.today.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.today.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.today.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.today.setHorizontalHeaderItem(2, item)
        self.today.horizontalHeader().setDefaultSectionSize(200)
        self.today.horizontalHeader().setHighlightSections(True)
        self.today.verticalHeader().setDefaultSectionSize(50)
        self.today.verticalHeader().setMinimumSectionSize(50)
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(639, 10, 211, 71))
        self.label_5.setStyleSheet("QLabel{\n"
"    border-radius: 20px;\n"
"    color:rgb(255, 255, 255);\n"
"    background-image: url(:/newPrefix/start2.jpg);font-size: 24pt; text-align: center;}")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.missing = QtWidgets.QTableWidget(self.tab)
        self.missing.setGeometry(QtCore.QRect(660, 190, 601, 451))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setKerning(True)
        self.missing.setFont(font)
        self.missing.setFocusPolicy(QtCore.Qt.NoFocus)
        self.missing.setStyleSheet("QTableWidget {\n"
"    border: 1px solid black;\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color:rgb(255, 255, 255);\n"
"    border: 1px solid rgb(15, 12, 107);\n"
"    font-weight: bold;\n"
"    font-size: 18px;\n"
"    color: rgb(170, 0, 0);\n"
"}\n"
"")
        self.missing.setObjectName("missing")
        self.missing.setColumnCount(3)
        self.missing.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.missing.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.missing.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.missing.setHorizontalHeaderItem(2, item)
        self.missing.horizontalHeader().setDefaultSectionSize(200)
        self.missing.verticalHeader().setDefaultSectionSize(50)
        self.missing.verticalHeader().setMinimumSectionSize(50)
        self.Welcome_11 = QtWidgets.QLabel(self.tab)
        self.Welcome_11.setGeometry(QtCore.QRect(570, 110, 391, 81))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.Welcome_11.setFont(font)
        self.Welcome_11.setAlignment(QtCore.Qt.AlignCenter)
        self.Welcome_11.setObjectName("Welcome_11")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(-40, -50, 1321, 851))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap(":/newPrefix/start.jpg"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.totalHome = QtWidgets.QLabel(self.tab)
        self.totalHome.setGeometry(QtCore.QRect(170, 670, 211, 71))
        self.totalHome.setStyleSheet("QLabel{\n"
"    border-radius: 20px;\n"
"    color:rgb(255, 255, 255);\n"
"    background-image: url(:/newPrefix/start2.jpg);font-size: 24pt; text-align: center;}")
        self.totalHome.setText("")
        self.totalHome.setObjectName("totalHome")
        self.label_6.raise_()
        self.Welcome.raise_()
        self.Welcome_3.raise_()
        self.Welcome_7.raise_()
        self.Signout.raise_()
        self.today.raise_()
        self.label_5.raise_()
        self.missing.raise_()
        self.Welcome_11.raise_()
        self.totalHome.raise_()
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.ordersMobile = QtWidgets.QLineEdit(self.tab_2)
        self.ordersMobile.setGeometry(QtCore.QRect(340, 200, 301, 51))
        self.ordersMobile.setStyleSheet("\n"
"QLineEdit{\n"
"    border-radius: 20px;\n"
"    font: 700 12pt \"Calibri\";\n"
"    border-color:rgb(0, 0, 0);\n"
"    text-align: center;\n"
"}")
        self.ordersMobile.setObjectName("ordersMobile")
        self.Welcome_5 = QtWidgets.QLabel(self.tab_2)
        self.Welcome_5.setGeometry(QtCore.QRect(-20, 80, 301, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(48)
        self.Welcome_5.setFont(font)
        self.Welcome_5.setAlignment(QtCore.Qt.AlignCenter)
        self.Welcome_5.setObjectName("Welcome_5")
        self.Welcome_6 = QtWidgets.QLabel(self.tab_2)
        self.Welcome_6.setGeometry(QtCore.QRect(-10, 200, 281, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(48)
        self.Welcome_6.setFont(font)
        self.Welcome_6.setAlignment(QtCore.Qt.AlignCenter)
        self.Welcome_6.setObjectName("Welcome_6")
        self.Welcome_8 = QtWidgets.QLabel(self.tab_2)
        self.Welcome_8.setGeometry(QtCore.QRect(30, 300, 221, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(48)
        self.Welcome_8.setFont(font)
        self.Welcome_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Welcome_8.setObjectName("Welcome_8")
        self.orderName = QtWidgets.QLineEdit(self.tab_2)
        self.orderName.setGeometry(QtCore.QRect(340, 310, 301, 51))
        self.orderName.setStyleSheet("\n"
"QLineEdit{\n"
"    border-radius: 20px;\n"
"    font: 700 12pt \"Calibri\";\n"
"    border-color:rgb(0, 0, 0);\n"
"    text-align: center;\n"
"}")
        self.orderName.setObjectName("orderName")
        self.deletebtn = QtWidgets.QPushButton(self.tab_2)
        self.deletebtn.setGeometry(QtCore.QRect(390, 630, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(True)
        self.deletebtn.setFont(font)
        self.deletebtn.setObjectName("deletebtn")
        self.Welcome_9 = QtWidgets.QLabel(self.tab_2)
        self.Welcome_9.setGeometry(QtCore.QRect(750, 710, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(48)
        self.Welcome_9.setFont(font)
        self.Welcome_9.setAlignment(QtCore.Qt.AlignCenter)
        self.Welcome_9.setObjectName("Welcome_9")
        self.ptintOrder = QtWidgets.QPushButton(self.tab_2)
        self.ptintOrder.setGeometry(QtCore.QRect(1070, 710, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(True)
        self.ptintOrder.setFont(font)
        self.ptintOrder.setObjectName("ptintOrder")
        self.ordersName = QtWidgets.QLineEdit(self.tab_2)
        self.ordersName.setGeometry(QtCore.QRect(340, 90, 301, 51))
        self.ordersName.setStyleSheet("\n"
"QLineEdit{\n"
"    border-radius: 20px;\n"
"    font: 700 12pt \"Calibri\";\n"
"    border-color:rgb(0, 0, 0);\n"
"    text-align: center;\n"
"}")
        self.ordersName.setText("")
        self.ordersName.setObjectName("ordersName")
        self.addbtn = QtWidgets.QPushButton(self.tab_2)
        self.addbtn.setGeometry(QtCore.QRect(200, 630, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(True)
        self.addbtn.setFont(font)
        self.addbtn.setObjectName("addbtn")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(-40, -30, 1321, 851))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/newPrefix/start.jpg"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.orderTable = QtWidgets.QTableWidget(self.tab_2)
        self.orderTable.setGeometry(QtCore.QRect(750, 80, 501, 601))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        self.orderTable.setFont(font)
        self.orderTable.setStyleSheet("QTableWidget {\n"
"    border: 1px solid black;\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #f0f0f0;\n"
"    border: 1px solid rgb(15, 12, 107);\n"
"    font-weight: bold;\n"
"    font-size: 18px;\n"
"    color: black;\n"
"}\n"
"")
        self.orderTable.setObjectName("orderTable")
        self.orderTable.setColumnCount(2)
        self.orderTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.orderTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.orderTable.setHorizontalHeaderItem(1, item)
        self.orderTable.horizontalHeader().setDefaultSectionSize(250)
        self.orderTable.verticalHeader().setDefaultSectionSize(50)
        self.orderTable.verticalHeader().setMinimumSectionSize(50)
        self.totalOrders = QtWidgets.QLabel(self.tab_2)
        self.totalOrders.setGeometry(QtCore.QRect(910, 710, 121, 51))
        self.totalOrders.setStyleSheet("QLabel{\n"
"    border-radius: 20px;\n"
"    color:rgb(255, 255, 255);\n"
"    background-image: url(:/newPrefix/start2.jpg);font-size: 24pt; text-align: center;}")
        self.totalOrders.setText("")
        self.totalOrders.setObjectName("totalOrders")
        self.Welcome_12 = QtWidgets.QLabel(self.tab_2)
        self.Welcome_12.setGeometry(QtCore.QRect(30, 420, 221, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(48)
        self.Welcome_12.setFont(font)
        self.Welcome_12.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Welcome_12.setObjectName("Welcome_12")
        self.quantity = QtWidgets.QLineEdit(self.tab_2)
        self.quantity.setGeometry(QtCore.QRect(340, 430, 301, 51))
        self.quantity.setStyleSheet("\n"
"QLineEdit{\n"
"    border-radius: 20px;\n"
"    font: 700 12pt \"Calibri\";\n"
"    border-color:rgb(0, 0, 0);\n"
"    text-align: center;\n"
"}")
        self.quantity.setObjectName("quantity")
        self.itemPrice = QtWidgets.QLineEdit(self.tab_2)
        self.itemPrice.setGeometry(QtCore.QRect(340, 540, 301, 51))
        self.itemPrice.setStyleSheet("\n"
"QLineEdit{\n"
"    border-radius: 20px;\n"
"    font: 700 12pt \"Calibri\";\n"
"    border-color:rgb(0, 0, 0);\n"
"    text-align: center;\n"
"}")
        self.itemPrice.setObjectName("itemPrice")
        self.Welcome_13 = QtWidgets.QLabel(self.tab_2)
        self.Welcome_13.setGeometry(QtCore.QRect(40, 530, 221, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(48)
        self.Welcome_13.setFont(font)
        self.Welcome_13.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Welcome_13.setObjectName("Welcome_13")
        self.label_3.raise_()
        self.ordersMobile.raise_()
        self.Welcome_5.raise_()
        self.Welcome_6.raise_()
        self.Welcome_8.raise_()
        self.orderName.raise_()
        self.deletebtn.raise_()
        self.Welcome_9.raise_()
        self.ptintOrder.raise_()
        self.ordersName.raise_()
        self.addbtn.raise_()
        self.orderTable.raise_()
        self.totalOrders.raise_()
        self.Welcome_12.raise_()
        self.quantity.raise_()
        self.itemPrice.raise_()
        self.Welcome_13.raise_()
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_4 = QtWidgets.QLabel(self.tab_3)
        self.label_4.setGeometry(QtCore.QRect(-40, -20, 1321, 821))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/newPrefix/start.jpg"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.Welcome_10 = QtWidgets.QLabel(self.tab_3)
        self.Welcome_10.setGeometry(QtCore.QRect(20, 50, 301, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(48)
        self.Welcome_10.setFont(font)
        self.Welcome_10.setAlignment(QtCore.Qt.AlignCenter)
        self.Welcome_10.setObjectName("Welcome_10")
        self.signup_button_5 = QtWidgets.QPushButton(self.tab_3)
        self.signup_button_5.setGeometry(QtCore.QRect(1080, 580, 171, 61))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(True)
        self.signup_button_5.setFont(font)
        self.signup_button_5.setObjectName("signup_button_5")
        self.ordersName_2 = QtWidgets.QLineEdit(self.tab_3)
        self.ordersName_2.setGeometry(QtCore.QRect(320, 60, 341, 51))
        self.ordersName_2.setStyleSheet("\n"
"QLineEdit{\n"
"    border-radius: 20px;\n"
"    font: 700 12pt \"Calibri\";\n"
"    border-color:rgb(0, 0, 0);\n"
"    text-align: center;\n"
"}")
        self.ordersName_2.setText("")
        self.ordersName_2.setObjectName("ordersName_2")
        self.signup_button_6 = QtWidgets.QPushButton(self.tab_3)
        self.signup_button_6.setGeometry(QtCore.QRect(580, 140, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(True)
        self.signup_button_6.setFont(font)
        self.signup_button_6.setObjectName("signup_button_6")
        self.tableWidget = QtWidgets.QTableWidget(self.tab_3)
        self.tableWidget.setGeometry(QtCore.QRect(50, 230, 1001, 501))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("QTableWidget {\n"
"    border: 1px solid black;\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #f0f0f0;\n"
"    border: 1px solid rgb(15, 12, 107);\n"
"    font-weight: bold;\n"
"    font-size: 18px;\n"
"    color: black;\n"
"}\n"
"")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(250)
        self.tableWidget.verticalHeader().setDefaultSectionSize(50)
        self.tableWidget.verticalHeader().setMinimumSectionSize(50)
        self.signup_button_8 = QtWidgets.QPushButton(self.tab_3)
        self.signup_button_8.setGeometry(QtCore.QRect(1080, 666, 171, 61))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(True)
        self.signup_button_8.setFont(font)
        self.signup_button_8.setObjectName("signup_button_8")
        self.tabWidget.addTab(self.tab_3, "")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 1301, 811))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/newPrefix/start.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.homeName_2 = QtWidgets.QLabel(Dialog)
        self.homeName_2.setGeometry(QtCore.QRect(0, 0, 1451, 811))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.homeName_2.sizePolicy().hasHeightForWidth())
        self.homeName_2.setSizePolicy(sizePolicy)
        self.homeName_2.setText("")
        self.homeName_2.setPixmap(QtGui.QPixmap(":/newPrefix/start.jpg"))
        self.homeName_2.setScaledContents(True)
        self.homeName_2.setObjectName("homeName_2")
        self.homeName_2.raise_()
        self.label_2.raise_()
        self.tabWidget.raise_()

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.Welcome.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:28pt; font-weight:600; color:#ffffff;\">Welcome</span></p></body></html>"))
        self.Welcome_3.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:28pt; font-weight:600; color:#ffffff;\">Total</span></p></body></html>"))
        self.Welcome_7.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:28pt; font-weight:600; color:#ffffff;\">Today\'s Purchases</span></p></body></html>"))
        self.Signout.setText(_translate("Dialog", "Sign out"))
        item = self.today.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Drug name"))
        item = self.today.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Quantitiy "))
        item = self.today.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Price"))
        item = self.missing.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Drug name"))
        item = self.missing.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "provider"))
        item = self.missing.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Quantitiy "))
        self.Welcome_11.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:28pt; font-weight:600; color:#aa0000;\">Low Stock</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Home"))
        self.Welcome_5.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:22pt; color:#ffffff;\">Customer name</span></p></body></html>"))
        self.Welcome_6.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:22pt; color:#ffffff;\">Mobile number</span></p></body></html>"))
        self.Welcome_8.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:24pt; color:#ffffff;\">Item name</span></p></body></html>"))
        self.deletebtn.setText(_translate("Dialog", "Delete"))
        self.Welcome_9.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:24pt; color:#ffffff;\">Total</span></p></body></html>"))
        self.ptintOrder.setText(_translate("Dialog", "Print order"))
        self.addbtn.setText(_translate("Dialog", "Add"))
        item = self.orderTable.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Drug name"))
        item = self.orderTable.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Quantitiy "))
        self.Welcome_12.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:24pt; color:#ffffff;\">Order quantity</span></p></body></html>"))
        self.Welcome_13.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:24pt; color:#ffffff;\">Item price</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Orders"))
        self.Welcome_10.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:24pt; color:#ffffff;\">Drugs available</span></p></body></html>"))
        self.signup_button_5.setText(_translate("Dialog", "Print report"))
        self.signup_button_6.setText(_translate("Dialog", "search"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Drug name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Quantity"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Expiry date"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Provider"))
        self.signup_button_8.setText(_translate("Dialog", "Add to stock"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Dialog", "Stock"))
import image_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
