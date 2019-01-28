# -*- coding: utf-8 -*-
# @Project : mcm
# @Author  : Jinglin Chen
# @File    : fp_node.py
# @Time    : 2019/1/28 15:14
# @IDE     : PyCharm


class Fpnode:
    def __init__(self, item='root'):
        self.item = item
        self.pa = None
        self.child = {}
        self.count = 0

    def is_root(self):
        return self.pa is None
