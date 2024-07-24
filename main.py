class House:
    def __init__(self, name, numberOfFloors):
        self.name = name
        self.numberOfFloors = abs(numberOfFloors)

    def __len__(self):
        return self.numberOfFloors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.numberOfFloors}'

    def goTo(self, newFloor):
        if newFloor <= self.numberOfFloors and newFloor > 0:
            for i in range(1, newFloor + 1):
                print(i)
        else:
            print('Такого этажа не существует')

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))