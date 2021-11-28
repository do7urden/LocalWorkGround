import csv
import requests

input_path = input(r'please put path of input: ')
output_path = input(r'Please put output path: ')

# input_path = 'C:\OD_HW6\Cities.txt'
# output_path = 'C:\OD_HW6\desired_output.csv'

with open(input_path, 'r',newline='') as cities:
    cityStr = cities.read()
    cityList = cityStr.split("\n")

#Unit = metric ile api dan gelen respone aşağıda metric e çevirildi.
#Rüzgar hızı default da api dan metric gelmekte(m/sn)
str_req = r"https://api.openweathermap.org/data/2.5/weather?q={0}&appid={1}&units=metric"
api_key = "d4d19cad040d7162b7d5c63353b31a6c"


try:
    with open (output_path, "w", newline='') as csvFile:
        fieldnames = ["Sehir Ismi", "Ulke Kodu", "Enlem ve Boylam(metric)", "Sıcaklık(metric)", "Ruzgar Hizi(metric)", "Ruzgar Yonu(derece)"]
        writer = csv.DictWriter(csvFile, fieldnames=fieldnames)
        writer.writeheader()
        for city in cityList:
            response = requests.get(str_req.format(city, api_key))
            my_weather = response.json()
            writer.writerow({"Sehir Ismi" : my_weather['name'], "Ulke Kodu" : my_weather['id'],
                            'Enlem ve Boylam(metric)' : f"{my_weather['coord']['lon']} {my_weather['coord']['lat']}",
                            'Sıcaklık(metric)'          : my_weather['main']['temp'],
                            'Ruzgar Hizi(metric)'       : my_weather['wind']['speed'],
                            'Ruzgar Yonu(derece)'       : my_weather['wind']['deg'],
                         })
except KeyError:
    print(f'{city} city name was not found')