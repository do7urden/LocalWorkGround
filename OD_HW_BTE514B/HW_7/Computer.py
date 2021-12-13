import random
import itertools

blankBoard_columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',]
blankBoard_rows = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def Board():

    name = 'HAL_9000'

    Comp_Carrier_row = []
    Comp_Carrier_column = []
    Comp_Carrier_column.append(random.choice(blankBoard_columns))
    Comp_Carrier_row.append(random.choice(blankBoard_rows))

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
    Comp_BattleShip_row = []
    Comp_BattleShip_column = []
    Comp_BattleShip_column.append(random.choice(blankBoard_columns))
    Comp_BattleShip_row.append(random.choice(blankBoard_rows))

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
    Comp_Destroyer_row = []
    Comp_Destroyer_column = []
    Comp_Destroyer_column.append(random.choice(blankBoard_columns))
    Comp_Destroyer_row.append(random.choice(blankBoard_rows))

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

    Comp_Submarine_row = []
    Comp_Submarine_column = []
    Comp_Submarine_column.append(random.choice(blankBoard_columns))
    Comp_Submarine_row.append(random.choice(blankBoard_rows))
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
    Comp_PatrolBoat_row = []
    Comp_PatrolBoat_column = []

    Comp_PatrolBoat_column.append(random.choice(blankBoard_columns))
    Comp_PatrolBoat_row.append(random.choice(blankBoard_rows))

    if (Comp_PatrolBoat_row[0] < 2):
        while len(Comp_PatrolBoat_row) < 2:
            lastItem = Comp_PatrolBoat_row[-1]
            Comp_PatrolBoat_row.append(lastItem + 1)
    else:
        while len(Comp_PatrolBoat_row) < 2:
            lastItem = Comp_PatrolBoat_row[-1]
            Comp_PatrolBoat_row.append(lastItem - 1)


    Comp_PatrolBoat = {Comp_PatrolBoat_column[0] : Comp_PatrolBoat_row}

    ##### OverlapCheck

    Carrier_Coor = list(Comp_Carrier.keys()) + list(Comp_Carrier.values())
    BattleShip_Coor = list(Comp_BattleShip.keys()) + list(Comp_BattleShip.values())
    Destroyer_Coor = list(Comp_Destroyer.keys()) + list(Comp_Destroyer.values())
    Submarine_Coor = list(Comp_Submarine.keys()) + list(Comp_Submarine.values())
    PatrolBoat_Coor = list(Comp_PatrolBoat.keys()) + list(Comp_PatrolBoat.values())
    #
    # print(f'Carrier_Coor is {Carrier_Coor}')
    # print(f'BattleShip_Coor is {BattleShip_Coor}')
    # print(f'Destroyer_Coor is {Destroyer_Coor}')
    # print(f'Submarine_Coor is {Submarine_Coor}')
    # print(f'PatrolBoat_Coor is {PatrolBoat_Coor}')

    cart_Carrier = itertools.product(Carrier_Coor[0], Carrier_Coor[1])
    cart_BattleShip = itertools.product(BattleShip_Coor[0], BattleShip_Coor[1])
    cart_Destroyer = itertools.product(Destroyer_Coor[0], Destroyer_Coor[1])
    cart_Submarine = itertools.product(Submarine_Coor[0], Submarine_Coor[1])
    cart_PatrolBoat = itertools.product(PatrolBoat_Coor[0], PatrolBoat_Coor[1])
    cart_Total = list(cart_Carrier) + list(cart_BattleShip) + list(cart_Destroyer) + list(cart_Submarine) + list(cart_PatrolBoat)

    # print(f'cart_Total {cart_Total}')
    # print()
    # Comp_Coordinates = []
    Comp_Coordinates = [cart_Total, Carrier_Coor, BattleShip_Coor, Destroyer_Coor, Submarine_Coor, PatrolBoat_Coor]
    return Comp_Coordinates


Comp_Coordinates = CompBoard()
cart_Total = Comp_Coordinates[0]
print(f'cart_Total is {cart_Total}')


while True:
    for k in cart_Total:
        if cart_Total.count(k) > 1:
            print('Overlapping found, calculating again')
            print(f'k is {k}')
            cart_Total = CompBoard()
            continue
    break



print(f'Board.Comp_Carrier is {Comp_Coordinates[1]}')
print(f'Board.Comp_BattleShip is {Comp_Coordinates[2]}')
print(f'Board.Comp_Destroyer is {Comp_Coordinates[3]}')
print(f'Board.Comp_Submarine is {Comp_Coordinates[4]}')
print(f'Board.PatrolBoat is {Comp_Coordinates[5]}')