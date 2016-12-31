# encoding:utf-8

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
import numpy as np


def classify_user_item(train_data_new, test_data_new, result9):
    data = np.loadtxt(train_data_new)
    X = data[:, :-1]  # select columns 0 through end-1
    y = data[:, -1]  # select column end
    print X
    print y
    print 'start train'

    clf2 = RandomForestClassifier(n_estimators=100)
    # clf2=GradientBoostingClassifier()
    clf2.fit(X, y)
    # clf2 = LogisticRegression().fit(X, y)
    print clf2.classes_

    data1 = np.loadtxt(test_data_new)
    X_test = data1[:, :]
    print 'testing data is ok'
    result = clf2.predict_proba(X_test)
    print 'output result'
    print result

    f_result = open(result9, 'w')
    for i in range(0, len(result)):
        f_result.write(str(result[i]) + '\n')

