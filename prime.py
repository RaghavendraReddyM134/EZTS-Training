# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 10:15:00 2024

@author: DELL
"""

m=int(input())
flag=0
if m<=1:
    flag=1
else:
    flag=0
for i in range(2,(m//2)+1):
    if m%i==0:
        flag=1
        break
if flag==0:
    print("valid feedback")
else:
    print("invalid feedback")