T = int(input())

cnt = 1
for i in range(T):
    dict = {}
    result = []
    st = input()

    for j in st:
        dict[j] = dict.get(j, 0) + 1

    for key, value in dict.items():
        if value % 2 != 0:
            result.append(key)

    print("#%d" % cnt, end=" ")
    if len(result) == 0:
        print("Good", end="")
    else:
        result.sort()
        for r in result:
            print(r, end="")

    print()
    cnt += 1