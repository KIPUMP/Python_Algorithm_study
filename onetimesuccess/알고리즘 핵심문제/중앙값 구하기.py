for i in range(int(input())) :
  M = int(input())
  ipt = []
  for _ in range(M // 10 + 1 if M % 10 else M // 10) :
    ipt += map(int,input().split())
  
  arr = []
  ans = 