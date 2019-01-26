# -*- coding: utf-8 -*-
# @Project : mcm
# @Author  : Yang Jiao
# @File    : data_tools.py.py
# @Time    : 2019/1/25 17:37
# @IDE     : PyCharm



def get_all_cities1(data):
    """
        获取数据中的不同城市集合

        :param: {list}data 从excel中获取的记录
        :return {set}different_cities 不同的城市名称（包含州名）的set
    """
    cities = [(record.Country + " " + record.State) for record in data]
    different_cities = set(cities)
    return different_cities


def get_all_cities2(data):
    """
        获取数据中的不同城市集合

        :param: {list}data 从excel中获取的记录
        :return {set}different_cities 不同的城市名称（不包含州名）的set
    """
    cities = [(record.Country) for record in data]
    different_cities = set(cities)
    return different_cities


def get_cities_records(data):
    """
        获取一个城市的不同年份的记录的集合

        :param: {list}data 从excel中获取的记录
        :return {list}cities_records 二维数组，其中每一维是一个city的所有年份记录的集合
    """
    cities_records = []
    cities = get_all_cities1(data)
    for city in cities:
        city_records = []
        for record in data:
            city_record = record.Country + " " + record.State
            if(city == city_record):
                city_records.append(record)
        cities_records.append(city_record)

    return cities_records

