class BankAccount:
    def __init__(self, money):
        self.money = money

    def add_money(self, amount):
        if amount < 0:
            raise ValueError("Сума поповнення не може бути від'ємною")
        self.money += amount
        print(f"Поповнено на: {amount}. Баланс: {self.money}")

    def withdraw(self, amount):
        if amount == 0:
            raise ValueError("Сума зняття не може бути 0")

        if amount < 0:
            raise ValueError("Не можна знімати мінус")
        if amount > self.money:
            diff = amount - self.money
            print(f"Недостатньо грошівв. Потрібно ще {diff} грн.")
            answer = input(f"Взяти кредит {diff} грн? (так/ні): ")
            if answer.lower() == "так":
                self.money += diff
                print(f"Кредит надан:). Баланс поповнено на {diff} грн.")
                # Здесь можно добавить логику хранения даты для расчета процентов
            else:
                raise ValueError("Операцію скасовано через відсутність коштів")

        self.money -= amount
        print(f"Знято: {amount}. Залишок: {self.money}")
account = BankAccount(100)
try:
    take = int(input("Скільки зняти коштів? "))
    account.withdraw(take)
except ValueError as e:
    print("Помилка:", e)
