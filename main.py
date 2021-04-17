import numpy as np

class Matrix(object):
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.mtx = np.array(n*[m*[0]])        

    def Addition(self, add):
        if self.n == add.n and self.m == add.m:
            result = Matrix(self.n, self.m)
            for row in range(0, self.n):
                for col in range(0, self.m):
                    result.mtx[row, col] = self.mtx[row, col] + add.mtx[row, col]
        return result
    
    def Subtraction(self, sub):
        if self.n == sub.n and self.m == sub.m:
            result = Matrix(self.n, self.m)
            for row in range(0, self.n):
                for col in range(0, self.m):
                        result.mtx[row, col] = self.mtx[row, col] - sub.mtx[row, col]
        return result

    def Multiplication(self, multby):
        if self.m == multby.n:
            result = Matrix(self.n, multby.m)
            for row in range(0, result.n):
                for col in range(0, result.m):
                    result.mtx[row, col] = 0
                    for i in range(0, self.n):
                        for j in range(0, self.m):
                            result.mtx[row, col] += self.mtx[i,j] * multby.mtx[j,i]
        return result

def getmatrix():
    n = int(input("Rows: "))
    m = int(input("Cols: "))
    result = Matrix(n,m)
    for row in range(0, n):
        for col in range(0, m):
            result.mtx[row, col] = input(f"{row+1}. row {col+1}. col: ")
    return result

def main():
    test1 = Matrix(2,2)
    test2 = Matrix(2,2)
    test1.mtx = np.array([[1,2],[3,4]])
    test2.mtx = np.array([[3,5],[2,0]])
    test3 = test1.Multiplication(test2)
    print(test3.mtx)

if __name__ == "__main__":
    main()