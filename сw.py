class BankAccount:
    def __init__(self, money):
        self.money = money

    def add_money(self, amount):
        if amount < 0:
            raise ValueError("Сума поповнення коштів не може бути від'ємною")
        self.money += amount
        print(f"Поповнено на: {amount}. Баланс: {self.money}")

    def withdraw(self, amount):
        if amount == 0:
            raise ValueError("Сума не може бути 0")
        if amount < 0:
            raise ValueError("Не можна знімати мінус")
        if amount > self.money:
            diff = amount - self.money
            print(f"У вас недостаток грошей. Потрібно ще {diff} грн.")
            answer = input(f"Взяти кредит {diff} грн?: ")

            if answer.lower() == "так":
                days = int(input("На скільки днів берете кредит? "))
                percent = 0.03 if days <= 30 else 0.04
                total_to_pay = diff + (diff * percent)
                self.money = 0
                print(f"Кредит надано: {diff} грн.")
                print(f"Сума до повернення через {days} днів: {total_to_pay:.2f} грн.")
            else:
                raise ValueError("Операцію скасовано через відсутність коштів")
        else:
            self.money -= amount
            print(f"Знято: {amount}. Залишок: {self.money}")
try:
    account = BankAccount(100)
    take = int(input("Скільки зняти грошів? "))
    account.withdraw(take)
except ValueError as e:
    print("Помилка:", e)
