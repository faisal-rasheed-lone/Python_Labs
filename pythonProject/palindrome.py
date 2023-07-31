# program for palindrome
str = input("enter the string")     # getting the user input

if str == str[::-1]:
    print("String is palindrome")
else:
    print("Not palindrome")