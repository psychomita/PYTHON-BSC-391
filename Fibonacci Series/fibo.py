def fibo (n) :
    a=0
    b=1
    print(a)
    print(b)
    for x in range (n-2) :
        c=a+b
        print(c)
        a=b
        b=c
n=int(input("Enter the number of terms in Fibonacci sequence : "))
fibo(n)
