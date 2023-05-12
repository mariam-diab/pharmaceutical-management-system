# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import sys
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
from signup_ui import Ui_Dialog
import mydatabase
import validations
from signup import SignupDialog
from welcome import WelcomeDialog



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = WelcomeDialog()
    dialog.show()
    sys.exit(app.exec_())
