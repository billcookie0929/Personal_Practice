#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/21 12:05
# @Author  : Yupeng Cui  
# @File    : If_else.py

n = int(input())
if n%2!=0:
    print("Weird")
elif 2<=n<=5:
    print("Not Weird")
elif 6<=n<=20:
    print("Weird")
elif n>=20:
    print("Weird")