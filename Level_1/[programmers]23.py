# 모의고사
def solution(answers):
    answer = []
    players = [0, 0, 0]
    pattern = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]

    for idx1, x in enumerate(answers):
        for idx2, y in enumerate(pattern):
            if x == y[idx1 % len(y)]:
                players[idx2] += 1

    for idx, value in enumerate(players):
        if value == max(players):
            answer.append(idx + 1)
    return answer