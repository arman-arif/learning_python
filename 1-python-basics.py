
# python comment

"""
python docstring
"""

# variables
x = 10
y = 5.25
name = "Arman"

# printing
print(x + y)
print(name)

# python data types
# 1. Numbers -> int, float, complex, bool
# 2. String ->
# 3. List
# 4. Dictionary
# 5. Tuple
# 6. Set
# Additional -> range

# Numbers
x = 10
print(type(x))  # int

pi = 3.1416
print(type(pi))  # float

ij = 4j
print(type(ij))  # complex

compare = x > pi
print(compare)
print(type(compare))  # bool

# String => strings are indexed with index number[0]
x = 'hello'
y = "world"
#z = input()

print(len(x))
print(x[4])
print(x[2:6])
print(x[1:3])
print(x.upper())
print(y.lower())
print(y[-3])
print(y[2])

# List -> list are rapped with [] brackets and indexed
myList = [11, 21, 23.5, 'Arman', 'Arif']
print(myList)
print(myList[2])
print(myList[3:5])

myList.append(550)
print(myList)

myList.insert(3, 234)
print(myList)

myList.reverse()
print(myList)

# Dictionary -> dictionary are rapped with {} brackets and declared with key value pairs
courses = {
    1: 'Python',
    2: 'Javascript',
    'Three': 'PHP',
    'Four': 'React'
}

print(courses)
print(courses['Three'])
print(courses[2])
print(courses.get(1))
print(courses.get('Four'))

courses['Four'] = 'React.js'
courses['Five'] = 'Laravel'
courses['Six'] = "Django"

print(courses)

# Tuple => can not be changed -> tuples are rapped with () brackets and they are indexed
animals = ("Tiger", "Lion", "Dog", 100, 100, 200, 'Tiger')
print(animals[1])
print(animals.count('Tiger'))

# Set => can not have duplicate values and does not support indexing
animals = {"Tiger", "Lion", "Dog", 100, 100, 200, 'Tiger'}
print(animals)

# Range
myRange = range(10)
print(myRange)
myRange = list(myRange)
print(myRange)
print(list(range(15)))

# Mics Tests
foods = ['Rice', 'Mutton', 'Chicken', 'Beaf']
cars = ('Toyota', 'Fords', 'BMW')
bikes = {'Yamaha', 'Honda', 'TVS', 'Bajaj', 'Suzuki', 'Runner'}
xyz = [foods, cars, bikes]
print(xyz)

# Type conversion -> int(), float(), tuple(), list(), set(), dict(), str()
name = 'Name'
x = 10
print(str(x) + name)

# Python Collections => is a specialised data structures for container data types

