import sys
a = list(map(int, sys.stdin.readline().split()))

[x, y, w, h] = a

if min(w-x, x-0) >= min(h-y, y-0) :
    print(min(h-y,y-0))
else:
    print(min(w-x, x-0))

