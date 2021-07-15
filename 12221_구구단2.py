T = int(input())

for i in range(T):
    A, B = map(int, input().split())
    if A >= 10 or B >= 10:
        print("#%d %d" % (i + 1, -1))
    else:
        print("#%d %d" % (i + 1, A * B))
