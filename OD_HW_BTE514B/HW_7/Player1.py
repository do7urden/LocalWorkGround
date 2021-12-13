import itertools

blankBoard_columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',]
blankBoard_rows = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# name = input(f'Name = ')
# Carrier = input(f'Carrier_Coor(column(A-J)/row(5X)')
# BattleShip = input(f'BattleShip_Coor(column(A-J)/row(4X)')
# Destroyer = input(f'Destroyer_Coor(column(A-J)/row(3X)')

name = 'onur'
Carrier = 'A/12345'
BattleShip = 'B/1234'
Destroyer = 'C/123'

# name = input(f'Name = '),
# Carrier = input(f'Carrier_Coor(column(A-J)/row(5X)'),
# BattleShip = input(f'BattleShip_Coor(column(A-J)/row(4X)'),
# Destroyer = input(f'Destroyer_Coor(column(A-J)/row(3X)')

class Player:
    def __init__(self, name, Carrier, BattleShip, Destroyer):
        self.name = name
        self.Carrier = Carrier.split('/')
        self.BattleShip = BattleShip.split('/')
        self.Destroyer = Destroyer.split('/')

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



    def Overlapping(self):
        self.cart_Carrier = itertools.product(self.Carrier[0], self.Carrier[1])
        self.cart_BattleShip = itertools.product(self.BattleShip[0], self.BattleShip[1])
        self.cart_Destroyer = itertools.product(self.Destroyer[0], self.Destroyer[1])
        # cart_Submarine = itertools.product(Submarine_Coor[0], Submarine_Coor[1])
        # cart_PatrolBoat = itertools.product(PatrolBoat_Coor[0], PatrolBoat_Coor[1])
        self.cart_Total = list(self.cart_Carrier) + list(self.cart_BattleShip) + list(self.cart_Destroyer)

        self.Comp_Coordinates = [self.cart_Total, self.Carrier, self.BattleShip, self.Destroyer]

        return self.Comp_Coordinates


Player1 = Player(name,Carrier,BattleShip,Destroyer)

Comp_Coordinates = Player1.Overlapping()
cart_Total = Comp_Coordinates[0]
print(f'cart_Total is {cart_Total}')

while True:
    for k in cart_Total:
        if cart_Total.count(k) > 1:
            print('Overlapping found, calculating again')
            print(f'overlapping occured at {k}')
            print("Please re-enter Coordinats")
            break
    break

print(Player1.name)
print(Player1.Carrier)
print(Player1.BattleShip)
print(Player1.Destroyer)