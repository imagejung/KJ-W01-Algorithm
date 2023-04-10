max = 0

for i in range(9):
    tmp = int(input())
    if max < tmp:
        max = tmp
        index = i+1

print(max)
print(index)
