#!/usr/bin/python3

"""
Rotate a 2D matrix 90 degrees clockwise in-place.
"""


def rotate_2d_matrix(matrix):
    """
    Rotates an n x n 2D matrix representing an image by 90 degrees clockwise.
    Args:
        matrix: A list of lists representing the image.
    """
    n = len(matrix)
    # Transpose the matrix
    for i in range(n):
        for j in range(i+1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # Reverse each row
    for row in matrix:
        row.reverse()
