def solution(numbers):
    answer = -1
    anynum = [1,2,3,4,5,6,7,8,9,0]
    for i in numbers:
        anynum.remove(i)
    answer= sum(anynum)
    
    return answer