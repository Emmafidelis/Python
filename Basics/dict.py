'''
point = dict(x=1, y=2)
point['z'] = 20
print(point.get('a', 0))
del point['x']
for key in point:
    print(key, point[key])
    # OR
for key, value in point.items():
    print(key, value)

# DICTIONARIES COMPREHENSION
values = {x: x * 2 for x in range(5)}
print(values)
'''
# GENERATORS EXPRESSION
from sys import getsizeof

values = (x * 2 for x in range(100000))
print(getsizeof(values))
