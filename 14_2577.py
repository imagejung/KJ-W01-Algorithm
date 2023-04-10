a = int(input())
b = int(input())
c = int(input())

abc = list(map(int, str(a*b*c)))

for i in range(10):
    cnt = 0
    for j in abc:
        if i == j:
            cnt += 1
    print(cnt)


