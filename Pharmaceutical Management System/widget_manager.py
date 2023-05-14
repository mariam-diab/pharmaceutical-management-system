import sys
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox, QMainWindow
from PyQt5 import uic, QtWidgets

#set up the basic infrastructure for creating a PyQt5-based graphical user interface (GUI) application.
app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
