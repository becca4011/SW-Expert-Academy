T = int(input())

for i in range(T):
    N, A, B = map(int, input().split())
    mx, mn = 0, 0
    if N == A and N == B and A == B:
        print("#%d %d %d" % (i + 1, N, N))
    else:
        mx = min(A, B)
        mn = 0 if A + B <= N else A + B - N
        print("#%d %d %d" % (i + 1, mx, mn))
