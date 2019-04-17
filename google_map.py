# encoding: utf-8
'''
@author: Ti Chen
@contact: tichen47@gmail.com
@file: web_crawler.py
@time: 4/5/2019 9:37 PM
'''

from googleplaces import GooglePlaces
import googlemaps
import json
from itertools import filterfalse

class GoogleMaps(object):
    """提供google maps服务"""

    def __init__(self):

        self._GOOGLE_MAPS_KEY = "#################" # Key here
        self._Google_Places = GooglePlaces(self._GOOGLE_MAPS_KEY)
        self._Google_Geocod = googlemaps.Client(key=self._GOOGLE_MAPS_KEY)

    def _text_search(self, query, language=None, location=None):
        """
        根据搜索字符串,请求google API传回推荐的列表
        :param query: 搜索字符串
        :param language: 语言
        :param location: 地区筛选
        :return:
        """
        # lat_lng = {"lat": "22.5745761", "lng": "113.9393772"}
        # 经纬度附近搜索
        # text_query_result = self.self._Google_Places.text_search(query='Gong Yuan', lat_lng=lat_lng)
        # location 为人可认识的名称
        # text_query_result = self.self._Google_Places.text_search(query='Tang Lang Shan', location='shenzhen')
        # 指定语言搜索
        text_query_result = self._Google_Places.text_search(query=query, language=language, location=location)
        return text_query_result.places

    def _reverse_geocode(self, lat, lng, language=None):
        """
        根据经纬度请求google API获取坐标信息,返回信息
        :param lat: 纬度
        :param lng:经度
        :param language:语言
        :return:
        """
        # 根据经纬度获取地址信息 pincode
        list_reverse_geocode_result = self._Google_Geocod.reverse_geocode((lat, lng), language=language)
        # print json.dumps(list_reverse_geocode_result, indent=4)
        return list_reverse_geocode_result

    def _return_reverse_geocode_info(self, lat, lng, language=None):
        """
        整理信息
        :param lat:纬度
        :param lng:经度
        :param language:语言
        :return:
        """
        list_reverse_geocode = self._reverse_geocode(lat, lng, language=language)
        if list_reverse_geocode:
            city = ''
            pincode = ''
            route = ''
            neighborhood = ''
            sublocality = ''
            administrative_area_level_1 = ''
            country = ''
            street_number = ''
            # 全名地址
            formatted_address = list_reverse_geocode[0]['formatted_address']
            for address_info in list_reverse_geocode[0]['address_components']:

                # 城市标识为locality
                if 'locality' in address_info['types']:
                    city = address_info['long_name']
                # 邮政编码标识为postal_code
                elif 'postal_code' in address_info['types']:
                    pincode = address_info['long_name']
                # 街道路
                elif 'route' in address_info['types']:
                    route = address_info['long_name']
                # 相似地址名
                elif 'neighborhood' in address_info['types']:
                    neighborhood = address_info['long_name']
                # 地区名
                elif 'sublocality' in address_info['types']:
                    sublocality = address_info['long_name']
                # 省份
                elif 'administrative_area_level_1' in address_info['types']:
                    administrative_area_level_1 = address_info['long_name']
                # 国家
                elif 'country' in address_info['types']:
                    country = address_info['long_name']
                # 门牌号
                elif 'street_number' in address_info['types']:
                    street_number = address_info['long_name']

            return {'formatted_address': formatted_address}
        else:
            return None

    def get_pincode_city(self, lat, lng, language=None):
        """
        根据经纬度获取该地区详细信息
        :param lat: 纬度
        :param lng: 经度
        :return:
        """
        reverse_geocode_info = self._return_reverse_geocode_info(lat, lng, language=language)
        if reverse_geocode_info:
            return {'city': reverse_geocode_info['city'], 'pincode': reverse_geocode_info['pincode']}
        else:
            return None

    def get_address_recommendation(self, query, return_size, point, language=None, location=None):
        """
        获取输入地址的推荐地址(最多返回5个)
        :param query: 搜索地址名称
        :param return_size: Num of city returned
        :param language: 语言
        :param location: 地区筛选
        :return:
        """
        list_return_info = list()
        list_places_text_search_result = self._text_search(query=query, language=language, location=location)
        # 默认返回5条数据

        # Only greater th an 4.5
        if point != 0:
            print(len(list_places_text_search_result))
            del_num = 0
            for i in range(len(list_places_text_search_result)):
                place = list_places_text_search_result[i - del_num]
                place.get_details()
                if place.rating <= point:
                    del list_places_text_search_result[i - del_num]
                    del_num += 1


        if len(list_places_text_search_result) > return_size:
            list_places_text_search_result = list_places_text_search_result[:return_size]
        for place in list_places_text_search_result:
            result_geocode = self._return_reverse_geocode_info(place.geo_location['lat'], place.geo_location['lng'], language=language)
            # 数据不为空
            if result_geocode:
                # 地点全路径加上地点名
                result_geocode['formatted_address'] = '{} {}'.format(place.name, result_geocode['formatted_address'])
                result_geocode['place_name'] = place.name
                '''
                # 经纬度
                result_geocode['lat'] = '{}'.format(place.geo_location['lat'])
                result_geocode['lng'] = '{}'.format(place.geo_location['lng'])
                '''
                # detail
                place.get_details()
                # website
                if place.website:
                    result_geocode['website'] = place.website
                else:
                    result_geocode['website'] = ''
                # rating
                result_geocode['rating'] = str(place.rating)
                # phone number
                result_geocode['phone number'] = str(place.local_phone_number)
                # Photos

                try:
                    place.photos[0].get(maxheight=200, maxwidth=200)
                    result_geocode['Photo_url'] = str(place.photos[0].url)
                except:
                    result_geocode['Photo_url'] = " "
                    pass

                # Types
                try:
                    result_geocode['types'] = place.types[0]
                except:
                    result_geocode['types'] = " "
                    pass

                list_return_info.append(result_geocode)
        return list_return_info

    def generate_recommendation_list(self, num_of_city, num_of_day, num_of_activity):
        ls_day = []
        rest_of_day = num_of_day
        for i in range(num_of_city):
            if i == num_of_city - 1:
                ls_day.append(self.generate_activity_day(num_of_activity, rest_of_day))
                break

            temp = 1 if rest_of_day == 2 else (rest_of_day // 2 + 1)
            ls_day.append(self.generate_activity_day(num_of_activity, temp))
            rest_of_day -= temp
        return ls_day


    def generate_activity_day(self, num_of_activity, num_of_day):
        ls_day = []
        rest_of_day = num_of_day
        for i in range(num_of_activity):
            if i == num_of_activity - 1:
                ls_day.append(rest_of_day)
                break

            temp = 1 if rest_of_day == 2 else (rest_of_day // 2 + 1)
            ls_day.append(temp)
            rest_of_day -= temp
        return ls_day


    def generate_all(self, citys, activities, num_of_day, point=0):
        if 'South India' in citys and not activities:
            activities = ['Nature', 'Theatre', 'Shopping']
        if not activities:
            activities = ['attraction']

        ret_ls = []
        num_of_city = len(citys)
        num_of_activity = len(activities)
        print("Day: {}, City: {}, Activities: {}".format(num_of_day, num_of_city, num_of_activity))
        activy_day_ls = self.generate_recommendation_list(num_of_city, num_of_day, num_of_activity)

        for city_index in range(num_of_city):
            for activy_index in range(num_of_activity):
                input_query = str(citys[city_index]) + " " + str(activities[activy_index])
                print(input_query)
                activy_day = activy_day_ls[city_index][activy_index]
                if activy_day <= 0:
                    continue
                ret_ls.extend(self.get_address_recommendation(query=input_query, return_size=activy_day, point=point, language='en', location='United States'))

        return ret_ls





if __name__ == '__main__':
    # 使用实例
    google_maps = GoogleMaps()
    cities = ['New York']
    activities = []
    num_of_day = 2
    ls = google_maps.generate_all(cities, [], num_of_day)
    for i in range(len(ls)):
        ls[i]['Day'] = 'Day ' + str(i + 1)

    print(json.dumps(ls, indent=num_of_day))


