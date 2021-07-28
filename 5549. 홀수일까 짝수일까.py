T = int(input())

for i in range(T):
    N = int(input())
    print("#%d Even" % (i + 1) if N % 2 == 0 else "#%d Odd" % (i + 1))
