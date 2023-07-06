import sys

def binary_search(arr,n,x) :
  arr.sort()
  start = 0
  end = n-1
  
  if start > end :
    return None

  else :
    mid = (start + end) // 2
    if x == arr[mid] :
      return arr[mid]
    
    elif x < arr[mid] :
      return binary_search(arr,start,mid-1)
    
    else :
      return binary_search(arr,mid+1,end)



n = int(sys.stdin.readline())
arr_1 = list(map(int,input().split()))
m = int(sys.stdin.readline())
arr_2 = list(map(int,input().split()))


for i in range(m) :
  if binary_search(arr_1,n,arr_2[i]) :
    print("yes",end=" ")
  else :
    print("no",end=" ")