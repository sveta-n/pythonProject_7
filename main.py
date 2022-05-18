class Animal:
    total_num = 0

    def __init__(self):
        Animal.total_num = Animal.total_num + 1

    def voice(self):
        pass

    def print_total():
        print(Animal.total_num)

    print_total = staticmethod(print_total)


class Dog(Animal):
    def voice(self):
        print('гав')


class Cat(Animal):
    def voice(self):
        print('мяу')


class Mouse(Animal):
    def voice(self):
        print('пи-пи-пи')


hachiko = Dog()
hachiko.voice()
tom = Cat()
tom.voice()
jerry = Mouse()
jerry.voice()

Animal.print_total()
