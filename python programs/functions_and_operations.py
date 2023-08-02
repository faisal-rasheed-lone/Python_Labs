# demonstration of using functions
def demo():         # defining a function
    print(" demo function ")


def sun(a, b):          # function with arguments
    print(a + b)


def sum_return(a, b):           # functions with return type
    return a + b


def main():
    demo()  # o/p demo function
    sun(10, 20)
    s = sum_return(20, 40)
    print(s)  # o/p 60


main()
