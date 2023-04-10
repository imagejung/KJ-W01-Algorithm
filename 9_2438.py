import sys
a = list(map(int, sys.stdin.readline().split()))
n = a[0]

for i in range(1,n+1):
    print("*"*i)
