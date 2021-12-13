import random
import itertools





class CompBoard:

    
    def __init__(self):
        self.name = 'HAL_9000'
        

    def Ships(self):
        blankBoard_columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', ]
        blankBoard_rows = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

        self.Comp_Carrier_row = []
        self.Comp_Carrier_column = []
        self.Comp_Carrier_column.append(random.choice(blankBoard_columns))
        self.Comp_Carrier_row.append(random.choice(blankBoard_rows))
        
        if (self.Comp_Carrier_row[0] < 5):
            while len(self.Comp_Carrier_row) < 5:
                lastItem = self.Comp_Carrier_row[-1]
                self.Comp_Carrier_row.append(lastItem + 1)
        else:
            while len(self.Comp_Carrier_row) < 5:
                self.lastItem = self.Comp_Carrier_row[-1]
                self.Comp_Carrier_row.append(self.lastItem - 1)


        self.Comp_Carrier = {self.Comp_Carrier_column[0] : self.Comp_Carrier_row}

    
        self.Comp_BattleShip_row = []
        self.Comp_BattleShip_column = []
        self.Comp_BattleShip_column.append(random.choice(blankBoard_columns))
        self.Comp_BattleShip_row.append(random.choice(blankBoard_rows))

        if (self.Comp_BattleShip_row[0] < 4):
            while len(self.Comp_BattleShip_row) < 4:
                lastItem = self.Comp_BattleShip_row[-1]
                self.Comp_BattleShip_row.append(lastItem + 1)
        else:
            while len(self.Comp_BattleShip_row) < 4:
                lastItem = self.Comp_BattleShip_row[-1]
                self.Comp_BattleShip_row.append(lastItem - 1)


        self.Comp_BattleShip = {self.Comp_BattleShip_column[0] : self.Comp_BattleShip_row}

        #####
        self.Comp_Destroyer_row = []
        self.Comp_Destroyer_column = []
        self.Comp_Destroyer_column.append(random.choice(blankBoard_columns))
        self.Comp_Destroyer_row.append(random.choice(blankBoard_rows))

        if (self.Comp_Destroyer_row[0] < 3):
            while len(self.Comp_Destroyer_row) < 3:
                lastItem = self.Comp_Destroyer_row[-1]
                self.Comp_Destroyer_row.append(lastItem + 1)
        else:
            while len(self.Comp_Destroyer_row) < 3:
                lastItem = self.Comp_Destroyer_row[-1]
                self.Comp_Destroyer_row.append(lastItem - 1)


        self.Comp_Destroyer = {self.Comp_Destroyer_column[0] : self.Comp_Destroyer_row}

        #####

        self.Comp_Submarine_row = []
        self.Comp_Submarine_column = []
        self.Comp_Submarine_column.append(random.choice(blankBoard_columns))
        self.Comp_Submarine_row.append(random.choice(blankBoard_rows))
        if (self.Comp_Submarine_row[0] < 2):
            while len(self.Comp_Submarine_row) < 2:
                lastItem = self.Comp_Submarine_row[-1]
                self.Comp_Submarine_row.append(lastItem + 1)
        else:
            while len(self.Comp_Submarine_row) < 2:
                lastItem = self.Comp_Submarine_row[-1]
                self.Comp_Submarine_row.append(lastItem - 1)


        self.Comp_Submarine = {self.Comp_Submarine_column[0] : self.Comp_Submarine_row}

        #####
        self.Comp_PatrolBoat_row = []
        self.Comp_PatrolBoat_column = []

        self.Comp_PatrolBoat_column.append(random.choice(blankBoard_columns))
        self.Comp_PatrolBoat_row.append(random.choice(blankBoard_rows))

        if (self.Comp_PatrolBoat_row[0] < 2):
            while len(self.Comp_PatrolBoat_row) < 2:
                lastItem = self.Comp_PatrolBoat_row[-1]
                self.Comp_PatrolBoat_row.append(lastItem + 1)
        else:
            while len(self.Comp_PatrolBoat_row) < 2:
                lastItem = self.Comp_PatrolBoat_row[-1]
                self.Comp_PatrolBoat_row.append(lastItem - 1)


        self.Comp_PatrolBoat = {self.Comp_PatrolBoat_column[0] : self.Comp_PatrolBoat_row}

        self.Comp_Coor_ListDict = [self.Comp_Carrier, self.Comp_BattleShip, self.Comp_Destroyer, self.Comp_Submarine, self.Comp_PatrolBoat]

        return self.Comp_Coor_ListDict
