def binaryToGray(binary):
    gray=binary[0]
    for i in range(1, len(binary)):
        gray+=str(int(binary[i]) ^ int(binary[i-1]))
    return gray
binary_num=input("Enter a binary number: ")
graycode=binaryToGray(binary_num)
print("The gray code representation of", binary_num, "is", graycode)
