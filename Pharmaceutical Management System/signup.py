import sys
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
from signup_ui import Ui_Dialog
import mydatabase
import email_validity

class SignupDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.signup_button.clicked.connect(self.signup)


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
        elif not valid.is_valid_email(email):
            QMessageBox.warning(self, "Signup Error", "Invalid email address")
        else:
            query = "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)"
            values = (username, email, password)
            mydatabase.mycursor.execute(query, values)
            mydatabase.db.commit()
            QMessageBox.information(self, "Signup Success", "User successfully registered")
            self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = SignupDialog()
    dialog.show()
    sys.exit(app.exec_())
