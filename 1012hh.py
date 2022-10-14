from cProfile import label
from re import A
import matplotlib.pyplot as plt
import numpy as np

# Creating vectors X and Y
x = np.linspace(-2*np.pi,2*np.pi,200)
a = np.sin(x)
b = np.cos(x)
c = 1/a
d = 1/b

# Create the plot
plt.plot(x,c,color ='blue', linewidth = 1)

plt.plot(x,d,color ='red', linewidth = 1)

plt.xlim(x.min()*1.1,x.max()*1.1)
plt.ylim(-4,4)


# Show the plot
plt.show()
