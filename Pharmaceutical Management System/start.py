from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
from start_ui import Ui_Dialog
import user_data
from widget_manager import widget
import welcome
import addToStock


class StartDialog(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        #self.ui.tabWidget.setCurrentIndex(0)
        self.ui.label_5.setText(user_data.name)
        self.ui.label_5.setStyleSheet("color: white;border-radius: 20px; border-color:rgb(0, 0, 0); background-image: url(:/newPrefix/start2.jpg); font-size: 28pt; text-align:center;")
        self.welcomeScreen = None
        self.StockScreen = None
        self.ui.Signout.clicked.connect(self.signOut)
        self.ui.signup_button_8.clicked.connect(self.addToStock)
        self.ui.signup_button_5.clicked.connect(self.print)

    def signOut(self):
        self.welcomeScreen = welcome.WelcomeDialog()
        widget.addWidget(self.welcomeScreen)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        QMessageBox.information(self, "Sign out", "Sign Out successful!")

    def addToStock(self):
        self.StockScreen = addToStock.StockDialog()
        widget.addWidget(self.StockScreen)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def print(self):
        QMessageBox.information(self, "print", "Printing.....")






