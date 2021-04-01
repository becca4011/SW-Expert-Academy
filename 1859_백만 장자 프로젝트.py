N = int(input())

cnt = 1
for i in range(N):
    x = int(input())
    item = list(map(int, input().split())) # 물건 가격

    dic = dict()
    for i in range(x):
        dic[item[i]] = dic.get(item[i], 0) + 1 # {물건 가격 : 물건 개수}

    key_sort = sorted(dic, reverse=True) # 물건의 최대 가격 순으로 정렬 (내림차순) / 리스트
    key_sort_dict = dict.fromkeys(key_sort, 0) # 리스트를 딕셔너리로 바꿈

    buy = [0, 0] # 물건 개수, 물건 가격
    sum = 0 # 이익

    for i in item:
        max_key = next(iter(key_sort_dict)) # max(dic) 시간초과, next(iter(dictionary))는 dict의 가장 처음의 키를 가져옴
        if i < max_key: # 최대 가격보다 작은 경우
            buy[0] += 1 # 개수
            buy[1] += i # 가격
            dic[i] -= 1 # 물건을 샀기 때문에 개수를 1 낮추기
            if dic[i] == 0:
                dic.pop(i)
                key_sort_dict.pop(i)

        elif i == max_key:
            if buy[0] >= 1: # 물건의 개수가 1개 이상
                sum += max_key * buy[0] - buy[1] # 이익 구하기
                buy[0] = buy[1] = 0 # buy 초기화
            dic[max_key] -= 1
            if dic[max_key] == 0:
                dic.pop(max_key)
                key_sort_dict.pop(i)

    print("#%d %d" % (cnt, sum))
    cnt += 1