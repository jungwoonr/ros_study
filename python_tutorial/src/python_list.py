list = [0,"1",2,"3"] #list는 중간에 문자열을 넣어도 상관없음 (배열은 X)
print(list)

# print(list[0] + list[2])

# print("join: ", ''.join(list))

# f'{list[1]}{list[0]}'

list2 = [0,"1",2,[100,200,300]]
print(list2)
print(list2[3][1])

list3 = ["h","e","l","l","o"]
list4 = ["w","o","r","l","d"]
# print(list3)
# print(list3[:])
print(list3 + list4)
print(len(list3 + list4))
print(str(list2[0]) == 0)
print(type(str(list2[0])))

del list3[2]
print("edit:", list3)

list3.append("w")
print("append:", list3)

list3.insert(2,"r")
print("insert:", list3)

# 클리어 모두 삭제 []
# list3.clear()
# v = list.pop(0)

sorting = [0,1,2,3,4,5,6,7,8,9]
sorting.sort()
print("sorting:", sorting)

sorting.sort(reverse=True)
print("sorting:", sorting)

sorting.reverse()
print("sorting:", sorting)

# 없는 인덱스 참조시 예외발생 (try로 잡아줘야함)
# sorting.index(10)

# print("sorting111:", sorting)

# 해당 인덱스를 삭제
# del sorting[2]
# 값이 동일한 항목삭제 (낮은 인덱스의 값만 제거)
sorting.remove(2)
print("remove:", sorting)

p = sorting.pop(2)
print("pop:", sorting)
print("p:", p)

sorting.extend([100,200])
print("sorting extend:", sorting)

tup = (0,1,2,3,4,5)
# list(tup)[2] = 10

# 6x6
#[
# [0,0,0,0,0,0]
# [0,0,0,0,0,0]
# [0,0,0,0,0,0]
# [0,0,0,0,0,0]
# [0,0,0,0,0,0]
# [0,0,0,0,0,0]
# ]

# 6x6
# [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]