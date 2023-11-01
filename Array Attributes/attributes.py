import numpy as np
rows=4
cols=2
user_input=[]


for i in range(rows):
    row=[]
    for j in range(cols):
        value=float(input("Enter the value for row "+ str(i+1)+" and column " +str(j+1)+ " : "))
        row.append(value)
    user_input.append(row)
my_array=np.array(user_input)
print(my_array)
print("The shape of the array : ", my_array.shape)
print("Dimension of the array : ", my_array.ndim)

