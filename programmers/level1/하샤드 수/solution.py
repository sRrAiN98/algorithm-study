def solution(x):
    answer = True
    
    temp = 0
    strx = str(x)
    counts = len(str(x))
    
    for i in range(counts):
        temp += int(strx[i])
        
    if x % temp == 0:
        return True
    else:
        return False
    
    print(temp)
    return answer