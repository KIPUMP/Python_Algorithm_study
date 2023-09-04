import sys
input = sys.stdin.readline
T = 0
while True :
  T += 1
  cnt = 0
  L,P,V = map(int,input().split())
  if L == 0 and P == 0 and V == 0 :
    break
  for _ in range(V//P) :
    cnt += L
  
  for i in range(V%P) :
    cnt += 1
  
  print(f"Case{T} : {cnt}")


  

