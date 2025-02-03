def solution(rows, columns, queries):
    answer = []
    matrix = [[r * columns + c + 1 for c in range(columns)] for r in range(rows)]
    for query in queries:
        x1, y1, x2, y2 = query
        x1 -= 1
        y1 -= 1
        x2 -= 1
        y2 -= 1
        
        rotation = []
        for y in range(y1, y2): rotation.append((x1, y))
        for x in range(x1, x2): rotation.append((x, y2))
        for y in range(y2, y1, -1): rotation.append((x2, y))
        for x in range(x2, x1, -1): rotation.append((x, y1))
        
        prv_x, prv_y = rotation[0]
        prv = matrix[prv_x][prv_y]
        min_ = prv
        for nxt_idx in range(1, len(rotation)):
            nxt_x, nxt_y = rotation[nxt_idx]
            nxt = matrix[nxt_x][nxt_y]
            
            if min_ > nxt: min_ = nxt
            
            matrix[nxt_x][nxt_y] = prv
            prv = nxt
        matrix[prv_x][prv_y] = prv
        
        answer.append(min_)
    
    return answer