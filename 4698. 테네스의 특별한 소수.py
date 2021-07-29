T = int(input())

# 에라토스테네스의 체
n = 1000000
a = [False, False] + [True] * (n - 1)
primes = []

for i in range(2, n + 1):
    if a[i]:
        primes.append(i)
        for j in range(2 * i, n + 1, i):
            a[j] = False

for i in range(T):
    D, A, B = map(int, input().split())
    cnt = 0
    for j in primes:
        if A <= j and B >= j:
            if str(D) in list(str(j)):
                cnt += 1
        if B < j:
            break

    print("#%d %d" % (i + 1, cnt))
