import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(-18,10,50)
x1=np.arange(2,20,.2)
y=x**3
y1=np.cos(x1)
print(x,y)
import matplotlib.pyplot
#plt.plot(x,y,'bo')
#plt.show()
#plt.plot(x,y,'ro--')
#plt.show()
#plt.plot(x,y,'v-')
#plt.show()
#plt.plot(x,y,'H-',markersize=25.5)
#plt.show()
#plt.plot(x,y,'k-',linewidth=6,markersize=25.5)
#plt.show()
plt.plot(x,y,x1,y1,'*-',linewidth=4,markersize=15.5,color='k')
plt.show()
plt.title('plot of cube function')
plt.xlabel("x-axis")
plt.ylabel("y-axis")
x=
