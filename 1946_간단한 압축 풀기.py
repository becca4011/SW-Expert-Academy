T = int(input())

for i in range(T):
    N = int(input())
    li = list()
    for j in range(N):
        C, K = input().split()
        li += list(C * int(K))

    print("#%d" % (i + 1))
    for j in range(len(li)):
        if j != 0 and j % 10 == 0:
            print("\n" + li[j], end="")
        else:
            print(li[j], end="")
    print()
