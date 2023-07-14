def quick_sort(arr) :
  if len(arr) <= 1 :
    return arr 
  else :
    pivot = arr[0] 
    arr = arr[1:]

    left_side = [x for x in arr if x <= pivot]
    right_side = [x for x in arr if x > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)


def binary_search(arr,target,start,end) :
  if start > end :
    return False
  else :
    mid = (start + end) // 2 
    if arr[mid] == target :
      return mid
    elif arr[mid] < target :
      return binary_search(arr,target,mid+1,end)
    else :
      return binary_search(arr,target,start,mid-1)
    
    