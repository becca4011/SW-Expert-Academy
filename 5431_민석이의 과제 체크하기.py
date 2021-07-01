T = int(input())
for i in range(T):
    res = list()
    N, K = map(int, input().split())
    submit = list(map(int, input().split()))
    submit.sort()

    for j in range(1, N + 1):
        if len(submit) != 0 and j == submit[0]:
            submit.pop(0)
        else:
            res.append(j)
    
    print("#%d" % (i + 1), end=" ")
    for j in range(len(res)):
        print(res[j], end=" ")

    print()