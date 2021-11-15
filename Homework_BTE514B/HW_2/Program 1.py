input00 = int()
input01 = int()
max = 0
min = None


while True:

    input00 = int(input('Please write a number: '))
    if (input00 == -1):
        print("Process terminated")
        break

    input01 = int(input('Please write a number: '))
    if (input01 == -1):
        print("Process terminated")
        break

    if (min == None):

        if (input00 < input01):
            min = input00

        elif (input01 < input00):
            min = input01


    if (input00 > input01 and input00 > max ):
        max = input00
    elif (input01 > input00 and input01 > max):
        max = input01


    if (input00 < input01 and input00 < min ):
        min = input00

    elif (input01 < input00 and input01 < min):
        min = input01


print(f"The {max} is highest, {min} is lowest number ")

