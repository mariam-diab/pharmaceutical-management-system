import sys
from PyQt5.QtWidgets import QApplication, QDialog, QTableWidgetItem, QMessageBox
from addtostock_ui import Ui_Dialog
import mydatabase
from widget_manager import widget

#Sets up the UI, connects button clicks to their respective functions
class StockDialog(Ui_Dialog, QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.start_dialog = None
        self.startstk_dialog= None
        self.ui.back.clicked.connect(self.Back)
        self.ui.signup_button_8.clicked.connect(self.add_drug)
        self.ui.signup_button_9.clicked.connect(self.remove_drug)
        # self.load_data()


    def refresh_data(self):
        self.load_data()

    #Retrieves data from the "stock" table in the database
    def load_data(self):
        self.ui.tableWidget.clearContents()
        self.ui.tableWidget.setRowCount(0)
        query = "SELECT item_name, provider_name, quantity, expire_date FROM stock"
        mydatabase.mycursor.execute(query)
        data = mydatabase.mycursor.fetchall()
        self.ui.tableWidget.setRowCount(len(data))
        for row_num, row_data in enumerate(data):
            self.ui.tableWidget.insertRow(row_num)
            for col_num, value in enumerate(row_data):
                item = QTableWidgetItem(str(value))
                self.ui.tableWidget.setItem(row_num, col_num, item)

    #retrieves drug-related information from the corresponding input fields in the UI and inserts a new record into the "stock" table in the database.
    def add_drug(self):
        drug_name = self.ui.ordersName_2.text()
        provider = self.ui.ordersName_5.text()
        expiry_date = self.ui.ordersName_4.text()
        quantity = self.ui.ordersName_3.text()
        try:
            query = "INSERT INTO stock (item_name, provider_name, expire_date, quantity) VALUES (%s, %s, %s, %s)"
            values = (drug_name, provider, expiry_date, quantity)
            mydatabase.mycursor.execute(query, values)
            mydatabase.db.commit()
            self.load_data()
            QMessageBox.information(self, "Added Drug", f"{drug_name} added to stock successfully!")
        except Exception as e:
            QMessageBox.information(self, "Error", f"An error '{e}' occurred while adding {drug_name} to the stock")


    #removes a drug from the "stock" table in the database based on the provided drug name.
    def remove_drug(self):
        drug_name = self.ui.ordersName_2.text()
        try:
            query = "SELECT * FROM stock WHERE item_name = %s"
            values = (drug_name,)
            mydatabase.mycursor.execute(query, values)
            drug = mydatabase.mycursor.fetchone()
            if not drug:
                QMessageBox.information(self, "Error", f"{drug_name} does not exist in the stock!")
                return
            query = "DELETE FROM stock WHERE item_name = %s"
            values = (drug_name,)
            mydatabase.mycursor.execute(query, values)
            mydatabase.db.commit()
            self.load_data()
            QMessageBox.information(self, "Removed Drug", f"{drug_name} removed from stock successfully!")
        except Exception as e:
            QMessageBox.information(self, "Error", f"An error '{e}' occurred while removing {drug_name} from the stock")
    #Return to the previous widget
    def Back(self):
        last_widget = widget.widget(widget.count() - 1)
        widget.removeWidget(last_widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = StockDialog()
    dialog.show()
    sys.exit(app.exec_())
