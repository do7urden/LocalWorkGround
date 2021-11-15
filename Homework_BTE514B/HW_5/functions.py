superSportCars = {
    'Aston Martin Vantage': 1,
    'McLaren570S': 2,
    'FerrariRome': 3,
    'Porsche911_RSR': 2
}

def flip_dickt(var_dick00):
    flipdick = {}
    for key, value in var_dick00.items():
        if value not in flipdick:
            flipdick[value] = key
        else:
            bckflip = flipdick.copy()
            flipdick.update({value:[key,bckflip[value]]})
    return flipdick

def expand_dict(var_dick01):
    expand_dick = {}
    for key, value in var_dick01.items():
       if type(value) is not list:
        expand_dick[value] = key
       else:
           expand_dick[value[-1]] = key
    return expand_dick

b_dic = flip_dickt(superSportCars)
print(f'\n###Function_1 START###\nb_dick= {b_dic}\n###Function_1 END###\n')

c_dic = expand_dict(b_dic)
print(f'\n###Function_2 START###\nc_dic= {c_dic}\n###Function_2 END###\n')


print("The End")
print()