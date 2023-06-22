def binary_search (arr, target, start, end) :
    if start > end :
        return None
    mid = (start + end) // 2

    if arr[mid] == target :
        return mid
    
    elif arr[mid] > target :
        return binary_search(arr, target, start, mid-1)
    
    else:
        return binary_search(arr, target, mid+1, end)

n, target = list(map(int,input().split()))

arr = list(map(int, input().split()))

result = binary_search(arr, target, 0, n-1)

<<<<<<< HEAD
print(result)
=======
if result == None :
    print("원소가 존재하지 않습니다")
else :
    print(result + 1)
>>>>>>> 3b90494c3bdb1350473da28d65ce901389a1c5e2

