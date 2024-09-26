#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 16:22:42 2024

@author: sscc
"""

print("Is is raining?")
answer = input().lower()
if answer == "yes":
    print("Is it windy?")
    answer2 = input().lower()
    if answer2 == "yes":
        print("It's too windy for an umbrella.")
    else:
        print("Take an umbrella.")
else:
    print("Enjoy your day.")        