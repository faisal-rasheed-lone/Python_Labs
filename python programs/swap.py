# program for swaping
def swap(a, b):
    c = a
    a = b
    b = c
    print("a = ", a, " b =", b)


def main():
    a = 10
    b = 20
    print("before swapping values :")
    print("a = ", a, " b =", b)
    print("After swap values = ")
    swap(a, b)


main()




