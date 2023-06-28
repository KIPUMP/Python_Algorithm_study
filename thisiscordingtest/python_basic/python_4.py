a = [1,2,3,4,5,6,7,8,9]
print(a)

print(a[3])

n = 10
a = [0]* n
print(a)
# 뒤 쪽에서 첫번쨰 문자 
print(a[-1])
# 뒤 쪽에
print(a[-3])

a[3] = 10
print(a)

b = [1,2,3,4,5,6,7,8,9]
# 리스트 슬라이싱 array[인덱스 : n번쨰 원소]
print(b[1:4])

c = [i for i in range(10)]
print(c)