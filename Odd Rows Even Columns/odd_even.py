import numpy as np
rows=int(input("Enter the number of rows : "))
cols=int(input("Enter the number of columns : "))
user_input=[]

print("Enter input for the array : ")
for i in range(rows):
    row=[]
    for j in range(cols):
        value=int(input("Enter the value for row "+ str(i+1)+" and column " +str(j+1)+ " : "))
        row.append(value)
    user_input.append(row)
my_array=np.array(user_input)

odd_rows_even_cols=my_array[::2,1::2]
print("Odd rows and Even columns : ",odd_rows_even_cols) 
