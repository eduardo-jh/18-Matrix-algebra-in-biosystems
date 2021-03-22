#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BE523 Biosystems Analysis & Design
HW18 - Question 3. Restaurant problem

Created on Sun Mar 21 03:53:39 2021
@author: eduardo
"""
import numpy as np
from scipy import linalg

# Concentration of CO, product of combustion in a urban environment
A = np.array([[225,   0,  -25],
              [  0, 175, -125],
              [225,  25, -250]])
b = np.array([1400, 100, 0])
x = linalg.solve(A, b)
print(x)

print("The concentrations C1={0:.2f} C2={1:.2f} C3={2:.2f}".format(x[0], x[1], x[2]))