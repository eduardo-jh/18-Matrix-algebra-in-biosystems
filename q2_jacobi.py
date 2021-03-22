#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BE523 Biosystems Analysis & Design
HW18 - Question 2. Jacobi method to solve x = A⁻¹*b

Created on Sun Mar 21 02:52:49 2021
@author: eduardo
"""
import numpy as np

def jacobi(A, b, N=25, x=None):
    """ Solves the equation Ax=b via the Jacobi iterative method, max iterations approach
    A: array, the matrix
    b: array, the vector
    N: int, max iterations
    x: array, initial iteration for x"""
    # Create an initial guess if needed
    if x is None:
        x = np.zeros(len(A[0]))
    # Create a vector of the diagonal elements of A and substract them from A
    D = np.diag(A)
    R = A - np.diagflat(D)
    
    # Iterate for N times
    for i in range(N):
        x = (b - np.dot(R, x)) / D
    return x

def jacobi_conv(A, b, maxiter=25, tol=1e-3, x=None):
    """ Solves the equation Ax=b via the Jacobi iterative method, tolerance approach
    A: array, the matrix
    b: array, the vector
    maxiter: int, max iterations
    tol: float, max tolerance
    x: array, initial iteration for x"""
    # Create an initial guess if needed
    if x is None:
        x = np.zeros(len(A[0]))
    # Create a vector of the diagonal elements of A and substract them from A
    D = np.diag(A)
    R = A - np.diagflat(D)
    
    x_prev = x + 2*tol  # Use 2*tol to make sure it is greater than tol
    diff = abs(max(x-x_prev))  # The max value of the array of differences
    iters = 0
    while diff > tol and  iters < maxiter:
        iters += 1
        x_prev = x
        x = (b - np.dot(R, x)) / D
        diff = abs(max(x-x_prev))
        # print(iters, x, diff, (x-x_prev))
    return x

A = np.array([[2, 1],
              [5, 7]])
b = np.array([11, 13])
guess = np.array([1, 1])

print("Using the max iterations approach")
x = jacobi(A, b, 25, guess)
print("A :")
print(A)
print("b :", b)
print("x :", x)

print("Using the convergence approach")
x = jacobi_conv(A, b, 25, 1e-3, guess)
print("A :")
print(A)
print("b :", b)
print("x :", x)
