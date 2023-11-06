import sys
sys.setrecursionlimit(10**6)
def binary_search(arr,target,start,end) :
  if start > end :
    return False 

  else :
    mid = (start + end) // 2
    if target < arr[mid] :
      return binary_search(arr,target,start,mid-1)
    elif target > arr[mid] :
      return binary_search(arr,target,mid+1,end)
    else :
      return mid

arr = sorted(map(int,input().split()))

print(binary_search(arr,3,0,len(arr)-1))
