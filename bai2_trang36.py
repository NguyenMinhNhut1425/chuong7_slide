# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 18:43:13 2024

@author: MINH NHUT
"""
import math
def chuvi(hinh, *args, **kwargs):
    if hinh == 'vuong':
        canh = args[0]
        return 4* canh
    elif hinh == 'chunhat':
        dai = args[0]
        rong = args[1]
        return 2 * (dai + rong)
    elif hinh == 'tron':
        bk = args[0]
        return 2*math.pi * bk
    else:
        return 'Hinh khong hop le'
if __name__ == "__main__":
    print('chu vi hinh vuong:', chuvi('vuong', 3))
    print('chu vi hinh chu nhat:', chuvi('chunhat', 3, 4))
    print('chu vi hinh tron:', chuvi('tron', 3))    