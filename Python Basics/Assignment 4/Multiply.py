def multiply() :
    num_list = [29, 5, 69, 26, 11, 12, 3]
    prod = 1
    for i in range(7) :
        prod = prod * num_list[i]
    print("The numbers in the list are :\n", num_list)
    return prod
product = multiply()
print("The product of all the numbers in the list is ", product)
