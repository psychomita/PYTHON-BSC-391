import numpy as np 
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D 
# Given data 
Y = np.array([293, 230, 172, 91, 113, 125]) 
x1 = np.array([1.6, 15.5, 22.0, 43.0, 33.0, 40.0]) 
x2 = np.array([851, 816, 1058, 1201, 1357, 1115]) 
# Create a 3D scatter plot 
fig = plt.figure() 
ax = fig.add_subplot(111, projection='3d') 
# Plot the data points 
ax.scatter(x1, x2, Y, c='b', marker='o', label='Data Points') 
# Set labels for the axes 
ax.set_xlabel('Oil Viscosity (x1)') 
ax.set_ylabel('Load (x2)') 
ax.set_zlabel('Bearing Wear (Y)') 
# Set title and legend 
plt.title('Multiple Linear Regression - 3D Scatter Plot') 
ax.legend() 
# Show the plot 
plt.show()
