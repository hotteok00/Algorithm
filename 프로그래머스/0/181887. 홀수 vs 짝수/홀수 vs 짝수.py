def solution(num_list):
    odd = 0
    even = 0
    for i in range(len(num_list)):
        if (i + 1) % 2 == 0: 
            even += num_list[i]
        else: 
            odd += num_list[i]
    
    return max(odd, even)