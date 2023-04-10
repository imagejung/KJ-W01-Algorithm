import sys
a = list(map(int, sys.stdin.readline().split()))

for i in range(a[0]):
    scores = list(map(int, sys.stdin.readline().split()))

    #평균 구하기
    scores_sum = 0
    for j in range(1, scores[0]+1):
        scores_sum += scores[j]
    scores_avg = scores_sum / scores[0]

    #평균보다 높은 학생수
    cnt = 0
    for k in range(1, scores[0]+1):
        if scores[k] > scores_avg:
           cnt += 1

    print("{:.3f}%".format((cnt / scores[0])*100))