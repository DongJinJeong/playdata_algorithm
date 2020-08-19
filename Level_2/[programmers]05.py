def solution(n):
    total = 0
    for idx in range(1, n+1):
        answer = 0
        while answer < n:
            answer += idx
            idx += 1
        if answer == n:
            total += 1

    return total