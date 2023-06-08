def solution(n):
    answer = n+1
    n1 = format(n, 'b')
    n2 = str(format(n, 'b'))    
    while (True):
        answer1 = str(format(answer, 'b'))
        
        if n2.count('1') == answer1.count('1'):
            return answer
        else:
            print(answer)
            answer += 1
    return answer
