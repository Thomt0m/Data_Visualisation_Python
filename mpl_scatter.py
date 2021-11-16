import matplotlib.pyplot as plt


desired_style = "seaborn-poster"
available_styles = plt.style.available
if desired_style in available_styles:
    plt.style.use(desired_style)



# Data
values = range(1, 1001)
squares = [x**2 for x in values]





font_size_title = 18
font_size_axis = 12
font_size_tick = 8






plt.figure(figsize=(16, 8))

# Create plots
fig_rows = 1
fig_colums = 3
ax01 = plt.subplot(fig_rows, fig_colums, 1)
ax02 = plt.subplot(fig_rows, fig_colums, 2)
ax03 = plt.subplot(fig_rows, fig_colums, 3)


# ---- PLOT 01, ax01 ----
ax01.scatter(values, squares, color='green', s=10)
# Set the range for x and y axis
ax01.axis([0,1100, 0,1.1e6])

ax01.set_title("Square numbers (01)", fontsize=font_size_title)
ax01.set_xlabel("Value (x)", fontsize=font_size_axis)
ax01.set_ylabel("Square value (x²)", fontsize=font_size_axis)
ax01.tick_params(axis='both', which='major', labelsize=font_size_tick)


# ---- PLOT 02, ax02 ----
ax02.scatter(values, squares, color=(0.8, 0.2, 0.2), s=10)

ax02.set_title("Square numbers (02)", fontsize=font_size_title)
ax02.set_xlabel("Value (x)", fontsize=font_size_axis)
ax02.set_ylabel("Square value (x²)", fontsize=font_size_axis)
ax02.tick_params(axis='both', which='major', labelsize=font_size_tick)


# ---- PLOT 03, ax03 ----
# Using a colourmap to create a visual differance between values
ax03.scatter(values, squares, c=squares, cmap=plt.cm.Blues, s=10)

ax03.set_title("Square numbers (03)", fontsize=font_size_title)
ax03.set_xlabel("Value (x)", fontsize=font_size_axis)
ax03.set_ylabel("Square value (x²)", fontsize=font_size_axis)
ax03.tick_params(axis='both', which='major', labelsize=font_size_tick)






# Print the figure to file
print_to_file = False
if print_to_file:
    plt.savefig(fname='mpl_scatter.png')



plt.show()



