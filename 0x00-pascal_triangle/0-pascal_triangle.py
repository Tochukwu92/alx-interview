#!/usr/bin/python3


def pascal_triangle(n):
    '''
    compute a pascal triangle
    '''
    triangle = []
    
    for row in range(n):
        new_row = [1] #  initialize every row with 1
        if triangle: #  check if the triangle is not empty
            last_row = triangle[-1] #  get the last row in the triangle list
            for i in range(len(last_row) - 1): #  loop throug each last row
                new_row.append(last_row[i] + last_row[i + 1])
            new_row.append(1)
        triangle.append(new_row)
    return triangle