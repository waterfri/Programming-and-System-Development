#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 16:07:27 2024

@author: sscc
"""

print("input a word:")
word = input()
if word[0] != "a" and word[0] != "e" and word[0] != "i" and word[0] != "o" and word[0] != "u":
    new_word = word[1:] + word[0] + "ay"
else:
    new_word = word + "way"
print(new_word)