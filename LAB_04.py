import numpy as np
# a=eval(input("GIVE ME YOUR FAVOURITE NUMBER :"))
# print(a)
# i=1
# while i<=a:
#     print(i,"MY NAME IS HAHAHHAHA")
#     i=i+1
#
# m1=np.asarray([[2,4],[1,4]])
# print(m1)
# m2=np.transpose(m1)
# print("TRANSPOSE OF MATRIX :",m2)
# s1=np.linalg.det(m1)
# print("DETREMINANT OF MATRIX =",s1)
# m3=np.linalg.inv(m1)
# print("DETERMINANT OF MATRIX IS :",m3)
# m4=np.linalg.inv(m1)
# print("INVERSE OF MATRIX =",m4)
# v1=np.dot(m1,m4)
# print("MULTIPLICATION OF TWO MATRIX IS =",v1)
n=eval(input("GIVE ME THE SIZE OF THE SQUARE CO-EFFICIENT "))
r=1
Matrix=[]
while r<=n:
    c=1
    row=[]
    while c<=n:
        print("ENTER VALUES OF ROWS ",r,"Column",c)
        x=eval(input(""))
        row.append(x)
        c=c+1
    Matrix.append(row)
    r=r+1
m=np.asarray(Matrix)
print("CO-EFFICEINT MATRIX =",m)
n1=np.linalg.det(m)
print("DETERMINANT OF THE MATRIX IS = ",n1)
m5=np.linalg.inv(m)
print("INVERSE OF YOUR MATRIX IS  =",m5)
vtr1=[]
c=1
while c<=n:
    print("ENTER CONSTANT OF EQUATION ",c)
    x=eval(input())
    vtr1.append(x)
    c=c+1
vtr2=np.asarray(vtr1)
ans=np.dot(m5,vtr2)
for i in range(len(ans)):
    print("value of x[",i+1,"]=","{:.2f)".format(ans[i]))