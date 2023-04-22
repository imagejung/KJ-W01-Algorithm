#분할정복 _ 재귀함수

n, r, c = map(int, input().split())

def sol(n, r, c):
    if n == 0:
        return 0

    return 4 * sol(n - 1, r // 2, c // 2) + 2 * (r % 2) + (c % 2)

print(sol(n, r, c))