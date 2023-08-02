print(" welcome to the world of Lists ")

# list creation
L = [1, 2, 3, 4, 5]
print(L)

# creating list using built-in function
L = list(range(10, 15, 2))
print(L)            # o/p [10, 12, 14]

# list comprehension I.e. creating list based on existing lists
L = [m for m in range(100, 110) if m % 2 == 0]
print(L)                # o/p [100, 102, 104, 106, 108]

# list comprehension example 2
L = []
for a in range(2000, 2010):
    L.append(a)
print(L)                # o/p [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009]

# printing list in reverse
L = [1, 2, 3, 4, 5]
print(L[-1::-1])            # o/p [5, 4, 3, 2, 1]

# iterating list
L = [1, 2, 3, 4, 5]
print(L[4])         # o/p 5
# mixed lists
L = [1, 2, 3, 'faisal', 'rasheed']
print(L)            # o/p [1, 2, 3, 'faisal', 'rasheed']

# nested lists
L = [1, 2, 3, [4, 5, 6]]
print(L)            # o/p [1, 2, 3, [4, 5, 6]]

# concatenating lists
L1 = [1, 3, 4]
L2 = [2, 5, 6]
L3 = L1 + L2
print(L3)       # o/p [1, 3, 4, 2, 5, 6]

# List Functions and their usage
# Functions related to deletion  1-del 2-pop 3-remove 4-clear

L = [1, 3, 4, 2, 5, 6]
del L[3]
print(L)            # o/p [1, 3, 4, 5, 6]

# usage of pop function
L = [10, 20, 30, 40]
L.pop(2)
print(L)            # o/p [10, 20, 40]
print(L.pop(1))        # o/p 20

# usage of remove function ... remove works on value
L = [100, 300, 400, 200, 500, 600]
L.remove(400)
print(L)            # o/p [100, 300, 200, 500, 600]

# usage of clear function
L = [100, 300, 400, 200, 500, 600]
L.clear()
print(L)                # o/p []

# insert() ... used to insert value at any given location
L = [100, 300, 400, 200, 500, 600]
L.insert(0, 1000)
print(L)            # o/p [1000, 100, 300, 400, 200, 500, 600]

# append() .... used to add elements to last of list
L1 = [100, 300, 400, 200, 500, 600, 700]
L.append(5000)
print(L)            # o/p [100, 300, 400, 200, 500, 600, 700, 5000]

# extend() ......used to extend the list
L1 = [100, 300, 400, 200, 500, 600, 700]
L2 = [222, 333]
L1.extend(L2)
print(L1)               # o/p [100, 300, 400, 200, 500, 600, 700, 222, 333]

# copying list
L1 = [100, 300, 400, 200, 500, 600, 700]
L2 = L1
print(L2)                   # o/p [100, 300, 400, 200, 500, 600, 700]

# count().... used to find the occurrence of an element in list
L1 = [100, 100, 100,  300, 400, 200, 500, 600, 700]
print(L1.count(100))                # o/p 3

# Max ad Min
L1 = [100, 300, 400, 200, 500, 600, 700]
print(max(L1))          # o/p 700
print(min(L1))             # o/p 100
L1.sort()           # o/p [100, 200, 300, 400, 500, 600, 700]
print(L1)
L1.reverse()           # o/p [700, 600, 500, 400, 300, 200, 100]
print(L1)
print(L1.index(500))        # o/p 2

# creating 2d list
L1 = [
      [10, 20, 30],
      [77, 22, 33],
      [11, 55, 70]
     ]
print(L1)       # o/p [[10, 20, 30], [77, 22, 33], [11, 55, 70]]
print(L1[2][2])     # o/p 70

# list slicing
L1 = [100, 300, 400, 200, 500, 600, 700]
print(L1[2:5])          # o/p [400, 200, 500]
print(L1[::2])          # o/p [100, 400, 500, 700]
print(L1[6::-1])        # o/p [700, 600, 500, 200, 400, 300, 100]

