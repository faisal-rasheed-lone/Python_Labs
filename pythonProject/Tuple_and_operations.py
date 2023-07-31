# usage of Tuples
# tuple creation
t = (1, 2, 3)
print(t)        # o/p (1, 2, 3)

t = ("abc", 1, 2, 55)
print(t)        # o/p ('abc', 1, 2, 55)

# tuple iteration
t = (1, 2, 3)
for a in t:
    print(a,end=" ")        # o/p 1 2 3
print()
# tuple slicing
t = (1, 2, 3, 4, 5, 6, 7)
print(t[2:4])           # o/p (3, 4)
print(t[-1:0:-1])           # o/p (7, 6, 5, 4, 3, 2)

# tuple functions
t = (1, 2, 3, 4, 5, 6, 7)
print(max(t))
print(min(t))
print(t.count(3))           # o/p 1
print(t.index(7))           # o/p 6
print(sum(t))       # o/p 28




