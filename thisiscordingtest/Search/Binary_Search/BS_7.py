def BS(arr,target,start,end) :
  arr.sort()
  if start > end :
    return False
  else :
    mid = (start+end) // 2 
    if arr[mid] == target :
      return mid
    elif arr[mid] < target :
      return BS(arr,target,mid+1,end)
    else :
      return BS(arr,target,start,mid-1)

arr = list(map(int,input().split()))

print(BS(arr,8,0,len(arr)-1))

