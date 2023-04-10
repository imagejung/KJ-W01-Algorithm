import sys
n = int(input())
a = list(map(int, sys.stdin.readline().split()))
ans = 0

for i in range(n):
    tmp = 0
    if a[i] == 1 or a[i] == 0:
        tmp = 1

    for j in range(2,a[i]):
        if a[i] % j == 0:
            tmp = 1

    if tmp == 0:
        ans += 1

print(ans)
