import sys
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))
[n,x] = a

answer = []
for i in range(n):
    if b[i]<x:
        answer.append(b[i])

print(*answer)
