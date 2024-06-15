# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 19:33:38 2024

@author: DELL
"""
def rolldice1(d1,ts1,i):
    if ts1%2==0 and d[i]%2!=0:
        ts1+=1
    return ts1

def rolldice(d,n,ts1):
    
    for i in range(0,n):
        if ts1%2==0 and d[i]%2!=0:
            ts1+=rolldice1(d[i+1],ts1,i)
        elif ts1%2==0 and d[i]%2==0:
            ts1+=1
        elif ts1%2!=0 and d[i]%2!=0:
            ts1-=d[i]
    return ts1


d=list(map(int,input().split()))
n=len(d)
ts1=0
print(rolldice(d,n,ts1))

