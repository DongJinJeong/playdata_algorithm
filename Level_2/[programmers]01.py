def solution(n):
    answer = ""

    while n > 0:
        n, i = divmod(n, 3)  # n : 몫, i : 나머지

        if i == 0:
            n = n - 1

        answer = '412'[i] + answer
    return answer