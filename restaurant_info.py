# encoding: utf-8
'''
@author: Ti Chen
@contact: tichen47@gmail.com
@file: restaurant_info.py
@time: 4/6/2019 10:23 PM
'''

class Restaurant_info:

    def __init__(self, name, display_phone, price, rating, url):
        self.name = name
        self.display_phone = "Tel: " + display_phone
        self.price = price
        self.rating = str(rating) + "/5.0"
        self.url = url



    def print_restaurant(self):
        print()
        print(self.name)
        print(self.display_phone)
        print(self.price)
        print(self.rating)
        print(self.url)

