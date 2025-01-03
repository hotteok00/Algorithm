def solution(topping):
    answer = 0
    
    left, right = set(), set()
    left_arr, right_arr = [], []
    
    for idx in range(len(topping)):
        left.add(topping[idx])
        left_arr.append(len(left))
        
    for idx in range(len(topping) - 1, -1, -1):
        right.add(topping[idx])
        right_arr.append(len(right))
    right_arr = list(reversed(right_arr))
        
#     print(left_arr)
#     print(right_arr)
    for idx in range(len(left_arr) - 1):
        if left_arr[idx] == right_arr[idx + 1]:
            answer += 1
    
    return answer