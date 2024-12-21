def solution(arr, delete_list):
    temp = []
    for a in arr:
        f = True
        for d in delete_list:
            if a == d:
                f = False
                break
        if f: temp.append(a)
        
    return temp