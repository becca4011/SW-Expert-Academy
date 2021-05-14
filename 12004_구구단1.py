T = int(input())

s = set()
for i in range(10):
    for j in range(10):
        s.add(i * j)

for i in range(T):
    N = int(input())
    if N in s:
        print("#%d Yes" % (i + 1))
    else:
        print("#%d No" % (i + 1))