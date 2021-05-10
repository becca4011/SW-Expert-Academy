T = int(input())

for i in range(T):
    D, L, N = map(int, input().split())
    
    d = D * N
    temp = [_ for _ in range(1, N)]
    temp = sum(temp)
    d += temp * L * (D // 100)
    # D * (1 + n * L * 1 / 100)

    # 1, 2, ..., N - 1 → N(N - 1) / 2
    # N * D + D * L * N * (N - 1) / 200
    
    print("#%d %d" % (i + 1, d))