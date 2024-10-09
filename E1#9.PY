def C_to_F(a):
    return (a * 9/5) + 32
def F_to_C(a):
    return (a - 32) * 5/9

print("celsius to fahrenheit and vise versa")

while True :
    print("1. celsius to fahrenheit")
    print("2. fahrenheit to celsius")
    print("3. exit")
    choice = input("enter your choice: ")
    if choice == "1":
        a = float(input("enter temperature in celsius: "))
        print("result is: ",C_to_F(a))
    elif choice=="2": 
        a = float(input("enter temperature in fahrenheit: "))
        print("result is: ",F_to_C(a))
    elif choice == "3":
        break
    else: 
        print("invalid input try again")
