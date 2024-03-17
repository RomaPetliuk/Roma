from vampir import vampir
from l2.Character1 import Character

player1 = vampir('Roma', damage=10)
player1.show_info()

player2 = Character('Kata', damage=5)


while player1.is_alive() and player2.is_alive():
      p1_damage = player1.attack(player2)
      print(f'{player1.name} атакував {player2.name} '
            f'і наніс {p1_damage} шкоди.')

      p2_damage = player2.attack(player1)
      print(f'{player2.name} атакував {player1.name} '
            f'і наніс {p2_damage} шкоди.')

      print(player1, player2, sep='\n')

print(player1, player2, sep='\n')

