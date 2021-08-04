n = 1000000
a = [False, False] + [True] * (n - 1)
primes = list()

for i in range(2, n + 1):
    if a[i]:
        primes.append(i)

        for j in range(2 * i, n + 1, i):
            a[j] = False

for i in primes:
    print(i, end=" ")
