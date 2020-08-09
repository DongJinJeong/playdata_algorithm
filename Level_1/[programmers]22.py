# 나누어 떨어지는 숫자 배열
def solution(arr, divisor):
    answer = []
    count = 0
    for i in range(len(arr)):
        if arr[i] % divisor == 0:
            answer.append(arr[i])
            count += 1

    if count == 0:
        answer.append(-1)
    return sorted(answer)