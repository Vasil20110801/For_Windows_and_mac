import random
def toto():
    win_numbers = []
    for _ in range(6):
        r1 = random.randint(1,49)
        win_numbers.append(r1)


    player_numbers = []
    while len(player_numbers) <= 6:

        try:
            player_input = int(input())
            if player_input not in player_numbers:
                player_numbers.append(player_input)
            else:
                print("Числото го има вече:")
                continue
            break
        except TypeError:
            print("Трябва да въведете цяло число:")
            continue

    obsti_cisla = 0
    for r1 in win_numbers:
        if r1 in win_numbers:
            pass







