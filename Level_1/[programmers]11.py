# 행렬의 덧셈
def solution(arr1, arr2):
    answer = list()
    x, y = len(arr1), len(arr2[0])
    for i in range(x):
        tmp = []
        for j in range(y):
            tmp.append(arr1[i][j] + arr2[i][j])
        answer.append(tmp)
    return answer