T = int(input())

for i in range(T):
    N, M, K = map(int, input().split()) # N명의 손님, M초에 K개의 붕어빵 만듦
    time = sorted(list(map(int, input().split()))) # 손님이 몇 초에 도착하는지
    
    num = 0
    res = 1
    for j in time:
        b = (j // M) * K # j초일 때 붕어빵의 갯수

        if b - num <= 0: # 붕어빵이 없는 경우 (불가능)
            res = 0
            break
        else:
            num += 1 # 하나 팖
    
    if res == 1:
        print("#%d Possible" % (i + 1))
    else:
        print("#%d Impossible" % (i + 1))