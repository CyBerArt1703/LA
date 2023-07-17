import numpy as np
size=eval(input("PLEASE ENTER SIZE OF SQUARE COFFICIENT MATRIX"))
r=1

matrix=[]
vector=[]

for i in range(size):
    column=1
    row=[]
    for i in range(size):
        print("ENTER VALUE OF ROW ", row, " COLUMN ", column)
        value = eval(input("ENTER VALUE"))
        row.append(value)
        column=column+1
    matrix.append(row)
    print("ENTER CONSTANT VALUR OF EQUATION ",r)
    value2= eval(input("ENTER VALUE"))
    vector.append(value2)
    r=r+1
m=np.array(matrix)
v1=np.array(vector)
print("Your Square Matrix=\n",m)
print("Your Constant Vector=\n",v1)

#Convert in to Column
aug=np.copy(m)
new_v1=[]

for i in v1:
    new_v1.append([i])

new_v1=np.asarray(new_v1)
print("your column vector = \n" ,new_v1)
aug=np.append(aug,new_v1,axis=1)
print("your final augumented matrix = \n",aug)

#scalar multiplication

def scalar_multiplication(mat,s1):#s1=number
    return mat*s1

#addition of two rows

def row_addition(mat,vect,rownum):#vector,row number
    mat[rownum]=mat[rownum]+vect
    return mat

for i in range(0,size):
    for j in range(i+1,size):
        ratio=aug[j][i]/aug[i][j]
        mul_result=scalar_multiplication(aug[i],ratio)
        print("multiplication result\n",mul_result)
        aug=row_addition(aug,-mul_result,j)
        print("augmented matrix  result\n", aug)
ans1=np.zeros(size)
ans1[size-1]=aug[size-1][size]/aug[size-1][size-1]

for i in range(size-2,-1,-1):
    ans1[i]=aug[i][size]
    for j in range (i+1,size):
        ans1[i]=ans1[i]-aug[i][j]*ans1[j]
    ans1[i]=ans1[i]/aug[i][i]

for i in range(len(ans1)):
    print(" Value of x[", i + 1, "]=",np.round(ans1[i],2),end='\n')