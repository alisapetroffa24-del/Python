class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def info(self):
        print("Зброя:", self.name)
        print("Шкода:", self.damage)

class Armor:
    def __init__(self, name, defense):
        self.name = name
        self.defense = defense

class Character:
    def __init__(self, name, level, weapon, armor):
        self.name = name
        self.level = level
        self.weapon = weapon
        self.armor = armor
        self.health = 100

    def show_stats(self):
        print("Ім'я:", self.name)
        print("HP:", self.health)
        print("Зброя:", self.weapon.name)
        print("Броня:", self.armor.name)

    def show_weapon(self):
        print(self.name, "використовує", self.weapon.name)

    def attack(self, enemy):
        print(self.name, "атакує", enemy.name)
        enemy.health -= self.weapon.damage
        print(enemy.name, "отримав шкоду")
        print("HP ворога:", enemy.health)

class Enemy:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def info(self):
        print("Ворог:", self.name)
        print("HP:", self.health)

armor1 = Armor(name="Iron Armor", defense=15)
weapon1 = Weapon(name="Steel Sword", damage=30)
player = Character(name="Warrior", level=8, weapon=weapon1, armor=armor1)

player.show_stats()

golden_armor = Armor(name="Golden Armor", defense=25)
diamond_armor = Armor(name="Diamond Armor", defense=50)

enemy1 = Enemy(name="Skeleton", health=120)
enemy2 = Enemy(name="Orc", health=150)

player.attack(enemy1)
player.attack(enemy2)
