def permutation(arr) :
  result = [arr[:]]
  c = [0] * len(arr)
  i = 0
  while i < len(arr) :
    if c[i] < i :
      if i % 2 == 0 :
        arr[0],arr[i] = arr[i] , arr[0]
      else :
        arr[c[i]],arr[i] = arr[i],arr[c[i]]
      result.append(arr[:])
      c[i] += 1
      i = 0
    else :
      c[i] = 0
      i += 1
    return result

def permutations(arr,n) :
  result = []
  if n == 0 :
    return [[]]
  for (i,num) in enumerate(arr) :
    for j in permutation(arr[:i] + arr[i+1 : ],n-1) :
      result.append([num] + j)
  return result