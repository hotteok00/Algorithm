def solution(order):
    answer = 0
    
    main = [i for i in range(1, len(order) + 1)]
    sub = []
    
    order_idx = 0
    main_idx = 0
    
    while main_idx < len(order):
        if order[order_idx] == main[main_idx]:
            order_idx += 1
            main_idx += 1
            answer += 1
        else:
            if sub and order[order_idx] == sub[-1]:
                sub.pop()
                order_idx += 1
                answer += 1
            else:
                sub.append(main[main_idx])
                main_idx += 1
    
    while sub and order[order_idx] == sub[-1]:
        sub.pop()
        order_idx += 1
        answer += 1
        
    return answer