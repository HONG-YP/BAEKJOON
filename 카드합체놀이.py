#https://www.acmicpc.net/problem/15903
import heapq

n, m = map(int, input().split())
card_list = list(map(int, input().split()))

heapq.heapify(card_list) # 카드 리스트를 힙으로 변경

for _ in range(m):
    card1 = heapq.heappop(card_list) # 가장 작은 두 원소들을 pop
    card2 = heapq.heappop(card_list) # 가장 작은 두 원소들을 pop

    heapq.heappush(card_list, card1 + card2) # pop해준 두 원소들을 합친 후 push
    heapq.heappush(card_list, card1 + card2) # pop해준 두 원소들을 합친 후 push

print(sum(h))
