#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@author: Vencent_Wang
@contact: Vencent_Wang@outlook.com
@file: data_process.py
@time: 2022/3/19 19:05
@desc:
'''
import os
import csv

path = "./data"
filename = "sid_train_data"

def load_data(path,filename):

    dir = "./{}/{}.csv".format(path, filename)
    assert os.path.exists(dir), "File does not existing, please read after cheaking!"
    # content = pd.read_csv(dir)
    # print(content)
    with open(dir, 'r') as f:
        file = csv.reader(f)
        contents = list(file)
        label = " ".join(contents[0])
        Num_X = label.count('X')
        Num_Y = label.count('y')
        Num_W = label.count('w')

        # print(content)
        data_X = []
        data_Y = []
        data_W = []
        data_id = []
        for content in contents[1:]:
            data_X.append([int(i) for i in content[1:Num_X+1]])
            data_Y.append(int(content[Num_X+1]))
            data_W.append(int(content[Num_X+Num_Y+1]))
            data_id.append(content[Num_X+Num_Y+Num_W+1])
    return data_X, data_Y, data_W, data_id

load_data(path, filename)