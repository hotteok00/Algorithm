def solution(str_list):
    rIdx, lIdx = len(str_list), len(str_list)
    
    if 'r' in str_list:
        rIdx = str_list.index("r")
    if 'l' in str_list:
        lIdx = str_list.index("l")
    
    if rIdx == len(str_list) and rIdx == lIdx: return []
    
    if rIdx < lIdx:
        return str_list[rIdx + 1:]
    else:
        return str_list[:lIdx]