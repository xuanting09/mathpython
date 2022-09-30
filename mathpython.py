import numpy as np
import matplotlib.pyplot as plt
xis=[]
yls=[]
for i in range(0,11):
    x1=int(input('x='))
    xis.append(x1)
    x2=1-x1**4
    yls.append(x2)
print(yls)
x= np.array(xis)
y = np.array(yls)
y0 = np.array([ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
x0 = np.array([ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
plt.plot( x, y, color='lightgray')
plt.plot( x0, y0, color='lightgray')
plt.plot( x, y )
plt.show()
