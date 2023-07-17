import matplotlib.pyplot as plt
import numpy as np
list=[1,3,20,56]
print(list)
vtr1=np.array(list)
print(vtr1)
list2=[[12],[40],[6],[10]]
print(list2)
list3=[10,20,30,40,50]
list4=[5,2,4,3,1]
vtr3=np.array(list3)
vtr4=np.array(list4)
print("we create vector from list3 ",vtr3)
print("we create vector from list4 ",vtr4)
vtr_add=vtr3+vtr4
print("SUM OF TWO VECTORS =" ,vtr_add)
vtr_sub=vtr3-vtr4
print("SUBTRACTION OF TWO VECTORS =" ,vtr_sub)
vtr_mul=vtr3*vtr4
print("MULTIPLICATION OF TWO VECTORS",vtr_mul)
vtr_dproduct=vtr3.dot(vtr4)
print("MULTIPLICATION OF TWO VECTORS",vtr_dproduct)
scl_mult=6+vtr3
print("Scalar multipilication ",scl_mult)
v1=[5,6]
v2=[3,2]
start=[0,0]
fig,ax=plt.subplots(figsize=(3,3))
ax.quiver(start[0],start[1],v1[0],v2[1],color='r')
plt.show()
fig=plt.figure()
ax=plt.axes(projection='3d')
ax.set