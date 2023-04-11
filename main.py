# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 14:02:41 2023

@author: gbuch
"""


import random
from itertools import combinations
from tqdm import tqdm


# list of given numbers and the answer
list_numbers = '[5, 6, 9, 11, 20, 25]'
answer = 546

# list of possible operations with and without division (in case the second number is 0)
list_opers = ['+', '-', '*', '/']
list_opers2 = ['+', '-', '*']


def reduce(x, hist):
    ret = dict()
    
    l = len(eval(x))
    for i in combinations(range(l), 2):
        x_temp = eval(x).copy()
        x_temp[i[0]], x_temp[-1] = x_temp[-1], x_temp[i[0]]
        n_1 = x_temp.pop()
        x_temp[i[1]-1], x_temp[-1] = x_temp[-1], x_temp[i[1]-1]
        n_2 = x_temp.pop()
        
        for o in list_opers:
            flag = True
            if o in {'+', '*'}:
                oper_new = str(n_1) + o + str(n_2)
                n_new = eval(oper_new)
            elif o =='-':
                oper_new = str(max(n_1,n_2)) + o + str(min(n_1,n_2))
                n_new = eval(oper_new)
            elif o == '/':
                if min(n_1,n_2)==0:
                    oper_new = str(min(n_1,n_2)) + o + str(max(n_1,n_2))
                    n_new = 0
                else:
                    oper_new = str(max(n_1,n_2)) + o + str(min(n_1,n_2))
                    n_new = eval(oper_new)
                    if n_new != int(n_new):
                        flag = False
            if flag:
                ret[str(sorted(x_temp+[n_new]))] = hist+[oper_new]
    return ret


record = {list_numbers: []}
for i in range(len(eval(list_numbers))):
    print(i)
    r = record.copy()
    for j in tqdm(r):
        record.update(reduce(j, record[j]))
    
    
ans = []
for r in record.keys():
    if answer in eval(r):
        ans += [r, record[r]]
for a in ans:
    print(a)

