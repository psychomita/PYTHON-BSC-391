def reverse(s) :
    l = len(s) - 1
    str = ""
    for i in range(l,-1,-1):
        str = str + s[i]
    return str
s = input("Enter a string:-\n")
print("The reversed string is :-\n")
str = reverse(s)
print(str)
