import matplotlib.pyplot as plt
from random import choice



class RandomWalk:
    """Generate random walks"""

    def __init__(self, num_points=5000) -> None:
        """Initialise, set base attributes of a walk"""

        self.num_points = num_points
        self._reset_walk()


    def fill_walk(self, num_points:int = -1, min_step_size:int = 0, max_step_size:int = 5):
        """Generate the points in the walk"""

        # If no value was given for num_points default to the value set by constructor (self.num_points)
        if num_points <= 0: num_points = self.num_points

        # Clear any previous walk
        self._reset_walk()

        while len(self.x_values) < num_points:
            
            x_step = self._get_step(min_step_size, max_step_size)
            y_step = self._get_step(min_step_size, max_step_size)

            # Discard steps that go nowhere
            if x_step == 0 and y_step == 0: continue

            self.x_values.append(self.x_values[-1] + x_step)
            self.y_values.append(self.y_values[-1] + y_step)


    def _get_step(self, min_step_size, max_step_size) -> int:
        """Generate a step in the walk"""
        direction = choice([1, -1])
        distance = choice(range(min_step_size, max_step_size))
        return direction * distance

    
    def _reset_walk(self):
        """Reset self.x_values and self.y_values"""
        # Start at (0, 0)
        self.x_values = [0]
        self.y_values = [0]





rw = RandomWalk()
rw.fill_walk(50000)

fig, ax = plt.subplots(figsize=(16, 9))

ax.scatter(rw.x_values, rw.y_values, c=range(len(rw.x_values)), cmap=plt.cm.viridis, s=1)
ax.scatter(0, 0, color=(0.2, 1, 0.2), s=20)
ax.scatter(rw.x_values[-1], rw.y_values[-1], color=(1, 0.2, 0.2), s=20)

ax.set_title("Random walk", fontsize=16)

# Remove both axes
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

plt.show()
