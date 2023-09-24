import math
def evaluatepolynomial(coefficients,x):
    result=0
    degree= len(coefficients)-1
    for i in range(len(coefficients)):
        result+=coefficients[i]*math.pow(x,degree-i)
    return result
coefficients=[]
degree=int(input("Enter the degree of the polynomial: "))
for i in range(degree+1):
    coeff=float(input("Enter coefficients: "))
    coefficients.append(coeff)
x_value=float(input("Enter the value of x: "))
result=evaluatepolynomial(coefficients,x_value)
print("The result of the polynomial equation is: ", result)
    
