import numpy as np

def cart2pol(x, y):
    rho = np.sqrt(x**2 + y**2)
    phi = np.arctan2(y, x)
    return(rho, phi)

def pol2cart(rho, phi):
    x = rho * np.cos(phi)
    y = rho * np.sin(phi)
    return(x, y)

class ResultantAngle:
    def __init__(self, Vw:np.ndarray, Vs:np.ndarray, da:float) -> None:
        self.Vw = Vw
        self.Vs = Vs
        self.Vr = np.zeros((2,1), float)

        self.da = da

        self.data = np.zeros((2,1), float)

    def calculateVr(self) -> None:
        self.Vr = np.add(self.Vw, self.Vs)

    def calculateAngle(self) -> float:
        angle = np.zeros((1,1), float)
        np.rad2deg(np.arctan2(self.Vr[0], self.Vr[1]), angle)
        return angle[0][0]-90

    def rotateVs(self, a) -> None:
        rho, phi = cart2pol(self.Vs[0][0], self.Vs[1][0])
        a_rad = np.zeros((1,1), float)
        np.deg2rad(a, a_rad)
        phi-=a_rad[0][0]
        self.Vs[0][0], self.Vs[1][0] = pol2cart(rho, phi)

    def calculateAllPosible(self) -> np.ndarray:
        a = 0
        while (True):
            self.calculateVr()
            angle = self.calculateAngle()
            
            if (a > 180):
                break
            a += self.da
            self.rotateVs(self.da)

            self.data = np.append(self.data, np.array([[a], [angle]]), 1)
        
        return self.data


def main():
    re = ResultantAngle(np.array([[0], [-2]],float), np.array([[1],[0]], float), 4)
    print(re.calculateAllPosible())

if __name__ == "__main__":
    main()