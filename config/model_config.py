# -*- coding: utf-8 -*-
# @Time    : 18-12-21
# @Author  : Yang Jiao
# @Site    : http://github.com/mrjiao2018
# @File    : model_config.py
# @IDE     : PyCharm Community Edition


from easydict import EasyDict as edict

__C = edict()

cfg = __C

# Train options
__C.TRAIN = edict()
# 传播模式设置，no_direction为等强度向周围传播，nswe_direction为区分东南西北的状况下向周围传播
__C.TRAIN.SPREAD_MODE = ['no_direction', 'nswe_direction']

# 传播强度的系数k
__C.TRAIN.SPREAD_K = 1
# 传播强度的偏置的下限
__C.TRAIN.SPREAD_BIAS_MIN = 0
# 传播强度的偏置的上限
__C.TRAIN.SPREAD_BIAS_MAX = 1