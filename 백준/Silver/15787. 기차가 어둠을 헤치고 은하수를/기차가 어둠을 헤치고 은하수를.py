def m():
    # Use a breakpoint in the code line below to debug your script.
      # Press Ctrl+F8 to toggle the breakpoint.

    answer = 0

    N, M = map(int, input().split()) # num of train
    # M = map(int, input().split()) # command

    train = [[0 for i in range(20)] for i in range(N)]

    for _ in range(M):
        data = list(map(int, input().split()))

        c = data[0]
        i = 0
        x = 0

        if c == 1:
            i = data[1] - 1
            x = data[2] - 1

            train[i][x] = 1
        elif c == 2:
            i = data[1] - 1
            x = data[2] - 1

            train[i][x] = 0
        elif c == 3:
            i = data[1] - 1

            tmp = train[i].copy()
            for a in range(19):
                train[i][a+1] = tmp[a]

            train[i][0] = 0
        else:
            i = data[1] - 1

            tmp = train[i].copy()
            for a in range(19):
                train[i][a] = tmp[a+1]

            train[i][19] = 0

    data = []
    for i in train:
        if i not in data:
            data.append(i)
            answer += 1


    print(answer)

m()