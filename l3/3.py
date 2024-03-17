from l2.Character1 import Character
from bercerk import Berserk

player1 = Character('Katyadyra')
player1.show_info()
player2 = Berserk('roma', damage=2)
print(player2)

while True:
    if player1.is_alive() > 0 and player2.is_alive() > 0:
        p1_damage = player2.attack(player1)
        p2_damage = player1.attack(player2)
        print(f'{player2.name} attack {player1.name} '
            f'1 наніс {p1_damage}  шкоди')
        print(player2, player1, sep='\n')
        print(f'{player1.name} attack {player2.name} '
              f'1 наніс {p2_damage}  шкоди')
        print(player1, player2, sep='\n')
    else:
        break

