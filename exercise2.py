#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 15:49:47 2024

@author: sscc
"""

print("Please input the first line of your favorite song:")
line = input()
print("the length of your line is:", len(line))
print("choose a starting and ending number:")
starting = int(input())-1
ending = int(input())-1
print(line[starting:ending])