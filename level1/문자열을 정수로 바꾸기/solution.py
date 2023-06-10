def solution(n):
    answer = 0
    strn = str(n)
    print(strn)
    for i in range(len(str(n))):
        answer += int(strn[i])

    return answer
