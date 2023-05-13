import sys
from PyQt5.QtWidgets import QApplication, QDialog
from start_ui import Ui_Dialog
import signup
import login



class StartDialog(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = StartDialog()
    dialog.show()
    sys.exit(app.exec_())

