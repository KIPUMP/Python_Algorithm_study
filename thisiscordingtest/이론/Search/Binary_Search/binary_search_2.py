def binary_search(arr,target,start,end) :
  arr.sort()
  if start > end :
    return None 
  else :
    mid = (start + end) // 2
    if arr[mid] == target :
      return mid
    elif arr[mid] < target :
      return binary_search(arr,target,mid+1,end)
    else :
      return binary_search(arr,target,start,mid-1)


dict = list(map(int,input().split()))
n = int(input())

print(binary_search(dict,n,0,len(dict)-1))