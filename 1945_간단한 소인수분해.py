T = int(input())

for i in range(T):
    li = [0, 0, 0, 0, 0]
    N = int(input())

    cnt = 0
    for j in [2, 3, 5, 7, 11]:
        while N % j == 0:
            N /= j
            li[cnt] += 1
        cnt += 1

    print("#%d" % (i + 1), end=" ")
    for j in li:
        print(j, end=" ")
    print()
