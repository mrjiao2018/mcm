# -*- coding: utf-8 -*-
# @Project : mcm
# @Author  : Jinglin Chen
# @File    : data_models.py
# @Time    : 2019/1/26 14:43
# @IDE     : PyCharm
from tools import geo_tools

class MCM_NFLIS_Data:
    """
    store the MCM_NFLIS_Data
    """

    def state_converse(self, State):
        return {
            'KY': 'Kentucky',
            'OH': 'Ohio',
            'PA': 'Pennsylvania',
            'VA': 'Virginia',
            'WV': 'West Virginia'
        }.get(State, 'error')

    def __init__(self, data_list):
        self.YYYY = data_list[0]
        # self.State = self.state_converse(data_list[1])
        self.State = data_list[1]
        self.COUNTY = data_list[2]
        self.FIPS_State = data_list[3]
        self.FIPS_County = data_list[4]
        self.FIPS_Combined = data_list[5]
        self.SubstanceName = data_list[6]
        self.DrugReports = data_list[7]
        self.TotalDrugReportsCounty = data_list[8]
        self.TotalDrugReportsState = data_list[9]
        # self.latitude, self.longitude = geo_tools.get_geo_info(self.State, self.COUNTY)



class ACS_5YR_DP02:
    def __init__(self, title_list, list):
        for i in range(len(list)):
            self.__setattr__(title_list[i], list[i])


