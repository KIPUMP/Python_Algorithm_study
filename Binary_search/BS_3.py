from bisect import bisect_left, bisect_right

arr = list(map(int, input().split()))
x = int(input())

arr.sort()

print(bisect_left(arr,x))
print(bisect_right(arr,x))


# bisect_left :  정렬된 순서를 유지하면서 배열 arr에 x를 삽일 할 가장
# 왼쪽 인덱스를 반환
#  bisect_right :  정렬된 순서를 유지하면서 배열 arr에 x를 삽입 할 가장 
#  오른쪽 인덱스를 반환 