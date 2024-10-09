str1=str(input())
str2=str(input())

str_concat= str1 + " " + str2
print ("concatinated strings: ", str_concat)
print("now we will do string slicing, the original string is")
str_original="hello, My name is Kartikey and I like to play games"
print("",str_original)
a= int(input("enter starting index for slicing:  "))
b= int(input("enter ending index for slicing:  "))
str_substring=str_original[a:b]
print("substring of original string: ", str_substring)