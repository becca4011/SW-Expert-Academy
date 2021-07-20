T = int(input())

for i in range(T):
    date = list(map(int, input().split()))
    day = 0
    if date[0] == date[2]:
        print("#%d %d" % (i + 1, date[3] - date[1] + 1))
    else:
        if date[0] in [1, 3, 5, 7, 8, 10, 12]:
            day = 31 - date[1] + 1
        elif date[0] == 2:
            day = 28 - date[1] + 1
        else:
            day = 30 - date[1] + 1

        for j in range(date[0] + 1, date[2]):
            if j in [1, 3, 5, 7, 8, 10, 12]:
                day += 31
            elif j == 2:
                day += 28
            else:
                day += 30

        day += date[3]
        print("#%d %d" % (i + 1, day))
