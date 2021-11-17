import csv
from datetime import datetime

import matplotlib.pyplot as plt




filename = 'Data\\Weather_USA\\death_valley_2018_simple.csv'




# Data to retrieve
headers = []
dates = []
temp_maxs = []
temp_mins = []



with open(filename) as file:
    reader = csv.reader(file)
    headers = next(reader)

    for row in reader:

        date = datetime.strptime(row[2], '%Y-%m-%d')

        try:
            temp_max = float((int(row[4])-32) * 5/9)
            temp_min = float((int(row[5])-32) * 5/9)

        except ValueError:
            print(f'Unable to read data for {date}')

        else:
            dates.append(date)
            temp_maxs.append(temp_max)
            temp_mins.append(temp_min)


plt.style.use('seaborn')
fig, ax = plt.subplots(sharex=True, figsize=(16, 9))


ax.plot(dates, temp_maxs, color=(1, 0.2, 0.2), label='max')
ax.plot(dates, temp_mins, color=(0.2, 0.2, 1), label='min')
ax.fill_between(dates, temp_maxs, temp_mins, facecolor='blue', alpha=0.1)
ax.set_title('Daily temperatures - 2018\nDeath Valley, CA', fontsize=20)
fig.autofmt_xdate()
ax.set_ylabel('Temperature (°C)')
ax.legend()


plt.show()
