import sys
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
from login_ui import Ui_Dialog
import mydatabase
import signup
import start

import user_data

from user_data import name

class LoginDialog(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.login_btn.clicked.connect(self.login)
        self.signu_btn.clicked.connect(self.open_signup)
        self.signup_dialog = None
        self.start_dialog = None
        self.username = None

    def open_start(self):
        self.start_dialog = start.StartDialog()
        self.start_dialog.show()
        self.close()


    def login(self):
        username = self.username_lineEdit.text()
        password = self.password_lineEdit.text()
        query = "SELECT * FROM users WHERE username=%s AND password=%s"
        values = (username, password)
        mydatabase.mycursor.execute(query, values)
        result = mydatabase.mycursor.fetchone()
        if result:
            QMessageBox.information(self, "Login Success", "Login successful!")
            user_data.name = username
            self.open_start()

        else:
            QMessageBox.warning(self, "Login Error", "Invalid username or password")
        mydatabase.db.close()

    def open_signup(self):
        self.signup_dialog = signup.SignupDialog()
        self.signup_dialog.show()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = LoginDialog()
    dialog.show()
    sys.exit(app.exec_())
