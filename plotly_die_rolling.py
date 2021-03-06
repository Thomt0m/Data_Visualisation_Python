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


    def roll(self, sides) -> int:
        """Roll the die, with a specified number of sides"""
        return randint(1, sides)


    def roll_multiple(self, roll_count:int) -> list:
        """Roll the die a specified number of times"""
        results = []
        for x in range(roll_count):
            results.append(self.roll())
        return results


    def roll_multiple(self, roll_count:int, die_count:int) -> list:
        """Roll a specified number of times with the specified number of dice"""
        results = []
        for roll in range(roll_count):
            results.append(0)
            for die in range(die_count):
                results[-1] += self.roll()
        return results


    def roll_multiple(self, roll_count:int, dice:list = []) -> list:
        """Roll a specified number of times with the specified number of dice, each with the specified number of sides"""
        results = []
        for roll in range(roll_count):
            results.append(0)
            for die in range(len(dice)):
                results[-1] += self.roll(dice[die])
        return results









# ---- Input values ----
number_of_rolls = 1000
die_sides_default = 6
dice = [6, 10]




die = Die(die_sides_default)
# Generate some data
results = die.roll_multiple(number_of_rolls, dice)

# Analyse the result
frequencies = []
for value in range(len(dice), (sum(dice)) + 1):
    frequencies.append(results.count(value))


# Visualise the result
x_values = list(range(len(dice), sum(dice) + 1))

fig = pgo.Figure([pgo.Bar(x=x_values, y=frequencies)])
fig.update_layout(title_text=f'Die rolls ({number_of_rolls}x)')
fig.show()
