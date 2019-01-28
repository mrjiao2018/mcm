# -*- coding: utf-8 -*-
# @Project : mcm
# @Author  : Yang Jiao
# @File    : data_tools.py.py
# @Time    : 2019/1/25 17:37
# @IDE     : PyCharm
from data_manager import county
from data_manager import data_manager
from tools import geo_tools
from config import model_config
CFG = model_config.cfg

def get_all_counties1(data):
    """
        获取数据中的不同城市集合

        :param: {list}data 从excel中获取的记录
        :return {set}different_cities 不同的城市名称（包含州名）的set
    """
    cities = [(record.COUNTY + " " + record.State) for record in data]
    different_cities = set(cities)
    return different_cities


def get_all_counties2(data):
    """
        获取数据中的不同城市集合

        :param: {list}data 从excel中获取的记录
        :return {set}different_cities 不同的城市名称（不包含州名）的set
    """
    cities = [(record.COUNTY) for record in data]
    different_cities = set(cities)
    return different_cities

def get_all_drugs(data):
    """
    获取所有的药品种类
    :param data:
    :return:
    """
    drugs = [record.SubstanceName for record in data]
    different_drugs = set(drugs)
    return different_drugs

def get_counties_records(data):
    """
        获取一个城市的不同年份的记录的集合

        :param: {list}data 从excel中获取的记录
        :return {list}cities_records 二维数组，其中每一维是一个city的所有年份记录的集合
    """
    # 所有城市的所有记录
    cities_records = []
    cities = get_all_counties1(data)
    for city in cities:
        # 同一个城市的所有记录
        city_records = []
        for record in data:
            city_record = record.COUNTY + " " + record.State
            if(city == city_record):
                # 将同一个城市的所有记录添加到city_records中
                city_records.append(record)
        # 将所有城市的所有记录添加到cities_records中
        cities_records.append(city_records)

    return cities_records

def get_counties(data, year):
    """
    获取 data 数据中指定年份的county对象的list集合

    :param data:
    :param year:
    :return:
    """
    counties = []
    counties_records = get_counties_records(data)
    i = 0
    for county_records in counties_records:
        #初始化基本数据
        fips = county_records[0].FIPS_Combined
        state = county_records[0].State
        county_name = county_records[0].COUNTY
        total_drug_reports_county = county_records[0].TotalDrugReportsCounty
        drug_level = {}
        #初始化指定年份中毒品报告数量信息和传播强度信息
        for county_record in county_records:
            if county_record.YYYY == year:
                drug_name = county_record.SubstanceName
                drug_reports_num = county_record.DrugReports
                drug_level.__setitem__(drug_name, drug_reports_num)

        county_obj = county.County(fips=fips, state=state, county=county_name, drug_level=drug_level,
                                     total_drug_reports_county=total_drug_reports_county, year=year)
        counties.append(county_obj)
        i = i + 1
        print("initialize counties, now {:d} counties has been initialized".format(i))


    return get_neighbor_counties(counties)

def get_neighbor_counties(counties):
    """
    获取城市的临近城市
    :return:
    """
    for county in counties:
        lat1 = county.latitude
        lon1 = county.longitude
        if lat1 == 9999:
            continue

        for other_county in counties:
            lat2 = other_county.latitude
            lon2 = other_county.longitude
            if lat1 == 9999:
                continue

            distance = geo_tools.get_distance(lat1=lat1, lon1=lon1, lat2=lat2, lon2=lon2)
            if distance > 0 and distance < CFG.DISANCE_THRESHOLD:
                county.neighbors.append(other_county.fips)

    return counties

if __name__ == '__main__':
    data = data_manager.read_xlsx()
    # counties1 = get_all_counties1(data)
    # counties2 = get_all_counties2(data)
    # drugs = get_all_drugs(data)
    # counties_records = get_counties_records(data)
    counties = get_counties(data, 2016)
    a = 0
