# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 18:19:19 2024

@author: MINH NHUT
"""
#bai 1 - slide 49
#a
def can_bac(x,n):
    return x ** (1/n)

#b
def binh_phuong(n):
    if n > 0:
        return n**2
    else:
        return "Nhập vào số dương"
    
#c
def kiem_tra(n):
    return n < 0 and n % 2 ==0

#d
def ktr_so(x):
    if x < 0 and x % 2 !=0:
        return -1
    elif x > 0 and x % 2 == 0:
        return 1
    return 0

#e
def ktra_gtri():
    gtri = input("Nhập giá trị: ")
    if gtri.replace('.', '', 1).replace('-', '',1).isdigit():
        gtri = float(gtri)
    if -89 <= gtri <= 90:
        return gtri
    print("Không hợp lệ nhập lại")
    return ktra_gtri()

if __name__=="__main__":
    print(can_bac(8, 3))
    print(binh_phuong(4))
    print(kiem_tra(-4))
    print(ktr_so(-3))
    print(ktra_gtri())
        