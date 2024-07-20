import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])

print(grey_squirrel_count)
print(red_squirrel_count)
print(black_squirrel_count)


data_dict = {
    "Primary Fur Color" : ["Gray", "Cinnamon", "Black"],
    "Count" : [grey_squirrel_count, red_squirrel_count, black_squirrel_count]
}

new_data = pandas.DataFrame(data_dict)
print(new_data)
new_data.to_csv("squirrel_count.csv")