# Take a json file and make it more human-readable by indenting the data


import json


# File to read data from
filename_source = 'Data/Earthquakes/eq_data_1_day_m1.json'
# File to write the data to
filename_readable_output = 'Data/Earthquakes/eq_data_1_day_m1_readable.json'


with open(filename_source) as file:
    eq_data = json.load(file)

with open(filename_readable_output, 'w') as file:
    json.dump(eq_data, file, indent=4)