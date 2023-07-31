# Python program for linear search

def linearSearch(arr, key):  #user-defined function
    for i in range(len(arr)):
        if (arr[i] == key):
            return i
    return -1

arr = [50, 90, 30, 70, 60]  #array
key = 70  #search key

index = linearSearch(arr, key) #calling function

# display result
if(index == -1):
    print(key, 'not Found')
else:
    print(key, 'Found at Index', index)
