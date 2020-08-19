def change(num):
    num_list = []
    while num > 0:
        num_list.append(num % 2)
        num = num // 2
    return num_list


def solution(n):
    answer = 0
    b = n
    a = change(n)

    while True:
        b += 1
        a_1 = change(b)
        if a.count(1) == a_1.count(1):
            answer = b
            break

    return answer