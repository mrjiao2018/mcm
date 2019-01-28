# -*- coding: utf-8 -*-
# @Project : basemap_test
# @Author  : Jinglin Chen
# @File    : draw_map.py
# @Time    : 2019/1/26 19:27
# @IDE     : PyCharm

import numpy as np
import matplotlib.pyplot as plt

from tools import data_tools
from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon
from matplotlib.colors import rgb2hex
from matplotlib.collections import PatchCollection
from matplotlib import pylab


class TestData:
    def __init__(self, fips, moi):
        self.FIPS = fips
        self.MOI = moi


def drawing(data_list):
    plt.figure(figsize=(10, 5))

    m = Basemap(projection='lcc', lat_0=40, lon_0=-80,
                llcrnrlat=35, urcrnrlat=45,
                llcrnrlon=-90, urcrnrlon=-73,
                rsphere=6371200., resolution='l', area_thresh=10000)
    m.drawcounties()
    m.drawstates()
    m.drawcoastlines()
    m.drawmapboundary()
    parallels = np.arange(0, 90, 10.)

    m.drawparallels(parallels, labels=[1, 0, 0, 0], fontsize=10)

    meridians = np.arange(-110., -60., 10.)
    m.drawmeridians(meridians, labels=[0, 0, 0, 1], fontsize=10)

    county_FIPS_list = list()
    colors = {}
    patches = []
    index_list = list()
    cmap = plt.cm.YlOrRd
    vmin_ele = min(data_list, key=lambda ele: ele.MOI)
    vmin = vmin_ele.MOI
    vmax_ele = max(data_list, key=lambda ele: ele.MOI)
    vmax = vmax_ele.MOI

    index = 0
    for county in m.counties_info:
        if county['STATE_FIPS'] in {'21', '39', '42', '51', '54'}:
            county_FIPS = county['FIPS']
            for i in data_list:
                if str(i.FIPS) == county_FIPS:
                    moi = i.MOI
                    colors[county_FIPS] = cmap(np.sqrt((moi - vmin) / (vmax - vmin)))
                    county_FIPS_list.append(county_FIPS)
                    index_list.append(index)
        index += 1
    ax = plt.gca()
    index = 0

    for nshape, seg in enumerate(m.counties):
        if nshape in index_list:
            color = rgb2hex(colors[county_FIPS_list[index]])
            poly = Polygon(seg, facecolor=color, edgecolor=color)
            index += 1
            patches.append(poly)
            ax.add_patch(poly)

    # add colorbar
    colors1 = [i[1] for i in colors.values()]
    colorVotes = plt.cm.YlOrRd
    p = PatchCollection(patches, cmap=colorVotes)
    p.set_array(np.array(colors1))
    pylab.colorbar(p)

    plt.show()

def draw_thermodynamic_map(year, type, drug_name):
    """
    绘制热力图
    :param year: 年份
    :param type: 热力图种类，可选值："spread_level"，"drug_level"
    :param drug_name: 可选值："Heroin", "Oxycodone", "Buprenorphine"等，详情参见excel中SubstanceName
    :return:
    """
    point = []
    counties = data_tools.get_counties_from_json('../datasets/handled_data/{:d}.json'.format(year))
    for county in counties:
        fips = county.fips
        level_dic = county.spread_level if type=='spread_level' else county.drug_level
        if level_dic[drug_name] != None:
            level = level_dic[drug_name]
        else:
            level = 0
        point.append(TestData(fips, level))

    drawing(point)

def draw_total_thermodynamic_map(year):
    """
    绘制county的指定年份药品报告总量热力图
    :param year: 年份
    :return:
    """
    point = []
    counties = data_tools.get_counties_from_json('../datasets/handled_data/{:d}.json'.format(year))
    for county in counties:
        fips = county.fips
        level = county.total_drug_reports_county
        point.append(TestData(fips, level))

    drawing(point)

if __name__ == "__main__":
    # td0 = TestData(21009, 383)
    # td1 = TestData(21013, 387)
    # td2 = TestData(21019, 504)
    # td3 = TestData(21037, 852)
    # td_list = list()
    # td_list.append(td0)
    # td_list.append(td1)
    # td_list.append(td2)
    # td_list.append(td3)
    # drawing(td_list)

    # 绘制2012年的海洛因的传播(spread_level)热力图
    draw_thermodynamic_map(year=2012, type='spread_level', drug_name='Heroin')

    # 绘制2016年的海洛因的报告数量(drug_level)热力图
    draw_thermodynamic_map(year=2012, type='drug_level', drug_name='Heroin')

    # 绘制2017年的各个county的药品报告热力图
    draw_total_thermodynamic_map(year=2017)
