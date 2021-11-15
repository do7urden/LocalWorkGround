lines = int(input("how many row do you want to input?: "))

count = 0
while count < lines:
    count += 1
    matrix = [int(i) for i in input("Please insert row:")]


print(matrix)