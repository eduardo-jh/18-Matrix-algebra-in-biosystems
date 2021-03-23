#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
E523 Biosystems Analysis & Design
HW18 - Question 4. Dunn problem for glucose consumption

Created on Tue Mar 23 00:11:50 2021
@author: eduardo
"""
import numpy as np
from scipy import linalg

RQ = 1  # Respiratory quotient CO2/O2
A = np.array([[RQ,     0,   6,  0],
              [0,      3, -10, -2],
              [2-2*RQ, 0,   3, -1],
              [0,     -1,   1,  0]])
b = np.array([2, -6, -1, 0])
x = linalg.solve(A, b)
print(x)

print("The concentrations a={0:.3f} b={1:.3f} c={2:.3f} d={3:.3f}".format(x[0], x[1], x[2], x[3]))