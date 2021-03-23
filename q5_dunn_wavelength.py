#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
E523 Biosystems Analysis & Design
HW18 - Question 5. Dunn problem for wavelength

Created on Tue Mar 23 00:16:29 2021
@author: eduardo
"""
import numpy as np
from scipy import linalg

# 'A' is the matrix of epsilon sums
A = np.array([[11300, 8150, 4500, 4000],
              [ 5000, 7500, 3650, 4200],
              [ 1900, 3900, 3000, 4800],
              [ 1500, 1400, 2000, 4850]])
# 'b' is the vector of absorvance, denoted as 'Ai' in the slides
b = np.array([0.6320, 0.5345, 0.3310, 0.1960])
# Find 'x', the concentration of the components of the solutions C(k)
x = linalg.solve(A, b)
print(x)

print("The concentrations:")
print("C240={0:.4g} C250={1:.4g} C260={2:.4g} C280={3:.4g}".format(x[0], x[1], x[2], x[3]))