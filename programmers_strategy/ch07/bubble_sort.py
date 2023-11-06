sample = [3,0,1,8,7,2,5,4,6,9]

def bubble_sort(data) :
  for i in range(len(data) - 1) :
    for j in range(i) :
      if data[i] > data[j+1] :
        data[j],data[j+1] = data[j+1],data[j]

bubble_sort(sample)
print(sample)