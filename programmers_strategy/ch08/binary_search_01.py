import sys
sys.setrecursionlimit(10**6)

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

    