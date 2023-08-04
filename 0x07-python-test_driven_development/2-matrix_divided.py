#!/usr/bin/python3

"""Program to take input in form of a list of list and divided each element by\
   a given divisor.
"""


def matrix_divided(matrix, div):

    """Routine to divide all elements of a matrix."""

    if type(div) is str or type(div) is bool:
        raise TypeError('div must be a number')
    if type(div) is tuple or type(div) is list or type(div) is dict:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    if type(matrix) is list:
        for row in matrix:
            if type(row) is not list:
                raise TypeError('matrix must be a (list of lists) of integers\
/floats')
    else:
        raise TypeError('matrix must be a (list of lists) of integers/floats')

    matrix_len = len(matrix[1])
    div_matrix = []
    for r in matrix:
        if len(r) is not matrix_len:
            raise TypeError('Each row of the matrix must have the same size')
        row = []
        for i in r:
            if type(i) is str or type(i) is bool:
                raise TypeError('matrix must be a (list of lists) of integers\
/floats')
            if type(i) is tuple or type(i) is list or type(i) is dict:
                raise TypeError('matrix must be a (list of lists) of integers\
/floats')
            else:
                row.append(round(i/div, 2))
        div_matrix.append(row)
    return div_matrix


if __name__ == "__main__":
    a = [[1, 2, 3], [4, 5, 6]]
    result = matrix_divided(a, 3)
    print(result)
# result = matrix_divided([[1,'3',{"a":"b","v":'n'}],[4,5,6]], 3)
    print(result)
# result = matrix_divided([[1,True,3],[4,5,6]], 3)
    print(result)
    result = matrix_divided([[False, 2, 3], [4, 5, 6]], 3)
    print(result)
