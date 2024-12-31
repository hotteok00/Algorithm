def solution(name):
    answer = 0
    n = len(name)
    min_move = n - 1
    
    for i in range(n):
        answer += shortest_distance_alphabet(name[i])
        
        # 현재 위치 i에서 연속된 'A'의 길이 찾기
        next_idx = i + 1
        while next_idx < n and name[next_idx] == 'A':
            next_idx += 1

        # 왼쪽으로 갔다가 다시 오른쪽으로 가는 경우
        distance_left_then_right = 2 * i + n - next_idx
        # 오른쪽으로 갔다가 다시 왼쪽으로 가는 경우
        distance_right_then_left = i + 2 * (n - next_idx)

        # 최소 이동 횟수 업데이트
        min_move = min(min_move, distance_left_then_right, distance_right_then_left)

    # 총 이동 횟수 합산
    answer += min_move
    return answer

def shortest_distance_alphabet(target):
    return min(ord(target) - ord('A'), ord('Z') + 1 - ord(target))