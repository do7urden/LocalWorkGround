print("******************* Both functions ******************\n")

print(f"##### First Programme Start #####\n\n")
def HW_3_1():
    import random


    def diceRan():
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        return dice1, dice2

    def diceSum(dice1, dice2):
        total = dice1 + dice2
        return total


    dice1, dice2 = diceRan()

    if dice1 != dice2:
        print(f"Result is {diceSum(dice1, dice2)}")
    else:
        res = 0
        while dice1 == dice2:

            res += diceSum(dice1, dice2)
            dice1, dice2 = diceRan()

        print(f"Result is {res + dice1 + dice2}")
HW_3_1()
print(f"\n\n##### First Programme End #####\n\n")



print(f"##### Second Programme Start #####\n\n")

def HW_3_2 (P0,i,req):

    countYear = 0
    while P0 <= req :
            countYear += 1
            P0 = (P0*i) + P0

    print(f"\n{countYear} years required for wanted income")

P0 = int(input(f"Please type principal: "))
i = float(input(f"Please type interest value: "))
req = int(input(f"Please type required outcome: "))
HW_3_2(P0,i,req)






print(f"\n\n##### Second Programme End #####")

print("******************* Both functions ******************")

