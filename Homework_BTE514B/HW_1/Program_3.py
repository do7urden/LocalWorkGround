year = (input('Enter the year: '))

try:
    year = int(year)

    if (year <= 0):
        print('Year can be neither zero nor negative ')

    else:

        if (year % 100 == 0 and year % 400 != 0):
            print('Year {} is not a leap year'.format(year))

        elif (year % 400 == 0):
            print('Year {} is a leap year'.format(year))

        elif (year % 4 == 0):
            print('Year {} is a leap year'.format(year))

        elif (year % 4 != 0):
            print('Year {} ia not a leap year'.format(year))


except ValueError:
    print('Invalid Input')

