x,y = map(int, input().split())
x_line = [0,x]
y_line = [0,y]
t = int(input())


for i in range(t):
    cut = list(map(int, input().split()))
    if cut[0] == 1 :
        x_line.append(cut[1])
    else:
        y_line.append(cut[1])
x_line.sort()
y_line.sort()


ans = []
for i in range(len(x_line)-1):
    for j in range(len(y_line)-1):
        ans.append(( x_line[i+1] - x_line[i] ) * ( y_line[j+1] - y_line[j] ))
ans.sort(reverse=True)


print(ans[0])




