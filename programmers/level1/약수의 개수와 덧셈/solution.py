import math
def solution(left, right):
    answer = 0
    divisor1 = []
    for i in range(left, right+1):
        for j in range(1, i+1):
            if i % j == 0:
                divisor1.append(j)
        if len(divisor1) % 2 == 0:
            answer += i
        else:
            answer -= i
        divisor1 = []
        print(f'{divisor1} {answer}')
    return answer
    

def solution2(left, right):    
    answer = 0
    for i in range(left, right + 1, 1):
        sqrt = math.sqrt(i)
        print(sqrt)
        if int(sqrt) == sqrt:
            answer -= i
        else:
            answer += i

    return answer