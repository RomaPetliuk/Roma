from FP3 import Action
class Person:
    name = 'Roma'
    mood = 50
    hp = 100
    money = 0
    def __str__(self):
        return f'{self.name} (hp:{self.hp},' \
               f' mood:{self.mood},' \
               f' money: {self.money})'

    def __init__(self, name, hp=100, mood=50, money=0):
        self.name = name
        self.hp = hp
        self.mood = mood
        self.money = money

    def change_state(self, hp=100, mood=50, money=0):
        self.hp += hp
        self.mood += mood
        self.money += money
        if hp < 0:
            print('я сдох')
        if mood < 0:
            print('я впал в депрессию')
        if money < 0:
            print('я бомж')

    def do(self, Action):
        self.hp += Action.hp
        self.mood += Action.mood
        self.money += Action.money


human = Person(name='Roma', money = 0, mood = 100, hp = 100)
print(human)
human.change_state(
    money=100,
    mood=-20,
    hp=-5
)

print(human)
print('Изменены значения')

human = Person(name = 'Roma', money = 0, mood = 100, hp = 100)

go_to_park = Action(name = 'Сходить в парк', money = 0, mood = 15, hp = 3)
human.do(go_to_park)

print(human)
print('Сходил в парк')

