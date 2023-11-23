from bisect import bisect_left, bisect_right

mylist = [1,2,3,3,3,7,9,11,33]
x = 3

print(bisect_left(mylist,x))
print(bisect_right(mylist,x))