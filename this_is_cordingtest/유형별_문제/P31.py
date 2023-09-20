for i in range(int(input())):
  n,m = map(int,input().split())
  d = [[0] * m for _ in range(n)]
  gold = list(map(int,input().split()))
  cnt = 0
  for i in range(n) :
    for j in range(m) :
      d[i][j] = gold[cnt]
      cnt += 1
      if cnt == len(gold) :
        break
    if cnt == len(gold) :
      break
  
  for j in range(1,m) :
    for i in range(n) :
      if i == 0 :
        left_up = 0
      else :
        left_up = d[i-1][j-1]
      if i == n - 1 :
        left_down = 0
      else :
        left_down = d[i+1][j-1]
      left = d[i][j-1]
      d[i][j] = d[i][j] + max(left,left_down,left_up)

  result = 0
  for i in range(n) :
    result = max(result,d[i][m-1])
  print(result)