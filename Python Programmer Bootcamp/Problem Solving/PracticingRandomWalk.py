import matplotlib.pyplot as plt
from random import choice
def random_walk(steps, walk_nums):
    options = [1, -1]
    x_axis = list(range(1, steps + 1))
    l = list(range(1, walk_nums + 1))
    for i in range(walk_nums):
        y_axis = [choice(options)]
        for j in range(1, steps):
            y_axis.append(y_axis[j - 1] + choice(options))
        plt.plot(x_axis, y_axis, label = "plot number" + ' ' + str(l[i]))
        plt.xlabel("distance walked")
        plt.ylabel("random movement")
        plt.title("Random Walk")
        plt.legend(loc = "lower left")
    plt.show()

random_walk(10, 5)
