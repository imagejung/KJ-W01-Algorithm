# N-Queen

n = int(input())

ans = 0
row = [0] * n


def is_promising(promising_x):
    for promising_i in range(promising_x):
        if row[promising_x] == row[promising_i] or abs(row[promising_x] - row[promising_i]) == abs(promising_x - promising_i):
            return False

    return True


def n_queens(queens_x):
    global ans
    if queens_x == n:
        ans += 1
        return

    else:
        for queens_i in range(n):
            # [x, i]에 퀸을 놓겠다.
            row[queens_x] = queens_i
            if is_promising(queens_x):
                n_queens(queens_x + 1)


n_queens(0)
print(ans)

