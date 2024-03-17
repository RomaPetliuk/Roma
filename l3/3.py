from l2.character import Character
from berserk import berserk


player1 = Character('Roma', damage=15)
player1.show_info()

player2 = berserk('Kata', damage=10)
print(player2)

while player1.is_alive() and player2.is_alive():
      p1_damage = player1.attack(player2)
      print(f'{player1.name} атакував {player2.name} '
            f'і наніс {p1_damage} шкоди.')

      p2_damage = player2.attack(player1)
      print(f'{player2.name} атакував {player1.name} '
            f'і наніс {p2_damage} шкоди.')

      print(player1, player2, sep='\n')

print(player1, player2, sep='\n')

