import sys
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox, QTableWidgetItem
from start_ui import Ui_Dialog
import user_data
from widget_manager import widget
import welcome
import addToStock
import mydatabase
import datetime


class StartDialog(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        # self.ui.tabWidget.setCurrentIndex(0)
        self.ui.label_5.setText(user_data.name)
        self.ui.label_5.setStyleSheet(
            "color: white;border-radius: 20px; border-color:rgb(0, 0, 0); background-image: url(:/newPrefix/start2.jpg); font-size: 28pt; text-align:center;")
        self.welcomeScreen = None
        self.StockScreen = None
        self.ui.Signout.clicked.connect(self.signOut)
        self.ui.signup_button_8.clicked.connect(self.addToStock)
        self.ui.signup_button_5.clicked.connect(self.print)
        self.ui.signup_button_4.clicked.connect(self.printorder)
        self.load_data()
        self.ui.signup_button_6.clicked.connect(self.search_drug)
        self.ui.signup_button_7.clicked.connect(self.add_drug)


    def add_drug(self):
        customer_name = self.ordersName.text()
        mobile_number = self.ordersMobile.text()
        drug_name = self.startShift_3.text()
        current_date = datetime.date.today()
        current_time = datetime.datetime.now().time()


    def search_drug(self):
        drug_name = self.ui.ordersName_2.text()
        self.load_data(drug_name)

    def load_data(self, drug_name=None):
        self.ui.tableWidget.clearContents()
        self.ui.tableWidget.setRowCount(0)
        query = "SELECT item_name, quantity , expire_date, provider_name FROM stock"
        if drug_name:
            query += f" WHERE item_name LIKE '%{drug_name}%'"
        mydatabase.mycursor.execute(query)
        data = mydatabase.mycursor.fetchall()
        self.ui.tableWidget.setRowCount(len(data))
        for row_num, row_data in enumerate(data):
            self.ui.tableWidget.insertRow(row_num)
            for col_num, value in enumerate(row_data):
                item = QTableWidgetItem(str(value))
                self.ui.tableWidget.setItem(row_num, col_num, item)

    def signOut(self):
        self.welcomeScreen = welcome.WelcomeDialog()
        widget.addWidget(self.welcomeScreen)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        QMessageBox.information(self, "Sign out", "Sign Out successful!")

    def signOut(self):
        self.welcomeScreen = welcome.WelcomeDialog()
        widget.addWidget(self.welcomeScreen)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        QMessageBox.information(self, "Sign out", "Sign Out successful!")

    def addToStock(self):
        self.StockScreen = addToStock.StockDialog()
        widget.addWidget(self.StockScreen)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def print(self):
        QMessageBox.information(self, "print", "Printing.....")

    def printorder(self):
        QMessageBox.information(self, "print", "Printing.....")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = StartDialog()
    dialog.show()
    sys.exit(app.exec_())
