##### 1
# for döngüsünü kulllanmak için elinde bir küme olması lazım. bu küme içerisindeki değerleri alır for döngüsü.
# 'in' ile bu topluluğun içindeki değerleri alır.
# C deki for dan farklı python daki

for var in "Tolga":
    print(var, end='')
print()
##### 2

for i in range(5): # 0 dan başlar 5 hariç veri oluşturur.
    print(i, end='')

print()

##### 3

for i in range(40,2,-5): # 5 er azaltarak ilerler.
    print(i,end='-')

print()

#####   4

yukseklik = 5

for i in range(yukseklik):
    for j in range(i+1):
        print('*',end='')
    print()

#####   5

print('-5')
yukseklik = 5
for i in range(yukseklik):
    for j in range(yukseklik-i):
        print('*',end='')
    print()

#####   6
print('-6')

yukseklik = 5
for i in range(yukseklik):
    for j in range(yukseklik-i):
        print('.',end='')
    for j in range(i+1):
        print('*', end='')


#####   7
print(-7)

