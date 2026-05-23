class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info(self):
        print("Ім'я:", self.name)
        print("Вік:", self.age)
    def sound(self):
        print(self.name, "видає звук")


class WildAnimal(Animal):
    def __init__(self, name, age, danger):
        super().__init__(name, age)
        self.danger = danger
    def info(self):
        super().info()
        print("опастность:", self.danger)


class Predator(WildAnimal):
    def __init__(self, name, age, danger):
        super().__init__(name, age, danger)
        self.food = []
    def add_food(self, prey):
        self.food.append(prey)
    def info(self):
        super().info()
        print("Список їжі:", self.food)

class Herbivorous(WildAnimal):
    def __init__(self, name, age, danger, grass):
        super().__init__(name, age, danger)
        self.grass = grass
    def info(self):
        super().info()
        print("Кількість трави:", self.grass)

class Lion(Predator):
    def sound(self):
        print(self.name, "ричить: Раррр")


class Tiger(Predator):
    def sound(self):
        print(self.name, "гарчить: раааааааррррр")

class Wolf(Predator):
    def sound(self):
        print(self.name, "виє: Аууу")


class Wildebeest(Herbivorous):
    def sound(self):
        print(self.name, "мукає: Муууу4уууу")
class Hare(Herbivorous):
    def sound(self):
        print(self.name, "пищить: Пі-пі")

class Deer(Herbivorous):
    def sound(self):
        print(self.name, "сопе: Фррр")

lion = Lion("Алекс", 5, "Висока")
tiger = Tiger("Шершень", 4, "Висока")
wolf = Wolf("Акула", 6, "Середня")
wildebeest = Wildebeest("Гокк", 3, "Низька", 50)
hare = Hare("Крош", 1, "Жодної", 10)
deer = Deer("кора", 2, "Низька", 30)
lion.add_food("М'ясо")
tiger.add_food("Кабан")
wolf.add_food("Заєць")

animals = [lion, tiger, wolf, wildebeest, hare, deer]

for animal in animals:
    animal.info()
    animal.sound()
    print("      ")
