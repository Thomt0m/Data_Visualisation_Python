import matplotlib.pyplot as plt
from matplotlib.style import available



# plotting a line

values = []
squares = []
for x in range(1,8):
    values.append(x)
    squares.append(x**2)

# Select a UI-style to use
available_styles = plt.style.available
# Set style == "seaborn"
plt.style.use(available_styles[9])





# Create a figure containing plots
fig = plt.figure()


# Create a new subplot, positioned in a grid with 1 row, 2 columns, at index 1
ax01 = plt.subplot(1, 2, 1)
# Create another subplot
ax02 = plt.subplot(1, 2, 2)




# ---- PLOT 1, ax01 ----
# Set title, and axis-labels
ax01.set_title("Square numbers", fontsize=24)
ax01.set_xlabel("Value (x)", fontsize=14)
ax01.set_ylabel("Square value (x²)", fontsize=14)
# Set size of tick labels
ax01.tick_params(axis="both", labelsize=14)
# Plot the values as a line
ax01.plot(values, squares, linewidth=2)
# Highlight anything of interest using scatter()
ax01.scatter(values[2], squares[2])



# ---- PLOT 2, ax0 ----
ax02.set_title("Square numbers", fontsize=24)
ax02.set_xlabel("Value (x)", fontsize=14)
ax02.set_ylabel("Square value (x²)", fontsize=14)
ax02.tick_params(axis="both", which="major", labelsize=14)
ax02.scatter(values[2], squares[2])








plt.show()