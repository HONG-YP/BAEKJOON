#https://programmers.co.kr/learn/courses/30/lessons/42628
# nlargest, nsmallest (n, iter): 힙에서 가장 큰값, 작은 값 n개 까지 반환

import heapq

def solution(operations):
    h = []
    for i in operations:
        oper = i.split()
        if oper[0] == 'I':
            heapq.heappush(h, int(oper[1]))
        else:
            if len(h) == 0:
                pass
            elif oper[1] == '-1':
                heapq.heappop(h)
            else:
                h.pop(h.index(heapq.nlargest(1, h)[0]))
    if len(h) == 0:
        return [0,0]
    else:
        return [heapq.nlargest(1, h)[0],heapq.nsmallest(1, h)[0]]
