import matplotlib.pyplot as plt



# plotting a line

values = []
squares = []
for x in range(1,8):
    values.append(x)
    squares.append(x**2)

# Create a figure 'fig' (matplotlib window) containing a plot 'ax'
fig, ax = plt.subplots()
ax.plot(values, squares, linewidth=2)

# set title, and axis-labels
ax.set_title("Square numbers", fontsize=24)
ax.set_xlabel("Value (x)", fontsize=14)
ax.set_ylabel("Square value (x²)", fontsize=14)

# Set size of tick labels
ax.tick_params(axis="both", labelsize=14)


plt.show()