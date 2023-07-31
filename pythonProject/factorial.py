# factorial
def fact(a):
    i = a
    fact = 1
    while i > 0:
        fact = fact * i
        i -= 1
    print("factorial of ", a, " is ", fact)

fact(6)