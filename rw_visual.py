import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Make a random walk and plot the points
while True:
    rw = RandomWalk(50000)
    rw.fill_walk()
    
    point_numbers = list(range(rw.num_points))
    # Create the plot, highlighting the start and end of the walk
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=.5)
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    # Remove the axes
    ax = plt.gca()  # Get current axes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
