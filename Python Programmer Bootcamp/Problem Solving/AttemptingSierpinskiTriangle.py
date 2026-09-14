from random import randint

import matplotlib.pyplot as plt


def trans1(x, y):
    return 0.5 * x, 0.5 * y

def trans2(x, y):
    return 0.5 * x + 0.5, 0.5 * y + 0.5

def trans3(x, y):
    return 0.5 * x + 1, 0.5 * y

start = (0, 0)
x_axis, y_axis = [], []
for i in range(10000):
    chosen = randint(0, 2)
    match chosen:
        case 0:
            start = trans1(*start)
        case 1:
            start = trans2(*start)
        case 2:
            start = trans3(*start)

    X, Y = zip(*[start])
    x_axis.append(X)
    y_axis.append(Y)
plt.plot(x_axis, y_axis, "o")
plt.show()