##### OverlapCheck




    def Cart(self):

        self.Carrier_Coor = list(self.Comp_Carrier.keys()) + list(self.Comp_Carrier.values())
        self.BattleShip_Coor = list(self.Comp_BattleShip.keys()) + list(self.Comp_BattleShip.values())
        self.Destroyer_Coor = list(self.Comp_Destroyer.keys()) + list(self.Comp_Destroyer.values())
        self.Submarine_Coor = list(self.Comp_Submarine.keys()) + list(self.Comp_Submarine.values())
        self.PatrolBoat_Coor = list(self.Comp_PatrolBoat.keys()) + list(self.Comp_PatrolBoat.values())

        print(f'Carrier_Coor is {self.Carrier_Coor}')
        print(f'BattleShip_Coor is {self.BattleShip_Coor}')
        print(f'Destroyer_Coor is {self.Destroyer_Coor}')
        print(f'Submarine_Coor is {self.Submarine_Coor}')
        print(f'PatrolBoat_Coor is {self.PatrolBoat_Coor}')

        self.cart_Carrier = itertools.product(self.Carrier_Coor[0], self.Carrier_Coor[1])
        self.cart_BattleShip = itertools.product(self.BattleShip_Coor[0], self.BattleShip_Coor[1])
        self.cart_Destroyer = itertools.product(self.Destroyer_Coor[0], self.Destroyer_Coor[1])
        self.cart_Submarine = itertools.product(self.Submarine_Coor[0], self.Submarine_Coor[1])
        self.cart_PatrolBoat = itertools.product(self.PatrolBoat_Coor[0], self.PatrolBoat_Coor[1])
        self.cart_Total = list(self.cart_Carrier) + list(self.cart_BattleShip) + list(self.cart_Destroyer) + list(self.cart_Submarine) + list(self.cart_PatrolBoat)

        # aşağıyı sil
        # self.cart_Carrier = itertools.product(self.Carrier[0], self.Carrier[1])
        # self.self.cart_BattleShip = itertools.product(self.BattleShip[0], self.BattleShip[1])
        # self.self.cart_Destroyer = itertools.product(self.Destroyer[0], self.Destroyer[1])
        # self.self.cart_Submarine = itertools.product(self.Submarine[0], self.Submarine[1])
        # self.self.cart_PatrolBoat = itertools.product(self.PatrolBoat[0], self.PatrolBoat[1])
        # self.self.cart_Total = list(self.cart_Carrier) + list(self.self.cart_BattleShip) + list(self.self.cart_Destroyer) + list(self.Submarine) + list(self.PatrolBoat)
        #
        # self.Comp_Coordinates = [self.self.cart_Total, self.Carrier, self.BattleShip, self.Destroyer, self.Submarine, self.PatrolBoat]
        #
        # print(f'self.cart_Total {self.cart_Total}')
        # print()
        # self.Comp_Coordinates = []
        # self.Comp_Coordinates = [self.cart_Total, self.Carrier_Coor, self.BattleShip_Coor, self.Destroyer_Coor, self.Submarine_Coor, self.PatrolBoat_Coor] ##
        return self.cart_Total

    def OverlappingCheck(self):
        # self.Comp_Coordinates = CompBoard()
        self.cart_Total = CompBoard.Cart(self)
        print(f'self.cart_Total is {self.cart_Total}')
    
        while True:
            for k in self.cart_Total:
                if self.cart_Total.count(k) > 1:
                    print('Overlapping found, calculating again')
                    print(f'k is {k}')
                    ReGen = CompBoard.Ships()
                    self.cart_Total = ReGen
                    continue
            break

    AI_Coor = Cart(self)

    
# print(f'Board.Comp_Carrier is {HAL_9000.Cart()}')
# print(f'Board.self.Comp_BattleShip is {CompBoard.Comp_Coordinates[2]}')
# print(f'Board.Comp_Destroyer is {CompBoard.Comp_Coordinates[3]}')
# print(f'Board.Comp_Submarine is {CompBoard.Comp_Coordinates[4]}')
# print(f'Board.PatrolBoat is {CompBoard.Comp_Coordinates[5]}')

HAl_9000 = CompBoard()
HAl_9000.Ships()

print(f'All_Ships_Coordinates = {HAl_9000.Cart()}')
print()

print(HAl_9000.AI_Coor)
# print(HAl_9000.OverlappingCheck())