"""numbers = [3, 5, 2, 8, 4, 19,54, 5, 53, 32, 64, 35, 58]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)
"""

"""
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in matrix:
    for item in row:
        print(item)



numbers = [2, 1, 3, 5, 2, 4, 2, 6, 4, 1, 2]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)


# numbers = list(range(20))
# print(numbers)

numbers = [1, 2, 3, 4, 5, 6, 7]
first, second, *other = numbers
print(first)
print(other)

letters = ["a", "b", "c"]
for index, letter in enumerate(letters):
    print(index, letter)


items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]


items.sort(key=lambda item: item[1])
print(items)


items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]
x = list(map(lambda item: item[1], items))
     or we can use list comprehension for it.
x = [item[1] for item in items]

print(x)

letters = ['a', 'b', 'c', 'b', 's', 'b']
for letter in letters:
    letter = letters
    letter.remove('b')
print(letter)


items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]

# prices = list(filter(lambda item: item[1] >= 10, items))
prices = [item for item in items if item[1] >= 10]
print(prices)


  # ZIP FUNCTION


list1 = [1,2, 3]
list2 = [10, 20, 30]
print(list(zip("abc", list1, list2)))
"""

  # ARRAYS

from array import array

numbers = array("i", [1, 2, 3])
numbers[0] = 5
print(numbers)