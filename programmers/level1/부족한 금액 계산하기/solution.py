def solution(price, money, count):
    answer = -1
    dab = 0 
    for i in range(1, count+1):
        dab += price * i
    if money - dab < 0:
        answer = money - dab
    else:
        answer = 0
    
    return abs(answer)


# def solution2():
#     answer = money
#     for i in range(1, count+1, 1):
#         answer -= price * i
        
#     print(f'{answer} ')
#     if answer < 0:
#         return abs(answer)
#     else:
#          answer = 0

#     return answer