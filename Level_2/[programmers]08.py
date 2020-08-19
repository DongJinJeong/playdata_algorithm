def solution(n):
    answer = 0
    F = [0, 1]

    for i in range(n - 1):
        F.append(F[i] + F[i + 1])

    answer = F[n] % 1234567
    return answer