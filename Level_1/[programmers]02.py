# 수박수박수박수박수?
def solution(n):
    answer = '수박'
    if n%2 == 0:
        answer *= n // 2
    else:
        answer *= n
        answer = answer[:n]
    return answer