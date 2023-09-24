def lcm(a,b):
    gcd = min(a,b)
    while gcd > 0 :
        if a % gcd == 0 & b % gcd == 0 :
            break
        gcd -= 1
    result = (a * b) / gcd 
    return result  
a = int(input("Enter a number : "))
b = int(input("Enter a number : "))
print("The LCM is ",lcm(a,b))
