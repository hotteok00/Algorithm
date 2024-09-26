def moveLeft(s):
    new_s = [s[i] for i in range(1, len(s))]
    new_s.append(s[0])
    return new_s

def isRight(S):
    pair = {'(':')','{':'}','[':']'}
    new_S = []
    
    for s in S:
        if len(new_S) == 0:
            new_S.append(s)
            continue
        if new_S[-1] in pair and pair[new_S[-1]] == s:
            new_S.pop()
            continue
        new_S.append(s)
    
    if len(new_S) == 0: return True
    return False

def solution(s):
    answer = 0
    s = list(s)
    
    for _ in range(len(s)):
        s = moveLeft(s)
        if isRight(s): answer += 1
    
    return answer