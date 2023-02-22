## prog5.py
## Sampson Ezieme
## November 23, 2016
##
## Homework 5

# Problem 1

def symmetric(squareMatrix):
    """This function test the symmetry of a square matrix
       by seeing if every element in row i, column j
       is equal to row j, column i.
       If the square matrix is symmetric the funtion returns True.
       If it isnt it returns False."""
    for i in range(0, len(squareMatrix)):
        for j in range(0, len(squareMatrix)):
            if squareMatrix[i][j] == squareMatrix[j][i]:
                pass
            else:
                return False
    return True

#Problem 2

def transpose(matrix):
    """This function takes a 2 dimensional table and transposes the matrix
       by making the rows the columns of the original matrix
       and the columns the rows of the original matrix
       and return a transposed matrix."""
    table =[]
    rows = len(matrix)
    cols = len(matrix[0])
    for c in range(0,cols):
        transposedRow = []
        for r in range(0, rows):
           value = matrix[r][c]
           transposedRow.append(value)
        table.append(transposedRow)
    return table

  
    
            
                         
        
    
