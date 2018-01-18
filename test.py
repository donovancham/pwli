#!/usr/bin/python3.4
import pyowmWeather
import json

# location = "kumamoto"
# output = updatecache(location)
# final = output[1]
# print(final)

result = {'1/21': {'6': {'Temperature': 10.33, 'ID': 500}, '18': {'Temperature': 2.04, 'ID': 500}, '9': {'Temperature': 5.96, 'ID': 801}, '12': {'Temperature': 0.98, 'ID': 802}, '15': {'Temperature': 0.07, 'ID': 803}, '21': {'Temperature': 2.23, 'ID': 501}, '0': {'Temperature': 1.95, 'ID': 800}, '3': {'Temperature': 10.11, 'ID': 802}}, '1/20': {'6': {'Temperature': 10.08, 'ID': 801}, '18': {'Temperature': -1.97, 'ID': 802}, '9': {'Temperature': 5.37, 'ID': 803}, '12': {'Temperature': 0.69, 'ID': 803}, '15': {'Temperature': 0.27, 'ID': 804}, '21': {'Temperature': -2.69, 'ID': 801}, '0': {'Temperature': 2.58, 'ID': 801}, '3': {'Temperature': 9.21, 'ID': 800}}, '1/19': {'6': {'Temperature': 10.55, 'ID': 500}, '18': {'Temperature': 3.04, 'ID': 500}, '9': {'Temperature': 5.65, 'ID': 500}, '12': {'Temperature': 2.43, 'ID': 500}, '15': {'Temperature': 3.96, 'ID': 500}, '21': {'Temperature': -1.34, 'ID': 800}, '0': {'Temperature': 1.79, 'ID': 500}, '3': {'Temperature': 8.63, 'ID': 500}}, '1/18': {'12': {'Temperature': -0.71, 'ID': 800}, '15': {'Temperature': -2.5, 'ID': 800}, '21': {'Temperature': -4.41, 'ID': 801}, '18': {'Temperature': -3.91, 'ID': 800}, '9': {'Temperature': 5.72, 'ID': 800}}, '1/22': {'6': {'Temperature': 6.79, 'ID': 500}, '18': {'Temperature': 3.48, 'ID': 500}, '9': {'Temperature': 3.23, 'ID': 500}, '12': {'Temperature': 0.76, 'ID': 800}, '15': {'Temperature': 1.82, 'ID': 500}, '21': {'Temperature': 3.31, 'ID': 500}, '0': {'Temperature': 3.51, 'ID': 501}, '3': {'Temperature': 6.98, 'ID': 501}}}

f = open("data.txt", "w")
f.write(str(result))
f.close()

p = open("data.txt", "r")
data = json.loads(p.readline().replace("'", "\""))

listdays = []
daytimes = []

for key in data.keys():
    listdays.append(key)
listdays.sort()
print("Forecast for: ", listdays, sep='\t')

day = listdays[0]
for key in result[day].keys():
    daytimes.append(key)
daytimes.sort(key=int)

lol = data[day][daytimes[0]]
print(lol["ID"], lol["Temperature"], sep='\n')