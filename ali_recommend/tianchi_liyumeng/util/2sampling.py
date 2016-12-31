# coding=utf-8

"""
本脚本用于对数据进行负例抽样
nega_rate配置项表示负例保留下来的概率
例如0.1，即表示负例抽样1/10

本工具也可通过命令行调用,例如：
python 2sampling.py f:\data.csv
输出文件f:\data.sample.csv
"""

import random
import sys

# 配置项
# 输入文件路径，需要是未进行归一化的文件
filename = ur'..\data\dutir_tianchi_recommend_data.csv'
#负例保留下来的概率
nega_rate = 0.1
#配置项结束
if len(sys.argv) > 1:
    src = sys.argv[1]
else:
    src = filename

#输出文件
dst = src.rstrip('.csv') + '.samp.csv'

dst_f = open(dst, 'w')
with open(src, 'r') as f:
    header = f.readline()
    print 'headers:', header
    length = len(header.rstrip('\n').rstrip(',').split(','))
    print 'count:', length

    dst_f.write(header)
    t = 0
    for tmp in f:
        items = [item for item in tmp.rstrip('\n').rstrip(',').split(',')]
        behavior = float(items[2])
        if behavior < 4 and random.random() > nega_rate:
            pass
        else:
            dst_f.write(tmp)
        t += 1
        if t % 1000 == 0:
            print t

dst_f.close()
print 'output complete.', t
print dst

