x = int(input('Please enter a number: '))


def zamazingo(x):
    while True:
        if x % 2 == 0:
            x = x / 2
        else:
            x = 3* x + 1
        return x


print('value of the x', x)