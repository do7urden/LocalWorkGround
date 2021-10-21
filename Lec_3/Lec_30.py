import random

tutulan_sayi = random.randint(1,100)
print(tutulan_sayi)

print('0 ile 100 arasınnda bir sayı tuttum')

while True:

    tahmin = int(input('Tahmin etttiğiniz sayıyı giriniz: '))

    if tahmin > tutulan_sayi:
        print('Yukarida kaldiniz')

        pass # gecici olarak burayı atlatmana yarar. Nasıl bir elif yazacağına karar verdiğinde kaldırabilirisn.

    elif tahmin < tutulan_sayi:
        print('Asagida kaldiniz')

    else:

        print('tebrikler')

    break



