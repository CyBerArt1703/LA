#code for solving nxn system of linear eqns by
#Guass Elimination Method
import numpy as np
a=eval(input("input the size of coefficient matrix"))
r=1
matrix=[]
vector=[]
for i in range(a):
    c=1
    row=[]
    for i in range(a):
        print("enter value of row", r, "column", c)
        x = eval(input())
        row.append(x)
        c += 1
    matrix.append(row)
    x = eval(input("please enter constant of equation, "))
    vector.append(x)
    r += 1
m=np.asarray(matrix)
v1=np.asarray(vector)
print("Your square matrix=\n",m)
print("Your square vector=\n",v1)
aug=np.copy(m)
new_v1=[]
for i in v1:
    new_v1.append([i])
new_v1=np.asarray(new_v1)
print("Your column vector=\n",new_v1)
aug=np.append(aug,new_v1,axis=1)      #axis=1 is used to add a column, axis=2 is used to add a column
print("Your final augmented matrix=\n",aug)
#scalar multiplication
def slr(mat,s1):
    return mat*s1
def row_add(mat,vect,rownum):
    mat[rownum]=mat[rownum]+vect
    return mat
for i in range(0,a):
    for j in range(i+1,a):
        ratio=aug[j][i]/aug[i][i]
        mul_result=slr(aug[i],ratio)
        print("Multiplication result= ",mul_result)
        aug=row_add(aug,-mul_result,j)
        print("Your augmented  result=\n ", aug)
ans=np.zeros(a)     #it places a zeros in ans,a number of zeros
ans[a-1]=aug[a-1][a]/aug[a-1][a-1]
for i in range(a-2,-1,-1):
    ans[i]=aug[i][a]
    for j in range(i+1,a):
        ans[i]=ans[i]-aug[i][j]*ans[j]
    ans[i]=ans[i]/aug[i][i]
for i in range(len(ans)):
    print("Value of x[", i + 1, "]=", np.round(ans[i], 2,end='\t'))
