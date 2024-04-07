from FP1 import Person
import random
human = Person(name = 'Roma', money = 0, mood = 100, hp = 100)
human.change_state(
        money = random.randint(50, 100),
        mood = random.randint(-20, -10),
        hp = random.randint(-10, -5)
    )
print(human)