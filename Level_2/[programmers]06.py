def solution(s):
    answer = []
    s_sp = s.split()
    s_list = list(map(int, s_sp))

    s_answer = sorted(s_list)
    answer.append(str(s_answer[0]))
    answer.append(str(s_answer[-1]))

    return " ".join(answer)