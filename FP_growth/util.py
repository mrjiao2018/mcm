# -*- coding: utf-8 -*-
# @Project : mcm
# @Author  : Jinglin Chen
# @File    : util.py
# @Time    : 2019/1/28 15:21
# @IDE     : PyCharm


def print_rules(rules):
    rules.sort()
    print('Association Rules:')
    for rule in rules:
        print('%s ==> %s' % (rule[0], rule[1]))


def print_frequent_itemset(result):
    result.sort()
    print('Frequent Itemset:')
    for s in result:
        setstr = ''
        for item in s:
            setstr += str(item) + ' '
        print(setstr)


def get_all_subsets(itemset):
    if len(itemset) == 0:
        return []
    result = [[]]
    for item in itemset:
        newSet = [oldSet + [item] for oldSet in result]
        result.extend(newSet)
    result = result[1:-1]  # remove empty subset and itemset itself
    for i in range(len(result)):
        result[i].sort()
    return result


def get_associaion_rules(frequent_itemset, support, minConfidenceRatio):
    rules = []
    for itemset in frequent_itemset:
        subsets = get_all_subsets(itemset)
        for subset in subsets:
            confidence = support[tuple(itemset)] / support[tuple(subset)]
            if confidence >= minConfidenceRatio:
                diffset = set(itemset).difference(set(subset))
                rules.append((tuple(subset), tuple(diffset)))
    return rules
