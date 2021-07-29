T = int(input())

for i in range(T):
    N = int(input())
    print("#%d" % (i + 1), end=" ")
    for j in range(N):
        print("%d/%d" % (1, N), end=" ")
    print()
