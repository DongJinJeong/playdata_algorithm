def solution(arr1, arr2):
    answer = []

    for idx1 in range(len(arr1)):
        row = []
        for idx2 in range(len(arr2[0])):
            num = 0
            for idx3 in range(len(arr1[0])):
                num += arr1[idx1][idx3] * arr2[idx3][idx2]
            row.append(num)
        answer.append(row)

    return answer