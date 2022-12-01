# sequential search : 순차탐색
def sequential_search(n, target, arr) :
    for i in range(n) :
        if arr[i] == target :
            return i+1
    

input_data = input().split()
n = int(input_data[0])
target = input_data[1]

arr = input().split()

print(sequential_search(n, target, arr))
