S = input()
all_num = 0
arr = []
for i in S:
    if i.isdigit() == True :
        all_num += int(i)
    else:
        arr.append(i)
        
arr.sort()
arr.append(str(all_num))
print(''.join(map(str,arr)))



