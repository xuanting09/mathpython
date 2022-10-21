import matplotlib.pyplot as plt
import numpy as np

 #Creating vectors X and Y
x = np.linspace(-2,2,100)
y = x ** 2

fig = plt.figure(figsize = (12, 7))

 #Add a title
plt.title('Equation plot')

 #Add X and y Label
plt.xlabel('x axis')
plt.ylabel('y axis')

 #Create the plot
plt.plot(x, y, label ='Y = X^2',
    color ='red', linewidth = 1)

plt.plot(x, 6 * y, label ='Y = 6 * X^2',
    color ='yellow', linewidth = 1)

 #Add a grid
plt.grid(linestyle ='-')

 #Add a Legend
plt.legend()

 #Show the plot
plt.show()