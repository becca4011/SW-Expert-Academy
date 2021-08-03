T = int(input())

res = list()
for i in range(T):
    A, B, C, D = map(int, input().split())
    res.append("ALICE" if A / B > C / D else "BOB" if A / B < C / D else "DRAW")

for i in range(T):
    print("#%d %s" % (i + 1, res[i]))
