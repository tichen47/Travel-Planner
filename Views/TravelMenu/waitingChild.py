from Views.TravelMenu.waiting import Ui_Dialog
from PyQt5 import QtWidgets

class waitingChild(QtWidgets.QMainWindow):

    def __init__(self):
        super(waitingChild, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.textEdit.setDisabled(True)

    def start(self):
        self.show()