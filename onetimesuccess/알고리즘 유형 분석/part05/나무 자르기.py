N,M = map(int,input().split())
tree = list(map(int,input().split()))
lo = 0
hi = max(tree)
mid = (lo + hi) // 2

def get_total_tree(h) :
  ret = 0
  for t in tree :
    if t > h :
      ret += t - h  
  return ret

result = 0
while lo <= hi :
  if get_total_tree(mid) >= M :
    result = mid
    lo = mid + 1
  else :
    hi = mid - 1
  mid = (lo + hi) // 2

print(result)
