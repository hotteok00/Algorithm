def solution(arr):
    answer = 0
    
    af = arr
    bf = [-1 for _ in range(len(arr))]
    
    while True:
        if bf == af:
            break
            
        bf = af.copy()
        for i in range(len(af)):
            if af[i] >= 50 and af[i] % 2 == 0: 
                af[i] /= 2
            elif af[i] < 50 and af[i] % 2 == 1: 
                af[i] = af[i] * 2 + 1
            
        answer += 1
    
    return answer - 1