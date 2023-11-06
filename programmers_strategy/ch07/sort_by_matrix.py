sample = [[0,4],[0,2],[1,3],[2,1]]

def second(x) :
  return x[1]

print(sorted(sample,key = second))
print(sorted(sample,key=lambda x : x[1]))