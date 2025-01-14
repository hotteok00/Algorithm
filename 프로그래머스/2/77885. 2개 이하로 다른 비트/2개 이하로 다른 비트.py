def solution(numbers):
    answer = []
    
    for number in numbers:
        if number % 2 == 0:
            answer.append(number + 1)
        else:
            binary = bin(number)[2:]
            last_zero = binary.rfind('0')
            
            if last_zero == -1:
                answer.append(number + (number + 1) // 2)
                continue
            
            new_binary = list(binary)
            new_binary[last_zero] = '1'
            new_binary[last_zero + 1] = '0'
            answer.append(int(''.join(new_binary), 2))
    
    return answer