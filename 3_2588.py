import sys
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

ans_3 = a[0] * (b[0]%10)
ans_4 = a[0] * (b[0]//10%10)
ans_5 = a[0] * (b[0]//100%10)
ans_final = ans_3 + 10*ans_4 + 100*ans_5

print(ans_3)
print(ans_4)
print(ans_5)
print(ans_final)
