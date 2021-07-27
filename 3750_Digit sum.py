T = int(input())

res = list()
for i in range(T):
    n = list(map(int, input()))

    while True:
        s = sum(n)
        if s < 10:
            res.append(s)
            break
        else:
            n = list(map(int, str(s)))

# 출력을 매번 하는게 아닌, 저장해서 한 번에 출력하는 것이 더 빠름
for i in range(T):
    print("#%d %d" % (i + 1, res[i]))
