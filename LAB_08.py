# Making L&U Decomposition of any nXn System of Linear Equation/Square Matrix:-
import numpy as np
a = eval(input("Enter size of the Co-efficient Matrix:"))
r = 1
matrix = [] # LIST sari rows store hongi

for i in range(a):
    c = 1
    row = []
    for i in range(a):
        print("Enter valur of row",r,"column",c)
        x = eval(input())
        row.append(x)
        c = c+1
    matrix.append(row)

    r = r+1
m = np.asarray(matrix)
print("Co-efficient Matrix",m)
print("Size of Matrix",m.shape)

################################################################

def row_interchange(mat,row1,row2):
    t1 = mat[row1].copy()
    t2 = mat[row2].copy()
    mat[row1] = t2
    mat[row2] = t1
    return mat
################################################################

def scalar_multiply(mat,scalar):
    return mat*scalar
################################################################

def row_addition(mat,vect,rownum):
    mat[rownum] = mat[rownum]+vect
    return mat

################################################################

L = np.eye(a)
U = []
for i in range(0,a):
    for j in range(i+1,a):
        if m[i][i] == 0:
            m = row_interchange(m,i,i+1)
        else:
            ratio = m[j][i] / m[i][i]
            L[j][i] = np.round(ratio, 2)
            mul_result = scalar_multiply(m[i], np.round(ratio, 2))  # row1 *
            print("Mul result", mul_result)
            U = row_addition(m, -mul_result, j)
            print("My new Upper Matrix is=\n", U)
            print("My new Lower Matrix is=\n", L)
mul = np.dot(L, U)
print("LxU=\n", mul)

################################################################
