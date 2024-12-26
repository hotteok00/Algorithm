def solution(picture, k):
    answer = [[' ' for _ in range(len(picture[0]) * k)] for _ in range(len(picture) * k)]
    
    for x in range(len(picture)):
        for y in range(len(picture[0])):
            pixel = picture[x][y]
            for i in range(k):
                for j in range(k):
                    answer[k * x + i][k * y + j] = pixel
    
    return [''.join(line) for line in answer]