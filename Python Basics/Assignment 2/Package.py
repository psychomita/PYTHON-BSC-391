a=int(input("Enter the amount"))
city=input("Enter the city")
if(a<1000):
    a=a+100
elif((a>=1000)&(a<2000)):
    a=a+50
print("The city is ",city)
print("The new amount is ",a)

      
