import sys
a = list(map(int, sys.stdin.readline().split()))

for i in range(a[0]):
    b = list(input())
    answer = 0
    tmp = 0
    for j in range(len(b)):
        if b[j] == "O":
            tmp += 1
            answer += tmp
        else:
            tmp = 0
    print(answer)