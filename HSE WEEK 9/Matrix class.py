from sys import stdin
from copy import deepcopy


class MatrixError(BaseException):
    def __init__(self, matrix, other):
        self.matrix1 = matrix
        self.matrix2 = other


class Matrix:
    def __init__(self, list_of_lists):
        self.matrix = deepcopy(list_of_lists)

    def size(self):
        matrix_size = (len(self.matrix), len(self.matrix[0]))
        return matrix_size

    def __str__(self):
        string = ''
        for i in self.matrix:
            for j in i:
                string += '%s\t' % j
            string = string[:-1] + '\n'
        string = string[:-1]
        return string

    def __add__(self, other):
        if len(self.matrix) == len(other.matrix):
            matrix_result = []
            num_massive = []
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[0])):
                    result = self.matrix[i][j] + other.matrix[i][j]
                    num_massive.append(result)
                    if len(num_massive) == len(self.matrix[0]):
                        matrix_result.append(num_massive)
                        num_massive = []
            return Matrix(matrix_result)
        else:
            raise MatrixError(self, other)

    def __mul__(self, number):
        matrix_result = []
        num_massive = []
        for i in self.matrix:
            for j in i:
                j *= number
                num_massive.append(j)
                if len(num_massive) == len(self.matrix[0]):
                    matrix_result.append(num_massive)
                    num_massive = []
        return Matrix(matrix_result)

    def __rmul__(self, number):
        return self.__mul__(number)

    def transpose(self):
        transMatrix = list(zip(*self.matrix))
        self.matrix = transMatrix
        return Matrix(transMatrix)

    def transposed(self):
        transMatrix = list(zip(*self.matrix))
        return Matrix(transMatrix)


exec(stdin.read())
