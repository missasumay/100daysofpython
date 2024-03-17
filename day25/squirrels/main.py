import pandas

data = pandas.read_csv("day25\\squirrels\\2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Amount": [gray_squirrels_count, red_squirrels_count, black_squirrels_count],
}

df = pandas.DataFrame(data_dict)

print(df)