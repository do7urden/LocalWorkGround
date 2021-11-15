base = input("Please type a text: ")

sub = input("Which section will be searched: ")

num = int(input("Which occurrence: "))

count = 0

if sub in base:
    start = 0

    while count < num:
        count += 1
        result = base.find(sub, start)
        start = result + 1

    print(f'"{base}" "{sub}" "{num}" "{result}"')

else:
    print("sub value is not in base!!! ")
