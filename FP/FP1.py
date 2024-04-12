from FP3 import Action
from FP4 import Work
from FP4 import Rest
class Person:
    def __str__(self):
        return f'{self.name} (hp:{self.hp},' \
               f' mood:{self.mood},' \
               f' money: {self.money})'

    def __init__(self, name, hp, mood, money):
        self.name = name
        self.hp = hp * 2
        self.mood = mood
        self.money = money

    def change_state(self, hp: int, mood: int, money: int):
        self.hp += hp
        self.mood += mood
        self.money += money
        if hp < 0:
            print('я сдох')
        if mood < 0:
            print('я впал в депрессию')
        if money < 0:
            print('я бомж')

    def do(self, a: Action):

        if type(a) == Work:
            if a.mood > 90:
                self.money += self.money * 0.1
        elif type(a) == Rest:
            if a.hp < 40:
                self.mood -= self.mood * 0.2
        elif type(a) == Action:
            self.hp += a.hp
            self.mood += a.mood
            self.money += a.money



human = Person(name='Roma', money = 0, mood = 100, hp = 100)

print(human)

cook_dinner = Action(name = 'Приготовить поесть', money = 50, mood = 15, hp = 30)
go_to_work = Work(name = 'Прогамирование', money = 1000, mood = 100, hp = 5, power = 2000)
go_to_park = Rest(name = 'Сходить в парк', money = 50, mood = 15, hp = 30, brain = 0)

print('Сходил в парк')
human.do(go_to_park)
print(human)

print('Приготови поесть')
human.do(cook_dinner)
print(human)

print('Прогамирование')
human.do(go_to_work)
print(human)
