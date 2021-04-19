import numpy as np


class Matrix(object):
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.mtx = np.array(n * [m * [0]])

    def addition(self, add):
        if self.n == add.n and self.m == add.m:
            result = Matrix(self.n, self.m)
            for row in range(0, self.n):
                for col in range(0, self.m):
                    result.mtx[row, col] = self.mtx[row, col] + add.mtx[row, col]
            return result
        else:
            print("The two matrix cant be added together!")
            return -1

    def subtraction(self, sub):
        if self.n == sub.n and self.m == sub.m:
            result = Matrix(self.n, self.m)
            for row in range(0, self.n):
                for col in range(0, self.m):
                    result.mtx[row, col] = self.mtx[row, col] - sub.mtx[row, col]
            return result
        else:
            print("The two matrix cant be subtracted!")
            return -1

    def multiplication(self, times):
        if type(times) == Matrix:
            if self.m == times.n:
                result = Matrix(self.n, times.m)
                for row in range(0, result.n):
                    for col in range(0, result.m):
                        result.mtx[row, col] = 0
                        for i in range(0, self.m):
                            result.mtx[row, col] += self.mtx[row, i] * times.mtx[i, col]
                return result
            else:
                print("The two matrix are not compatible!")
                return -1
        elif type(times) == int:
            result = Matrix(self.n, self.m)
            result.mtx = [
                [
                    self.mtx[row, col] * times for col in range(len(self.mtx[0]))
                    ] for row in range(len(self.mtx))
                ]
            return result

def initialize():
    n = int(input("Rows: "))
    m = int(input("Cols: "))
    result = Matrix(n, m)
    for row in range(0, n):
        for col in range(0, m):
            result.mtx[row, col] = input(f"{row + 1}. row {col + 1}. col: ")
    return result


def main():
    print("""
-------------------------------------------------------------------
                            ______________
                ,===:'.,            `-._
                        `:.`---.__         `-._
                        `:.     `--.         `.
                            \.        `.         `.
                    (,,(,    \.         `.   ____,-`.,
                (,'     `/   \.   ,--.___`.'
            ,  ,'  ,--.  `,   \.;'         `
            `{D, {    \  :    \;
                V,,'    /  /    //
                j;;    /  ,' ,-//.    ,---.      ,
                \;'   /  ,' /  _  \  /  _  \   ,'/
                    \   `'  / \  `'  / \  `.' /
                    `.___,'   `.__,'   `.__,'  
___  ___      _        _       ______                             
|  \/  |     | |      (_)      |  _  \                            
| .  . | __ _| |_ _ __ ___  __ | | | |_ __ __ _  __ _  ___  _ __  
| |\/| |/ _` | __| '__| \ \/ / | | | | '__/ _` |/ _` |/ _ \| '_ \ 
| |  | | (_| | |_| |  | |>  <  | |/ /| | | (_| | (_| | (_) | | | |
\_|  |_/\__,_|\__|_|  |_/_/\_\ |___/ |_|  \__,_|\__, |\___/|_| |_|
                                                 __/ |            
                                                |___/             
--------------------------------------------------------------------
    """)
    matrixstack = []
    while True:
        print("Matrix(1) | Addition(2) | Subtraction(3) | Multipication(4) | Exit(0)")
        Option = int(input("Option: "))
        # Exit from console app
        if Option == 0:
            print("Exiting...")
            break
        # New matrix in the stack
        elif Option == 1:
            print(f"{len(matrixstack)+1}. Matrix:\n")
            matrixstack.append(initialize())
            for mtx in range(len(matrixstack)):
                print(f"{mtx+1}. =\n{matrixstack[mtx].mtx}")
        # Addition
        elif Option == 2:
            for mtx in range(len(matrixstack)):
                print(f"{mtx+1}. =\n{matrixstack[mtx].mtx}")
            print("Which two Matrix do you wanna Add together?\n")
            mtx1 = matrixstack[int(input())-1]
            print("+")
            mtx2 = matrixstack[int(input())-1]
            print("=\n")
            print(f"{mtx1.addition(mtx2)}\n")
        # Subtraction
        elif Option == 3:
            for mtx in range(len(matrixstack)):
                print(f"{mtx+1}. =\n{matrixstack[mtx].mtx}")
            print("Which two Matrix do you wanna Subtract from each other?\n")
            mtx1 = matrixstack[int(input())-1]
            print("-")
            mtx2 = matrixstack[int(input())-1]
            print("=\n")
            print(f"{mtx1.addition(mtx2)}\n")
        # Multiplication
        elif Option == 4:
            print("Options: Matrix X Matrix (1) | Matrix X Number (2)")
            multoption = int(input("Option: "))
            for mtx in range(len(matrixstack)):
                print(f"{mtx+1}. =\n{matrixstack[mtx].mtx}")
            # Matrix multiplied by another Matrix
            if multoption == 1:
                print("Matrix 1: ")
                mtx1 = matrixstack[int(input())-1]
                print("X\n")
                print("Matrix 2: ")
                mtx2 = matrixstack[int(input())-1]
                print("=\n")
                print(mtx1.multiplication(mtx2).mtx)
            # Matrix multiplied by a number
            elif multoption == 2:
                print("Matrix : ")
                mtx1 = matrixstack[int(input())-1]
                print("X\n")
                print("Matrix 2: ")
                times1 = int(input())
                print("=\n")
                print(mtx1.multiplication(times1).mtx)
        print('\n')


if __name__ == "__main__":
    main()
