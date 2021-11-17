from random import randint

# Plotly
from plotly import offline
# recommended starting point
import plotly.express as px
# in-depth access point
import plotly.graph_objects as pgo



class Die:
    """A single die"""

    def __init__(self, sides:int = 6) -> None:
        """Initialise a new die"""
        self.sides = sides


    def roll(self) -> int:
        """Roll the die"""
        return randint(1, self.sides)

    def roll_multiple(self, roll_count) -> list:
        """Roll the die a specified number of times"""
        results = []
        for x in range(roll_count):
            results.append(self.roll())
        return results








# ---- Input values ----
number_of_rolls = 1000
die_sides = 6




die = Die(die_sides)
# Generate some data
results = die.roll_multiple(number_of_rolls)

# Analyse the result
frequencies = []
for value in range(1, die.sides+1):
    frequencies.append(results.count(value))


# Visualise the result
x_values = list(range(1, die.sides+1))

fig = pgo.Figure([pgo.Bar(x=x_values, y=frequencies)])
fig.update_layout(title_text=f'Die rolls ({number_of_rolls}x)')
fig.show()
