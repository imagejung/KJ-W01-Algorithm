import sys
a = list(map(int, sys.stdin.readline().split()))
arr = [[0 for col in range(2)] for row in range(a[0])]

for i in range(0,a[0]):
    b = list(map(int, sys.stdin.readline().split()))
    arr[i]=[b[0],b[1]]

for i in range(0,a[0]):
    print(arr[i][0]+arr[i][1])

