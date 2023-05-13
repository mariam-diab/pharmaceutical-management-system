import sys
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
from PyQt5 import uic, QtWidgets
from addtostock_ui import Ui_Dialog
import mydatabase
import signup
import start
from main import widget
import user_data
from user_data import name
import startstock


class StockDialog(Ui_Dialog, QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.start_dialog = None
        self.startstk_dialog= None
        self.ui.back.clicked.connect(self.Back)

    def Back(self):
        last_widget = widget.widget(widget.count() - 1)
        widget.removeWidget(last_widget)









