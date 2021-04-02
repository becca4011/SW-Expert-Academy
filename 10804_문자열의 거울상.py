T = int(input())

mirror = {'b' : 'd', 'd' : 'b', 'p' : 'q', 'q' : 'p'}

cnt = 1
for i in range(T):
    st = list(input())
    st.reverse()

    print("#%d" % cnt, end=" ")
    for j in st:
        print(mirror[j], end="")
    
    print()
    cnt += 1