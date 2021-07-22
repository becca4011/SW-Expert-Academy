T = int(input())

for i in range(T):
    N = list(map(int, input().split()))
    sum = 0
    cnt = 0
    for j in N:
        if j == max(N) or j == min(N):
            continue
        sum += j
        cnt += 1

    print("#%d %d" % (i + 1, round(sum / cnt)))
