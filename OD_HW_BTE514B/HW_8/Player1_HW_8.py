import itertools

blankBoard_columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J' ]
blankBoard_rows = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


class Player:
    def __init__(self, name, Carrier, BattleShip, Destroyer, Submarine, PatrolBoat):
        self.name = name
        self.Carrier = Carrier.split('/')
        self.BattleShip = BattleShip.split('/')
        self.Destroyer = Destroyer.split('/')
        self.Submarine = Submarine.split('/')
        self.PatrolBoat = PatrolBoat.split('/')

        self.Carrier_Col = (self.Carrier[0])
        self.Carrier_Row = list((self.Carrier[1]))
        self.Carrier_Row = [int(item) for item in self.Carrier_Row]
        self.Carrier = []
        self.Carrier.append(self.Carrier_Col)
        self.Carrier.append(list(self.Carrier_Row))

        self.BattleShip_Col = (self.BattleShip[0])
        self.BattleShip_Row = list((self.BattleShip[1]))
        self.BattleShip_Row = [int(item) for item in self.BattleShip_Row]
        self.BattleShip = []
        self.BattleShip.append(self.BattleShip_Col)
        self.BattleShip.append(list(self.BattleShip_Row))

        self.Destroyer_Col = (self.Destroyer[0])
        self.Destroyer_Row = list((self.Destroyer[1]))
        self.Destroyer_Row = [int(item) for item in self.Destroyer_Row]
        self.Destroyer = []
        self.Destroyer.append(self.Destroyer_Col)
        self.Destroyer.append(list(self.Destroyer_Row))

        self.Submarine_Col = (self.Submarine[0])
        self.Submarine_Row = list((self.Submarine[1]))
        self.Submarine_Row = [int(item) for item in self.Submarine_Row]
        self.Submarine = []
        self.Submarine.append(self.Submarine_Col)
        self.Submarine.append(list(self.Submarine_Row))

        self.PatrolBoat_Col = (self.PatrolBoat[0])
        self.PatrolBoat_Row = list((self.PatrolBoat[1]))
        self.PatrolBoat_Row = [int(item) for item in self.PatrolBoat_Row]
        self.PatrolBoat = []
        self.PatrolBoat.append(self.PatrolBoat_Col)
        self.PatrolBoat.append(list(self.PatrolBoat_Row))

        return

    def Overlapping(self):
        self.cart_Carrier =     itertools.product(self.Carrier[0],      self.Carrier[1])
        self.cart_BattleShip =  itertools.product(self.BattleShip[0],   self.BattleShip[1])
        self.cart_Destroyer =   itertools.product(self.Destroyer[0],    self.Destroyer[1])
        self.cart_Submarine =   itertools.product(self.Submarine[0],    self.Submarine[1])
        self.cart_PatrolBoat =  itertools.product(self.PatrolBoat[0],   self.PatrolBoat[1])

        self.cart_Carrier = list(self.cart_Carrier)
        self.cart_BattleShip = list(self.cart_BattleShip)
        self.cart_Destroyer = list(self.cart_Destroyer)
        self.cart_Submarine = list(self.cart_Submarine)
        self.cart_PatrolBoat = list(self.cart_PatrolBoat)
        self.cart_Total2 = self.cart_Carrier + self.cart_BattleShip + self.cart_Destroyer + self.cart_Submarine + self.cart_PatrolBoat

        for k in self.cart_Total2:
            if self.cart_Total2.count(k) > 1:
                print('Overlapping found, calculating again')
                print(f'overlapping occurred at {k}')
                print("Please re-enter Coordinates")
                break

        return self.cart_Total2
