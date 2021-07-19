T = int(input())

for i in range(T):
    node = list(input())
    a, b = 1, 1

    for j in node:
        if j == "L":
            b += a
        elif j == "R":
            a += b

    print("#%d %d %d" % (i + 1, a, b))
