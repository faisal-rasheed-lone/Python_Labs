# calculation of simple interest
def simple_interest():
    p = int(input("Enter the Principle Amount: "))
    r = float(input("Enter Rate of Interest (%): "))
    t = float(input("Enter Time Period: "))
    si = (p * r * t) / 100
    print("Simple Interest Amount: ", si)


def compound_interest():
    # Python program to find compound interest

    p = float(input("Enter the principle amount : "))
    r = float(input("Enter the rate of interest : "))
    t = float(input("Enter the time in the years: "))

    # calculating compound interest
    ci = p * (pow((1 + r / 100), t))

    # printing the values
    print("Principle amount  : ", p)
    print("Interest rate     : ", r)
    print("Time in years     : ", t)
    print("compound Interest : ", ci)


simple_interest()
compound_interest()