# encoding:utf-8

import csv

def product_test_data():
    csvfile = file('../data/test_data.csv', 'wb')
    writer = csv.writer(csvfile)

    for line in csv.reader(file(r'../data/all.csv', 'rb')):
        time_s = line[5].split(' ')
        time_slot = time_s[0].split('-')
        month = int(time_slot[1])
        day = int(time_slot[2])
        dis_day = (12 - month) * 30 + (17-day)
        if dis_day <= 2:
            writer.writerow(line)  # 将12/15-12/17的数据作为测试

