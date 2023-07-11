def solution(s):
    if s[0] == ")" or s.count("(") != s.count(")"):
        return False
    
    que = []
    for i in s:
        if i == "(":
            que.append("(")            
        if i == ")":
            if not que:
                return False
            que.pop()
            
    if not que:
        return True
    else: 
        return False
