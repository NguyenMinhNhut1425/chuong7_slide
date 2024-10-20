# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 19:51:21 2024

@author: MINH NHUT
"""
#Bai 3 - slide
import random
#1
def tao_seqA():
    n = random.randint(30,80)
    seqA = []
    for i in range(n+1):
        if random.randint(0, 1) == 0:
            seqA.append(round(random.uniform(-79, 39), 2))
        else:
            seqA.append(random.randint(-79, 39))
    return seqA

#2
def kt_kieudulieu(seqA):
    return [type(i).__name__ for i in seqA]

#3
def thong_ke(seqA):
    return len(seqA)

#4
def sapxep_seqB(seqA):
    return sorted(seqA)

#5
def trung_binh(seqA):
    return sum(seqA)/len(seqA) if seqA else 0

#6
def trung_binh_seqB(seqB):
    x = len(seqB)
    return (seqB[x//2 -1] + seqB[x//2]) //2 if x % 2 == 0 else seqB[(x-1) // 2]

#7
def khoangcach_maxmin(seq):
    return max(seq) - min(seq)
    
#8
def sosanh(seqA, seqB):   
    return trung_binh(seqA),trung_binh_seqB(seqB), trung_binh(seqA)==trung_binh_seqB(seqB)

if __name__ == "__main__":
    seqA = tao_seqA()
    print(seqA)
    print(kt_kieudulieu(seqA))
    print(thong_ke(seqA))
    print(trung_binh(seqA))
    seqB = sapxep_seqB(seqA)
    print(seqB)
    print(sapxep_seqB(seqA))
    print(trung_binh_seqB(seqB))
    print(khoangcach_maxmin(seqA))
    print(khoangcach_maxmin(seqB))
    trung_binh(seqA), trung_binh_seqB(seqB)
    sosanhAB = sosanh(seqA, seqB)
    print(sosanhAB)
