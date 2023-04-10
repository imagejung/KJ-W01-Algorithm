import sys
a = list(map(int, sys.stdin.readline().split()))

for i in range(1,10):
    print("{} * {} = {}".format(a[0], i, a[0]*i))
