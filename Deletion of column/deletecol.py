import numpy as np
rows=int(input("Enter the number of rows : "))
cols=int(input("Enter the number of columns : "))
user_input=[]
newcol=[]

print("Enter input for the array : ")
for i in range(rows):
    row=[]
    for j in range(cols):
        value=int(input("Enter the value for row "+ str(i+1)+" and column " +str(j+1)+ " : "))
        row.append(value)
    user_input.append(row)
my_array=np.array(user_input)

print("Enter the new column : ")
for i in range(cols):
        value=int(input("Enter the value for row "+ str(i+1)+" and column 2 : "))
        newcol.append(value)

print("Original Array : ")
print(my_array)

my_array=np.delete(my_array,1, axis=1)


my_array=np.insert(my_array,1,newcol,axis=1)

print("Updated Array : ")
print(my_array)
