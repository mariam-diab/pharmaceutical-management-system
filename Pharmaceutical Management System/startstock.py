from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
from start_ui import Ui_Dialog
import user_data
from widget_manager import widget
import welcome
import addToStock

#Sets up the UI
class StkDialog(Ui_Dialog, QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.tabWidget.setCurrentIndex(2)



