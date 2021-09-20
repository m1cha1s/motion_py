import numpy as np
import matplotlib.pyplot as plt

from resultantAngle import ResultantAngle

def main():
    re = ResultantAngle(np.array([[0], [-2]]), np.array([[0], [1.666666666666]]), 4)
    data = re.calculateAllPosible()
    print(data)
    plt.plot(data[0],data[1])
    plt.grid()
    plt.show()

if __name__ == "__main__":
    main()