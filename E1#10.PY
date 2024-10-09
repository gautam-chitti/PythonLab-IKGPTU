n = int(input("max width of the design: "))
for i in range(1, n + 1):  # start from 1, not 0
    print("*" * i)
for i in range (n-1,0,-1):
    print("*" * (i))
print("\n")