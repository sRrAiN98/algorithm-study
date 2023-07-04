def solution(arr1, arr2):
    answer = arr1
    arrSize1 = len(arr1)
    arrSize2 = len(arr1[0])
    
    for i in range(arrSize1):
        for j in range(arrSize2):
            answer[i][j] = arr1[i][j] + arr2[i][j]
    return answer
