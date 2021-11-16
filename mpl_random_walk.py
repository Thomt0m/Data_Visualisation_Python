import matplotlib.pyplot as plt
from random import choice

import numpy



class RandomWalk:
    """Generate random walks"""

    def __init__(self, num_points=5000) -> None:
        """Initialise, set base attributes of a walk"""

        self.num_points = num_points

        # Starting point (0, 0)
        self.x_values = [0]
        self.y_values = [0]


    def fill_walk(self, num_points:int = -1, min_step_size:int = 0, max_step_size:int = 5):
        """Generate the points in the walk"""

        # If no value was given for num_points default to the value set by constructor (self.num_points)
        if num_points <= 0: num_points = self.num_points

        # Clear any previous walks
        self.x_values.clear()
        self.y_values.clear()
        # Start at (0, 0)
        self.x_values = [0]
        self.y_values = [0]

        while len(self.x_values) < num_points:

            x_direction = choice([1, -1])
            x_distance = choice(range(min_step_size, max_step_size))
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice(range(min_step_size, max_step_size))
            y_step = y_direction * y_distance

            # Discard steps that go nowhere
            if x_step == 0 and y_step == 0: continue

            self.x_values.append(self.x_values[-1] + x_step)
            self.y_values.append(self.y_values[-1] + y_step)




rw = RandomWalk()
rw.fill_walk()

plt.scatter(rw.x_values, rw.y_values, c=range(len(rw.x_values)), cmap=plt.cm.viridis, s=6)
plt.scatter(0, 0, color=(0.2, 1, 0.2), s=20)
plt.scatter(rw.x_values[-1], rw.y_values[-1], color=(1, 0.2, 0.2), s=20)
plt.show()
