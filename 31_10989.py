#수 정렬하기 3
import sys

n = int(sys.stdin.readline())
a = [0]*10001

#계수 정렬 활용
for i in range(n):
    num = int(sys.stdin.readline())
    a[num] += 1

for i in range(len(a)):
    if a[i] != 0:
        for j in range(a[i]):
            print(i)