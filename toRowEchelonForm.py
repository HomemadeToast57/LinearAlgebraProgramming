""" 
█▀▄ ██▀ █▀    ▄▀▄ █▀▄    █▀▄ █▀▄ ██▀ █▀ 
█▀▄ █▄▄ █▀    ▀▄▀ █▀▄    █▀▄ █▀▄ █▄▄ █▀ 
 """
# Convert any matrix to REF or RREF. To choose RREF or REF, set isReduced parameter to True or False.
def toRowEchelonForm(M, isReduced):
    if M == None:
        print("Matrix is None")
        return None

    # make sure size of all rows is the same
    size = -1
    for row in M:
        if size == -1:
            size = len(row)
        elif len(row) != size:
            print("Matrix is invalid")
            return None

    numRows = len(M)
    numCols = len(M[0])

    # check if matrix is all zeros
    zeroMatrix = True
    for row in M:
        for entry in row:
            if entry != 0:
                zeroMatrix = False

    # keep track of which pivot column we are working on
    pivot = 0

    if zeroMatrix == False:
        while pivot < numRows and pivot < numCols:

            # get a nonzero in the position of pivot
            for i in range(pivot, numRows):
                if M[i][pivot] != 0:
                    rowSwap(M, i, pivot)
                    break

            # if the pivot is zero, move to the next column
            if M[pivot][pivot] == 0:
                pivot += 1
                continue

            # divide row by pivot to make the pivot equal to 1
            c = M[pivot][pivot]

            M = rowMultiply(1/c, M, pivot)

            if isReduced == True:
                # add scalar multiple of the pivot row to all other rows to make the entries above and below the pivot equal to 0
                for i, row in enumerate(M):
                    if i != pivot:
                        c = M[i][pivot]
                        M = rowMultiplyAdd(-c, M, pivot, i)
            else:
                # add scalar multiple of the pivot row to all other rows ONLY below to make the entries ONLY below the pivot equal to 0
                for i, row in enumerate(M):
                    if not i <= pivot:
                        c = M[i][pivot]
                        M = rowMultiplyAdd(-c, M, pivot, i)

            pivot += 1

    return M


""" 
██▀ █▀▄ ▄▀▄ " ▄▀▀
█▄▄ █▀▄ ▀▄▀   ▄█▀
"""
# Multiply a row by a scalar
def rowMultiply(c, matrix, row1):
    rowCpy = matrix[row1]
    for i in range(len(rowCpy)):
        matrix[row1][i] *= c
    return matrix

# Add a scalar multiple of a row to another row
def rowMultiplyAdd(c, matrix, row1, row2):
    rowCpy = matrix[row1]
    for i in range(len(rowCpy)):
        matrix[row2][i] += c*rowCpy[i]
    return matrix

# Swap two rows
def rowSwap(matrix, row1, row2):
    temp = matrix[row1]
    matrix[row1] = matrix[row2]
    matrix[row2] = temp
    return matrix

# Print a matrix in a readable format
def printMatrix(matrix):
    for row in matrix:
        print("[", end=" ")
        for entry in row:
            print(f'{entry + 0: .1f}', end=" ")
        print("]")


""" 
▀█▀ ██▀ ▄▀▀ ▀█▀ 
 █  █▄▄ ▄█▀  █   
"""
# RREF Test
matrix = [[-3, 1], [5, 0]]
matrixRREF = toRowEchelonForm(matrix, True)

if matrixRREF != None:
    print("Matrix in reduced row echelon form: ")
    printMatrix(matrixRREF)

# REF Test
matrix = [[-3, 1], [5, 0]]
matrixREF = toRowEchelonForm(matrix, False)

if matrixREF != None:
    print("Matrix in row echelon form: ")
    printMatrix(matrixREF)
