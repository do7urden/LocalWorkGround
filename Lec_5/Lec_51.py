# Listeler içerisinde hem integer lar da string de aritmetik operatörlere maruz kalabilir.

a_list = [0, 1, 2]
b_list = [3 ,4, 5]
print (a_list + b_list)
a_list.append(b_list) # b_list i tek bir eleman olarak(liste olarak) a_list üzerine ekler! Ayrıca append func.ı liste üzerinde çalışır dolayısıyla print içine yazarsan hata verir.
print(a_list)


# a_list == b_list dediğinde listelerin içeriğini kontrol ediyor. a_list is b_list ise adresleri kontrol ediyor aynı mı diye.

# pass_by_value ve pass_by_reference konularına bakabilirsin. Mevzu functiona value mu adres mi gönderiyorsun muhabbeti. Function içine gönderdiğin değer ile func. içindeki işlemler yapılırken memory de yer kaplar func. bitttikten sonra memory de aldığı değer silinir.

# listelerde düz = dersen adres kopyalarsın. b_list = a_list.copy() (shallow copy denir buna) ile içeriğini kopyalarsın ve farklı bir adreste tutulur bu liste dolayısıyla copyada yapılan değişiklik ilk listede etkisi olmaz.

