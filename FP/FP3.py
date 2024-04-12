class Action:
    name: str
    money: int
    mood: int
    hp: int
    def __init__(self, name, hp, mood, money):
        self.name = name
        self.hp = hp
        self.mood = mood
        self.money = money