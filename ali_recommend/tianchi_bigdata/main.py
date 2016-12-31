# coding=utf-8

'''
fetch_feature.py：提取特征(训练集和测试集)
fetch_sample:提取正、负样本
fetch_negative_sample:负样本抽样
combine_feature_txt:混合正负样本特征
cut_data_set.py:按照移动窗口方式，分割数据集

product_test_data.py:产生测试数据
classify_user_item.py:训练学习特征，并预测
get_recommend_result_6.py:对最后分类结果取置信度，并得到相应的推荐结果

get_feature_vector_txt_4.py:提取特征向量，去掉用户-商品标示
global_feature.py:提取全局比例特征
'''

from datetime import date
import fetch_feature
import fetch_sample
import fetch_negative_sample
import combine_feature_txt
import cut_data_set
import product_test_data
import classify_user_item
import get_recommend_result_6


row_data = '../data/dutir_tianchi_mobile_recommend_train_user_train.csv'
feature_data = '../data/temp_train_feature.csv'
test_data = '../data/test.csv'
temp_test_feature = '../data/temp_test_feature.csv'
combine_feature = '../data/combine_txt_feature.txt'
train_data_new = '../data/combine_txt_feature_shuf_new.txt'
test_data_new = '../data/temp_test_feature_new.txt'

result9 = '../data/result9.txt'
output_final_result_csv = '../data/tianchi_predict_9.csv'

if __name__ == "__main__":
    # BEGINDAY = date(2014, 11, 18)
    # SEPERATEDAY = date(2014, 12, 16)
    # cut_data_set.split_file(row_data, SEPERATEDAY, BEGINDAY)
    #
    # item_brand = dict()
    # fetch_feature.fetch_feature(row_data, feature_data, item_brand)
    #
    # item_brand2 = dict()
    # fetch_feature.fetch_feature(test_data, temp_test_feature, item_brand2)
    #
    # fetch_sample.fetch_sample(test_data, feature_data)  # 拿到训练特征集的正例和负例
    #
    # fetch_negative_sample.fetch_negative_sample()  # 负采样
    #
    # combine_feature_txt.combine(combine_feature)  # 混合正负样本特征
    #
    # product_test_data.product_test_data()  # 将12/15-12/17的数据作为测试(未执行)
    #
    # classify_user_item.classify_user_item(train_data_new, test_data_new, result9)  # 训练学习特征，并预测
    #
    get_recommend_result_6.get_result(result9, output_final_result_csv, test_data_new)

















