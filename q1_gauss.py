#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BE523 Biosystems Analysis & Design
HW18 - Question 1. Gauss elimination to solve x = A⁻¹*b

Created on Sun Mar 21 01:31:25 2021
@author: eduardo
"""
import numpy as np
from scipy import linalg

def myGauss(m):
    """ A Gauss elimination function to solve x = A⁻¹*b
    m: array, the matrix to solve
    return: array, the solution x
    """
    # Eliminate columns
    for col in range(len(m[0])):
        for row in range(col+1, len(m)):
            r = [(rowValue * (-(m[row][col] / m[col][col]))) for rowValue in m[col]]
            m[row] = [sum(pair) for pair in zip(m[row], r)]
    # Now backsolve the substitution
    ans = []
    m.reverse()
    for sol in range(len(m)):
        if sol == 0:
            ans.append(m[sol][-1]/m[sol][-2])
        else:
            inner = 0
            # Substitute in all known coefficients
            for x in range(sol):
                inner += (ans[x]*m[sol][-2-x])
            # The equation is now reduced to a ax+b=c form
            # solve with (c-b)/a
            ans.append((m[sol][-1]-inner)/m[sol][-sol-2])
    ans.reverse()
    return ans

# Using A*x = b, then M = [A b]]
M = [[2, 1, -1, 7],
      [2, 6, 5, 0],
      [3, 1, 1, 5]]
x = myGauss(M)
print("Solution:")
print("x =", x)

# Comprobation using A*x = b
A = np.array([[2, 1, -1],
              [2, 6, 5],
              [3, 1, 1]])
b = A.dot(x)
print("Comprobation:")
print("b =", b)
