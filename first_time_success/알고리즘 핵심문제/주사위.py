n = int(input())
dice = sorted(map(int,input().split()))

def get_min3() :
  result = 150
  for i in range(4) :
    for j in range(i+1,5) :
      if i + j != 5 :
        for k in range(j+1,6) :
          if j + k != 5 and k + i != 5 :
            result = min(result,dice[i] + dice[j] + dice[k])
  return result

def get_min2() :
  result = 100
  for i in range(5) :
    for j in range(i+1,6) :
      if i + j != 5 :
        result = min(result,dice[i] + dice[j])

  return result


if n == 1:
  print(sum(dice)- max(dice))
else :
  print(4 * get_min3() + 4 * (2 * n - 3) * get_min2() + (n-2) * (5 * n - 6) * min(dice))
