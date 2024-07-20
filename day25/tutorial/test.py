import pandas
import csv


# with open("weather_data.csv", 'r') as f:
#     data = f.readlines()
#     print(data)


# with open("weather_data.csv", 'r') as f:
#     data = csv.reader(f)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))

#     print(temperatures)

data = pandas.read_csv("weather_data.csv")
print(data['temp'])