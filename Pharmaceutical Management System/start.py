import sys
from PyQt5.QtWidgets import QApplication, QDialog
from start_ui import Ui_Dialog
import signup
import login
import user_data



class StartDialog(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.homeName.setText(user_data.name)
        self.ui.homeName.setStyleSheet("color: white;border-radius: 20px; border-color:rgb(0, 0, 0); background-image: url(:/newPrefix/start2.jpg); font-size: 28pt; text-align:center;")








# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     dialog = StartDialog()
#     dialog.show()
#     sys.exit(app.exec_())
#
