def solution(orders):
    answer = 0
    
    americano, americano_str = 4500, 'americano'
    cafelatte, cafelatte_str = 5000, 'cafelatte'
    anything, anything_str = 4500, 'anything'
    
    for order in orders:
        if americano_str in order:
            answer += americano
            continue
            
        if cafelatte_str in order:
            answer += cafelatte
            continue
            
        if anything_str in order:
            answer += anything
    
    return answer