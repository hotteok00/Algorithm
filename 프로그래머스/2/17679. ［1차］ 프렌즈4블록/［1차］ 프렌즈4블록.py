def solution(m, n, board):
    block = set()
    answer = 0
    
    while True:
        block = delblock(m, n, board, block)
        if len(block) == 0: break
        downblock(m, n, board, block)
        block.clear()
    
    for i in range(m):
        for j in range(n):
            if board[i][j] == '0': answer += 1
    
    # print(board)
    return answer

def delblock(m, n, board, block):
    for x in range(m-1):
        for y in range(n-1):
            if board[x][y] != '0' and isblock(x, y, board):
                block.add((x, y))
                block.add((x+1, y))
                block.add((x, y+1))
                block.add((x+1, y+1))
    
    # print(block)
    for x, y in list(block): board[x] = board[x][:y] + '0' + board[x][y+1:]
    
    return block

def isblock(x, y, board):
    if board[x][y] == board[x+1][y] == board[x][y+1] == board[x+1][y+1]:
        return True
    return False
    
def downblock(m, n, board, block):
    for i in range(m-1, -1, -1):
        for j in range(n):
            if board[i][j] == '0':
                for up in range(i-1, -1, -1):
                    if board[up][j] != '0':
                        board[i] = board[i][:j] + board[up][j] + board[i][j+1:]
                        board[up] = board[up][:j] + '0' + board[up][j+1:]
                        break

