for i in range(10):
    T = int(input())
    s = input()
    st = input()

    cnt = 0
    while st.find(s) != -1:
        st = st[st.find(s) + len(s) :]
        cnt += 1
    print("#%d %d" % (T, cnt))
