#!/usr/bin/python3

'''Roate 2D Matrix'''

def rotate_2d_matrix(matrix):
    '''
    Rotate a 2D matrix 90 degrees clockwise in-place
    matrix: list of lists, representing the 2D matrix
    '''
    n = len(matrix)

    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for row in matrix:
        row.reverse()
