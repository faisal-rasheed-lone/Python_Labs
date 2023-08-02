import numpy

arr = numpy.array([1, 2, 3, 4, 5])

print(arr)
print(type(arr))
num1 = 36
num2 = 44

print(numpy.gcd(num1, num2))        # o/p fxns from numpy
print(numpy.lcm(num1, num2))

# 2d arrays
arr = numpy.array([[1, 2, 3], [4, 5, 6]])
print(arr)

# 3d arrays
arr = numpy.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr)

a = numpy.array(42)
b = numpy.array([1, 2, 3, 4, 5])
c = numpy.array([[1, 2, 3], [4, 5, 6]])
d = numpy.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)