def binary_search(arr,target,start,end) :
  if start > end :
    return False 
  else :
    mid = (start + end) // 2
    if arr[mid] == target :
      return mid
    elif arr[mid] > target :
      return binary_search(arr,target,start,mid-1)
    else :
      return binary_search(arr,target,mid+1,end)



arr = list(map(int,input().split()))
n = int(input())
if binary_search(arr,3,n,len(arr)-1) :
  print("false")
else :
  print(binary_search(arr,n,0,len(arr)-1))