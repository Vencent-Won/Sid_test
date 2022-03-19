#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@author: Vencent_Wang
@contact: Vencent_Wang@outlook.com
@file: main.py
@time: 2022/3/19 19:05
@desc:
'''
#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@author: Vencent_Wang
@contact: Vencent_Wang@outlook.com
@file: config.py
@time: 2022/3/19 19:05
@desc:
'''
import argparse

def arg_parse():
    parser = argparse.ArgumentParser(description='GraphPool arguments.')

    parser.add_argument('--datadir', dest='datadir')
    parser.add_argument('--dataname', dest='dataname')
    parser.add_argument('--model', type=str, dest='model')
    parser.add_argument('--seed', type=int, dest='seed')
    parser.add_argument('--iters', type=int, default='5')
    parser.set_defaults(datadir='data',
                        dataname='sid_train_data',
                        model="RF",
                        iters=5,
                        seed=200,)
    return parser.parse_args()
