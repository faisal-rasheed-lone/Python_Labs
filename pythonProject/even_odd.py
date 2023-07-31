# even odd prog using module
number = int(input("enter any number"))     # getting user input
if number & 1 != 1:                         # bitwise comparison
    print(number, "is even")
else:
    print(number, 'is odd')


def even_odd(num1):
    if num1 % 2 == 0:
        print(num1, " is even")
    else:
        print(num1, " is odd")


def main():
    num = int(input("enter number "))
    even_odd(num)


main()
