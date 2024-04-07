
class Action:
    name = 'Roma'
    mood = 50
    hp = 100
    money = 0

    def __init__(self, name, hp=100, mood=50, money=0):
        self.name = name
        self.hp = hp
        self.mood = mood
        self.money = money

