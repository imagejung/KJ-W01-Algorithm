#수 정렬하기 2
import sys
n = int(sys.stdin.readline())
a = [int(sys.stdin.readline()) for i in range(n)]

# 내장함수 활용
a.sort()

for i in range(n):
    print(a[i])