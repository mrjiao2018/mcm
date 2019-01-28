from easydict import EasyDict as edict

__C = edict()

cfg = __C

# 判定为临近城市的距离阈值，此处设置40公里以内都为邻居
__C.DISANCE_THRESHOLD = 40