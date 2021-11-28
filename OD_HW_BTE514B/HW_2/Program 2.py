values = []
w0 = 0

while w0 < 4:

    w0 +=1
    value = int(input("please add your numbers: "))

    try:
        if value <= 0:
            raise ValueError

    except ValueError:
        print("The number is not positive integer")
        break

    else:
          (values).append(value)

print(values)


w1_i = 0
w1_j = len(values)-1


while w1_i < w1_j:
    values[w1_i], values[w1_j] = values[w1_j], values[w1_i]
    w1_i +=1
    w1_j -=1
print(values)

