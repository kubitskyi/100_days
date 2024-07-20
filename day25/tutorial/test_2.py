import pandas


data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(data['temp'])

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data['temp'].to_list()

# avg = sum(temp_list) / len(temp_list)
# print(avg)

# print(data['temp'].mean())
# print(data['temp'].max())

# Get data in Columns
# print(data['condition'])
# print(data.condition)

# Get data in Row
# print(data[data.day == 'Monday'])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == 'Monday']
# print(monday.condition)

data_dict = {
    "students" : ['Amy', 'James', 'Angela'],
    "score" : [76, 56, 70]
}

tets_data = pandas.DataFrame(data_dict) # print(tets_data)
tets_data.to_csv('new_data.csv')
