day1 = input("HH:MM farmat input: ")
day2 = input("HH:MM farmat input: ")

day1= (day1.split(":"))
day2= (day2.split(":"))

day1_hour = day1[0]
day1_min = day1[1]

day2_hour = day2[0]
day2_min = day2[1]

try:
    if day1_hour > day2_hour:
        print(f"Former time is {day1}")

    elif day2_hour > day1_hour:
        print(f"Former time is {day2}")

    else:
        if day1_min > day2_min:
            print(f"Former time is {day1}")

        elif day1_min < day2_min:
            print(f"Former time is {day2}")

        else:
            print(f"{day1} and {day2} is the exactly same moment")
    raise Exception ("Yanlis birim")

except:
    print("app error")
