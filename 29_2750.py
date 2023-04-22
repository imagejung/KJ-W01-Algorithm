#수 정렬하기
n = int(input())
a = [int(input()) for i in range(n)]

# 삽입 정렬 활용
for i in range(1,n):
    while i>0:
        if a[i] < a[i-1]:
            a[i],a[i-1] = a[i-1],a[i]
            i -= 1
        else:
            break

for i in range(n):
    print(a[i])
