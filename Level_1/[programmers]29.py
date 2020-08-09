# 시저암호
def solution(s, n):
    answer = list()

    for i in list(s):
        i = ord(i)

        if 64 < i < 91:
            if 90 < i + n:
                i = 64 + n - (90 - i)
                answer.append(chr(i))
            else:
                answer.append(chr(i + n))
        elif 96 < i < 123:
            if 122 < i + n:
                i = 96 + n - (122 - i)
                answer.append(chr(i))
            else:
                answer.append(chr(i + n))
        else:
            answer.append(chr(i))

    answer = "".join(answer)
    return answer