from LocalWorkGround.Lec_7 import Lec_71_Computer
from LocalWorkGround.Lec_7 import Lec_72_Player1
import itertools
import random

def Action(name, Carrier, BattleShip, Destroyer, Submarine, PatrolBoat):


    AI = Lec_71_Computer.CompBoard(Player0='HAl_9000')
    AI_Ships_All_Coor = AI.Cart()
    print(f'\nAI_Ships_All_Coor = {AI_Ships_All_Coor}\n')

    PlayerCoor = Lec_72_Player1.Player(name, Carrier, BattleShip, Destroyer, Submarine, PatrolBoat)
    Player1_All_Coor = PlayerCoor.Overlapping()
    print(f'Player1_Ships_All Coor = {Player1_All_Coor}')

    blankBoard_columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    blankBoard_rows = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    All_Board = itertools.product(blankBoard_columns, blankBoard_rows)
    All_Board = list(All_Board)

    print(f'All_Board {All_Board}')

    Players = []
    Players.append(AI_Ships_All_Coor)
    Players.append(Player1_All_Coor)
    CurrentPlayer = random.choice(Players)
    print(f'CurrentPlayer is {CurrentPlayer}')

    while len(AI_Ships_All_Coor) != 0 and len(Player1_All_Coor) != 0:
        if CurrentPlayer == AI_Ships_All_Coor:
            fire = random.choice(All_Board)
            if fire in Player1_All_Coor:
                Player1_All_Coor.remove(fire)
                CurrentPlayer = Player1_All_Coor
            else:
                CurrentPlayer = Player1_All_Coor
                fire = random.choice(All_Board)
                if fire in AI_Ships_All_Coor:
                    AI_Ships_All_Coor.remove(fire)
        else:
            # CurrentPlayer = Player1_All_Coor
            fire = random.choice(All_Board)
            if fire in AI_Ships_All_Coor:
                AI_Ships_All_Coor.remove(fire)
                CurrentPlayer = AI_Ships_All_Coor
            else:
                CurrentPlayer = AI_Ships_All_Coor

    if len(AI_Ships_All_Coor) == 0:
        print('Player1 Won')
    else:
        print('AI Won!')










name = 'onur'
Carrier = 'A/12345'
BattleShip = 'B/6789'
Destroyer = 'C/765'
Submarine = 'D/98'
PatrolBoat = 'J/78'

Action(name, Carrier, BattleShip, Destroyer, Submarine, PatrolBoat)
