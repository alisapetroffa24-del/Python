class Student:
    def __init__(self, name, age, money, knowledge):
        self.name = name
        self.age = age
        self.money = money
        self.knowledge = knowledge

    def say_name(self):
        print("Мене звати", self.name)

    def grow(self):
        self.age += 1
        print(self.name, "став старше:", self.age)

    def work(self):
        self.money += 200
        self.knowledge -= 10
        print(self.name, "працював")
        print("Грошей:", self.money)
        print("Знання:", self.knowledge)

    def study(self):
        self.knowledge += 20
        self.money -= 50
        print(self.name, "вчився")
        print("Грошей:", self.money)
        print("Знання:", self.knowledge)

    def rest(self):
        self.money -= 100
        self.knowledge -= 5
        print(self.name, "відпочивав")
        print("Грошей:", self.money)
        print("Знання:", self.knowledge)

    def live_year(self):
        for month in range(1, 13):
            print("\nМісяць", month)

            if self.money < 100:
                self.work()

            elif self.knowledge < 50:
                self.study()

            else:
                self.rest()

        self.grow()


s1 = Student("Олег", 13, 300, 60)

s1.say_name()
s1.live_year()