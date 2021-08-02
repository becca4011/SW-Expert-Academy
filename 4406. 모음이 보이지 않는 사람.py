T = int(input())

for i in range(T):
    S = input()
    res = ""
    for j in S:
        if j not in ["a", "e", "i", "o", "u"]:
            res += j
    print("#%d %s" % (i + 1, res))
