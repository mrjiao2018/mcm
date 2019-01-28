# -*- coding: utf-8 -*-
# @Project : basemap_test
# @Author  : Jinglin Chen
# @File    : draw_map.py
# @Time    : 2019/1/26 19:27
# @IDE     : PyCharm

import numpy as np
import matplotlib.pyplot as plt

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


if __name__ == "__main__":
    td0 = TestData(21009, 383)
    td1 = TestData(21013, 387)
    td2 = TestData(21019, 504)
    td3 = TestData(21037, 852)
    td_list = list()
    td_list.append(td0)
    td_list.append(td1)
    td_list.append(td2)
    td_list.append(td3)
    drawing(td_list)
