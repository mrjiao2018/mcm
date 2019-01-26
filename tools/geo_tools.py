# -*- coding: utf-8 -*-
# @Project : mcm
# @Author  : Yang Jiao
# @File    : geo_tools.py.py
# @Time    : 2019/1/25 17:37
# @IDE     : PyCharm
from geopy.geocoders import Nominatim


def get_geo_info(state, country):
    """
        通过country和state获取经纬度
    """
    # 获取data中的县和州的基本信息
    address = country + ' ' + state
    # 通过geopy获取对应的经纬度信息
    geolocator = Nominatim()
    location = geolocator.geocode(address)

    return location.latitude, location.longitude