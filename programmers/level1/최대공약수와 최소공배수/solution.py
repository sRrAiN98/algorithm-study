def solution(n, m):
    answer = [None]
    i = 1
    
    while n > i or m > i:
        if n % i == 0 and m % i == 0:
            print(i)
            answer[0] = i
        i+=1
        if n <= i and m <= i:
            print(i)

        
    for i in range(max(n,m), (n*m) + 1):
        if i % n == 0 and i % m == 0:
            answer.append(i)
            break

    return answer