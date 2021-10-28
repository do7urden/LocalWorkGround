val = r"Tolga Ovatman \n"
print(val)

val2 = "Tolga Ovatman"
print(val2, end="")

# r raw string tanımlamana izin verir. Bu sayede string içinde escape karakteri aramaz.

deneme = "' sa  sasas" \
         "asas" \
         "as" \
         "as" \
         "a" \
         "sa" \
         "s"

print(deneme)

triple = ''' sads
asdas
d
as
ds
'''

print(triple)


# in aynı zamanada true false değeri dönen bundan içinde var mı demektri. if içinde de kullanmabilirisin.

print('lg' in 'Tolga')

var1 = 'lg'
var2 = 'Tolga'

print(f"variable is include {var1 in var2}") # dikkat ettiysen sadece tru/false dönüş yapıyor.

