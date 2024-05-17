from sys import stdin, stdout
import sys

input = stdin.read
sys.setrecursionlimit(100000)

# 입력을 읽고 초기화
data = input().split()
N = int(data[0])
M = int(data[1])
K = int(data[2])

arr = [0] * N
index = 3
for i in range(N):
    arr[i] = int(data[index])
    index += 1

# 세그먼트 트리의 크기는 4*N으로 설정
segment_tree = [0] * (4 * N)

# 세그먼트 트리를 빌드하는 함수
def build_tree(start, end, node):
    if start == end:
        segment_tree[node] = arr[start]
        return segment_tree[node]
    
    mid = (start + end) // 2
    segment_tree[node] = build_tree(start, mid, node * 2) + build_tree(mid + 1, end, node * 2 + 1)
    return segment_tree[node]

# 특정 인덱스의 값을 업데이트하는 함수
def update_tree(start, end, node, idx, value):
    if start == end:
        segment_tree[node] = value
        return
    
    mid = (start + end) // 2
    if start <= idx <= mid:
        update_tree(start, mid, node * 2, idx, value)
    else:
        update_tree(mid + 1, end, node * 2 + 1, idx, value)
    
    segment_tree[node] = segment_tree[node * 2] + segment_tree[node * 2 + 1]

# 구간 합을 구하는 함수
def sum_tree(start, end, node, left, right):
    if right < start or end < left:
        return 0
    if left <= start and end <= right:
        return segment_tree[node]
    
    mid = (start + end) // 2
    return sum_tree(start, mid, node * 2, left, right) + sum_tree(mid + 1, end, node * 2 + 1, left, right)

# 세그먼트 트리 빌드
build_tree(0, N - 1, 1)

# 쿼리를 처리하는 부분
results = []
for i in range(M + K):
    a = int(data[index])
    b = int(data[index + 1])
    c = int(data[index + 2])
    index += 3
    
    if a == 1:
        update_tree(0, N - 1, 1, b - 1, c)
    else:
        result = sum_tree(0, N - 1, 1, b - 1, c - 1)
        results.append(result)

# 결과 출력
stdout.write('\n'.join(map(str, results)) + '\n')
