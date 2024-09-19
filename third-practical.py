 # Create strings
str1 = "Hello"
str2 = "World"
str3 = "Python Programming"

concatenated_str = str1 + " " + str2
print(f"Concatenated String: {concatenated_str}")

    # Printing  individual strings
print("")
print("******* INDIVIDUAL STRINGS *******")
print(f"String 1: {str1}")
print(f"String 2: {str2}")
print(f"String 3: {str3}")

    # Accessing substrings
print(" ")
substring1 = str3[0:6]   
substring2 = str3[7:]    
substring3 = str3[:6]    
substring4 = str3[-11:-1]
print("******* SUBSTRINGS STRINGS *******")
print(f"Substring from index 0 to 5: {substring1}")
print(f"Substring from index 7 to end: {substring2}")
print(f"Substring from start to index 5: {substring3}")
print(f"Substring using negative indexing: {substring4}")