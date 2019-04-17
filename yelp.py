# encoding: utf-8
'''
@author: Ti Chen
@contact: tichen47@gmail.com
@file: yelp.py.py
@time: 4/6/2019 3:07 PM
'''

from yelpapi import YelpAPI
from pprint import pprint
from restaurant_info import  Restaurant_info

def return_restaurant(location_name):
    api_key = "Ws_y__PwjQDdu8XF1yU66OHl5V4Wkrapy_I-DWvKn4WP_r6JPZwyKiKdPcnn9lUy5ZEiJy9Lqfygl-wVDfSWxy97eHl2ADcruuX1fJ06T8mGh82-O4thXWtZYQapXHYx"
    yelp_api = YelpAPI(api_key)
    # pprint(yelp_api.search_query(term='restaurant', location=location_name, sort_by='rating', limit=5))
    results = yelp_api.search_query(term='restaurant', location=location_name, limit=5)['businesses']
    print('connected')
    all_restaurant = []
    for i in range(5):
        name = ''
        display_phone = ''
        price = ''
        rating = ''
        url = ''
        if 'name' in results[i]:
            name = results[i]['name']
        if 'display_phone' in results[i]:
            display_phone = results[i]['display_phone']
        if 'price' in results[i]:
            price = results[i]['price']
        if 'rating' in results[i]:
            rating = results[i]['rating']
        if 'url' in results[i]:
            url = results[i]['url']

        temp_restaurant = Restaurant_info(name, display_phone, price, rating, url)
        # all_restaurant.append({'name':name, 'display_phone':display_phone,'price':price,'rating':rating,'url':url})
        all_restaurant.append(temp_restaurant)
    return all_restaurant

if __name__ == '__main__':
    # client_id = "ajpUI-_RTJeY5w4oyo4EZQ"
    api_key = "Ws_y__PwjQDdu8XF1yU66OHl5V4Wkrapy_I-DWvKn4WP_r6JPZwyKiKdPcnn9lUy5ZEiJy9Lqfygl-wVDfSWxy97eHl2ADcruuX1fJ06T8mGh82-O4thXWtZYQapXHYx"
    yelp_api = YelpAPI(api_key)
    location_name = 'New York'
    ls = return_restaurant(location_name)
    for item in ls:
        item.print_restaurant()

