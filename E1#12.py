def factorial(a):
    factorial_no = a
    if a==0 or a==1:
        return factorial_no
    else:
        factorial_no = factorial_no * factorial(a-1)
        a = a-1
        return factorial_no

a=6
print(factorial(a))