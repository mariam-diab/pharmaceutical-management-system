from PyQt5.QtWidgets import QApplication, QDialog,QMainWindow
from welcome_ui import Ui_Dialog
import signup
import login
from widget_manager import widget


#Sets up the UI, connects button clicks to their respective functions
class WelcomeDialog(QDialog, Ui_Dialog, QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Pharmaceutical application")
        self.ui.pushButton.clicked.connect(self.openlogin)
        self.ui.pushButton_2.clicked.connect(self.opensignup)
        self.signup_dialog = None
        self.login_dialog = None

    #Opens the login widget
    def openlogin(self):
        self.login_dialog = login.LoginDialog()
        widget.addWidget(self.login_dialog)
        widget.setCurrentIndex(widget.currentIndex()+1)

    #Opens the signup widget
    def opensignup(self):
        self.signup_dialog = signup.SignupDialog()
        widget.addWidget(self.signup_dialog)
        widget.setCurrentIndex(widget.currentIndex() + 1)


