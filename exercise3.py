#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 16:02:41 2024

@author: sscc
"""

print("Please enter your name:")
name = input()
if len(name)<5:
    print("enter your surname")
    surname = input()
    fullname = name + surname
    print(fullname.lower())
else:
    print(name.lower())