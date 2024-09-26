#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 16:28:58 2024

@author: sscc
"""

print("What's your age?")
age = int(input())
if age >= 18:
    print("you can vote")
elif age == 17:
    print("you can learn how to drive")
elif age == 16:
    print("you can by a lottery ticket")
else:
    print("you can go trick-or-treating")
    