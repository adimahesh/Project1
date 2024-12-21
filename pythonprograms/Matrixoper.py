def matrixcre(rows,cols):
    matrix = []
    for x in range(rows):
        row=[]
        for y in range(cols):
            val = int(input(f"enter {x} {y} ele"))
            row.append(val)
        matrix.append(row)   
    return matrix  
def printmat(matrix):
    for row in matrix:
        print(row) 
        print()    


matrix1= matrixcre(2,2)

print(matrix1)
