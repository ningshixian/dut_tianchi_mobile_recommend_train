# encoding:utf-8

'''
     负采样--负例特征采样
'''

import csv

def fetch_negative_sample():
    num = 1
    csvfile = file('../data/sample_17_negative.csv', 'wb')
    writer = csv.writer(csvfile)
    for line in csv.reader(file('../data/17_negative.csv', 'r')):
        if num % 200 == 0:
            writer.writerow(line)
        num = num + 1
    print num

if __name__ == '__main__':
    fetch_negative_sample()