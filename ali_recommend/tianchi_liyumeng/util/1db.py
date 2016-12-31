# coding=utf-8


# coding=utf-8

# 本脚本可将阿里天池平台公布的数据文件，转换成可以直接导入到mysql数据库中的文件
# 需配置src为从天池平台下载的数据

##配置项
#############
#原始数据文件路径
src = r"..\data\dutir_tianchi_recommend_data.csv"
#生成文件路径
dst = src + ".mysql.csv"
#############
##配置项结束

f_dst = open(dst, 'w')
print ur'正在读取:', src
with open(src) as f:
    #输出表头
    f_dst.write(f.readline())
    #循环输出表内容
    for line in f:
        #原内容为：'98047837,232431562,1,,4245,2014-12-06 02\n'
        #修改后为：'98047837,232431562,1,,4245,2014-12-06 02:00:00\n'
        f_dst.write(line.replace('\n', ':00:00\n'))
    f_dst.close()

print ur'已输出至：', dst

#请使用HeidiSQL将输出的文件到如到数据库中
##
#导入命令：LOAD DATA LOW_PRIORITY LOCAL INFILE 'F:\\AliRecommend2Data\\tianchi_mobile_recommend_train_user.csv.mysql.csv' REPLACE INTO TABLE `AliRecommend2Data`.`T_UserAction` FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"' ESCAPED BY '"' LINES TERMINATED BY '\n' IGNORE 1 LINES (`userid`, `itemid`, `behaviortype`, `usergeography`, `category`, `actiondate`);




