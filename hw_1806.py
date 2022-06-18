# # 14.1
#
class Dog:


    def __init__(self, height, weight, name, age):
        self.height = height
        self.weight = weight
        self.name = name
        self.age = age


    def jump(self, length):
        return f'{self.name} обычно прыгает в длину на {length} метров'


    def run(self, distance):
        return f'{self.name} может пробежаьб {distance} километров'


    def bark(self, bark):
        return f'Лай {self.name} напоминает {bark}'


muhtar = Dog(1.2, 50, 'Mukhtar', 10)
jim = Dog(0.8, 45, 'Jim', 5)

print(muhtar.__dict__)
print(jim.__dict__)
print(jim.jump(10))
print(muhtar.run(25))
print(jim.bark('wooooo'))



# 14.2

class Dog:


    def __init__(self, height, weight, name, age):
        self.height = height
        self.weight = weight
        self.name = name
        self.age = age


    def change_name(self, new_name):
        self.name = new_name
        return


muhtar = Dog(1.2, 50, 'Mukhtar', 10)


print(muhtar.name)
muhtar.change_name('Kashtanka')
print(muhtar.name)

