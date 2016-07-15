class Animal(object):
    def breed(self):
        return Animal()

# Cat is a subclass of Animal
# Animal is the parent class (or base class) of Cat
# Cat is-a Animal
# Cat inherits all things (methods, attributes) from Animal
class Cat(Animal):
    def meow(self):
        print 'Meow!'

my_cat = Cat()
my_cat.meow()
kitten = my_cat.breed()

class Dog(Animal):
    def woof(self):
        print 'Woof!'

class Pomeranian(Dog):
    def woof(self):
        print 'WOOOOOOOOF!'

class Person(Animal):
    def __init__(self, name):
        self.name = name

    def greet(self):
        print 'Hello!'

bob.name = 'Robert'

# type - type(obj) will give you the class from which obj was created
# isinstance(obj, clazz) - will give you True or False value telling you whether the object is classified as an instance of that clazz
