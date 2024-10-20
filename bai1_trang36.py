# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 18:29:38 2024

@author: MINH NHUT
"""

def tinh_tong(*args):
    return sum(args)
def tinh_tich(*args):

    r = 1
    for i in args:
       r *= i
    return r

if __name__ == "__main__":
    ds = [1,2,3,4,5]
    
    print(tinh_tong(*ds))
    print(tinh_tich(*ds))