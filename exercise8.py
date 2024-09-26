#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 16:36:59 2024

@author: sscc
"""

print("input a letter:")
letter = input().lower()
if letter == "a" and "e" and "i" and "o" and "u":
    print("it's a vowel.")
elif letter == "y":
    print("sometimes it is a vowel and sometimes it is a consonant.")
else:
    print("it is a consonant.")