class Character:
    def __init__(self, name, level, health):
        self.name = name
        self.level = level
        self.health = health
        self.inventory = []

    def info(self):
        print("Ім'я:", self.name)
        print("Рівень:", self.level)
        print("HP:", self.health)
    def rest(self):
        self.health += 10
        print(self.name, "відпочиває. HP:", self.health)
    def attack(self):
        print(self.name, "атакує")
    def add_item(self, item):
        self.inventory.append(item)
    def show_inventory(self):
        print("Інвентар:", self.inventory)


class Warrior(Character):
    def __init__(self, name, level, health, strength):
        super().__init__(name, level, health)
        self.strength = strength
        self.energy = 50
    def shield(self):
        print(self.name, "використовує щит")

    def attack(self):
        if self.energy >= 10:
            self.energy -= 10
            print(self.name, "б'є мечем. Енергія:", self.energy)
        else:
            print(self.name, "нету енергії")


class Mage(Character):
    def __init__(self, name, level, health, magic):
        super().__init__(name, level, health)
        self.magic = magic
        self.mana = 100
    def teleport(self):
        if self.mana >= 20:
            self.mana -= 20
            print(self.name, "телепортується. Мана:", self.mana)
        else:
            print(self.name, "нету мани")
    def attack(self):
        if self.mana >= 15:
            self.mana -= 15
            print(self.name, "кидає фаєрбол. Мана:", self.mana)
        else:
            print(self.name, "немту мани")


class Archer(Character):
    def __init__(self, name, level, health, agility):
        super().__init__(name, level, health)
        self.agility = agility
        self.energy = 40



    def dodge(self):
        print(self.name, "ухиляється від удару")
    def attack(self):
        if self.energy >= 5:
            self.energy -= 5
            print(self.name, "стріляє з лука. Енергія:", self.energy)
        else:
            print(self.name, "нету енергії")


class EliteWarrior(Warrior):
    def __init__(self, name, level, health, strength, bonus):
        super().__init__(name, level, health, strength)
        self.bonus = bonus
    def super_strike(self):
        if self.energy >= 30:
            self.energy -= 30
            print(self.name, "робить суперррудар. Енергія:", self.energy)
        else:
            print(self.name, "нету енергії")


warrior = Warrior("Мечник", 10, 150, 40)
mage = Mage("Мерлін Монро", 12, 80, 100)
archer = Archer("Ролл", 11, 100, 60)
elite = EliteWarrior("Леонардо", 20, 300, 80, 50)

warrior.add_item("Меч")
mage.add_item("Зілля")
archer.add_item("Стріли")
elite.add_item("Золотий щит")
heroes = [warrior, mage, archer, elite]
for hero in heroes:
    hero.info()
    hero.show_inventory()
    hero.attack()
    print("---")

mage.teleport()
warrior.shield()
archer.dodge()
elite.super_strike()