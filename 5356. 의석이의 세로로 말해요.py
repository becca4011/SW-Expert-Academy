T = int(input())

for i in range(T):
    li = list()
    for j in range(5):
        li.append(list(input()))

    add = 0
    for j in range(5):
        add += len(li[j])
    res = list()
    cnt = 0
    while True:
        for j in range(5):
            if len(li[j]) != 0:
                res.append(li[j].pop(0))

        if len(res) == add:
            break

    print("#%d" % (i + 1), end=" ")
    for j in res:
        print(j, end="")
    print()
