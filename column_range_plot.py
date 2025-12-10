import numpy as np
import matplotlib.pyplot as plt

def column_range_plot(A, filename="column_ranges.pdf"):
    c_ranges = np.max(A, axis=0) - np.min(A, axis=0)

    plt.bar(range(len(c_ranges)), c_ranges, color="blue")
    plt.title("Column Ranges")
    plt.xlabel("Column Index")
    plt.ylabel("Range")
    plt.legend(["Column Ranges"], loc = "upper left")
    plt.savefig(filename)

    plt.savefig(filename)
    plt.show()

    return c_ranges