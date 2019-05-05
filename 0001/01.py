# coding=utf-8
import random

def generatingKey(num = 0):
    key = ''
    for j in range(0, num):
        for i in range(0, 4):
            a = random.randint(0, 35)
            if a < 10:
                a = a + 48
            else:
                a = a + 55
            if chr(a) == 48: # 0 != O
                a = 79
            key = key + chr(a)
        if j is not num-1:
           key = key + '-'
    return key

for i in range(0, 200):
    key = generatingKey(8)
    print(key)
