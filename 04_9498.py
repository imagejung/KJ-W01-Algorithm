import sys
a = list(map(int, sys.stdin.readline().split()))

if a[0] >= 90:
    print("A")
elif a[0] >= 80:
    print("B")
elif a[0] >= 70:
    print("C")
elif a[0] >= 60:
    print("D")
else:
    print("F")
