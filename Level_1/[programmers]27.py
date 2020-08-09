# 예산
def solution(d, budget):
    d.sort()
    for x in range(len(d)):
        if sum(d) > budget:
            d.pop()
    return len(d)