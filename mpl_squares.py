import matplotlib.pyplot as plt



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


fig_rows = 1
fig_columns = 3

# Create a new subplot, positioned in a grid with fig_rows amount of rows, fig_columns amount of columns, at position 1 (index 0 if looked at as an array)
ax01 = plt.subplot(fig_rows, fig_columns, 1)
# Create another subplot
ax02 = plt.subplot(fig_rows, fig_columns, 2)
# Create another subplot
ax03 = plt.subplot(fig_rows, fig_columns, 3)




# ---- PLOT 1, ax01 ----
# Set title, and axis-labels
ax01.set_title("Plot", fontsize=24)
ax01.set_xlabel("Value (x)", fontsize=14)
ax01.set_ylabel("Square value (x²)", fontsize=14)
# Set size of tick labels
ax01.tick_params(axis="both", labelsize=14)
# Plot the values as a line
ax01.plot(values, squares, linewidth=2)
# Highlight anything of interest
ax01.scatter(values[2], squares[2])



# ---- PLOT 2, ax02 ----
ax02.set_title("Scatter", fontsize=24)
ax02.set_xlabel("Value (x)", fontsize=14)
ax02.set_ylabel("Square value (x²)", fontsize=14)
ax02.tick_params(axis="both", which="major", labelsize=14)
ax02.scatter(values, squares)
ax02.scatter(values[2], squares[2])

# ---- PLOT 3, ax03 ----
ax03.set_title("Bars", fontsize=24)
ax03.set_xlabel("Value (x)", fontsize=14)
ax03.set_ylabel("Square value (x²)", fontsize=14)
ax03.tick_params(axis="both", which="major", labelsize=14)
ax03.bar(values, squares)
ax03.bar(values[2], squares[2])








plt.show()