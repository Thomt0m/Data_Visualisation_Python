import csv


filename = 'Data/Weather_USA/sitka_weather_07-2018_simple.csv'
with open(filename) as file:
    reader = csv.reader(file)
    header_row = next(reader)
    print(header_row)