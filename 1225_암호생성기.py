for i in range(10):
    t = int(input())
    li = list(map(int, input().split()))

    j = 1
    while True:
        num = li.pop(0) - j
        if num > 0:
            li.append(num)
        else:
            li.append(0)
            break
        j += 1
        if j == 6:
            j = 1

    print("#%d" % t, end=" ")
    for j in li:
        print(j, end=" ")
    print()
