mport numpy as np
rows=2
cols=2
user_input=[]
user_inputt=[]

print("Enter input for first array : ")
for i in range(rows):
    row=[]
    for j in range(cols):
        value=int(input("Enter the value for row "+ str(i+1)+" and column " +str(j+1)+ " : "))
        row.append(value)
    user_input.append(row)
my_array1=np.array(user_input)

print("Enter input for second array : ")
for i in range(rows):
    row=[]
    for j in range(cols):
        value=int(input("Enter the value for row "+ str(i+1)+" and column " +str(j+1)+ " : "))
        row.append(value)
    user_inputt.append(row)
my_array2=np.array(user_inputt)
print("The Sum of the array : ")
sum= my_array1 + my_array2
print(sum)
square= sum**2
print("The Square of the array : ")
print(square)
