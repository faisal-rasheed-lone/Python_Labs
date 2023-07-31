# program for second largest
arr = []
n = 10
print("enter elements for list")
for i in range(n):
    x = int(input())
    arr.append(x)

arr.sort()
print("List : ", end="")
print(arr)
print("The second largest element is ", arr[-2])
