class Person:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print('Привет! Меня зовут', self.name)

p = Person('Swaroop')
p.say_hi()