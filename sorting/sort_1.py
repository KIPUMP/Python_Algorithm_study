#선택 정렬
arr = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(arr)):
    min = i
    for j in range(i+1,len(arr)):
        if arr[min] > arr[j] :
            min = j
    arr[i], arr[min] = arr[min] , arr[i]      #swap

print(arr)