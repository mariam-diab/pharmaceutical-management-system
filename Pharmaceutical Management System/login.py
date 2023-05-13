import sys
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
from PyQt5 import uic, QtWidgets
from login_ui import Ui_Dialog
import mydatabase
import signup
import start
from main import widget

class LoginDialog(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.login_btn.clicked.connect(self.login)
        self.signu_btn.clicked.connect(self.open_signup)
        self.signup_dialog = None
        self.start_dialog = None

    def open_start(self):
        self.start_dialog = start.StartDialog()
        widget.addWidget(self.start_dialog)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def login(self):
        username = self.username_lineEdit.text()
        password = self.password_lineEdit.text()
        query = "SELECT * FROM users WHERE username=%s AND password=%s"
        values = (username, password)
        mydatabase.mycursor.execute(query, values)
        result = mydatabase.mycursor.fetchone()
        if result:
            QMessageBox.information(self, "Login Success", "Login successful!")
            self.open_start()
        else:
            QMessageBox.warning(self, "Login Error", "Invalid username or password")
        mydatabase.db.close()
        self.close()

    def open_signup(self):
        self.signup_dialog = signup.SignupDialog()
        widget.addWidget(self.signup_dialog)
        widget.setCurrentIndex(widget.currentIndex()+1)

#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     widget = QtWidgets.QStackedWidget()
#     dialog = LoginDialog()
#     dialog2 = signup.SignupDialog()
#     widget.addWidget(dialog)
#     widget.addWidget(dialog2)
#     widget.setFixedSize(700, 500)
#     widget.show()
#     #dialog.show()
#     sys.exit(app.exec_())
