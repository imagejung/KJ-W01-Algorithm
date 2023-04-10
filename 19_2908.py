a = list(map(str, input().split()))

num1 = int(a[0][2]+a[0][1]+a[0][0])
num2 = int(a[1][2]+a[1][1]+a[1][0])

print(max(num1,num2))