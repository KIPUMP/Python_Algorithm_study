import heapq
# 최소힙 구현
h = []
heapq.heappush(h,123)
heapq.heappush(h,789)
heapq.heappush(h,456)

while len(h) :
  print(heapq.heappop(h))