import random


class Person:
    def __init__(self, name):
        self.name = name
        self.age = random.randint(0, 100)


names = ['Scott', 'Fred', 'Ann', 'Dave', 'Clara', 'Sam', 'Alex', 'Greg', 'Christina', 'Mary', 'Jane', 'Layla']
quantity = input('Enter the number of people:')
persons = []

for i in range(int(quantity)):
    nameX = random.choice(names)
    personX = Person(nameX)
    persons.append(personX)


old = []
young = []


for person in persons:
    if person.age <= 50:
        young.append(person)
    else:
        old.append(person)


print('Old people:')
for person in old:
    print(person.name, person.age)


print('Young people:')
for person in young:
    print(person.name, person.age)


