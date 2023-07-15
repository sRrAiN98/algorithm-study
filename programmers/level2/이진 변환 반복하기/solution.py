def solution(s):
    answer = []
    zero = 0
    count = 0 
    while s != "1":
        nums = ""
        for i in s:
            if i == "1":
                nums += i
            elif i == "0":
                zero += 1
        count += 1
        s = str(bin(len(nums))[2:])
        print(f"{count} {s}")
        
    answer.append(count)
    answer.append(zero)
    return answer