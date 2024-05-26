S, P = map(int, input().split())
DNA = input()
sub = dict(zip('ACGT', list(map(int, input().split()))))

cnt = 0

left = 0
right = 0
tmp = dict(zip('ACGT', [0,0,0,0]))

while right < S:    
    if right < P - 1:
        tmp[DNA[right]] += 1
        right += 1
        continue
    
    tmp[DNA[right]] += 1
    right += 1
    
    # print(tmp)
    if (sub['A'] <= tmp['A'] and 
        sub['C'] <= tmp['C'] and 
        sub['G'] <= tmp['G'] and 
        sub['T'] <= tmp['T']):
        cnt += 1
        
    tmp[DNA[left]] -= 1
    left += 1
    
print(cnt)