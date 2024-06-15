# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 10:33:47 2024

@author: DELL
"""

m=int(input())
a=0
b=1
for i in range(2,m+1):
    print(a)
    print(b)
    temp=a
    c=a+b
    a=b
    b=c
    print(c,end=" ")    