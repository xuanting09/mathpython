import matplotlib.pyplot as plt
import numpy as np

# Creating vectors X and Y
x = np.linspace(-np.pi,np.pi,201)
y = np.sin(x)

fig = plt.figure(figsize = (12, 7))

# Add a title
plt.title('Equation plot')

# Add X and y Label
plt.xlabel('x axis')
plt.ylabel('y axis')

# Create the plot
plt.plot(x,np.sin(x),
    color ='blue', linewidth = 1)
s
plt.plot(x, np.cos(x),
    color ='red', linewidth = 1)

# Add a grid
plt.grid(linestyle ='-')

# Add a Legend
plt.legend()

# Show the plot
plt.show()
