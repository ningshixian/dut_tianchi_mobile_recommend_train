# coding=utf-8

"""
本脚本用于对未归一化的数据进行归一化
二进制文件格式
文件前4个字节为文件总行数
接下来4个字节为每行的维度数
接下来是数据，数据的每一维是4个字节
"""

import struct
import sys

# 配置项
# 输入文件路径，需要是未进行归一化的文件
filename = ur'..\data\temp_test.csv'

#配置项结束
if len(sys.argv) > 1:
    src = sys.argv[1]
else:
    src = filename
    # print ur'请输入文件路径：'
    # src = raw_input()
    # if len(src) == 0:
    #     src = filename

dst = src.rstrip('.csv') + ".bin"

if len(sys.argv) > 2:
    dst = sys.argv[2]

dstfile = open(dst, 'wb')

#写入文件行数
dstfile.write(struct.pack('i', 0))

lineCount = 0
print ur'正在输出...'
with open(src) as f:
    line = f.readline()
    headers = line.rstrip('\n').rstrip(',').split(',')
    print line
    '''
        userid,itemid,label开头这3列是int型，
        其余全部double型，第4列是o2o，要辅助用作常数项，所以也用double了）
    '''
    length = len(headers)
    dstfile.write(struct.pack('i', length))

    for line in f:
        items = line.rstrip('\n').rstrip(',').split(',')
        for i in xrange(3):
            val = struct.pack('i',int(items[i]))
            dstfile.write(val)

        x = struct.pack('s', str(items[3]))
        dstfile.write(x)

        for i in xrange(4,length-1):
            b = struct.pack('d',float(items[i]))
            dstfile.write(b)

        b = struct.pack('s', str(items[-1]))
        dstfile.write(b)

        lineCount += 1
        if lineCount % 1000 == 0:
            print lineCount

print ur'总行数：', lineCount
dstfile.seek(0)
dstfile.write(struct.pack('i', lineCount))
dstfile.close()
print ur'文件保存完毕'