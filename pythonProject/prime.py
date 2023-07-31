# checking whether a number is prime or not
num = int(input("enter number "))
i = 2
flag = 0
while i <= num/2:
    if num % i == 0:
        flag = 1
        break
    i = i + 1

if flag == 1:
    print('not prime')
else:
    print("prime")