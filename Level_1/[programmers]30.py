# 비밀지도
import numpy as np

def solution(n, arr1, arr2):
    answer = []
    arr1_2 = []
    arr1_2_list = []
    arr2_2 = []
    arr2_2_list = []
    total_list = []
    s_list = []

    for i in arr1:
        for j in range(n):
            arr1_2.append(i % 2)
            i = i // 2
        arr1_2_list.append(arr1_2[::-1])
        arr1_2 = []

    for i in arr2:
        for j in range(n):
            arr2_2.append(i % 2)
            i = i // 2
        arr2_2_list.append(arr2_2[::-1])
        arr2_2 = []

    total_list = np.array(arr1_2_list) + np.array(arr2_2_list)

    print(total_list)
    for i in total_list:
        for j in range(len(i)):
            if i[j] >= 1:
                s_list.append("#")
            else:
                s_list.append(" ")
        answer.append("".join(s_list))
        s_list = []

    return answer