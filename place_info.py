# encoding: utf-8
'''
@author: Ti Chen
@contact: tichen47@gmail.com
@file: place_info.py
@time: 4/6/2019 9:40 PM
'''

class Place_info:

    def __init__(self):
        self.day = ""
        self.place_name = ""
        self.place_type = ""
        self.rating = ""
        self.website = ""
        self.phone_number = ""
        self.address = ""
        self.photo = ""

    def set_everything(self, day, place_name, place_type, rating, website, phone_number, address, photo):
        self.day = day
        self.place_name = place_name
        self.place_type = "Type: " + place_type
        self.rating = "Rating: " + str(rating) + "/5.0"
        self.website = website
        self.phone_number = "Phone Number: " + phone_number
        self.address = "Address: " + address
        self.photo = photo

    def print_all(self):
        print()
        print(self.day)
        print(self.place_name)
        print(self.place_type)
        print(self.rating)
        print(self.website)
        print(self.phone_number)
        print(self.address)
        print(self.photo)
        print()
