#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/11 18:00
# @Author  : Yupeng Cui  
# @File    : Write_a_function.py
def is_leap(year):
    leap = False
    if year % 4 == 0 and year % 100 != 0:
        leap = True
    if year % 400 == 0:
        leap = True
    return leap

year = eval(input())
print(is_leap(year))