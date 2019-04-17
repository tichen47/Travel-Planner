from Views.TravelMenu.testing import Ui_Dialog
from PyQt5 import QtWidgets
import yelp
from google_map import GoogleMaps
from place_info import Place_info
from Entity.TravelCriteria import get_place_lists

class testingChild(QtWidgets.QDialog):

    def __init__(self):
        super(testingChild, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        # self.ui.scrollArea.setFixedWidth(381)
        # self.ui.textEdit.setDisabled(True)
        self.goo_map = GoogleMaps()
        self.num_of_day = 0
        self.page_number = 0
        self.city = list()
        self.place_lists = list()
        self.restaurant_lists = list()

    def setCriteria(self, city, num_of_day):
        self.city = city
        self.num_of_day = num_of_day


    def start(self):
        self.show()

    def listener(self):
        self.ui.pushButton_3.clicked.connect(self.refineResults)
        self.ui.pushButton.clicked.connect(self.previousPage)
        self.ui.pushButton_2.clicked.connect(self.nextPage)
        self.ui.pushButton_7.clicked.connect(self.act1)
        self.ui.pushButton_8.clicked.connect(self.act2)
        self.ui.pushButton_9.clicked.connect(self.act3)
        self.ui.pushButton_10.clicked.connect(self.act4)

    def act1(self):
        name = self.ui.textBrowser_17.toPlainText()
        # send that to generate restraunts
        self.set_restaurant_by_name(name)

    def act2(self):
        name = self.ui.textBrowser_18.toPlainText()
        # send that to generate restraunts
        self.set_restaurant_by_name(name)

    def act3(self):
        name = self.ui.textBrowser_19.toPlainText()
        # send that to generate restraunts
        self.set_restaurant_by_name(name)

    def act4(self):
        name = self.ui.textBrowser_20.toPlainText()
        # send that to generate restraunts
        self.set_restaurant_by_name(name)

    def previousPage(self):
        if self.page_number > 0:
            self.page_number -= 1
            self.set_value(get_place_lists(), self.page_number)

    def nextPage(self):
        if self.page_number < self.num_of_day // 4:
            self.page_number += 1
            self.set_value(get_place_lists(), self.page_number)



    def refineResults(self):
        activities = self.getActivities()
        rating = self.getRatings()
        print(rating)
        ls = self.goo_map.generate_all(self.city, activities, self.num_of_day, point=rating)
        for i in range(len(ls)):
            ls[i]['Day'] = 'Day ' + str(i + 1)
        self.convert_list(ls)
        self.page_number = 0
        self.set_value(self.place_lists, self.page_number)
        self.show()



    def getActivities(self):
        x = list()

        if self.ui.checkBox_30.isChecked():
            x.append("Nature")
        if self.ui.checkBox_31.isChecked():
            x.append("Religious")
        if self.ui.checkBox_32.isChecked():
            x.append("Theatre")
        if self.ui.checkBox_33.isChecked():
            x.append("Shopping")
        if self.ui.checkBox_34.isChecked():
            x.append("Picnic")
        if self.ui.checkBox_35.isChecked():
            x.append("Sports")

        return x

    def getRatings(self):
        x = -1

        if self.ui.checkBox_36.isChecked():
            x = 4.5
        elif self.ui.checkBox_37.isChecked():
            x = 4.0
        else:
            x = 0.0

        return x




    def set_value(self, ls_of_places, page_number):
        first_index = page_number * 4
        num = len(ls_of_places)
        if first_index < num:
            self.ui.frame_7.show()
            place_1 = ls_of_places[first_index]
            self.ui.textBrowser_17.setText("Name: " + place_1.place_name)
            self.ui.textEdit_65.setText(place_1.day)
            self.ui.textEdit_66.setText(place_1.rating)
            self.ui.textEdit_67.setText(place_1.phone_number)
            self.ui.textEdit_68.setText(place_1.place_type)
            self.ui.textEdit_69.setText(place_1.address)
            self.set_restaurant_by_name(place_1.place_name)

        if (first_index+1) < num:
            self.ui.frame_8.show()
            place_2 = ls_of_places[first_index+1]
            self.ui.textBrowser_18.setText("Name: " + place_2.place_name)
            self.ui.textEdit_70.setText(place_2.day)
            self.ui.textEdit_71.setText(place_2.rating)
            self.ui.textEdit_72.setText(place_2.phone_number)
            self.ui.textEdit_73.setText(place_2.place_type)
            self.ui.textEdit_74.setText(place_2.address)
        else:
            self.ui.frame_8.hide()

        if (first_index+2) < num:
            self.ui.frame_9.show()
            place_3 = ls_of_places[first_index+2]
            self.ui.textBrowser_19.setText("Name: " + place_3.place_name)
            self.ui.textEdit_75.setText(place_3.day)
            self.ui.textEdit_76.setText(place_3.rating)
            self.ui.textEdit_77.setText(place_3.phone_number)
            self.ui.textEdit_78.setText(place_3.place_type)
            self.ui.textEdit_79.setText(place_3.address)
        else:
            self.ui.frame_9.hide()

        if (first_index+3) < num:
            self.ui.frame_10.show()
            place_4 = ls_of_places[first_index+3]
            self.ui.textBrowser_20.setText("Name: " + place_4.place_name)
            self.ui.textEdit_80.setText(place_4.day)
            self.ui.textEdit_81.setText(place_4.rating)
            self.ui.textEdit_82.setText(place_4.phone_number)
            self.ui.textEdit_83.setText(place_4.place_type)
            self.ui.textEdit_84.setText(place_4.address)
        else:
            self.ui.frame_10.hide()


    def set_restaurant_by_name(self, placename):
        rest_list = yelp.return_restaurant(placename)
        res_1 = rest_list[0]
        self.ui.textBrowser.setText(res_1.name)
        self.ui.textEdit_3.setText(res_1.display_phone)
        self.ui.textEdit_4.setText(res_1.rating)
        self.ui.textEdit_5.setText(res_1.price)

        res_2 = rest_list[1]
        self.ui.textBrowser_7.setText(res_2.name)
        self.ui.textEdit_29.setText(res_2.display_phone)
        self.ui.textEdit_27.setText(res_2.rating)
        self.ui.textEdit_28.setText(res_2.price)

        res_3 = rest_list[2]
        self.ui.textBrowser_8.setText(res_3.name)
        self.ui.textEdit_32.setText(res_3.display_phone)
        self.ui.textEdit_30.setText(res_3.rating)
        self.ui.textEdit_31.setText(res_3.price)

        res_4 = rest_list[3]
        self.ui.textBrowser_10.setText(res_4.name)
        self.ui.textEdit_38.setText(res_4.display_phone)
        self.ui.textEdit_36.setText(res_4.rating)
        self.ui.textEdit_37.setText(res_4.price)

        res_5 = rest_list[4]
        self.ui.textBrowser_12.setText(res_5.name)
        self.ui.textEdit_44.setText(res_5.display_phone)
        self.ui.textEdit_42.setText(res_5.rating)
        self.ui.textEdit_43.setText(res_5.price)

    def convert_list(self, ls):
        self.place_lists = list()
        for item in ls:
            print(item)
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

        for place in self.place_lists:
            place.print_all()
