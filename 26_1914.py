n = int(input())

def hanoi (n, a, b, c):  # n개를 a에서 b로
    if n == 1:
        print("{} {}".format(a, c))
    else:
        hanoi (n-1, a, c, b)
        hanoi (1, a, b, c)
        hanoi (n-1, b, a, c)

print(2**n-1)
if (n<=20):
    hanoi (n, 1, 2, 3)
