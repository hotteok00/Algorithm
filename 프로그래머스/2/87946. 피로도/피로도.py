def solution(k, dungeons):
    max_count = -1
    
    perms_of_dungeons = get_perms(dungeons)
    for p in perms_of_dungeons:
        # print(p)
        count = get_count_of_enable_dungeons(k, p)
        max_count = max(count, max_count)
    
    return max_count

def get_perms(arr):
    if len(arr) == 0:
        return [[]]
    
    perms = []
    for i in range(len(arr)):
        current = arr[i]
        remaining = arr[:i] + arr[i+1:]
        for p in get_perms(remaining):
            perms.append([current] + p)
    
    return perms

def get_count_of_enable_dungeons(k, dungeons):
    count = 0
    
    for need, cost in dungeons:
        if need > k: break
        k -= cost
        count += 1
        
    return count