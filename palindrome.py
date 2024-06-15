# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 10:46:03 2024

@author: DELL
"""
m=int(input("enter the number of digit:-"))
n=int(input())
temp=n
rev=0
for i in range(m):
    rem=n%10
    rev=(rev*10)+rem
    n=n//10
if rev==temp:
    print("palindrome sequence")
else:
    print("not a palindrom sequence")
        