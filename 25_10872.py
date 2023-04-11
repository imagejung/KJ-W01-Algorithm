n = int(input())

def fact(value):
    ans = 1
    if value>1:
        ans = value * fact(value-1)
    return ans

print(fact(n))