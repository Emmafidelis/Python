import random
import string
from pathlib import Path

# print(random.random())
# print(random.randint(1, 20))
# print(random.randrange(100))
# print(random.choice([1, 2, 3, 4]))
# print(random.choices([1, 2, 3, 4, 5], k=4))
# print("".join(random.choices("abcdefghijk", k=6)))
print("".join(random.choices(string.ascii_letters + string.digits, k=8)))

numbers = [1, 2, 3, 4]
random.shuffle(numbers)
print(numbers)
# print(string.ascii_letters)
# print(string.ascii_lowercase)
# print(string.hexdigits)
# print(string.digits)