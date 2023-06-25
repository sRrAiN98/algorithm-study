def solution(arr):
    answer = []
    if arr[0] == 10:
        answer.append(-1) 
    else:
        answer = arr
        answer.remove(min(answer))
    return answer