## Problem Statement : 
    Form a 3D Scatter Plot following the given data by importing the necessary Python libraries.

## 3D Scatter Plot :
Creating a three-dimensional scatter plot of data is a useful way to visualize the relationships between three variables simultaneously. To create such a plot, you'll typically need software that supports 3D plotting, such as Python with libraries like Matplotlib or 3D-capable software like MATLAB.

## Algorithm :
1. We import the necessary libraries, including Matplotlib and its 3D toolkit.
2. We define sample data for the X, Y, and Z axes.
3. We create a 3D scatter plot using fig.add_subplot(111, projection='3d').
4. We use ax.scatter() to create the scatter plot, passing in the X, Y, and Z data. Customize the marker style and color as needed.
5. We set labels for the X, Y, and Z axes using ax.set_xlabel(), ax.set_ylabel(), and ax.set_zlabel().
6. Finally, we display the plot using plt.show().
