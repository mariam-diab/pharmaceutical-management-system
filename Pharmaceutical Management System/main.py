import sys
import welcome
import widget_manager
from widget_manager import widget

#Starts the application
if __name__ == '__main__':
    app = widget_manager.app
    dialog = welcome.WelcomeDialog()
    widget.addWidget(dialog)
    widget.setWindowTitle("Pharmaceutical Management System")
    widget.setFixedSize(1275, 834)
    widget.show()
    sys.exit(app.exec_())
