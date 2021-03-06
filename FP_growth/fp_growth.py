# -*- coding: utf-8 -*-
# @Project : mcm
# @Author  : Jinglin Chen
# @File    : fp_growth.py
# @Time    : 2019/1/28 15:13
# @IDE     : PyCharm


from util import print_rules
from util import print_frequent_itemset
from util import get_all_subsets
from util import get_associaion_rules
from fp_node import Fpnode
import numpy as np


def compute_frequency(dataset):
    frequency = {}
    for data in dataset:
        for item in data[0]:
            frequency[item] = frequency.get(item, 0) + data[1]
    return frequency


def sort_data(dataset, frequency):
    result = []
    for i in range(len(dataset)):
        data = dataset[i]
        data[0].sort(key=lambda item: frequency[item], reverse=True)
        result.append(data)
    return result


def prune(dataset, frequency, minSupport):
    result = []
    for i in range(len(dataset)):
        data = dataset[i]
        listdata = [item for item in data[0] if frequency[item] >= minSupport]
        result.append((listdata, data[1]))
    return result


def insert_data(data, root, header):
    for item in data[0]:
        if item not in root.child.keys():
            newnode = Fpnode(item)
            newnode.pa = root
            root.child[item] = newnode
            if item not in header.keys():
                header[item] = None
            header[item] = (newnode, header[item])
        root = root.child[item]
        root.count = root.count + data[1]


def print_fptree(root):
    print('%s %d' % (root.item, root.count))
    for subnode in root.child.values():
        print_fptree(subnode)

def build_fptree(dataset, minSupport, suffix):
    if len(dataset) == 0:
        return [], {}

    root = Fpnode()
    header = {}
    frequent_itemset = []
    support = {}
    frequency = compute_frequency(dataset)
    dataset = prune(dataset, frequency, minSupport)
    dataset = sort_data(dataset, frequency)
    for data in dataset:
        insert_data(data, root, header)
        # print(data)

    for h in header.keys():
        sup_count = 0
        t = header[h]
        while t is not None:
            sup_count += t[0].count
            t = t[1]
        listitem = [h] + suffix
        frequent_itemset.append(listitem)
        listitem.sort()
        support[tuple(listitem)] = sup_count

    for item in sorted(header.items(), key=lambda item: frequency[item[0]]):
        t = item[1]
        newdataset = []
        while t is not None:
            count = t[0].count
            newdata = []
            panode = t[0].pa
            while not panode.is_root():
                newdata.append(panode.item)
                panode = panode.pa
            newdata.reverse()
            newdata = (newdata, count)
            t = t[1]
            if len(newdata[0]) != 0:
                newdataset.append(newdata)
        newsuffix = [item[0]] + suffix
        new_itemset, new_support = build_fptree(newdataset, minSupport, newsuffix)
        frequent_itemset.extend(new_itemset)
        support.update(new_support)

    return frequent_itemset, support


def fpgrowth(dataset, minSupportRatio, minConfidenceRatio):
    dataset = [(list(data), 1) for data in dataset]
    minSupport = int(minSupportRatio * len(dataset))
    frequent_itemset, support = build_fptree(dataset, minSupport, [])
    rules = get_associaion_rules(frequent_itemset, support, minConfidenceRatio)
    return frequent_itemset, rules

