#!/usr/bin/python3


def pascal_triangle(n):
    '''
    compute a pascal triangle
    '''
    triangle = []
    
    if n <= 0:
        return triangle
    
    for row in range(n):
        new_row = [1] #  initialize every row with 1
        if triangle: #  check if the triangle is not empty
            last_row = triangle[-1] #  get the last row in the triangle list
            for i in range(len(last_row) - 1): #  loop throug each last row
                new_row.append(last_row[i] + last_row[i + 1])
            new_row.append(1)
        triangle.append(new_row)
    return triangle

"""

def pascal_triangle(n):
    '''
    calculate and output a pascal triangle
    '''
    #  declear list to hold the entire triangle 
    triangle = []
    for i in range(n):
        
        #  stores indivitual rows of the triangle
        row = []
        
        #  loop through the rows
        for j in range(i + 1):
            
            #  this stores first and second rows
            if (j == 0) or (j == i):
                row.append(1)
            else:
                row.append(
                    triangle[i - 1][j - 1] + triangle[i - 1][j])
        triangle.append(row)
    return triangle  
"""