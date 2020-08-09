# 자릿수 더하기
def solution(n):
    answer = list()
    answer_list = list(str(n))
    for i in answer_list:
        answer.append(int(i))

    return sum(answer)