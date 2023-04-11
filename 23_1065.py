a = input()
cnt = 0

if int(a) < 100:
    print(a)
else:
    for i in range(100, int(a)+1):
        j = str(i)
        if int(j[2]) - int(j[1]) == int(j[1]) - int(j[0]):
            cnt += 1
    print("{}".format(cnt + 99))

