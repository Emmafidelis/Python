# class: blueprint for creating new objects
# object: is the instance of a class

# clas vs instance attributes
'''class Point:
    default_color = "red"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x}, {self.y})")

point = Point(1, 2)
print(point.defaul_color)
point.draw()
'''

# class vs instance methods
"""
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def zero(cls):
        return cls(0, 0)

    def draw(self):
        print(f"Point ({self.x}, {self.y})")

point = Point.zero()
point.draw()
"""

# magic methods
'''
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def draw(self):
        print(f"Point ({self.x}, {self.y})")

point = Point(1, 2)
print(point)
print(str(point))
'''

# compairing objects
'''
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

point = Point(10, 20)
other = Point(1, 2)
print(point == other)
print(point > other)
'''

# Supporting Arithmetic Operations
'''
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

point = Point(10, 20)
other = Point(1, 2)
combined = point + other
print(combined.x)
'''

# Creating custom containers
'''class TagCloud:
  def __init__(self):
    self.tags = {}

  def add(self, tag):
    self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1

  def __getitem__(self, tag):
    return self.tags.get(tag.lower(), 0)

  def __setitem__(self, tag, count):
    self.tags[tag.lower()] = count

  def __len__(self):
    return len(self.tags)

  def __iter__(self):
    return iter(self.tags)


cloud = TagCloud()
cloud["python"] = 10
len(cloud)
cloud.add("Python")
cloud.add("python")
cloud.add("python")
print(cloud.tags)
'''

# Private Members
'''
class TagCloud:
  def __init__(self):
    self.__tags = {}

  def add(self, tag):
    self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

  def __getitem__(self, tag):
    return self.__tags.get(tag.lower(), 0)

  def __setitem__(self, tag, count):
    self.__tags[tag.lower()] = count

  def __len__(self):
    return len(self.__tags)

  def __iter__(self):
    return iter(self.__tags)


cloud = TagCloud()
print(cloud._TagCloud__tags)
'''
# Properties
'''
class Product:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self.__price = value


product = Product(20)
print(product.price)
'''
# Inheritance
'''
class Animal:
    def __int__(self):
        self.age = 1

    def eat(self):
        print("eat")

# Animal: Parent, Base
# Mammal: Child, Sub
class Mammal(Animal):
    def walk(self):
        print("walk")

class Fish(Animal):
    def swim(self):
        print("swim")

m = Mammal()
m.eat()
print(m.age)
'''
# Object Class
'''
class Animal:
    def __int__(self):
        self.age = 1

    def eat(self):
        print("eat")

# Animal: Parent, Base
# Mammal: Child, Sub
class Mammal(Animal):
    def walk(self):
        print("walk")

class Fish(Animal):
    def swim(self):
        print("swim")

m = Mammal()
print(isinstance(m, object))
print(issubclass(Mammal, Animal))
'''
# Method Overiding
'''
class Animal:
    def __int__(self):
        print("Animal Constructor")
        self.age = 1

    def eat(self):
        print("eat")


class Mammal(Animal):
    def __int__(self):
        print("Mammal Constructor")
        self.weight = 2
        super().__int__()

    def walk(self):
        print("walk")


m = Mammal()
print(m.age)
print(m.weight)
'''
# Multi level Inheritance
'''
class Animal:
    def eat(self):
        print("eat")


class Bird(Animal):
    def fly(self):
        print("fly")

class Chicken(Bird):
    pass
'''
# Multiple Inheritance
'''
class Flyer:
    def fly(self):
        pass


class Swimer:
    def swim(self):
        pass


class FlyingFish(Flyer, Swimer):
    pass
'''
# Example of Inheritance and AbstractMethod
'''
from abc import ABC, abstractmethod

class InvalidOperationError(Exception):
    pass

class Stream(ABC):
    def __int__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already opened.")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream is already closed.")
        self.opened = False

    @abstractmethod
    def read(self):
        pass

class FileStream(Stream):
    def read(self):
        print("Reading data from a file")


class NetworkStream(Stream):
    def read(self):
        print("Reading data from a network")


class MemoryStream(Stream):
    def read(self):
        print('Reading data from a memory')

stream = MemoryStream()
stream.read()
'''
# Polymorphism
'''
from abc import ABC, abstractmethod

class UIControl(ABC):
    @abstractmethod
    def draw(self):
        pass


class TextBox(UIControl):
    def draw(self):
        print("TextBox")


class DropDownList(UIControl):
    def draw(self):
        print("DropDownBox")


def draw(controls):
    for control in controls:
        control.draw()


ddl = DropDownList()
textbox = TextBox()
draw([ddl, textbox])
'''
# Duck Typing
'''
from abc import ABC, abstractmethod

class TextBox:
    def draw(self):
        print("TextBox")


class DropDownList:
    def draw(self):
        print("DropDownBox")


def draw(controls):
    for control in controls:
        control.draw()


ddl = DropDownList()
textbox = TextBox()
draw([ddl, textbox])
'''
# Extending Built-in Types
'''
class Text(str):
    def duplicate(self):
        return self + self


class TrackableList(list):
    def append(self, object):
        print("Append called")
        super().append(object)

list = TrackableList()
list.append("1")
'''
# Data Classes
'''
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
p1 = Point(x=1, y=2)
print(p1.x)
p2 = Point(x=1, y=2)
print(p1 == p2)
'''


