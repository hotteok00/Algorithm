def solution(answers):
    answer = [-1, 0, 0, 0]
    
    num1 = [1, 2, 3, 4, 5]
    num2 = [2, 1, 2, 3, 2, 4, 2, 5]
    num3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    for i in range(len(answers)):
        if num1[i % len(num1)] == answers[i]: answer[1] += 1
        if num2[i % len(num2)] == answers[i]: answer[2] += 1
        if num3[i % len(num3)] == answers[i]: answer[3] += 1
        
    result = []
    
    max_score = answer[0]
    for i in range(1, 4):
        if max_score < answer[i]:
            result.clear()
            result.append(i)
            max_score = answer[i]
        elif max_score == answer[i]:
            result.append(i)
    
    return result