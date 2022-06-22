class Pets:

    def __init__(self, name, age, master):
        self.name = name
        self.age = age
        self.master = master

    def run(self):
        return f'{self.name} can run'

    def jump(self):
        return f'{self.name} can jump so high'

    def birthday(self):
        return f'In 2023 {self.name} will be {self.age + 1} years old'

    def sleep(self, hours):
        return f'{self.name} likes sleep {hours} hours'

class Dog(Pets):
    def __init__(self, name, age, master):
        super().__init__(name, age, master)

    def bark(self):
        return f'The {self.name} barks "wof-wof-wof"'


dog = Dog('Scubydoo', 5, 'Alex')


class Cat(Pets):
    def __init__(self, name, age, master):
        super().__init__(name, age, master)

    def meow(self):
        return f'The {self.name} meow "жраааааааать"'

cat = Cat('Tom', 1, 'Lucy')


class Parrot(Pets):
    def __init__(self, name, age, master):
        super().__init__(name, age, master)

    def fly(self):
        return f'The {self.name} can fly very good'


parrot = Parrot('Voody', 2.5, 'Ann')


print(parrot.jump())
print(cat.run())
print(dog.sleep(5))
print(dog.birthday())

print(dog.bark())
print(cat.meow())
print(parrot.fly())





