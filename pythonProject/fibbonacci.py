# fibbonacci series generator
def fibo(a, b, n):
    i = 1
    print(a, b, end=" ")
    while i < n:
        c = a + b
        print(c, end=" ")
        a = b
        b = c
        i += 1


fibo(1, 2, 10)




