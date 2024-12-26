def solution(wallet, bill):
    cnt = 0
    
    while True:
        if check_size(wallet, bill): break
        
        if bill[0] > bill[1]:
            bill[0] = int(bill[0] / 2)
        else:
            bill[1] = int(bill[1] / 2)
            
        cnt += 1
    
    return cnt

def check_size(wallet, bill):
    if bill[0] <= wallet[0] and bill[1] <= wallet[1]:
        return True
    if bill[1] <= wallet[0] and bill[0] <= wallet[1]:
        return True
    return False