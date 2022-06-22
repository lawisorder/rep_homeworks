
class Dog:

    def __init__(self, name, age, master):
        self.name = name
        self.age = age
        self.master = master

    def run(self):
        return f'{self.name} can run'

    def jump(self):
        return f'{self.name} can jump high'

    def birthday(self):
        return f'In 2023 {self.name} it will be {self.age + 1} years old'

    def sleep(self, hours):
        return f'{self.name} likes sleep {hours} hours'

    def bark(self):
        return f'The {self.name} barks "wof-wof-wof"'

scubydoo = Dog('Scubydoo', 5, 'Alex')

class Cat:

    def __init__(self, name, age, master):
        self.name = name
        self.age = age
        self.master = master

    def run(self):
        return f'{self.name} can run'

    def jump(self):
        return f'{self.name} can jump high'

    def birthday(self):
        return f'In 2023 {self.name} it will be {self.age + 1} years old'

    def sleep(self, hours):
        return f'{self.name} likes sleep {hours} hours'

    def meow(self):
        return f'The {self.name} meow "жраааааааать"'

cat = Cat('Tom', 1, 'Lucy')

class Parrot:

    def __init__(self, name, age, master):
        self.name = name
        self.age = age
        self.master = master

    def run(self):
        return f"{self.name} can't run"

    def jump(self):
        return f'{self.name} can jump high'

    def birthday(self):
        return f'In 2023 {self.name} it will be {self.age + 1} years old'

    def sleep(self, hours):
        return f'{self.name} likes sleep {hours} hours'

    def fly(self):
        return f'The {self.name} can fly very good'

parrot = Parrot('Voody', 2.5, 'Ann')



