T = int(input())

res = list()
for i in range(T):
    L, U, X = map(int, input().split())
    res.append(L - X if L > X else 0 if L <= X and U >= X else -1)

for i in range(T):
    print("#%d %d" % (i + 1, res[i]))
