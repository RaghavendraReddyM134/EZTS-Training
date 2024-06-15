# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 13:54:38 2024

@author: DELL
probleam:-no of questions solved in a given tym 
"""

def no_of_que(min):
    i=1
    tym=0
    ques=0
    while(tym<=min):
        tym+=5*i
        ques+=1
        i+=1
    return ques        
     
    
start=int(input("enter the tym in hrs:-"))

min=(start*60)
print(no_of_que(min))