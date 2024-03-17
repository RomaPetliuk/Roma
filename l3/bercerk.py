from l2.Character1 import Character
class Berserk(Character):
    def __init__(self, name, health = 100, damage = 1, defence = 0):
        super().__init__(name, health, damage, defence)
        self.max_health = health

    def attack(self, target):
        additional_damage = (1 - self.health / self.max_health) * self.damage
        return target.take_damage(
            self.damage + additional_damage
        )