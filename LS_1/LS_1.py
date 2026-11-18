from os import name

class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education

    def introduce(self):
        print(f'My name is {self.name} , birth_date: {self.birth_date}, occupation: {self.occupation}, higher_education: {self.higher_education}\n-----------------------------------------------------------')


man = Person('Aziz', 1997, 'Developer', 'Muk')
man.introduce()

man2 = Person('Isken', 1991, 'Doter', 'Bank')
man2.introduce()

man3 = Person('Zakir', 1976, 'Imam', 'Doctor')
man3.introduce()

man4 = Person('Isa', 1997, 'Billionaire', 'none')
man4.introduce()

