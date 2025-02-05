def split(s, length):
    arr = []
    for j in range(0, len(s), length):
        arr.append(s[j:j+length])
    return arr

def compression(s, length) -> None:
    s_splited = split(s, length)
    arr = []
    prv = s_splited[0]
    count = 1
    
    for i in s_splited[1:]:
        if i == prv:
            count += 1
        else:
            if count > 1:
                arr.append(str(count))
            arr.append(prv)
            prv = i
            count = 1
    if count > 1:
        arr.append(str(count))
    arr.append(prv)
        
    return ''.join(arr)

def solution(s):
    answer = len(s)
    length = len(s) // 2
    
    for l in range(1, length + 1):
        tmp = len(compression(s, l))
        if answer > tmp: answer = tmp
    
    return answer