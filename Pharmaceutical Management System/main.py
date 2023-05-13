# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import sys
import welcome
import widget_manager
from widget_manager import widget

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = widget_manager.app
    dialog = welcome.WelcomeDialog()
    widget.addWidget(dialog)
    widget.setWindowTitle("Pharmaceutical Management System")
    widget.setFixedSize(1275, 834)
    widget.show()
    sys.exit(app.exec_())
