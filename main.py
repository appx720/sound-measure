import matplotlib.pyplot as plt
import numpy as np
import math


def get_radius(dB1, dB2):
    """
    return radius(distance) from center
    ~~~~~~
    dB1: dacibel from standard point
    dB2: dacibel from target point
    """
    l2 = math.pow(10, (dB1 - dB2) / 20)
    return l2



plt.figure(figsize = (5, 5))
center = [[0, 0], [0, 1.7], [1.7, 1.7], [1.7, 0]]

dB1 = 69
dB2 = [68, 65, 0, 71]

for i in range(4):
    radius = get_radius(dB1, dB2[i])

    theta = np.linspace(0, 2 * np.pi, 100)
    x = center[i][0] + radius * np.cos(theta)
    y = center[i][1] + radius * np.sin(theta)

    plt.plot(x, y)


plt.xlim(0, 2)
plt.ylim(0, 2)
plt.title('dB circle visualization')
plt.grid(True)
plt.show()