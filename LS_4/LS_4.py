from abc import ABC, abstractmethod

# Абстрактный класс Animal
class Animal(ABC):
    @abstractmethod # декоратор
    def make_sound(self):
        pass


class Dog(Animal):
    def make_sound(self):
        print(f"гав-гав")


class Cat(Animal):
    def make_sound(self):
        print()



puppy = Dog()
puppy.make_sound()

