a = input()
cnt = 0

if int(a) < 100:
    print(a)
else:
    for i in range(100,int(a)+1):
        if int(a[2]) - int(a[1]) == int(a[1]) - int(a[0]):
            cnt += 1

print ("{}".format(cnt + 99))