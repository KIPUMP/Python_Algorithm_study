array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array) :
  if len(array) <= 1 :
    return array 
  else :
    pivot = array[0]
    array = array[1:]
    left_side = [x for x in array if x < pivot]
    right_side = [x for x in array if x > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))