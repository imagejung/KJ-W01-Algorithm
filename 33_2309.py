#일곱 난쟁이 (다른 풀이도 공부 필요)
import sys

a = [int(sys.stdin.readline()) for i in range(9)]
a.sort()

sum_total = sum(a)

for i in range(8):
    for j in range(i+1, 9):
        if (sum_total - a[i] - a[j]) == 100:
            first = i
            second = j
            break

del a[first]
del a[second-1]

for i in range(7):
    print(a[i])
