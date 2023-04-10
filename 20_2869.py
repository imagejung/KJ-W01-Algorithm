import sys
input_value = list(map(int, sys.stdin.readline().split()))

a,b,v = input_value
h = 0
day = 0

if (v-a)%(a-b) == 0:
    day = (v-a)/(a-b) + 1
else:
    day = (v-a)/(a-b) + 2

print(int(day))
