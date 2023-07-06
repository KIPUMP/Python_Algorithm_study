def quick_sort(arr) :
  if len(arr) <= 1 :
    return arr
  else :
    pivot = arr[0]
    arr = arr[1:]
    
    left_side = [x for x in arr if x <= pivot]
    right_side = [x for x in arr if pivot < x]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)


mess = list(map(int,input().split()))

print(quick_sort(mess))