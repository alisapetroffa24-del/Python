class Mission:
    def __init__(self, name, difficulty, reward):
        self.name = name
        self.difficulty = difficulty
        self.reward = reward
    def show_info(self):
        print(f"{self.name} | Сложность: {self.difficulty} | Награда: {self.reward} XP")

class Cadet:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.xp = 0
    def complete_mission(self, mission):
        self.xp += mission.reward
        if self.xp >= self.level * 100:
            self.level += 1
            print("Уровень повышен!")
    def show_status(self):
        print(f"\nИмя: {self.name}")
        print(f"Уровень: {self.level}")
        print(f"Опыт: {self.xp}")

class EliteCadet(Cadet):
    def complete_mission(self, mission):
        bonus_reward = int(mission.reward * 1.3)
        self.xp += bonus_reward
        if self.xp >= self.level * 100:
            self.level += 1
            print("Уровень повышен!")

        print(f"Бонус элитного курсанта: +{bonus_reward - mission.reward} XP")

class MissionCenter:
    def __init__(self):
        self.missions = []
    def add_mission(self, mission):
        self.missions.append(mission)
    def show_missions(self):
        print("\nСписок миссий:")
        for i, mission in enumerate(self.missions, start=1):
            print(f"{i}. ", end="")
            mission.show_info()


class Academy:
    def __init__(self):
        self.center = MissionCenter()
        self.center.add_mission(Mission("Сектор А-7", 1, 50))
        self.center.add_mission(Mission("Спасение дрона", 2, 80))
        self.center.add_mission(Mission("Восстановление NEXUS", 3, 120))

    def run(self):
        print("=== MISSION FORGE ===")
        name = input("Введите имя: ")
        elite = input("Элитный курсант? (да/нет): ").lower()
        if elite == "да":
            cadet = EliteCadet(name)
        else:
            cadet = Cadet(name)

        while True:
            print("\n1 - Показать миссии")
            print("2 - Выполнить миссию")
            print("3 - Статус")
            print("4 - Выход")
            choice = input("Ваш выбор: ")

            if choice == "1":
                self.center.show_missions()
            elif choice == "2":
                self.center.show_missions()
                number = int(input("Введите номер миссии: ")) - 1
                if 0 <= number < len(self.center.missions):
                    mission = self.center.missions[number]
                    print(f"\nМиссия '{mission.name}' выполнена!")
                    cadet.complete_mission(mission)

            elif choice == "3":
                cadet.show_status()
            elif choice == "4":
                print("До свидания!")
                break
            else:
                print("Неверный выбор!")


academy = Academy()
academy.run()