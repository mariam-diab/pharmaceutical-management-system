import sys
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
from signup_ui import Ui_Dialog
import login
import mydatabase
import validations
from main import widget

#Sets up the UI, connects button clicks to their respective functions
class SignupDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.signup_button.clicked.connect(self.signup)
        self.ui.uname_line.textChanged.connect(self.check_username)
        self.ui.signup_button_3.clicked.connect(self.open_login)
        self.ui.password_lineEdit.textChanged.connect(self.check_password)
        self.login_dialog = None

    #Checks if username is alphanumeric and set the buttons and value of username
    def check_username(self):
        username = self.ui.uname_line.text()
        if not username.isalnum():
            self.ui.uname_line.setStyleSheet("background-color: #FFB6C1")
            self.ui.signup_button.setEnabled(False)
        else:
            self.ui.uname_line.setStyleSheet("")
            self.ui.signup_button.setEnabled(True)
    #Checks if password is alphanumeric and set the buttons  and value of password
    def check_password(self):
        password = self.ui.password_lineEdit.text()
        if not validations.is_valid_password(password):
            self.ui.password_lineEdit.setStyleSheet("background-color: #FFB6C1")
            self.ui.signup_button.setEnabled(False)

        else:
            self.ui.password_lineEdit.setStyleSheet("")
            self.ui.signup_button.setEnabled(True)
    #Handles signup conditions to add to database
    def signup(self):
        username = self.ui.uname_line.text()
        email = self.ui.email_lineEdit.text()
        password = self.ui.password_lineEdit.text()
        query = "SELECT * FROM users WHERE username=%s OR email=%s"
        values = (username, email)
        mydatabase.mycursor.execute(query, values)
        result = mydatabase.mycursor.fetchone()
        if result:
            QMessageBox.warning(self, "Signup Error", "Username or email already exists")
        elif not validations.is_valid_email(email):
            QMessageBox.warning(self, "Signup Error", "Invalid email address")
        else:
            query = "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)"
            values = (username, email, password)
            mydatabase.mycursor.execute(query, values)
            mydatabase.db.commit()
            QMessageBox.information(self, "Signup Success", "User successfully registered")
            self.close()
    #opens login widget
    def open_login(self):
        self.login_dialog = login.LoginDialog()
        widget.addWidget(self.login_dialog)
        widget.setCurrentIndex(widget.currentIndex()+1)


