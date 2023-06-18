def solution(s):
    word = s.split(" ")
    lists = []
    #word = ["3people", "unFollowed", "me"]
    for a in word:
        if (a == "") :
            lists.append(a)
        else :
            temp = a[0].upper() + a[1:].lower()
            lists.append(temp)
    answer = " ".join(lists)
    return answer

def best_solution(s):
    return ' '.join([word.capitalize() for word in s.split(" ")])
