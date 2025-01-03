count = 0
answer = 0
def solution(word):
    default = ["A", "E", "I", "O", "U"]
    max_depth = 5
    
    def dfs(depth, current_word):
        global count, answer
        
        if current_word == word:
            answer = count
            
        count += 1
        
        if depth == max_depth:
            return
        
        for char in default:
            dfs(depth + 1, current_word + char)
    
    dfs(0, '')
    return answer