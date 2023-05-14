import sys
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox, QTableWidgetItem
from start_ui import Ui_Dialog
import user_data
from widget_manager import widget
import welcome
import addToStock
import mydatabase
import datetime


# Sets up the UI, connects button clicks to their respective functions
class StartDialog(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        # self.ui.tabWidget.setCurrentIndex(0)
        self.load_data()
        self.ui.label_5.setText(user_data.name)
        self.ui.label_5.setStyleSheet(
            "color: white;border-radius: 20px; border-color:rgb(0, 0, 0); background-image: url(:/newPrefix/start2.jpg); font-size: 28pt; text-align:center;")
        self.welcomeScreen = None
        self.StockScreen = None
        self.ui.Signout.clicked.connect(self.signOut)
        self.ui.signup_button_8.clicked.connect(self.addToStock)
        self.ui.signup_button_5.clicked.connect(self.print)
        self.ui.ptintOrder.clicked.connect(self.printorder)
        self.ui.signup_button_6.clicked.connect(self.search_drug)
        self.ui.addbtn.clicked.connect(self.add_order)
        self.total = 0
        self.ui.totalOrders.setText(str(self.total))
        self.ui.deletebtn.clicked.connect(self.remove_order)
        self.today_purchases()

    def today_purchases(self):
        current_date = current_date = datetime.date.today()
        self.ui.today.clearContents()
        self.ui.today.setRowCount(0)
        query = "SELECT item_name, quantity, provider FROM purchases WHERE purchase_date = %s"
        values = (current_date,)
        mydatabase.mycursor.execute(query, values)
        data = mydatabase.mycursor.fetchall()
        self.ui.today.setRowCount(len(data))
        for row_num, row_data in enumerate(data):
            self.ui.today.insertRow(row_num)
            for col_num, value in enumerate(row_data):
                item = QTableWidgetItem(str(value))
                self.ui.today.setItem(row_num, col_num, item)

    def load_order(self, customer_name, current_date=None):
        if current_date is None:
            current_date = datetime.date.today()
        self.ui.orderTable.clearContents()
        self.ui.orderTable.setRowCount(0)
        query = "SELECT item_name, quantity FROM purchases WHERE customer_name = %s and purchase_date = %s"
        values = (customer_name, current_date)
        mydatabase.mycursor.execute(query, values)
        data = mydatabase.mycursor.fetchall()
        self.ui.orderTable.setRowCount(len(data))
        for row_num, row_data in enumerate(data):
            self.ui.orderTable.insertRow(row_num)
            for col_num, value in enumerate(row_data):
                item = QTableWidgetItem(str(value))
                self.ui.orderTable.setItem(row_num, col_num, item)

    # Function to record orders in purchases and update stock
    def add_order(self):
        customer_name = self.ui.ordersName.text()
        customer_phone = self.ui.ordersMobile.text()
        drug_name = self.ui.orderName.text()
        quantity = int(self.ui.quantity.text())
        current_date = datetime.date.today()
        current_time = datetime.datetime.now().time()
        check_query = "SELECT quantity FROM stock WHERE item_name = %s"
        mydatabase.mycursor.execute(check_query, (drug_name,))
        stock_data = mydatabase.mycursor.fetchone()
        if not stock_data:
            QMessageBox.critical(self, "Error", f"{drug_name} is not available in stock.")
        elif stock_data[0] < quantity:
            QMessageBox.critical(self, "Error",
                                 f"No enough quantity in stock for {drug_name}. Available stock: {stock_data[0]}.")
        else:
            price_query = "SELECT price FROM stock WHERE item_name = %s"
            mydatabase.mycursor.execute(price_query, (drug_name,))
            price_data = mydatabase.mycursor.fetchone()
            price = price_data[0] * quantity
            self.total += price
            self.ui.totalOrders.setText(str(self.total))
            query = "INSERT INTO purchases (item_name, quantity, purchase_date, purchase_time, customer_name, customer_phone, price) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            values = (drug_name, quantity, current_date, current_time, customer_name, customer_phone, price)
            mydatabase.mycursor.execute(query, values)
            update_query = "UPDATE stock SET quantity = quantity - %s WHERE item_name = %s"
            mydatabase.mycursor.execute(update_query, (quantity, drug_name))
            mydatabase.db.commit()
            self.load_data()
            self.load_order(customer_name, current_date)
            QMessageBox.information(self, "Success", "Drug added successfully.")

    # Function to record orders in purchases and update stock
    def remove_order(self):
        customer_name = self.ui.ordersName.text()
        drug_name = self.ui.orderName.text()
        quantity = int(self.ui.quantity.text())
        check_query = "SELECT quantity FROM purchases where customer_name = %s AND item_name = %s"
        mydatabase.mycursor.execute(check_query, (customer_name, drug_name))
        check_data = mydatabase.mycursor.fetchone()
        if not check_data:
            QMessageBox.critical(self, "Error", f"{drug_name} was not added to the order")
        elif check_data[0] < quantity:
            QMessageBox.critical(self, "Error", f"You only added {check_data[0]} to the order")
        else:
            price_query = "SELECT price FROM stock WHERE item_name = %s"
            mydatabase.mycursor.execute(price_query, (drug_name,))
            price_data = mydatabase.mycursor.fetchone()
            remaining_quantity = check_data[0] - quantity
            new_price = self.total - quantity * price_data[0]
            update_query = "UPDATE purchases SET quantity = %s, price = %s WHERE customer_name = %s AND item_name = %s"
            mydatabase.mycursor.execute(update_query, (remaining_quantity, new_price, customer_name, drug_name))
            mydatabase.db.commit()
            stock_query = "UPDATE stock SET quantity = quantity + %s WHERE item_name = %s"
            mydatabase.mycursor.execute(stock_query, (quantity, drug_name))
            self.total -= price_data[0] - new_price
            self.ui.totalOrders.setText(str(self.total))
            mydatabase.db.commit()
            self.load_data()
            self.load_order(customer_name)
            QMessageBox.information(self, "Success", f"{quantity} {drug_name} was removed from the order.")

    # Search for the drugs using user input
    def search_drug(self):
        drug_name = self.ui.ordersName_2.text()
        self.load_data(drug_name)

    # Retrieves the data from database
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

    # Opens sign out widget
    def signOut(self):
        self.welcomeScreen = welcome.WelcomeDialog()
        widget.addWidget(self.welcomeScreen)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        QMessageBox.information(self, "Sign out", "Sign Out successful!")

    # Opens add to stock widget
    def addToStock(self):
        self.StockScreen = addToStock.StockDialog()
        widget.addWidget(self.StockScreen)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    # Print report for stock
    def print(self):
        QMessageBox.information(self, "print", "Printing.....")

    # Print receipt
    def printorder(self):
        QMessageBox.information(self, "print", "Printing.....")
        self.total = 0
        self.ui.totalOrders.setText(str(self.total))
        self.ui.orderTable.clearContents()
        self.ui.orderTable.setRowCount(0)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = StartDialog()
    dialog.show()
    sys.exit(app.exec_())
