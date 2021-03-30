N = int(input())

cnt = 1
for i in range(N):
    x = int(input())
    item = list(map(int, input().split()))

    dic = dict()
    for i in range(x):
        dic[item[i]] = dic.get(item[i], 0) + 1

    key_sort = sorted(dic, reverse=True)
    key_sort_dict = dict.fromkeys(key_sort, 0)

    buy = [0, 0]
    sum = 0

    for i in item:
        max_key = next(iter(key_sort_dict)) # max(dic) 시간초과, next(iter(dictionary))는 dict의 가장 처음의 키를 가져옴
        if i < max_key:
            buy[0] += 1 # 개수
            buy[1] += i # 가격
            dic[i] -= 1
            if dic[i] == 0:
                dic.pop(i)
                key_sort_dict.pop(i)

        elif i == max_key:
            if buy[0] >= 1:
                sum += max_key * buy[0] - buy[1]
                buy[0] = buy[1] = 0
            dic[max_key] -= 1
            if dic[max_key] == 0:
                dic.pop(max_key)
                key_sort_dict.pop(i)

    print("#%d %d" % (cnt, sum))
    cnt += 1