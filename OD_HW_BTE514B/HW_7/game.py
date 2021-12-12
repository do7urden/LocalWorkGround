import random

blankBoard_columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',]
blankBoard_rows = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


class CompBoard:

    name = 'AI'

    Comp_Carrier_row = []
    Comp_Carrier_column = []
    Comp_Carrier_column.append(random.choice(blankBoard_columns))
    Comp_Carrier_row.append(random.choice(blankBoard_rows))

    #####

    Comp_BattleShip_row = []
    Comp_BattleShip_column = []
    Comp_BattleShip_column.append(random.choice(blankBoard_columns))
    Comp_BattleShip_row.append(random.choice(blankBoard_rows))

    #####

    Comp_Destroyer_row = []
    Comp_Destroyer_column = []
    Comp_Destroyer_column.append(random.choice(blankBoard_columns))
    Comp_Destroyer_row.append(random.choice(blankBoard_rows))

    #####

    Comp_Submarine_row = []
    Comp_Submarine_column = []
    Comp_Submarine_column.append(random.choice(blankBoard_columns))
    Comp_Submarine_row.append(random.choice(blankBoard_rows))

    #####

    Comp_PatrolBoat_row = []
    Comp_PatrolBoat_column = []
    Comp_PatrolBoat_column.append(random.choice(blankBoard_columns))
    Comp_PatrolBoat_row.append(random.choice(blankBoard_rows))

    for


    if (Comp_Carrier_row[0] < 5):
        while len(Comp_Carrier_row) < 5:
            lastItem = Comp_Carrier_row[-1]
            Comp_Carrier_row.append(lastItem + 1)
    else:
        while len(Comp_Carrier_row) < 5:
            lastItem = Comp_Carrier_row[-1]
            Comp_Carrier_row.append(lastItem - 1)


    Comp_Carrier = {Comp_Carrier_column[0] : Comp_Carrier_row}

    #####

    if (Comp_BattleShip_row[0] < 4):
        while len(Comp_BattleShip_row) < 4:
            lastItem = Comp_BattleShip_row[-1]
            Comp_BattleShip_row.append(lastItem + 1)
    else:
        while len(Comp_BattleShip_row) < 4:
            lastItem = Comp_BattleShip_row[-1]
            Comp_BattleShip_row.append(lastItem - 1)


    Comp_BattleShip = {Comp_BattleShip_column[0] : Comp_BattleShip_row}

    #####

    if (Comp_Destroyer_row[0] < 3):
        while len(Comp_Destroyer_row) < 3:
            lastItem = Comp_Destroyer_row[-1]
            Comp_Destroyer_row.append(lastItem + 1)
    else:
        while len(Comp_Destroyer_row) < 3:
            lastItem = Comp_Destroyer_row[-1]
            Comp_Destroyer_row.append(lastItem - 1)


    Comp_Destroyer = {Comp_Destroyer_column[0] : Comp_Destroyer_row}

    #####

    if (Comp_Submarine_row[0] < 2):
        while len(Comp_Submarine_row) < 2:
            lastItem = Comp_Submarine_row[-1]
            Comp_Submarine_row.append(lastItem + 1)
    else:
        while len(Comp_Submarine_row) < 2:
            lastItem = Comp_Submarine_row[-1]
            Comp_Submarine_row.append(lastItem - 1)


    Comp_Submarine = {Comp_Submarine_column[0] : Comp_Submarine_row}

    #####

    if (Comp_PatrolBoat_row[0] < 2):
        while len(Comp_PatrolBoat_row) < 2:
            lastItem = Comp_PatrolBoat_row[-1]
            Comp_PatrolBoat_row.append(lastItem + 1)
    else:
        while len(Comp_PatrolBoat_row) < 2:
            lastItem = Comp_PatrolBoat_row[-1]
            Comp_PatrolBoat_row.append(lastItem - 1)


    Comp_PatrolBoat = {Comp_PatrolBoat_column[0] : Comp_PatrolBoat_row}




print(f'CompBoard.Comp_Carrier is {CompBoard.Comp_Carrier}')
print(f'CompBoard.Comp_BattleShip is {CompBoard.Comp_BattleShip}')
print(f'CompBoard.Comp_Destroyer is {CompBoard.Comp_Destroyer}')
print(f'CompBoard.Comp_Submarine is {CompBoard.Comp_Submarine}')
print(f'CompBoard.PatrolBoat is {CompBoard.Comp_PatrolBoat}')