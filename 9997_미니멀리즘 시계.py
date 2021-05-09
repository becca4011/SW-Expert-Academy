T = int(input())

cnt = 1
for i in range(T):
    hour_hand = int(input()) * 2

    hour = hour_hand // 60 if hour_hand // 60 != 12 else 0
    print("#%d" % cnt, hour, hour_hand % 60)
    cnt += 1