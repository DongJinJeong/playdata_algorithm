def solution(N, stages):
    fail_rate = {}
    user = len(stages)

    for stage in range(1, N+1):
        if user != 0:
            fail = stages.count(stage)
            fail_rate[stage] = fail / user
            user -= fail
        else:
            fail_rate[stage] = 0

    return sorted(fail_rate, key=lambda x : fail_rate[x], reverse=True)