def square_number(x) :
    return (x*x)
print("The square of numbers are :-\n")
for x in range(1,101) :
    sq = square_number(x)
    print("Square of ",x," is ",sq,"\n")