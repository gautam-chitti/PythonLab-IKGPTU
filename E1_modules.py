def right_triangle(a,b,c):
    LHS = a*a
    RHS = b*b+c*c
    if (LHS == RHS ):
        print("the triangle is right angled")
    else:
        print("the triangle is not right angled")

def fibo_series(n):
    fib_sequence = [0,1]

    for i in range(2, n):
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])

    print (fib_sequence)

def factorial(a):
    factorial_no = a
    if a==0 or a==1:
        return factorial_no
    else:
        factorial_no = factorial_no * factorial(a-1)
        a = a-1
        return factorial_no

def G_no(a,b,c):
    if a>b and a>c:
        print("the greatest number is: ",a)
    elif b>a and b>c:
        print("the greatest number is: ",b)
    else:
        print("the greatest number is: ",c)