#!/usr/modelin/env python
# -*- coding: utf-8 -*-

'''
@author: Vencent_Wang
@contact: Vencent_Wang@outlook.com
@file: main.py
@time: 2022/3/19 19:05
@desc:
'''

from sklearn import metrics
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

from config import arg_parse
from data_process import load_data

Classifier_Model_dict = {'SVM': SVC, 'RF': DecisionTreeClassifier, 'LOG': LogisticRegression}

def main(args):
    # load data
    dataX, dataY, dataW, dataid = load_data(args.datadir, args.dataname)

    # data split
    ids = range(len(dataX))
    train_split, test_split = train_test_split(ids, test_size=0.2, random_state=args.seed)
    X_train = [dataX[i] for i in train_split]
    Y_train = [dataY[i] for i in train_split]

    X_test = [dataX[i] for i in test_split]
    Y_test = [dataY[i] for i in test_split]

    # train
    if args.model == "SVM":
        clf = Classifier_Model_dict[args.model](probability=True)
    else:
        clf = Classifier_Model_dict[args.model]()
    clf.fit(X_train, Y_train)
    y_pred = clf.predict(X_test)
    # 仅使用SVM模型时有效
    y_pro = clf.predict_proba(X_test)
    acc = metrics.accuracy_score(y_pred, Y_test)
    print("Accuracy({}):{}".format(args.model, acc))

if __name__ == "__main__":
    args = arg_parse()
    main(args)
