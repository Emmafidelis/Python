"""
course = '''
Hi John,

Here is our first email to you.

Thank you!
the support team 

'''
print(course)
"""

numbers = [1, 2, 1, 1, 3, 2, 5, 3, 2, 3]
first = set(numbers)
second = {1, 6}

print(first | second)
print(first & second)
print(first - second)
print(first ^ second)
