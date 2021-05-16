T = int(input())

for i in range(T):
    d = dict()
    S = input()
    for j in S:
        d[j] = d.get(j, 0) + 1

    if len(d) == 2:
        print("#%d Yes" % (i + 1))
    else:
        print("#%d No" % (i + 1))