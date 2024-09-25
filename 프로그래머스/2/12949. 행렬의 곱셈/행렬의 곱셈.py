def solution(arr1, arr2):
    answer = []
    
    # [a by b] * [b by c]
#     for idx_a, a in enumerate(arr1):
#         answer.append([])
#         for idx_c in range(len(arr2[0])):
#             b = [ arr2[idx_b][idx_c] for idx_b in range(len(a)) ]
            
#             sumOfMul_arr1_arr2 = 0
#             for idx in range(len(a)):
#                 sumOfMul_arr1_arr2 += a[idx] * b[idx]
            
#             answer[idx_a].append(sumOfMul_arr1_arr2)
    
    len_a = len(arr1)
    len_b = len(arr2)
    len_c = len(arr2[0])
    
    answer = [[0 for _ in range(len_c)] for _ in range(len_a)]
    
    for i in range(len_a):
        for j in range(len_c):
            for k in range(len_b):
                answer[i][j] += arr1[i][k] * arr2[k][j]
    
    return answer