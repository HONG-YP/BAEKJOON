#https://programmers.co.kr/learn/courses/30/lessons/12909

def solution(s):
    stack = []
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(s[i])
        else:
            if stack == []:
                return False
            else:
                stack.pop()
    return stack == []
