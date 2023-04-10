a = int(input())

def find_sosu(n):
    tmp = 0
    if n == 1 or n == 0:
        tmp = 1

    for i in range(2,n):
        if n % i == 0:
            tmp = 1
            break

    if tmp == 0:
        return 0
    else:
        return 1


for i in range(a):
    b = int(input())

    n =  b // 2
    while n != 1:
        if find_sosu(n) == 0:
            if find_sosu(b-n) == 0:
                print("{} {}".format(n, b-n))
                break
            else:
                n -= 1
        else:
            n -= 1
