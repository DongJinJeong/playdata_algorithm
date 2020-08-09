# 같은 숫자는 싫어
def solution(arr):
    answer = []
    for i in range(len(arr)):
        if arr[i:i+1] == arr[i+1:i+2]:
            continue
        else:
            answer.append(arr[i])
    return answer