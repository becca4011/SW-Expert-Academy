from collections import Counter

T = int(input())

for i in range(T):
    C = int(input())
    li = list(map(int, input().split()))
    cnt = Counter(li).most_common()
    max_cnt = cnt[0][0]
    mode = cnt[0][1]

    for j in cnt:
        if j[0] > max_cnt and j[1] == mode:
            max_cnt = j[0]

    print("#%d %d" % (C, max_cnt))
