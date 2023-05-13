import sys
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
from PyQt5 import uic, QtWidgets
from signup_ui import Ui_Dialog
import mydatabase
import validations
import signup
import welcome

app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
