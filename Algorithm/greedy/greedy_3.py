S = str(input())
arr = []
i = 0
j = 1
result = 0

for num in S:
    arr.append(num)

while i != len(S)-1 :
    
    if int(arr[i]) == 0 or int(arr[j]) ==0 :
        result = int(arr[i]) + int(arr[j])
    else :
        result = int(arr[i]) * int(arr[j])
    
    i +=1
    j +=j
    
print(result)
        
        
        