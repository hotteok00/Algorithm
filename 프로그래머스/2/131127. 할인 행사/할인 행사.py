def solution(want, number, discount):
    answer = 0

    current_dict = {}
    for i in range(9):
        if discount[i] not in current_dict:
            current_dict[discount[i]] = 0    
        current_dict[discount[i]] += 1
    
    for i in range(len(discount) - 9):
        if discount[i + 9] not in current_dict:
            current_dict[discount[i + 9]] = 0
        current_dict[discount[i + 9]] += 1
        
        if check_want_current(want, number, current_dict):
            answer += 1
            
        current_dict[discount[i]] -= 1
    
    return answer

def check_want_current(want, number, current_dict):
    for item, num in zip(want, number):
        if item not in current_dict or current_dict[item] != num:
            return False
    return True