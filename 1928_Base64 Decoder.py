T = int(input())
"""
# 거꾸로 푼 문제
encode = list()
decode = dict()

for i in range(26):
    decode[i] = chr(i + 65)

for i in range(26, 52):
    decode[i] = chr(i - 26 + 97)

for i in range(52, 62):
    decode[i] = i - 52

decode[62] = '+'
decode[63] = '/'

cnt = 1
for i in range(T):
    bit = ""
    decoding = input()

    for j in decoding:
        bit += format(ord(j), 'b').zfill(8) # 아스키코드 8자리로 맞춰서 리스트에 삽입

    k = 0
    while(k <= len(bit) - 6):
        encode.append(int(bit[k:k+6], 2))
        k += 6

    print("#%d" % cnt, end=" ")
    for d in encode:
        print(decode[d], end="")
        encode = []
    print()
    cnt += 1
"""

decode = list()
encode = dict()

for i in range(26):
    encode[chr(i + 65)] = i

for i in range(26, 52):
    encode[chr(i - 26 + 97)] = i

for i in range(52, 62):
    encode[str(i - 52)] = i

encode['+'] = 62
encode['/'] = 63

cnt = 1
for i in range(T):
    bit = ""
    encoding = input()

    for j in encoding:
        bit += format(encode[j], 'b').zfill(6)

    k = 0
    while(k <= len(bit) - 8):
        decode.append(int(bit[k:k+8], 2))
        k += 8


    print("#%d" % cnt, end=" ")
    for d in decode:
        print(chr(d), end="")
        decode = []
    print()
    cnt += 1