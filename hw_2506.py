# 14.8-14.9

class myError(Exception):
    def __init__(self, text):
        self.text = text

class NonNegative:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if value <= 0:
            raise ValueError('Only positive!')
        instance.__dict__[self.name] = value

class NonEmpty:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if value == '':
            raise myError('Not empty!')
        instance.__dict__[self.name] = value

class Pets:
    age = NonNegative()
    name = NonEmpty()
    master = NonEmpty()

    def __init__(self, name, age, master):
        self.name = name
        self.age = age
        self.master = master

    def run(self):
        return f'{self.name} can run'

    def jump(self):
        return f'{self.name} can jump so high'


class Dog(Pets):
    def __init__(self, name, age, master):
        super().__init__(name, age, master)

    def bark(self):
        return f'The {self.name} barks "wof-wof-wof"'


dog = Dog('Scubydoo', 5, 'Alex')
dog.master = ''
print(dog.__dict__)




