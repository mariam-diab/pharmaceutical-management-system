import sys
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
from login_ui import Ui_Dialog
import mydatabase
import signup


class LoginDialog(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.login_btn.clicked.connect(self.login)
        self.signu_btn.clicked.connect(self.open_signup)
        self.signup_dialog = None

    def login(self):
        username = self.username_lineEdit.text()
        password = self.password_lineEdit.text()
        query = "SELECT * FROM users WHERE username=%s AND password=%s"
        values = (username, password)
        mydatabase.mycursor.execute(query, values)
        result = mydatabase.mycursor.fetchone()
        if result:
            QMessageBox.information(self, "Login Success", "Login successful!")
        else:
            QMessageBox.warning(self, "Login Error", "Invalid username or password")
        mydatabase.db.close()
        self.close()

    def open_signup(self):
        self.signup_dialog = signup.SignupDialog()
        self.signup_dialog.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = LoginDialog()
    dialog.show()
    sys.exit(app.exec_())
