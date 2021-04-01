# 문제 거꾸로 함
T = int(input())

decode = list()
encode = dict()

for i in range(26):
    encode[i] = chr(i + 65)

for i in range(26, 52):
    encode[i] = chr(i - 26 + 97)

for i in range(52, 62):
    encode[i] = i - 52

encode[62] = '+'
encode[63] = '/'

cnt = 1
for i in range(T):
    bit = ""
    encoding = input()

    for j in encoding:
        bit += format(ord(j), 'b').zfill(8) # 아스키코드 8자리로 맞춰서 리스트에 삽입

    k = 0
    while(k <= len(bit) - 6):
        decode.append(int(bit[k:k+6], 2))
        k += 6

    print("#%d" % cnt, end=" ")
    for d in decode:
        print(encode[d], end="")
        decode = []
    
    cnt += 1