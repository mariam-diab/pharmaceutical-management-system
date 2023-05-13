# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import sys
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox, QWidget, QVBoxLayout, QPushButton, QSizePolicy
from PyQt5 import uic, QtWidgets
from signup_ui import Ui_Dialog
import mydatabase
import validations
import login
import signup
import welcome
import widget_manager
from widget_manager import widget

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = widget_manager.app
    dialog = welcome.WelcomeDialog()
    #dialog.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
    widget.addWidget(dialog)
    #widget.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
    widget.setFixedSize(1251, 811)
    widget.show()
    sys.exit(app.exec_())
