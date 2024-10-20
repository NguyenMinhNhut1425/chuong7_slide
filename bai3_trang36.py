# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 19:04:43 2024

@author: MINH NHUT
"""

import math
def chuvi_dt(hinh, pheptinh, *args, **kwargs):
    if hinh == 'vuong':
        canh = args[0]
        return 4* canh if pheptinh == 'chuvi' else canh**2
    
    elif hinh == 'chunhat':
        dai = args[0]
        rong = args[1]
        return 2 * (dai + rong) if pheptinh == 'chuvi' else dai*rong
    
    elif hinh == 'tron':
        bk = args[0]
        return 2*math.pi * bk if pheptinh == 'chuvi' else math.pi* bk**2
    
    else:
        return 'Hinh khong hop le'
if __name__ == "__main__":
    print('chu vi hinh vuong:', chuvi_dt('vuong', 'chuvi', 3))
    print('chu vi hinh vuong:', chuvi_dt('vuong', 'dientich', 3))

    print('chu vi hinh chu nhat:', chuvi_dt('chunhat', 'chuvi',3, 4))
    print('chu vi hinh chu nhat:', chuvi_dt('chunhat', 'dientich', 3, 4))

    print('chu vi hinh tron:', chuvi_dt('tron', 'chuvi',3))
    print('chu vi hinh tron:', chuvi_dt('tron', 'dientich', 3))