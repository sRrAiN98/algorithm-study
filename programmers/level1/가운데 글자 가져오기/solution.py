def solution(s):
    answer = ''
    if len(s) % 2 == 0:
        length = int(len(s) / 2)
        answer = s[length-1:length+1]
    else:
        length = int(len(s) / 2)
        answer = s[length:length+1]
    return answer