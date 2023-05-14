import sys
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
from start_ui import Ui_Dialog
import signup
import login
import user_data
import widget_manager
from widget_manager import widget
import welcome

class StartDialog(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.homeName_2.setText(user_data.name)
        self.ui.homeName_2.setStyleSheet("color: white;border-radius: 20px; border-color:rgb(0, 0, 0); background-image: url(:/newPrefix/start2.jpg); font-size: 28pt; text-align:center;")
        self.welcomeScreen = None
        self.ui.Signout.clicked.connect(self.signOut)

    def signOut(self):
        self.welcomeScreen = welcome.WelcomeDialog()
        widget.addWidget(self.welcomeScreen)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        QMessageBox.information(self, "Sign out", "Sign Out successful!")











# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     dialog = StartDialog()
#     dialog.show()
#     sys.exit(app.exec_())

