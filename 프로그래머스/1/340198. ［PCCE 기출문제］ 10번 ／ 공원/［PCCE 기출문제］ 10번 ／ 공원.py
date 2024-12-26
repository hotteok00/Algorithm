def solution(mats, park):
    mats = [-1] + mats
    mats.sort()
    
    x, y, mat_idx = 0, 0, 0
    for x in range(len(park)):
        for y in range(len(park[0])):
            while mat_idx + 1 < len(mats) and possible_mat(x, y, mats[mat_idx + 1], park):
                mat_idx += 1
    
    return mats[mat_idx]

def possible_mat(x, y, mat, park):
    if park[x][y] != "-1":
        return False
    
    if len(park) - x < mat or len(park[0]) - y < mat:
        return False
    
    for i in range(x, x + mat):
        for j in range(y, y + mat):
            if park[i][j] != "-1":
                return False
            
    return True