import sys
from PyQt5.QtWidgets import QApplication, QDialog
from welcome_ui import Ui_Dialog
import signup
import login


class WelcomeDialog(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.openlogin)
        self.ui.pushButton_2.clicked.connect(self.opensignup)
        self.signup_dialog = None
        self.login_dialog = None

    def openlogin(self):
        self.login_dialog = login.LoginDialog()
        self.login_dialog.show()
        self.close()

    def opensignup(self):
        self.signup_dialog = signup.SignupDialog()
        self.signup_dialog.show()
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = WelcomeDialog()
    dialog.show()
    sys.exit(app.exec_())
