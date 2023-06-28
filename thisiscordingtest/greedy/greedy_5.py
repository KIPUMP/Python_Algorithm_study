N = int(input())            #거스름돈을 입력받는다
arr = [100 , 10, 50, 500]     #동전 sort 필요
arr.sort()
arr.reverse()			
count = []
m = 0

for i in arr :
    n = N // i
    count.append(n)
    N = N % i

for j in count :

    print(arr[m],"원: ",j, end = " \n")
    m+=1