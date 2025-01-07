def solution(numbers):
    answer = [-1 for _ in range(len(numbers))]
    
    stack = [-1]
    for idx in range(len(numbers)-1,-1,-1):
        while stack and numbers[idx] >= stack[-1]:
            stack.pop()
            
        if stack:
            answer[idx] = stack[-1]
            
        stack.append(numbers[idx])
            
    return answer