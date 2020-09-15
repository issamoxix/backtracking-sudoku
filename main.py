brd = [
    [5,0,0,6,8,7,0,9,3],
    [0,0,0,1,0,9,0,0,0],
    [0,0,8,0,0,0,0,0,0],
    [8,6,0,4,9,0,0,3,2],
    [3,0,0,0,0,0,0,0,5],
    [4,5,0,0,6,2,0,8,7],
    [0,0,0,0,0,0,2,0,0],
    [2,0,0,7,0,6,0,0,0],
    [9,0,0,2,1,8,0,0,6]
]
def brrd(brd):
    for o in range(0,9):
        print(brd[o])
brrd(brd)

def solve(bo):
    find = find_em(bo)
    if not find:
        return True
    else:
        row, col = find
    for i in range(1,10):
        if valid(bo, i, (row, col)):
            bo[row][col]=i
            if solve(bo):
                return True
            bo[row][col]=0
    return False

def valid(bo, num ,pos):
    #ver hori 
    for i in range(len(bo[0])):
        if bo[pos[0]][i]==num and pos[1] != i:
            return False
    #check verti
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False 
    #ver box
    b_x =pos[1] // 3
    b_y=pos[0] // 3
    for i in range(b_y*3, b_y*3 +3):
        for j in range(b_x * 3,b_x*3+3):
            if bo[i][j] ==num and (i,j) != pos:
                return False
    return True


def find_em(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] ==0:
                return (i, j)
    return None
    
solve(brd)
print("=============================")
brrd(brd)