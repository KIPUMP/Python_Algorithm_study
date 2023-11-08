sample = [3,0,1,8,7,2,5,4,6,7]

def merge(left,right) :
  result = []
  while len(left) > 0 and len(right) > 0 :
    if left[0] <= right[0] :
      result.append(left[0])
      left = left[1:]
    else :
      result.append(right[0])
      right = right[1:]
  result.extend([*left,*right])
  return result

def merge_sort(data) :
  if len(data) <= 1 :
    return data
  mid = len(data) // 2
  left = merge_sort(data[:mid])
  right = merge_sort(data[mid:])
  return merge(left,right)

print(merge_sort(sample))