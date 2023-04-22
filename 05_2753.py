import sys
a = list(map(int, sys.stdin.readline().split()))

if a[0] % 4 == 0:
    if (a[0]%100 != 0) or (a[0]%400 == 0):
        print(1)
    else:
        print(0)
else:
    print(0)
