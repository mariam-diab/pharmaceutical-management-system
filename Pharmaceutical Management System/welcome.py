import sys
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5 import uic, QtWidgets
from welcome_ui import Ui_Dialog
import signup
import login
import main
import widget_manager
from widget_manager import widget



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
        widget.addWidget(self.login_dialog)
        widget.setCurrentIndex(widget.currentIndex()+1)


    def opensignup(self):
        self.signup_dialog = signup.SignupDialog()
        widget.addWidget(self.signup_dialog)
        widget.setCurrentIndex(widget.currentIndex() + 1)


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     widget = QtWidgets.QStackedWidget()
#     dialog = WelcomeDialog()
#     #dialog.show()
#     widget.addWidget(dialog)
#     widget.setFixedSize(700, 500)
#     widget.show()
#     sys.exit(app.exec_())
