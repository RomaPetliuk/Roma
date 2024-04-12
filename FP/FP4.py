from FP3 import Action
class Work(Action):
    name: str
    money: int
    mood: int
    hp: int
    power: int
    def __init__(self, name, money, mood, hp, power):
        super().__init__(name, hp, mood, money)
        self.power = power
class Rest(Action):
    name: str
    money: int
    mood: int
    hp: int
    brain: int
    def __init__(self, name, money, mood, hp, brain):
        super().__init__(name, hp, mood, money)
        self.brain = brain