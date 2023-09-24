import cmath
a=int(input("Enter the value of a in equation "))
b=int(input("Enter the value of b in equation "))
c=int(input("Enter the value of c in equation "))
x1=(-b+cmath.sqrt((b**2)-(4*a*c)))/(2*a)
x2=(-b-cmath.sqrt((b**2)-(4*a*c)))/(2*a)
print("The roots of the equation are ",x1," and ",x2)
