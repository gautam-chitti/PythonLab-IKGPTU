def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    if b==0:
        raise ValueError("cannot divide by zero!")
    return a/b

def solve(equation):
    num1,operator,num2 = equation.split()
    a = float(num1)
    b = float(num2)
    result=float
    if operator == '+':
        result=(add(a,b))
    elif operator == '-':
        result=(sub(a,b))
    elif operator == '*':
        result=(mul(a,b))
    elif operator == '/':
        result=(div(a,b))
    else:
        raise ValueError ("invalid input")
    return result

equation = input("enter an equation(e.g. 4-3, 2+5, 6/4, 9*7): ")
result = solve(equation)
print ("the result of " + equation +" is " + str (result))