def QS(arr) :
  if len(arr) <=1 :
    return arr
  else :
    pivot = arr[0]
    arr = arr[1:]
    
    left_side = [x for x in arr if x <= pivot]
    right_side = [x for x in arr if x > pivot]

    return QS(left_side) + [pivot] + QS(right_side)

arr = list(map(int,input().split()))

print(QS(arr))