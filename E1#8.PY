a=int(input("input first number: "))
b=int(input("input second number: "))
c=int(input("input third number: "))
if a>b and a>c:
    print("the greatest number is: ",a)
elif b>a and b>c:
    print("the greatest number is: ",b)
else:
    print("the greatest number is: ",c)