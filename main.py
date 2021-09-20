import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage.measurements import label

from resultantAngle import ResultantAngle

def main():
    re = ResultantAngle(np.array([[0], [-2]]), np.array([[0], [-1.666666666666]]), 1)
    data = re.calculateAllPosible()
    maxAngle = re.findMaxAngle()
    # print(data)
    # print(maxAngle)
    maxAngle = [np.where(data == maxAngle[0]), maxAngle[0]]
    # print(data, maxAngle)
    plt.plot(data[0],data[1], label="Data")
    plt.scatter(maxAngle[0], maxAngle[1], label="Max angle")
    plt.legend()
    plt.grid()
    plt.show()

if __name__ == "__main__":
    main()