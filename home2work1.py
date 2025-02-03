class Hero:
    def __init__(self, name, lvl, HP):
        self.name = name
        self.lvl = lvl
        self.HP = HP

    def introduce(self):
        print(f"Привет, меня зовут {self.name}, мой lvl {self.lvl}, мое HP {self.HP}")

    def is_adult(self):
        return self.lvl >= 10

# Создание нескольких экземпляров
hero1 = Hero("бека", 5, 100)
hero2 = Hero("самир", 12, 150)
hero3 = Hero("аяна", 10, 120)

# Проверка метода is_adult
print(f"{hero1.name} is_adult: {hero1.is_adult()}")
print(f"{hero2.name} is_adult: {hero2.is_adult()}")
print(f"{hero3.name} is_adult: {hero3.is_adult()}")