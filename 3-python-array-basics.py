# Python Array
# -> a data structure holds more then one value
# -> indexed that starts with 0 also supports negative indexing
# -> can hold a single data type elements but can hold any data
# -> arrays are change able mutable

# import array
#
# a = array.array('i', [1, 2, 3, 4, 5, 6])
# print(a)

# import array as arr
#
# a = arr.array('i', [1, 2, 3, 4, 5, 6])
# print(a)

from array import *

a = array('i', [1, 2, 3, 4, 5, 6])
print(a[2])
print(a[-2])

# Basic Array Operations
arr = array('d', [1.2, 2.3, 3.4, 4.5, 5.6, 6.1])
print(arr)
print(len(arr))

# adding elements
# append()
# extend()
# insert()
print(a)

a.append(7)
print(a)

a.extend([8,9,5,3])
print(a)

a.insert(9,10)
print(a)

# deleting elements
# pop()
# remove()
print(a)

print(a.pop())
print(a)
print(a.pop(10))
print(a)

# print(a.remove(10))  # returns nothing
a.remove(10)
print(a)

# Array Concatenation
arr1 = array('i', [1, 2, 3])
arr2 = array('i', [4, 5, 6])
arr3 = array('i')
arr3 = arr1 + arr2
print(arr3)

# Array Slicing
print(arr3[2:5])

# Looping through Array
print(a)

for x in a:
    print(x)

# for x in a[1:-2]:
#     print(x)

# print(a[::-1])

tmp = 0
while tmp < a[6]:
    print(a[tmp])
    tmp += 1


