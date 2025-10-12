def QS(arr) :
  if len(arr) <= 1 :
    return arr

  else :
    pivot = arr[0]
    arr = arr[1:]

    left_side = [i for i in arr if i <= pivot]
    right_side = [i for i in arr if i > pivot]

    return QS(left_side) + [pivot] + QS(right_side)

arr = list(map(int,input().split()))

print(QS(arr))