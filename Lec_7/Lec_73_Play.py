from LocalWorkGround.Lec_7 import Lec_71_Computer
from LocalWorkGround.Lec_7 import Lec_72_Player1
import itertools
import random

def Action(name, Carrier, BattleShip, Destroyer, Submarine, PatrolBoat):


    AI = Lec_71_Computer.CompBoard(Player0='HAl_9000')
    AI_Ships_All_Coor = AI.Cart()
    print(f'\n#####AI_Ships_All_Coor = {AI_Ships_All_Coor}\n')

    PlayerCoor = Lec_72_Player1.Player(name, Carrier, BattleShip, Destroyer, Submarine, PatrolBoat)
    Player1_All_Coor = PlayerCoor.Overlapping()
    print(f'\n#####Player1_Ships_All Coor = {Player1_All_Coor}\n')

    blankBoard_columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    blankBoard_rows = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    All_Board = itertools.product(blankBoard_columns, blankBoard_rows)
    All_Board = list(All_Board)

    # print(f'All_Board {All_Board}')

    Players = []
    Players.append(AI_Ships_All_Coor)
    Players.append(Player1_All_Coor)
    CurrentPlayer = random.choice(Players)
    # print(f'CurrentPlayer is {CurrentPlayer}')

    while len(AI_Ships_All_Coor) != 0 and len(Player1_All_Coor) != 0:
        if CurrentPlayer == AI_Ships_All_Coor:
            # CurrentPlayer = AI
            # fire = random.choice(All_Board)
            fire = ['A', 1]
            if fire in Player1_All_Coor:

                Player1_All_Coor.remove(fire)
                print(f'Ship hit at {fire}')
                CurrentPlayer = Player1_All_Coor
            else:
                # CurrentPlayer = Player1
                while True:
                    fire = list(input(f'Please type coordinates where you would like to fire: (example: C4) '))
                    try:
                        fire[1] = int(fire[1])
                        fire = tuple(fire)

                    except ValueError:
                        print('Acceptable Rage is (A-J)(0-9)')
                        continue

                    if fire not in All_Board:
                        print('Acceptable Rage is (A-J)(0-9)')
                        continue
                    else:
                        break
                if fire in AI_Ships_All_Coor:
                    AI_Ships_All_Coor.remove(fire)
                    print(f'Ship hit at {fire}')
                    CurrentPlayer = AI_Ships_All_Coor
                else:
                    CurrentPlayer = AI_Ships_All_Coor

        else:
            # CurrentPlayer = Player1
            while True:
                fire = list(input(f'Please type coordinates where you would like to fire: (example: C4) '))
                try:
                    fire[1] = int(fire[1])
                    fire = tuple(fire)
                except ValueError:
                    print('Acceptable Rage is (A-J)(0-9)')
                    continue

                if fire not in All_Board:
                    print('Acceptable Rage is (A-J)(0-9)')
                    continue
                else:
                    break

            if fire in AI_Ships_All_Coor:
                AI_Ships_All_Coor.remove(fire)
                print(f'Ship hit at {fire}')
                CurrentPlayer = AI_Ships_All_Coor
            else:
                # CurrentPlayer = AI
                CurrentPlayer = AI_Ships_All_Coor

    if len(AI_Ships_All_Coor) == 0:
        print(f'{name} Won')
    else:
        print('AI Won!')



name = 'Onurd'
Carrier = 'A/12345'
BattleShip = 'B/6789'
Destroyer = 'C/765'
Submarine = 'D/98'
PatrolBoat = 'J/78'

Action(name, Carrier, BattleShip, Destroyer, Submarine, PatrolBoat)

