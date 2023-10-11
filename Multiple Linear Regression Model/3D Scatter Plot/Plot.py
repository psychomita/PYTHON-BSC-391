import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#Feeding data from .csv file
df=pd.read_csv(r"C:\Users\suchi\OneDrive\Desktop\Plot\table.csv") #implement the data in a .csv file and paste your own file path here
print(df)

#Creating a 3D Scatter Plot
fig= plt.figure()
ax=fig.add_subplot(111,projection='3d')

#Marking axes
x=df['x1'].values
y=df['x2'].values
z=df['Y'].values
a=ax.set_xlabel('Oil Viscocity (x1)',linespacing=3.2)
b=ax.set_ylabel('Load (x2)',linespacing=3.1)
d=ax.set_zlabel('Bearing of Wear (Y)',linespacing=3.1)
ax.scatter(x, y, z, c='b', marker='o', label='Data Points')

#Setting title and legend
ax.set_title('Multiple Linear Regression- 3D Scatter Plot')
ax.legend()

#Showing the plot
plt.show()
