#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
E523 Biosystems Analysis & Design
HW18 - Question 4. Dunn problem for glucose consumption

Input
* Glucose, Methanol and Hexadecane are inputs for cell culture
* Cell composition: 47% C, 6.5% H, 31% O, 10%, N... 5.5% ash
* O2 and NH4 --> Biomass, CO2, H2O
* Air: 21% O2, 79% N2

Output:
* Substrate  %N2   %CO2    %O2
  glucose   78.8   10.2   11.0
Calculate yield coefficients
1. Convert cell composition by mass to fractions of moles in molecular formula
2. Find formula of glucose and add other nutrients
3. Calculate RQ
C6H12O6 + O2 + N2 --> C,H,O,N + N2 + CO2 + O2 + H2O

T = total atomic weight, find the number of C,H,O,N using their atomic numbers
x=number of C molecules, x*12/T = C = 0.47     x = 0.47/12*T
y=number of H molecules, y*1/T  = H = 0.065    y = 0.065/1*T
z=number of O molecules, z*16/T = O = 0.31     z = 0.31/16*T
w=number of N molecules, w*14/T = N = 0.1      w = 0.1/14*T

A*x = b is:
12*x + 0*y + 0*z + 0*w = 0.47 *T
 0*x + 1*y + 0*z + 0*w = 0.065*T
 0*x + 0*y +16*z + 0*w = 0.31 *T
 0*x + 0*y + 0*z +14*w = 0.1  *T
 1*x + 1*y + 1*z + 1*w = 1*T

Created on Tue Mar 23 00:11:50 2021
@author: eduardo
"""
import numpy as np
from scipy import linalg

A = np.array([[12.011, 0, 0, 0],
              [0, 1.008, 0, 0],
              [0, 0, 15.999, 0],
              [0, 0, 0, 14.007]])
b = np.array([0.47, 0.065, 0.31, 0.1])
x = linalg.solve(A, b)
print(x)  # This are proportions of each C,H,O,N 
x_atoms = (x / x[1])*10  # calculte number of atoms making H an integer to get a reasonable number
print(x_atoms)

print("The number of atoms:")
print("    C={0:-8.2f}".format(x_atoms[0]))
print("    H={0:-8.2f}".format(x_atoms[1]))
print("    O={0:-8.2f}".format(x_atoms[2]))
print("    N={0:-8.2f}".format(x_atoms[3]))
print("Total={0:-8.2f}".format(sum(x_atoms)))

"""
Based on the number of atoms, the biomass is: C6H10O3N1, thus
C6H12O6 + O2 + N2 --> C6H10O3N1 + N2 + CO2 + O2 + H2O
Use coefficients (a, b, c, d, e) to count atoms:
C6H12O6 + a*O2 + b*N2 --> c*C6H10O3N1 + d*H2O + e*CO2
C: 6 = 6c + e
H:12 = 10c + 2d
O: 6 + 2a = 3c + d + 2e
N: 2b = c
RQ = CO2_out/(O2_out - O2_in) = 10.2/(21-10) = 1.02 = e/a, respiratory quotient

   0*a + 0*b + 6*c + 0*d + 1*e = 6
   0*a + 0*b +10*c + 2*d + 0*e = 12
   2*a + 0*b + 3*c + 1*d + 2*e = 6
   0*a + 2*b + 1*c + 0*d + 0*e = 0
1.02*a + 0*b + 0*c + 0*d + 1*e = 0
"""
RQ = 1.02
A = np.array([[0, 0, 6, 0, 1],
              [0, 0, 10, 2, 0],
              [2, 0, 3, 1, 2],
              [0, 2, 1, 0, 0],
              [RQ,0, 0, 0, 1]])
b = np.array([6, 12, 6, 0, 0])
x = linalg.solve(A, b)
print(x)
factor = 19  # Multiply by factor to get reasonable number
x_moles = x * factor

print("Moles of (negatives are reactants):")
print("Glucose ={0:-8.2f}".format(factor))
print("O2      ={0:-8.2f}".format(x_moles[0]))
print("N2      ={0:-8.2f}".format(x_moles[1]))
print("Cells   ={0:-8.2f}".format(x_moles[2]))
print("H2O     ={0:-8.2f}".format(x_moles[3]))
print("CO2     ={0:-8.2f}".format(x_moles[4]))

# RQ = 1  # Respiratory quotient CO2/O2
# A = np.array([[RQ,     0,   6,  0],
#               [0,      3, -10, -2],
#               [2-2*RQ, 0,   3, -1],
#               [0,     -1,   1,  0]])
# b = np.array([2, -6, -1, 0])
# x = linalg.solve(A, b)
# print(x)

# print("The concentrations a={0:.3f} b={1:.3f} c={2:.3f} d={3:.3f}".format(x[0], x[1], x[2], x[3]))