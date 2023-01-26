import sys

inFile = sys.argv[1]

def printFormatMatrix(arrey):
    x = '\n'.join([''.join(['{:1}'.format(item)
                  for item in row]) for row in arrey])
    print(x)


def playMatrix(file):
    with open(file, 'r') as f:
        matrix = [list(line.strip()) for line in f]
    return matrix

def findStart(array):
    rows = len(array)
    columns = len(array[0])
    for j in range(columns):
        for i in range(rows):
            if (array[i][j] == 'S'):
                return (i, j), 0
                

matrix = playMatrix(inFile)
element_start = findStart(matrix)
visited = [element_start[0]]
play_set = [element_start]
def findStartsWith_a(array):
    rows = len(array)
    columns = len(array[0])
    for j in range(columns):
        for i in range(rows):
            if (array[i][j] == 'a'):
                play_set.append(((i, j), 0))
                visited.append((i,j))
# uncoment for second solution                
#findStartsWith_a(matrix)

moves = [[1, 0], [-1, 0], [0, 1], [0, -1]]

while play_set:
    element = play_set.pop(0)
    char_element = matrix[element[0][0]][element[0][1]]
    if char_element == 'E':
        print(element[1])
        exit()
    if char_element == 'S':
        char_element = 'a'
    for move in moves: 
        m1 = move[0] + element[0][0]
        m2 = move[1] + element[0][1] 
        if m1>=len(matrix) or m1<0 or m2 >=len(matrix[0]) or m2<0:
            continue
        char_value = matrix[m1][m2]
        if  char_value == 'E':
            char_value = 'z'  
        if (m1,m2) not in visited and ord(char_value) <= ord(char_element)+1 : 
            visited.append((m1,m2))
            play_set.append(((m1,m2),element[1]+1))
#print(play_set)