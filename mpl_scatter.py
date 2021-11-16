import matplotlib.pyplot as plt


desired_style = "seaborn-poster"
available_styles = plt.style.available
if desired_style in available_styles:
    plt.style.use(desired_style)



values = range(1, 1001)
squares = [x**2 for x in values]



fig, ax = plt.subplots()


ax.scatter(values, squares, s=10)

# Set the range for x and y axis
ax.axis([0,1100, 0,1.1e6])


ax.set_title("Square numbers", fontsize=24)
ax.set_xlabel("Value (x)", fontsize=14)
ax.set_ylabel("Square value (x²)", fontsize=14)
ax.tick_params(axis='both', which='major', labelsize=14)




plt.show()

