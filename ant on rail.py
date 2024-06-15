# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 22:03:30 2024

@author: DELL


@ant on rail
"""
def AonRail(n,arr):
    count=0
    for i in range(n-1):
        if arr[i]==1 and arr[i+1]==-1:
            count+=1
    return count


n=int(input())
arr=list(map(int,input().split()))
print(AonRail(n, arr))