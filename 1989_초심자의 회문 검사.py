T = int(input())

for i in range(T):
    palindrome = input()
    rev = palindrome[::-1]

    if palindrome == rev:
        print("#%d %d" % (i + 1, 1))
    else:
        print("#%d %d" % (i + 1, 0))
