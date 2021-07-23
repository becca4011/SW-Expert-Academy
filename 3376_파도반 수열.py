T = int(input())

li = [1, 1, 1]
for i in range(99):
    li.append(li[i] + li[i + 1])

for i in range(T):
    N = int(input())
    print("#%d %d" % (i + 1, li[N - 1]))
