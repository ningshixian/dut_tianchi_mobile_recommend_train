# encoding:utf-8

import random

def combine(combine_feature):
    f1 = open(combine_feature, 'wb')

    with open("../data/17_positive.csv", "r") as f:
        lines = f.readlines()
        for line in lines:
            f1.write(line)
    with open("../data/sample_17_negative.csv", "r") as f:
        lines = f.readlines()
        for line in lines:
            f1.write(line)
    f1.close()


if __name__=="__main__":
    combine()