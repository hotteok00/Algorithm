from sys import stdin, stdout
input = stdin.readline
output = stdout.write

N, M = map(int, input().split())

# who comes party
P = [i for i in range(N + 1)]

def find(a):
    if a == P[a]: return a
    P[a] = find(P[a])
    return P[a]

def union(a, b):
    a = find(a)
    b = find(b)
    if a != b: P[a] = b

# who knows truth
T = list(map(int, input().split()))
T_len, T = T[0], T[1:]

if T_len > 0:
    prev_p = T[0]
    for i in range(1, T_len):
        next_p = T[i]
        union(prev_p, next_p)
        prev_p = next_p

# num of party that can tell exaggerated story
party = []
for _ in range(M):
    p_tmp = list(map(int, input().split()))
    party.append(p_tmp)
    p_len, p_tmp = p_tmp[0], p_tmp[1:]
    
    prev_p = p_tmp[0]
    for i in range(1, p_len):
        next_p = p_tmp[i]
        union(prev_p, next_p)
        prev_p = next_p
        
    # print("P", P)

count = 0
for p_tmp in party:
    p_len, p_tmp = p_tmp[0], p_tmp[1:]
    
    ans = True
    
    for i in range(0, p_len):
        a = find(p_tmp[i])
        for j in range(0, T_len):
            b = find(T[j])
            
            # print("a, b =", a, b)
            if a == b:
                ans = False
                break
            
        if not ans: break
    
    if ans: 
        # print("count += 1", p_tmp)
        count += 1

print(count)