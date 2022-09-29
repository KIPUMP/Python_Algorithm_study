# 사전 자료형
# data = dict()
# data['사과'] = 'apple'
# data['바나나'] = 'banana'
# data['코코넛'] = 'coconut'

# print(data)

# if '사과' in data :
#     print("사과 를 키로 가지는 데이터가 존재합니다.")


# 집합 자료형
# a = set([1,2,3,4,5])
# b = set([1,2,3,4,5,2])
# print(a|b)
# print(a&b)
# print(a-b)

a = set([1,2,3])
a.add(4)
print(a)

a.update([5,6])
print(a)
a.remove(1)

print(a)