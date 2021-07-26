T = int(input())

for i in range(T):
    N = list(map(int, input().split()))
    cnt = dict()

    for j in range(len(N)):
        cnt[N[j]] = cnt.get(N[j], 0) + 1

    for k in cnt:
        if cnt[k] == 1 or cnt[k] == 3:
            print("#%d %d" % (i + 1, k))
