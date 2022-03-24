import sys
### Declare any constants
INT_MAX = sys.maxsize

def create_matrix(rows, cols, default_val = 0):
    """
    Creates a matrix filled with default_val
        :param rows: the number of rows the matrix should have
        :param cols: the number of columns the matrix should have

        :return: list of lists that form the matrix
    """
    M = []
    while len(M) < rows:
        M.append([])
        while len(M[-1]) < cols:
            M[-1].append(default_val)

    return M

def question1(rows: int, cols: int, input_matrix):
    ## Create an adjacency list
    blackholes = dict() # '1': [list of i,js that have number 1]

    for i in range(rows):
        for j in range(cols):
            if input_matrix[i][j] > 0:
                if input_matrix[i][j] in blackholes:
                    blackholes[input_matrix[i][j]].append((i,j))
                else:
                    blackholes[input_matrix[i][j]] = [(i,j)]
    ## Iterate through the matrix diagonally and calculate the minsteps.
    minSteps = create_matrix(rows, cols)
    ## Corner cases: if rows or columns = 1
    for i in range(rows):
        for j in range(cols):
            minSteps[i][j] = i + j

    for j in range(cols):
        for i in range(j+1):
            if i >= rows:
                break

            minSteps[i][j-i]=min(
                                minSteps[i-1][j-i] + 1 if i != 0 else INT_MAX , ## up
                                minSteps[i][j-i-1] + 1 if j-i != 0 else INT_MAX, ## left
                                minSteps[i+1][j-i] + 1 if i != rows-1 else INT_MAX, ## down
                                minSteps[i][j-i+1] + 1 if j-i != cols-1 else INT_MAX, ## right
                                minSteps[i][j-i] ## original value
                                )
            ## blackhole encountered
            if input_matrix[i][j-i] > 0:
                for row, col in blackholes[input_matrix[i][j-i]]:
                    minSteps[row][col] = min(
                                            minSteps[row][col], ## a cell connected through a blackhole
                                            minSteps[i][j-i] ## the original blackhole
                                            )
    for i in range(1,rows):
        for j in range(rows-i):
            #print(i+j,cols-j-1)
            if cols-1-j < 0:
                break
            minSteps[i+j][cols-j-1]=min(
                                minSteps[i+j-1][cols-1-j] + 1 if i+j != 0 else INT_MAX , ## up
                                minSteps[i+j][cols-j-2] + 1 if cols-j-1 != 0 else INT_MAX, ## left
                                minSteps[i+j+1][cols-j-1] + 1 if i+j != rows-1 else INT_MAX, ## down
                                minSteps[i+j][cols-j] + 1 if cols-j-1 != cols-1 else INT_MAX, ## right
                                minSteps[i+j][cols-j-1] ## original value
                                )
            ## blackhole encountered
            if input_matrix[i+j][cols-j-1] > 0:
                for row, col in blackholes[input_matrix[i+j][cols-j-1]]:
                    minSteps[row][col] = min(
                                            minSteps[row][col], ## a cell connected through a blackhole
                                            minSteps[i+j][cols-j-1] ## the original blackhole
                                            )
    return minSteps[rows-1][cols-1]


N,M = map(int, sys.stdin.readline().split())
positions = [list(map(int, sys.stdin.readline().split())) for row in range(N)]
#print(positions)
output = question1(N, M, positions)
print(output)
