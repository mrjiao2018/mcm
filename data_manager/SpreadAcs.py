# -*- coding: utf-8 -*-
# @Project : mcm
# @Author  : Jinglin Chen
# @File    : SpreadAcs.py
# @Time    : 2019/1/28 14:43
# @IDE     : PyCharm


class SpreadAcs:
    def __init__(self, title_list, data_list, spread_level, drug_level):
        for i in range(len(data_list)):
            self.__setattr__(title_list[i], data_list[i])
        self.spread_level = spread_level
        self.drug_level = drug_level

    def to_spread_list(self):
        dict = {}
        dict.update(self.__dict__)
        values = list(dict.values())
        values.pop()
        return values

    def to_drug_list(self):
        dict = {}
        dict.update(self.__dict__)
        values = list(dict.values())
        values.pop(-2)
        return values




