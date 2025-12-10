import numpy as np
import matplotlib.pyplot as plt

def detect_turning_points(signal, filename="turning_points.pdf"):
    d = np.diff(signal)

    turning_points = []

    for i in range(1, len(d)):
        if d[i] * d[i - 1] < 0:
            turning_points.append(i)

    turning_points = np.array(turning_points)

    plt.plot(signal, label = "Signal")

    plt.plot(turning_points, signal[turning_points], '*' ,color = 'blue' ,label = "Turning Points")

    plt.title("Turning Points in the Signal")
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.legend(["Turning Points"], loc = "upper left")

    plt.savefig(filename)
    plt.show()

    return turning_points