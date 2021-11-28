
v_1 = [int(item) for item in input("Enter the list items : ")]
v_2 = [int(item) for item in input("Enter the list items : ")]
if (len(v_1) == len(v_2)):


    print(f"{v_1}\n{v_2}")

    multiRes = [v_1[i]*v_2[i] for i in range(len(v_2))]
    print(f"dot product = {sum(multiRes)}")

else:
    print("Inputs lengts are not same!!! ")