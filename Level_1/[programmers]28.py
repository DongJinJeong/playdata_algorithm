# 체육복
def solution(n, lost, reserve):
    answer = 0
    total = list()

    for i in range(n):
        total.append(1)

    for i in lost:
        total[i - 1] -= 1

    for i in reserve:
        total[i - 1] += 1

    for i in range(len(total)):
        if total[i] == 2:
            if i - 1 >= 0:
                if total[i - 1] == 0:
                    total[i - 1] += 1
                    total[i] -= 1
        if total[i] == 2:
            if i + 1 < len(total):
                if total[i + 1] == 0:
                    total[i + 1] += 1
                    total[i] -= 1

    for student in total:
        if student >= 1:
            answer += 1

    return answer