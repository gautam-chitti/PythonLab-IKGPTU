int_a = 15
int_b = 4
float_a = 15.0
float_b = 4.0
    
    # Integer arithmetic operations
print(f"Integer Operations:")
print(f"Addition: {int_a} + {int_b} = {int_a + int_b}")
print(f"Subtraction: {int_a} - {int_b} = {int_a - int_b}")
print(f"Multiplication: {int_a} * {int_b} = {int_a * int_b}")
print(f"Division: {int_a} / {int_b} = {int_a / int_b}")
print(f"Modulus: {int_a} % {int_b} = {int_a % int_b}")
print(f"Exponentiation: {int_a} ** {int_b} = {int_a ** int_b}")
print(f"Floor Division: {int_a} // {int_b} = {int_a // int_b}")
    
    # Floating-point arithmetic operations
print("\nFloating-Point Operations:")
print(f"Addition: {float_a} + {float_b} = {float_a + float_b}")
print(f"Subtraction: {float_a} - {float_b} = {float_a - float_b}")
print(f"Multiplication: {float_a} * {float_b} = {float_a * float_b}")
print(f"Division: {float_a} / {float_b} = {float_a / float_b}")
print(f"Modulus: {float_a} % {float_b} = {float_a % float_b}")
print(f"Exponentiation: {float_a} ** {float_b} = {float_a ** float_b}")
print(f"Floor Division: {float_a} // {float_b} = {float_a // float_b}")
    
    # Additional example with mixed types
print("\nMixed Type Operations (int and float):")
mixed_addition = int_a + float_b
mixed_subtraction = float_a - int_b
mixed_multiplication = int_a * float_b
mixed_division = float_a / int_b
print(f"Addition: {int_a} + {float_b} = {mixed_addition}")
print(f"Subtraction: {float_a} - {int_b} = {mixed_subtraction}")
print(f"Multiplication: {int_a} * {float_b} = {mixed_multiplication}")
print(f"Division: {float_a} / {int_b} = {mixed_division}")