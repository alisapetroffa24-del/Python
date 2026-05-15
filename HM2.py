class Item:
    def __init__(self, name, value):
        self.name = name
        self.value = value


class Player:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.inventory = []

    def attack(self, target):
        target.hp = target.hp - self.damage
        print(self.name, "атакує", target.name)
        print("У", target.name, "залишилось HP:", target.hp)

    def add_item(self, item):
        self.inventory.append(item)
        print("Предмет", item.name, "додано в інвентар")

    def show_inventory(self):
        print("--- Ваш інвентар ---")
        for item in self.inventory:
            print("-", item.name, "(цінність:", item.value, ")")


class Enemy:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def attack(self, target):
        target.hp = target.hp - self.damage
        print(self.name, "атакує", target.name)
        print("У", target.name, "залишилось HP:", target.hp)


player = Player("Knight", 100, 20)
enemy = Enemy("Goblin", 60, 10)

sword = Item("Golden Sword", 100)
potion = Item("Health Potion", 50)

player.add_item(sword)
player.add_item(potion)
player.show_inventory()

print("Бій починається!")

while player.hp > 0 and enemy.hp > 0:
    player.attack(enemy)

    if enemy.hp <= 0:
        print(enemy.name, "переможений! Перемога!")
        break

    enemy.attack(player)

    if player.hp <= 0:
        print(player.name, "загинув... Гра закінчена.")
        break