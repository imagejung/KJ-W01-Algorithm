#단어 정렬
import sys

#입력 받기
t = int(sys.stdin.readline())
a = [sys.stdin.readline().strip() for i in range(t)]

#글자수랑 묶어서 list 만들어줌
sort_a = []
for i in a:
    sort_a.append((len(i),i))

answer = sorted(sort_a)

#마지막 글자 출력위해 list index 1 늘려줌
answer.append((0,0))

#중복 비교 및 출력
for i in range(len(answer)-1):
    if answer[i][1] == answer[i+1][1]:
        continue
    else:
        print(answer[i][1])




# import sys
#
# t = int(sys.stdin.readline())
# a = [sys.stdin.readline().strip() for i in range(t)]
#
# # 알파벳 순으로 정렬
# a.sort()
#
# # 글자수 별로 정렬
# for i in range(1, t):
#     while i>0:
#         if len(a[i]) < len(a[i-1]):
#             a[i],a[i-1] = a[i-1],a[i]
#             i -= 1
#         else:
#             break
#
# a.append("end")
#
# # 중복된 항목 삭제하여 출력
# for i in range(t):
#     if a[i] == a[i+1]:
#         continue
#     else:
#         print(a[i])

