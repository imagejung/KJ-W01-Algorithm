#외판원 순회2 (라이브러리 추가해서 순열로 품. 다른 방법도 해보기)

import sys
from itertools import permutations

t = int(input())
cost = [list(map(int, sys.stdin.readline().split())) for i in range(t)]

per = permutations(list(range(t)))


