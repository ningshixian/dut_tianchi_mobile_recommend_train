# encoding:utf-8

'''
    提取训练集的正、负样本--加标签
'''

import csv
import os

def fetch_sample(test_data, feature_data):
    buy = set()
    for line in csv.reader(file(test_data, 'rb')):
        # if line[5].find('2014-12-17') >= 0:
        if line[2] == '4':
            buy.add((line[0], line[1]))  # 正例集

    csvfile = file('../data/17_negative.csv', 'wb')
    writer = csv.writer(csvfile)

    csvfile2 = file('../data/17_positive.csv', 'wb')
    writer2 = csv.writer(csvfile2)

    for line in csv.reader(file(feature_data, 'rb')):
        if (line[0], line[1]) not in buy:
            line.append(0)
            writer.writerow(line)  # 负例特征
        else:
            line.append(1)
            writer2.writerow(line)  # 正例特征


if __name__ == '__main__':
    test_data = '../data/test.csv'
    feature_data = '../data/temp_train_feature.csv'
    fetch_sample(test_data, feature_data)