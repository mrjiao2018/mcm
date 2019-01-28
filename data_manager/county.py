# -*- coding: utf-8 -*-
# @Project : mcm
# @Author  : Yang Jiao
# @File    : county.py
# @Time    : 2019/1/27 15:18
# @IDE     : PyCharm
import random
from config import model_config
from tools import geo_tools
CFG = model_config.cfg

class County():
    def __init__(self, county, state, year, fips, total_drug_reports_county, drug_level):
        self.county = county
        self.state = state
        self.year = year
        self.fips = fips
        self.total_drug_reports_county = total_drug_reports_county
        self.latitude, self.longitude = geo_tools.get_geo_info(state=self.state, county=self.county)
        # drug_level为城市毒品报告数量，key为毒品名称，value为毒品报告数量
        self.drug_level = drug_level
        # spread_level为城市毒品报告数量等强度向周围传播的情况下的传播强度参数，key为毒品名称，value为毒品传播强度参数
        self.spread_level = self._init_spread_level()
        # 以下为城市毒品报告数量不等强度(不同方向的强度不同)向周围传播的情况下的传播强度参数，key为毒品名称，value为毒品传播强度参数
        self.east_spread_level = self._init_spread_level()
        self.west_spread_level = self._init_spread_level()
        self.north_spread_level = self._init_spread_level()
        self.south_spread_level = self._init_spread_level()
        # 临近城市集合，存储为fips_combined code
        self.neighbors = []

    def _init_spread_level(self):
        spread_level = {}
        drugs = list(self.drug_level.keys())
        for drug in drugs:
            bias = random.uniform(CFG.TRAIN.SPREAD_BIAS_MIN, CFG.TRAIN.SPREAD_BIAS_MAX)
            spread_level_value = (CFG.TRAIN.SPREAD_K * self.drug_level[drug] + bias) if self.drug_level[drug] > 0 else 0
            spread_level.__setitem__(drug, spread_level_value)

        return spread_level


if __name__ == '__main__':
    drug_level = {'drug':123, 'medical':456}

    spread_level = {}
    drugs = drug_level.keys()
    spread_level.__setitem__("123", 123)
    print(spread_level)