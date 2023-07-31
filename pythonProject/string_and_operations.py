# various operations on strings
str1 = "welcome to the world of python."

print(str1)                 # o/p welcome to the world of python

# string slicing

print(str1[0:7])            # o/p welcome

print(str1[10:16])          # o/p  the w

print(str1[::2])            # o/p wloet h ol fpto

# reverse slicing

print(str1[-1::-1])         # o/p nohtyp fo dlrow eht ot emoclew

print(str1[::-1])           # o/p nohtyp fo dlrow eht ot emoclew

# iterating strings

for a in str1:
    print(a, end="")        # o/p welcome to the world of python
print()

# string functions

print(str1.upper())         # o/p WELCOME TO THE WORLD OF PYTHON

print(str1.lower())         # o/p welcome to the world of python

print(str1.title())         # o/p Welcome To The World Of Python

print(str1.capitalize())    # o/p Welcome to the world of python

print(str1.isalpha())       # o/p False

print(str1.isdigit())       # o/p False

print(str1.isalnum())       # o/p False

print(str1.find('p'))       # o/p 24

print(str1.count('w'))      # o/p 2

print(str1.index('p'))      # o/p 24

print(str1.endswith('.'))   # o/p True