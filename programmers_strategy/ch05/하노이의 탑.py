def hanoi(n,start,mid,end,answer) :
  if n == 1 :
    return answer.append((start,mid))
  else :
    hanoi(n-1,start,end,mid,answer)
    hanoi(1,start,mid,end,answer)
    hanoi(n-1,mid,start,end,answer)

answer = []
n = int(input())
hanoi(n,1,2,3,answer)
for i in answer :
  print(*i)
