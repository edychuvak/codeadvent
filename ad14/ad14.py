import sys

inFile = sys.argv[1]


def printFormatMatrix(arrey):
    x = '\n'.join([''.join(['{:1}'.format(item)
                  for item in row]) for row in arrey])
    print(x)


def playData(file):
    with open(file, 'r') as f:
        matrix = [list(((line.replace(' ', '')).strip()).split('->'))
                  for line in f]
    return matrix


def findPlayBorder(array):
    element = array[0][0].split(',')
    min_row = 0
    max_row = int(element[1])
    min_col = int(element[0])
    max_col = int(element[0])
    rows = len(array)
    columns = len(array[0])
    for j in range(rows):
        for i in range(len(array[j])):
            element = array[j][i].split(',')
            if max_row < int(element[1]):
                max_row = int(element[1])
            if max_col < int(element[0]):
                max_col = int(element[0])
            if min_col > int(element[0]):
                min_col = int(element[0])
    min_col -= max_row - min_row
    max_col += max_row - min_row
    return (min_col, max_col), (min_row, max_row)


def setSource(boder):
    rows = int(border[0][1]) - int(border[0][0]) + 1
    columns = int(border[1][1]) + 1 - int(border[1][0])
    matrixPlay = [0]*columns
    for i in range(len(matrixPlay)):
        matrixPlay[i] = [0]*rows
        for j in range(len(matrixPlay[i])):
            matrixPlay[i][j] = '.'
    matrixPlay[0][500-int(border[0][0])] = '+'
    return matrixPlay


def datatoMatrix(data, matrix, border):
    for line in range(len(data)):
        for element in range(len(data[line])-1):
            myelement = data[line][element + 1].split(',')
            myelementforvard = data[line][element].split(',')
            myelement[0] = int(myelement[0]) - int(myelementforvard[0])
            myelement[1] = int(myelement[1]) - int(myelementforvard[1])
            myelementforvard[0] = int(myelementforvard[0]) - int(border[0][0])
            myelementforvard[1] = int(myelementforvard[1])
            if myelement[1] > 0:
                for i in range(myelement[1]+1):
                    matrix[myelementforvard[1]+i][myelementforvard[0]] = '#'
            elif myelement[1] < 0:
                for i in range(0, myelement[1]-1, -1):
                    matrix[myelementforvard[1]+i][myelementforvard[0]] = '#'
            elif myelement[0] > 0:
                for i in range(myelement[0]+1):
                    matrix[myelementforvard[1]][myelementforvard[0]+i] = '#'
            elif myelement[0] < 0:
                for i in range(0, myelement[0]-1, -1):
                    matrix[myelementforvard[1]][myelementforvard[0]+i] = '#'


def letSand(matrix, source):
    x_old = [0]*2
    x_old[0] = 0
    x_old[1] = source
    x_new = [1000]*2
    while True:
        if x_new[0] != 1000:
            x_old = x_new
        if matrix[x_old[0]+1][x_old[1]] == '.':
            x_new[0] = x_old[0]+1
            x_new[1] = x_old[1]
        elif matrix[x_old[0]+1][x_old[1]-1] == '.':
            x_new[0] = x_old[0]+1
            x_new[1] = x_old[1]-1
        elif matrix[x_old[0]+1][x_old[1]+1] == '.':
            x_new[0] = x_old[0]+1
            x_new[1] = x_old[1]+1
        else:
            matrix[x_new[0]][x_new[1]] = 'o'
            break


data = playData(inFile)
border = findPlayBorder(data)
playMatrix = setSource(border)
datatoMatrix(data, playMatrix, border)
playMatrix.insert(len(playMatrix), ['.']*len(playMatrix[0]))
z = 0
# uncomment next two line to calculate second part of advent
#playMatrix.insert(len(playMatrix), ['#']*len(playMatrix[0]))
#z = 1
while True:
    try:
        letSand(playMatrix, int(500 - border[0][0]))
        z += 1
    except IndexError as e:
        print(e)
        print("Sand is out of playGround")
        print('result=', z)
        break
