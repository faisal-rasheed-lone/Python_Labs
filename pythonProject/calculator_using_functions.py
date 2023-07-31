# calculator using functions by faisal rasheed

def addition():
    a = int(input("enter value of a : "))
    b = int(input("enter value of b : "))
    return a + b


def multiplication():
    a = eval(input("enter value of a : "))
    b = eval(input("enter value of b : "))
    return a * b


def subtraction():
    a = eval(input("enter value of a : "))
    b = eval(input("enter value of b : "))
    return a - b


def division():
    a = eval(input("enter value of a : "))
    b = eval(input("enter value of b : "))
    return a / b


def int_division():
    a = eval(input("enter value of a : "))
    b = eval(input("enter value of b : "))
    return a // b


def main():
    ch = 'y'
    while ch == 'y':
        print('''
            select any  operation :
            1 = addition
            2 = multiplication
            3 = subtraction
            4 = division
            5 = integer division''')
        print()
        a = int(input("Your choice : "))
        if a == 1:
            sum = addition()
            print(sum)
        elif a == 2:
            mul = multiplication()
            print(mul)
        elif a == 3:
            sub = subtraction()
            print(sub)
        elif a == 4:
            div = division()
            print(div)
        elif a == 5:
            in_div = int_division()
            print(in_div)
        else:
            print("wrong choice")
            exit()
        ch = input("do u want to continue ")


main()
