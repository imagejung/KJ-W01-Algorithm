#차이를 최대로 (라이브러리 추가 코드, 순열 라이브러리 추가 하지 않고도 확인해보기)
from itertools import permutations
import sys

t = int(input())
a = list(map(int, sys.stdin.readline().split()))

per = permutations(a)

ans = 0
for i in per:
    tmp = 0
    for j in range(t-1):
        tmp += abs(i[j]-i[j+1])
    if tmp>ans:
        ans = tmp

print(ans)