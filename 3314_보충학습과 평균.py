T = int(input())

for i in range(T):
    score = list(map(int, input().split()))

    sum = 0
    for j in score:
        sum += j if j >= 40 else 40

    print("#%d %d" % (i + 1, sum // 5))
