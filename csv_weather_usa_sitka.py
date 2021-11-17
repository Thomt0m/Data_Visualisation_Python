import csv
from datetime import datetime

import matplotlib.pyplot as plt




filename = 'Data/Weather_USA/sitka_weather_2018_simple.csv'

# Info from file, columns 0 and 1 respectively, extracted by hand for simplicity
station = 'USW00025333'
name = 'SITKA AIRPORT, AK US'

# Header of each column, providing information on the nature of the data
headers = []

# Data to retrieve
dates = []
temp_maxs = []
temp_mins = []


with open(filename) as file:
    reader = csv.reader(file)
    headers = next(reader)

    # Get the desired info from file
    for row in reader:
        dates.append(datetime.strptime(row[2], '%Y-%m-%d'))
        temp_maxs.append(float((int(row[5])-32) * 5/9))
        temp_mins.append(float((int(row[6])-32) * 5/9))






plt.style.use('seaborn')
fig, ax = plt.subplots(sharex=True, figsize=(16, 9))


ax.plot(dates, temp_maxs, color=(1, 0.2, 0.2), label='max')
ax.plot(dates, temp_mins, color=(0.2, 0.2, 1), label='min')
ax.fill_between(dates, temp_maxs, temp_mins, facecolor='blue', alpha=0.1)
ax.set_title('Daily temperatures, 2018', fontsize=20)
fig.autofmt_xdate()
ax.set_ylabel('Temperature (°C)')
ax.legend()


plt.show()



