# coding=utf-8

"""
本脚本用于对未归一化的数据进行归一化
"""
import sys

#配置项
#输入文件路径，需要是未进行归一化的文件
filename = ur'..\dutir_tianchi_recommend_data.csv.mysql.samp.csv'
#配置项结束

if len(sys.argv) > 1:
    src = sys.argv[1]
else:
    src = filename

#输出文件
dst = src.rstrip('.csv') + '.norm.csv'

dst_f = open(dst,'w')
with open(src,'r') as f:
    header = f.readline()
    print 'headers:'
    print header
    length = len(header.rstrip('\n').rstrip(',').split(','))
    print 'count:',length
    min = [0] * length
    max = [0] * length
    t = 0
    for tmp in f:
        items = [float(item) for item in tmp.rstrip('\n').rstrip(',').split(',')]
        length = len(items)
        for i in xrange(length):
            if items[i] > max[i]:
                max[i] = items[i]
            if items[i] < min[i]:
                min[i] = items[i]
        t+=1
        if t % 1000 == 0:
            print t
print 'max:',','.join(map(str,max))
print 'min:',','.join(map(str,min))

dis = [0] * length
for i in xrange(length):
    dis[i] = max[i] - min[i]

t = 0
with open(src,'r') as f:
    header = f.readline()
    dst_f.write(header)
    for tmp in f:
        items = [float(item) for item in tmp.rstrip('\n').rstrip(',').split(',')]
        for i in xrange(2,length):
            if dis[i] > 0:
                items[i] = (items[i] - min[i]) / dis[i]
        dst_f.write(','.join(map(str,items)))
        dst_f.write('\n')
        t+=1
        if t % 1000 == 0:
            print t
dst_f.close()
print 'output complete.'
print dst