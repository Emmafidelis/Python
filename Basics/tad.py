'''
secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == secret_number:
        print('You won!')
        break
else:
    print("Sorry, you failed!")

temperature = 35

if temperature > 32:
    print("It's hot day")
else:
    print("It's cold day")

first = 'John'
last = 'Smith'
msg = f'{first} [{last}] is a coder'
print(msg)

weight = int(input('Weight: '))
unit = input('(L)bs or (K)g: ')
if unit.upper() == "L":
    converted = weight * 0.45
    print(f"you are {converted} kilos")
else:
    converted = weight / 0.45
    print(f"you are {converted} pounds")

name =input('What is your name? ')
color = input('What is your favourite color? ')
print(name + ' likes ' + color)

z = lambda x:x*x
print(z(6))

is_hot = False
is_cold = False

if is_hot:
    print("It's hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's cold day")
    print("wear warm clothes")
else:
    print("It's lovely day")
print("Enjoy your day")
'''
"""
quantity = 3
item_no = 567
price = 49
my_order = "I want {} pieces of item number {} for {:.2f} dollars."
print(my_order.format(quantity, item_no, price))


point = dict(x=1, y=2)
point['x'] = 10
point['z'] = 20
print(point.get('a', 0))
del point['x']
print(point)
#for key in point:
 #   print(key, point[key])

#for x in point.items():
 #   print(x)

for key, value in point.items():
    print(key, value)

from sys import getsizeof

values = (x * 2 for x in range(10000))
print('gen:', getsizeof(values))


#numbers = [1, 2, 3]
#print(*numbers)
"""
