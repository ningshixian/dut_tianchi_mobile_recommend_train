# coding=utf-8

from datetime import date
import numpy as np

def test_slice():
    data = np.arange(0,16).reshape(4,4)
    print data
    X = data[:, -1]  # select columns 1 through end
    print X


def comma_replace1():
    with open("data/combine_txt_feature_shuf_new.txt", 'w') as f1:
        with open("data/combine_txt_feature_shuf.txt", 'r') as f:
            for line in f.readlines():
                new_line = line.replace(',', ' ')
                f1.write(new_line)

def comma_replace2():
    with open("data/temp_test_feature_new.txt", 'w') as f1:
        with open("data/temp_test_feature.txt", 'r') as f:
            for line in f.readlines():
                new_line = line.replace(',', ' ')
                f1.write(new_line)


if __name__ == "__main__":
    comma_replace2()



