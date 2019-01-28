# -*- coding: utf-8 -*-
# @Project : mcm
# @Author  : Yang Jiao
# @File    : geo_tools.py.py
# @Time    : 2019/1/25 17:37
# @IDE     : PyCharm
from geopy.geocoders import Nominatim
from math import radians, cos, sin, asin, sqrt

def get_geo_info(state, county):
    """
        通过country和state获取经纬度
    """
    # 获取data中的县和州的基本信息
    address = county + ' ' + state
    # 通过geopy获取对应的经纬度信息
    try:
        geolocator = Nominatim()
        location = geolocator.geocode(address)
    except:
        location = None
    if location != None:
        # 剔除不是指定五个州中的情况
        if location.latitude < 36.31 or location.latitude > 42.17 or location.longitude < -89.35 or location.longitude > -74.41:
            return 9999,9999
        else:
            return location.latitude, location.longitude
    else:
        return 9999, 9999

def get_distance(lon1, lat1, lon2, lat2): # 经度1，纬度1，经度2，纬度2 （十进制度数）
    """
    通过经纬度计算两地之间的距离
    :param lon1:
    :param lat1:
    :param lon2:
    :param lat2:
    :return:
    """
    # 将十进制度数转化为弧度
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine公式
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    r = 6371  # 地球平均半径，单位为公里
    return c * r


if __name__ == '__main__':
    lat1, lon1 = get_geo_info("VA", "WARREN")
    lat2, lon2 = get_geo_info("PA", "WARREN")
    print(lat1, lon1)
    print(lat2, lon2)
    print(get_distance(lon1=lon1, lat1=lat1, lon2=lon2, lat2=lat2))
