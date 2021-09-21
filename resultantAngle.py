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

        self.data = np.zeros((2,int(180/self.da)), float)

    def calculateVr(self) -> None:
        np.add(self.Vw, self.Vs, self.Vr)

    def calculateAngle(self) -> float:
        angle = np.zeros((1,1), float)
        np.rad2deg(np.arctan2(self.Vr[1], self.Vr[0]), angle)
        return angle[0][0]+90

    def rotateVs(self, a) -> None:
        rho, phi = cart2pol(self.Vs[0][0], self.Vs[1][0])
        a_rad = np.zeros((1,1), float)
        np.deg2rad(a, a_rad)
        phi+=a_rad[0][0]
        self.Vs[0][0], self.Vs[1][0] = pol2cart(rho, phi)

    def calculateAllPosible(self) -> np.ndarray:

        self.data.fill(0)
        self.data.resize((2,int(180/self.da)))
        
        a = 0
        for i in range(int(180/self.da)):
            self.calculateVr()
            angle = self.calculateAngle()
            
            
            a += self.da
            self.rotateVs(self.da)

            self.data[0][i], self.data[1][i] = a, angle
        return self.data
        

    def findMaxAngle(self) -> np.ndarray:
        return np.amax(self.data[1])


def main():
    re = ResultantAngle(np.array([[0], [-2]],float), np.array([[1],[0]], float), 1)
    re.calculateAllPosible()
    print(re.findMaxAngle())

if __name__ == "__main__":
    main()