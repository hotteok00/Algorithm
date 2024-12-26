def solution(board, h, w):
    answer = 0
    
    for dh, dw in [[1,0],[0,1],[-1,0],[0,-1]]:
        if (0 <= h + dh < len(board)) and (0 <= w + dw < len(board[0])) and board[h][w] == board[h + dh][w + dw]:
            answer += 1
    
    return answer