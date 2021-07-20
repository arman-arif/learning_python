# Python Collections => is a specialised data structures for container data types

# namedtuple()
from collections import namedtuple

courseStructure = namedtuple('Courses', 'Name, Technology')
myCourse = courseStructure('React.js', 'JavaScript')
print(myCourse)

myCourse = courseStructure._make(['React.js', 'JavaScript'])
print(myCourse)

# deque -> 'deck'
from collections import deque

arman = ['A', 'r', 'm', 'a', 'n']
d = deque(arman)
print(d)

d.append('Arif')
print(d)

d.appendleft('Name:')
print(d)

d.pop()
print(d)

d.popleft()
print(d)

# Chainmap
from collections import ChainMap

a = {1: 'edureka', 2: 'python'}
b = {3: 'ML', 4: 'AI'}
x = ChainMap(a, b)
print(x)

# counter -> is a dict subclass for counting hashable objects
from collections import Counter

x = [1, 1, 2, 3, 4, 5, 4, 4, 5, 5, 3, 6, 2, 2, 3, 1, 4, 3, 2, 1]
c = Counter(x)
print(c)
print(list(c.elements()))
print(c.most_common())
sub = {2:2, 6:1}
c.subtract(sub)
print(c)

# OrderedDict -> remembers order of dictionary
from collections import OrderedDict

d = OrderedDict()
d[1] = 'A'
d[2] = 'r'
d[3] = 'm'
d[4] = 'a'
d[5] = 'n'
print(d)
print(d.keys())
print(d.items())
d[1] = 'a'
print(d)

# defaultdict -> calls a factory function to supply missing value
from collections import defaultdict

dd = defaultdict(int)
dd[1] = 'python'
dd[2] = 'javascript'
print(dd)
print(dd[3])

# UserDict, UserList, UserString
# from collections import UserDict, UserList, UserString



