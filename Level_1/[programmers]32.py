def solution(s):
    answer = []
    n_answer = s.split(" ")

    print(n_answer)

    for i in n_answer:
        for idx, j in enumerate(list(i)):
            if idx % 2 == 0:
                answer.append(j.upper())
            else:
                answer.append(j.lower())
        answer.append(" ")

    return "".join(answer)[:-1]