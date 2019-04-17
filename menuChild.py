from Views.TravelMenu.travelMenu import Ui_MainWindow
from Entity.TravelCriteria import TravelCriteria
from Entity.fileInput import fileInput
from PyQt5 import QtWidgets

from google_map import GoogleMaps
import json
from place_info import Place_info

class menuChild(QtWidgets.QMainWindow):

    def __init__(self):
        super(menuChild, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.textEdit_6.setDisabled(True)
        self.ui.textEdit_5.setDisabled(True)
        self.ui.textEdit_3.setDisabled(True)
        self.ui.textEdit_4.setDisabled(True)
        self.ui.textEdit.setDisabled(True)
        self.menuInput = TravelCriteria()
        self.cityInputs = list()
        self.stateInputs = list()
        self.goo_map = GoogleMaps()
        self.place_info_list = list()

    def listener(self):

        self.addStates()
        self.show()

        self.cityInputs.append(self.ui.textEdit_2)
        self.stateInputs.append(self.ui.comboBox)

        self.ui.pushButton.clicked.connect(self.newLocation)
        self.ui.pushButton_2.clicked.connect(self.processInput)

    def processInput(self):
        for i in self.cityInputs:
            self.menuInput.add_city(i.toPlainText())

        for i in self.stateInputs:
            self.menuInput.add_states(str(i.currentText()))

        temp = self.ui.dateEdit.date()
        self.menuInput.set_beginDate(temp.toPyDate())

        temp = self.ui.dateEdit_2.date()
        self.menuInput.set_endDate(temp.toPyDate())

        num_of_day = self.menuInput.days_staying().days
        citis = self.menuInput.cities
        ls = self.goo_map.generate_all(citis, [], num_of_day)
        for i in range(len(ls)):
            ls[i]['Day'] = 'Day ' + str(i + 1)

        # print(json.dumps(ls, indent=num_of_day))
        self.add_place_to_list(ls)
        self.output_all_place()

        self.menuInput = TravelCriteria()
        self.place_info_list = list()


    def newLocation(self):
        self.menuInput.add_city(self.ui.textEdit_2.toPlainText())
        self.menuInput.add_states(str(self.ui.comboBox.currentText()))
        self.ui.textEdit_2.setPlainText("City")

    def addStates(self):
        f = fileInput()
        slist = f.getStates()
        self.ui.comboBox.addItems(slist)

    def add_place_to_list(self, ls):
        for item in ls:
            temp_place = Place_info()
            day = item['Day']
            place_name = item['place_name']
            place_type = item['types']
            rating = item['rating']
            website = item['website']
            phone_number = item['phone number']
            address = item['formatted_address']
            photo = item['Photo_url']
            temp_place.set_everything(day, place_name, place_type, rating, website, phone_number, address, photo)
            self.place_info_list.append(temp_place)

    def output_all_place(self):
        for place in self.place_info_list:
            place.print_all()