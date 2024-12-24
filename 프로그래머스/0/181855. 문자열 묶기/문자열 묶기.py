def solution(strArr):
    lenArr = [len(str_) for str_ in strArr]
    
    counts = {}
    for len_ in lenArr:
        if len_ not in counts:
            counts[len_] = 0
        counts[len_] += 1
    
    return max(counts.values())