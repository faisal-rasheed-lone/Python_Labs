num = int(input("enter number"))
arr = []
i = 1
while i < num:
    if num % i == 0:
        arr.append(i)
    i += 1

x = sum(arr)
if x == num:
    print(num, "is a perfect number ")
else:
    print(num, "is not a perfect number")