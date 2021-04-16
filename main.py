import numpy as np

class Matrix(object):
    def __init__(self, n, m,):
        self.n = n
        self.m = m
        self.mtx = n*[m*[0]]

def main():
    mtx1 = Matrix(2,2)
    print(mtx1.mtx)
    


if __name__ == "__main__":
    main()