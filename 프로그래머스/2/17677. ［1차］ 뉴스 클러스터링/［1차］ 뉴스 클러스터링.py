def solution(str1, str2):   
    str1 = LtS(str1.lower())
    str2 = LtS(str2.lower())
    
    # union = set(str1) | set(str2)
    # inter = set(str1) & set(str2)
    union = get_union(str1, str2)
    inter = get_inter(str1, str2)
    
    # print(union, inter)
    
    if len(union) == 0: return 65536
    return int((len(inter)/len(union)) * 65536)

def LtS(string):
    return sorted([string[i:i+2] for i in range(len(string) - 1) if string[i:i+2].isalpha()])

def get_union(str1, str2):
    union = []
    idx1, idx2 = 0, 0
    
    while (idx1 < len(str1)) and (idx2 < len(str2)):
        if str1[idx1] == str2[idx2]:
            union.append(str1[idx1])
            idx1 += 1
            idx2 += 1
        else:
            if str1[idx1] < str2[idx2]:
                union.append(str1[idx1])
                idx1 += 1
            else:
                union.append(str2[idx2])
                idx2 += 1
        
    if idx1 < len(str1):
        union = union + str1[idx1:]
    else:
        union = union + str2[idx2:]
    
    return union

def get_inter(str1, str2):
    inter = []
    idx1, idx2 = 0, 0
    
    while (idx1 < len(str1)) and (idx2 < len(str2)):
        if str1[idx1] == str2[idx2]:
            inter.append(str1[idx1])
            idx1 += 1
            idx2 += 1
        else:
            if str1[idx1] < str2[idx2]:
                idx1 += 1
            else:
                idx2 += 1
    
    return inter