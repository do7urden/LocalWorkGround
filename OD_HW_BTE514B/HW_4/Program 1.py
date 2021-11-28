v_total = []

v_total = [int(item) for item in input("Enter the list items : ")]
if (len(v_total)%2 == 0):




    middle = len(v_total)//2

    v_1 = v_total[:middle]
    v_2 = v_total[middle:]
    print(f"{v_1}\n{v_2}")

    multiRes = [v_1[i]*v_2[i] for i in range(len(v_2))]
    print(f"dot product = {sum(multiRes)}")

else:
    print("Inputs lengts are not same!!! ")
