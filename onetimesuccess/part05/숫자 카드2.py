from bisect import bisect_left,bisect_right

N = int(input())
card = sorted(map(int,input().split()))
M = int(input())
find_card = list(map(int,input().split()))
result = []

for i in find_card :
  result.append(bisect_right(card,i) - bisect_left(card,i))

for i in result :
  print(i,end=" ")
