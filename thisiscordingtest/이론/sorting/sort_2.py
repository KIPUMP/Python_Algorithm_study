#삽입 정렬
arr = [7,5,9,0,3,1,6,2,4,8]

for i in range(1,len(arr)):
    for j in range(i,0,-1) :        # 0에서 i 까지 1씩 빼주면서 비교
        if arr[j] < arr[j-1]:
            arr[j],arr[j-1] = arr[j-1] , arr[j]     #swap
        else :
            break

print(arr)