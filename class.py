# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 10:06:08 2024

@author: DELL
"""

class car:
    def __init__(self,name,model,year):
        self.nm=name
        self.mm=model
        self.yr=year


nm=input("enter the name of car")
mm=input("enter the model of car")
yr=input("enter theyear model")

c1=car(nm,mm,yr)
print(c1.nm,c1.mm,c1.yr)
print(type(c1))