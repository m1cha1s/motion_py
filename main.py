import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage.measurements import label

from resultantAngle import ResultantAngle

def main():
    re = ResultantAngle(np.array([[0], [-2]]), np.array([[0], [-(5/3)]]), 0.001)
    data = re.calculateAllPosible()
    maxAngle = re.findMaxAngle()
    maxAngleIndex = np.where(data==maxAngle)[1][0]
    print(maxAngle)
    print(data[0][maxAngleIndex])

    plt.plot(data[0],data[1], label="Data")
    plt.scatter(data[0][maxAngleIndex], maxAngle, label="Max angle")

    plt.legend()
    plt.grid()
    plt.show()

if __name__ == "__main__":
    main()