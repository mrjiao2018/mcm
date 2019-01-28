# -*- coding: utf-8 -*-
# @Project : mcm
# @Author  : Yang Jiao
# @File    : geo_metacell_model.py.py
# @Time    : 2019/1/25 17:37
# @IDE     : PyCharm
from tools import data_tools


class GeoMetacell():
    def __init__(self, source2010_path,source2011_path,source2012_path,source2013_path,
                 source2014_path,source2015_path,source2016_path,source2017_path):
        """

        :param source_data_file_path: 源数据地址
        """
        self.counties_2010 = data_tools.get_counties_from_json(source2010_path)
        self.counties_2011 = data_tools.get_counties_from_json(source2011_path)
        self.counties_2012 = data_tools.get_counties_from_json(source2012_path)
        self.counties_2013 = data_tools.get_counties_from_json(source2013_path)
        self.counties_2014 = data_tools.get_counties_from_json(source2014_path)
        self.counties_2015 = data_tools.get_counties_from_json(source2015_path)
        self.counties_2016 = data_tools.get_counties_from_json(source2016_path)
        self.counties_2017 = data_tools.get_counties_from_json(source2017_path)
        pass

    def build_model(self):
        """
        核心思想：通过指定county的neighbors来计算下一年该county的预期毒品报告数量，
                 通过将预期数量与实际下一年报告数目比较，从而修正neighbors的spread_level
        :return:
        """
        for county in self.counties_2010:
            # 获取county的neighbors
            neighbors = []
            for neighbor_fips in county.neighbors:
                neighbor_county = data_tools.find_county_by_fips(self.counties_2010, neighbor_fips)
                neighbors.append(neighbor_county)

            # 预测该county下一年的drug_level
            drug_level = county.drug_level
            drug_level_next_year = self.preidct(drug_level, neighbors)

            # 通过损失函数修正邻居的spread_level


    def preidct(self, drug_level, neighbors):
        """
        通过自身的drug_level和邻居的spread_level来预测下一年自身的drug_level情况
        :param {dic}drug_level:
        :param {list}neighbors:
        :return:
        """
        pass


    def caculate_loss(self, predict, truth):
        """
        计算损失值
        :param {dict}predict:
        :param {dict}truth:
        :return:
        """
        if abs(predict-truth) < 2:
            return 0
        else:
            return abs(predict-truth)/(predict+truth)

    def optimize(self, county, drug_level_next_year, source_data_next_year):
        county_fips = county.fips
        neighbors = county.neighbors
        # 找到county在下一年中的记录
        county_next_year = data_tools.find_county_by_fips(counties=source_data_next_year,
                                                          fips=county_fips)
        loss=self.caculate_loss(predict=drug_level_next_year, truth=county_next_year.drug_level)
        pass


if __name__ == '__main__':
        pass