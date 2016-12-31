# coding=utf-8
import os
from datetime import *

'''
    将数据集分割为训练集和测试集（并排序）
'''

# 解析日期
def parse_date(raw_date):
    # entry_date = raw_date.decode("gbk")
    entry_date = raw_date
    year, month, day = entry_date.split(" ")[0].split("-")
    return int(year), int(month), int(day)


# 文件排序
def generate_sortedfile(origin_file_path, filename):
    originfile = open(origin_file_path)

    entrys = originfile.readlines()
    entrys.sort(key=lambda x: x.split(",")[0])
    sortedfile = open(filename, "w")
    for i in entrys:
        sortedfile.write(i)
    sortedfile.close()
    originfile.close()
    os.remove(origin_file_path)


# 分割数据  分割为训练集和测试集
def split_file(raw_file_path, seperate_day, begin_date):
    train_file_path = "train.csv"
    test_file_path = "test.csv"
    all_file_path = "all.csv"

    raw_file = open(raw_file_path)
    t_train = open(train_file_path, 'w')
    t_test = open(test_file_path, 'w')
    t_all = open(all_file_path, 'w')

    interval_days = (seperate_day - begin_date).days  # 28
    raw_file.readline()  # 读出栏位名
    for line in raw_file:
        entry = line.split(",")
        entry_date = date(*parse_date(entry[5]))
        date_delta = (entry_date - begin_date).days
        # dis_day = (12 - month) * 30 + (19 - day)
        if date_delta <= interval_days:
            t_train.write(line)
        else:
            t_test.write(line)  # 12/17
        t_all.write(line)

    t_all.close()
    t_test.close()
    t_train.close()
    raw_file.close()

    generate_sortedfile(train_file_path, "temp_" + train_file_path)
    print "generate train_file completed"
    generate_sortedfile(test_file_path, "temp_" + test_file_path)
    print "generate validation_file completed"
    generate_sortedfile(all_file_path, "temp_" + all_file_path)
    print "generate all_file completed"


if __name__ == "__main__":
    BEGINDAY = date(2014, 11, 18)
    SEPERATEDAY = date(2014, 12, 16)

    train_file_path = "data\dutir_tianchi_mobile_recommend_train_user_train.csv"

    begin_time = datetime.now()
    split_file(train_file_path, SEPERATEDAY, BEGINDAY)
    print datetime.now() - begin_time





