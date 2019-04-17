from Views.TravelMenu.travelMenu import Ui_MainWindow
from Views.TravelMenu.waitingChild import waitingChild

from Entity.TravelCriteria import TravelCriteria
from Entity.fileInput import fileInput
from PyQt5 import QtWidgets
import time
from google_map import GoogleMaps
from place_info import Place_info
from restaurant_info import Restaurant_info
import json
from Entity.TravelCriteria import set_place_lists


class menuChild(QtWidgets.QMainWindow):

    def __init__(self):
        self.city_num = 0
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
        self.controlls = list()
        self.goo_map = GoogleMaps()
        self.page_number = 0
        self.place_lists = list()
        self.restaurant_lists = list()

    def listener(self, controlls):
        self.controlls = controlls
        self.addStates()
        self.show()
        self.hideBoxes()

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
        # list of places
        ls = self.goo_map.generate_all(citis, [], num_of_day)

        for i in range(len(ls)):
            ls[i]['Day'] = 'Day ' + str(i + 1)

        self.convert_list(ls)
        self.controlls[2].set_value(self.place_lists, 0)


        self.controlls[0].hide()
        self.controlls[1].show()
        self.controlls[1].hide()
        self.controlls[2].setCriteria(citis, num_of_day)
        self.controlls[2].show()
        self.controlls[2].listener()

        # call a function to process google api stuff
        # call to show the gui for the results

    def newLocation(self):
        self.city_num += 1
        self.menuInput.add_city(self.ui.textEdit_2.toPlainText())
        self.menuInput.add_states(str(self.ui.comboBox.currentText()))
        precity = self.ui.textEdit_2.toPlainText()
        prestate = str(self.ui.comboBox.currentText())
        precity += ", "
        precity += prestate
        self.ui.textEdit_2.setPlainText("City")
        if self.city_num > 4:
            pass
        elif self.city_num == 4:
            self.ui.frame_9.show()
            self.ui.textEdit_15.setPlainText(precity)
        elif self.city_num == 3:
            self.ui.frame_5.show()
            self.ui.textEdit_13.setPlainText(precity)
        elif self.city_num == 2:
            self.ui.frame_7.show()
            self.ui.textEdit_11.setPlainText(precity)
        elif self.city_num == 1:
            self.ui.frame_3.show()
            self.ui.textEdit_7.setPlainText(precity)

    def hideBoxes(self):
        self.ui.textEdit_7.setReadOnly(True)
        self.ui.textEdit_11.setReadOnly(True)
        self.ui.textEdit_13.setReadOnly(True)
        self.ui.textEdit_15.setReadOnly(True)
        self.ui.frame_9.hide()
        self.ui.frame_5.hide()
        self.ui.frame_7.hide()
        self.ui.frame_3.hide()

    def addStates(self):
        f = fileInput()
        slist = f.getStates()
        self.ui.comboBox.addItems(slist)


    def convert_list(self, ls):
        for item in ls:
            temp = Place_info()
            day = item['Day']
            place_name = item['formatted_address']
            place_type = item['types']
            rating = item['rating']
            website = item['website']
            phone_number = item['phone number']
            address = item['formatted_address']
            photo_url = item['Photo_url']

            temp.set_everything(day, place_name, place_type, rating, website, phone_number, address, photo_url)
            self.place_lists.append(temp)

        set_place_lists(self.place_lists)

        for place in self.place_lists:
            place.print_all()

