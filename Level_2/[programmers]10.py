def solution(s):
    answer = []
    s_list = list(s)

    for i in range(len(s_list)):
        if i == 0:
            answer.append(s_list[i].upper())
            continue
        elif s_list[i] == " ":
            answer.append(s_list[i])
        elif s_list[i - 1] == " ":
            answer.append(s_list[i].upper())
        else:
            answer.append(s_list[i].lower())

    return "".join(answer)