T = int(input())

for i in range(T):
    N = int(input())
    P = list(map(int, input().split()))
    cnt = 0

    for j in range(1, N - 1):
        if P[j - 1] > P[j] and P[j + 1] < P[j] or P[j - 1] < P[j] and P[j + 1] > P[j]:
            cnt += 1

    print("#%d %d" % (i + 1, cnt))