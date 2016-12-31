# coding=utf-8

"""
本脚本用于扩展出除法特征
"""
import sys

# 配置项
# 输入文件路径，需要是未进行归一化的文件
filename = ur'..\dutir_tianchi_recommend_data.csv.mysql.samp.csv'
#配置项结束
if len(sys.argv) > 1:
    src = sys.argv[1]
else:
    src = filename

#输出文件
dst = src.rstrip('.csv') + '.expand.csv'

#ui 在4~39，u在44~79，i在111~146，c在151~186，uc在218~253
ui_range = range(4, 40)
u_range = range(44, 80)
i_range = range(111, 147)
c_range = range(151, 187)
uc_range = range(218, 254)


def divide(a, b):
    if b > 0 or b < 0:
        return 1.0 * a / b
    else:
        return 0


dst_f = open(dst, 'w')
with open(src, 'r') as f:
    header = f.readline()
    tail = []
    for a, b in zip(ui_range, u_range):  #ui 在4~39，u在44~79，i在111~146，c在151~186，uc在218~253
        tail.append("%d_%d" % (a, b))
    for a, b in zip(uc_range, c_range):
        tail.append("%d_%d" % (a, b))
    for a, b in zip(ui_range, uc_range):
        tail.append("%d_%d" % (a, b))
    for a, b in zip(i_range, c_range):
        tail.append("%d_%d" % (a, b))
    for a, b in zip(uc_range, u_range):
        tail.append("%d_%d" % (a, b))

    header = header.rstrip('\n') + ','.join(tail) + '\n'
    print 'headers:', header
    length = len(header.rstrip('\n').rstrip(',').split(','))
    print 'count:', length

    dst_f.write(header)
    t = 0

    #ui 在4~39，u在44~79，i在111~146，c在151~186，uc在218~253
    alist = ui_range + uc_range + ui_range + i_range + uc_range
    blist = u_range + c_range + uc_range + c_range + u_range
    ziplen = len(alist)
    ziplist = zip(range(ziplen), alist, blist)
    tail = [0] * ziplen

    for tmp in f:
        items = [item for item in tmp.rstrip('\n').rstrip(',').split(',')]
        for i, a, b in ziplist:
            tail[i] = divide(float(items[a]), float(items[b]))
        dst_f.write(tmp.rstrip('\n').rstrip(','))
        dst_f.write(',')
        dst_f.write(','.join(map(str, tail)))
        dst_f.write('\n')

        t += 1
        if t % 1000 == 0:
            print t

dst_f.close()
print ur'生成除法特征完毕,文件行数：', t
print ur'输出路径：', dst

