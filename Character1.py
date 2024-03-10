class Character:
    name = ''
    hp = 100
    damage = 1
    Def = 0

    def __init__(self, name, hp=100, damage=1, Def=0):
        self.name = name
        self.hp = hp
        self.Def = Def
        self.damage = damage

    def show_info(self):
        print(self.__str__())

    def __str__(self):
        return f' = {self.name} =\n' \
              f' hp: {self.hp} \n' \
              f' Def: {self.Def}\n' \
              f'Damage: {self.damage}\n' \

    def take_damage(self, damage):
        self.hp -= damage
        return damage

    def attack(self, target):
        return target.take_damage(self.damage)
