T = int(input())

for i in range(T):
    S = list(input())
    H = int(input())
    H_num = sorted(list(map(int, input().split())), reverse=True)

    for j in H_num:
        S.insert(j, "-")

    print("#%d" % (i + 1), end=" ")
    for j in S:
        print(j, end="")
    print()
