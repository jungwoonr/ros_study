from ast import Try


print('Hello')

# while True:
#     print('Hello')
#     if exit:
#         break

integer = 10
double = 10.1123123123131312313123123131321323
integer2 = -10
double2 = -10.10

print("숫자 integer:", integer)
print("숫자 double:", double)
print("숫자 integer2:", integer2)
print("숫자 double2:", double2)


print("숫자 integer+integer2:", integer+integer2)
print("숫자 double+double2:", double+double2)

print("숫자 10**10:", 10 ** 10)
print("숫자 7 % 3:", 7 % 3)
print("숫자 7 // 4:", 7 // 4)


# 문자 == 단 하나의 문자만, 문자열 == 하나의 문자가 나열된거, 열은 다수, 순서를 가지고 있는 다수 
# "문자" '문자'   "'를 '문자'로 표시할때"   '"를 "문자"로 표시할때'

print("'문자열'")
print('"문자열"')

a = 'hello'
b = 'world'
print(a + b)

print("쌍따옴표를 표시하는 방법으로 \"서식문자\"")
print("줄내림 역시도 서식문자로\n표현이 가능합니다")

print('''
이렇게 줄내림을 해두면
명시적으로 우리 눈에서 이해가 쉽기에\n사용하면 가독성에 도움을 줄 수 있다
''')

print("="*50)
print("하나의문자열"*2)
print("="*50)

print("이 asdf문장의 길이는 몇일까? len:", len("이 asdf문장의 길이는 몇일까?"))

text = "문자열로써 인덱싱을 하는데 사용할 문자열"

# str = text[6:-5] + '추가된 글자'
# print("str: ", str)

format = "%10s" % "12345"
print("format:", format, sep="")

formatF = "%010.2f" % 3.14
print("formatF:", formatF, sep="")

print("1: 나의 이름은 {1}, {0} 입니다".format("이", "재권"))

print("2: 나의 이름은 {name}, {0} 입니다".format("이", name="재권"))

print("{0:#<10}끝".format("12345"))

print("{0:10.2f}끝".format(3.14))

print("{{}}".format())

name = "재권"
lastname = "이"

print(f'{name}, {lastname} {{}}')
print(f'{name:>10}')

print(f'{12345.14:010.5f}')

a = "aaabbbccc"
b = 'aaabbbccc'
c = str('aaabbbccc')

print("a의 개수: ", a.count('a'))
print("a의 개수: ", b.count('a'))
print("a의 개수: ", c.count('a'))

# print("b값의 인덱스: ", a.find('z'))

try:
    print("b값의 인덱스: ", a.index('z'))
except:
    print("오류:")

print("계속진행")

print("join: ", "#".join("asdf"))
print("join: ", "-".join(['010','9907','0317']))

print("upper: ", "a".upper())
print("lower: ", "B".lower())

# risekon@gmail.com
print("lower: ", "risekon@GMAIL.COM".lower())
print("lstrip:", "    risekon@GMAIL.COM".lower().lstrip(), sep="")
print("rstrip:", "risekon@GMAIL.COM    ".lower().rstrip() + "끝", sep="")
print("strip:", "    risekon@GMAIL.COM    ".lower().strip() + "끝", sep="")
print("replace:", "    risekon@GMAIL.COM    끝".replace(" ", ""), sep="")
print("replace:", "asdfasdf".replace("s", "w"), sep="")
print("replace:", "asdfasdf".replace("s", "w", 1), sep="")

print("join: ", "".join(["0","1","2"]))
print("split: ", "0,1,2".split(","))

split = "risekon@gmail.com".split("@")
id = split[0]
domain = split[1]

print("id:", id, sep="")
print("domain:", domain, sep="")
print("email:", "@".join([id, domain]) , sep="")



# print("type a: ", type(a))
# print("type b: ", type(b))
# print("type c: ", type(c))



#----------------------------



#문자열 formating....

name = "홍길동"                                        #name안에 홍길동이라는 문자열  
age = 30                                               #age라는 변수안에 30이라는 정수
                                                      
print(f'내 이름은{name}입니다.나이는 {age}입니다.')    # 출력/ f 포메팅을 이용한 name,age 값 넣어주기. 
print(f'내 나이는 {age+1}입니다.')                     # 출력/ f 포메팅은 표현식!! 가능.(표현식이란? 문자열안에서 변수와 +,-와 같은 수기 함께 사용하는것)




#------------------------------



d = {'Name' : '홍길동', 'Age' : 30}                             #d라는 딕셔너리, 키: Name,Age  값: 홍길동,30  
 
print(f"내 이름은 {d['Name']}입니다. 나이는 {d['Age']}입니다.")  #     {    } 중괄호 안에,  d[  ] d라는 딕셔너리를 리스트로 쓰고, 그 안에 key를 쓰면 
                                                                #value 값이 나온다.


# F 정렬

f'{"hi":<10}'             #왼쪽 정렬                < ,> ,^ 왼쪽, 오른쪽 ,가운데를 나타냄
print(f'{"hi":<10}')

f"{'hi':>10}"             #오른쪽 정렬             뒤에 숫자는 hi를 포함하여 10개 크기의 문자 공간을 만든다는 뜻.
print(f"{'hi':>10}")                          

f"{'hi':^10}"             #가운데 정렬             
print(f"{'hi':^10}")


print(f"{'ddddefef':<10}'korean'")       #ddddefef라는 10개 크기의 문자열을 왼쪽에 정렬한 후, korean이라고 출력해라.
                                         #ddddefef  'korean// ddddefef는 총 8개의 크기사용, 공백은 2개, 다시'korean' 출력.
print(len(f"{'ddddefef':<10}'korean'"))  #문자열의 길이를 정확게 계산해보기. len()함수를 이용해서 문자열 길이 계산.
                                         #ddddefef =8개, 공백 =2개 , 'korean' = 8개, '도 문자열 하나로 취급된다.

#----------------------------------

#소수점 표현.

#(1)
y = 3.141592                            # y에 실수 3.141592
f'{y:0.4f}'                             # f포매팅사용.  소수점 네자리까지만 사용
print(f'{y:0.4f}')                      # 5째자리에서 반올리하여서 소수점 네자리까지 출력. 3.1416
print(len((f'{y:0.4f}')))               # 길이 구해보기 3.1416  3,.,1,4,1,6  총 6개

#(2)
f'{y:<10.4f}'                           # f포매팅사용.  소수점 네자리까지만 사용, 왼쪽 정렬이고, 소수점 앞 숫자는 총 길이를 나타냄.
print(f'{y:<10.4f}')                    # y안에 있는 실수를 .4(소수점 네자리까지 사용하고),<(왼쪽 정렬하고),10(총길이는 10이다.)
print(len((f'{y:<10.4f}')))             # 길이 구해보기. 3,.,1,4,1,6 + 오른쪽 공백 4개.

#(3)
print(f'{y:>10.4f}')                    # 오른쪽 정렬을 했기에    3.1416 이렇게 나옴.  
print(len((f'{y:>10.4f}')))             # 위(2)번 예제와 다른점은 방향에(<,>) 따른 정렬일 뿐,len의 길이는 10으로 같다.

#문자열 관련함수 정리.

a = "hobby"
a.count('b')                            # b의 개수 세기 
print(a.count('b'))                     # 2개

a.index('b')                            # b의 개수가 두개이므로 앞에 먼저 오는 b의 위치를 반환한다.
print(a.index('b'))                     # 2번째.
#print(a.index('z'))                     # 문자열 a에 없는 문자이므로 에러 발생.

a.find('b')                             # 위의 인덱스와 같은 역할이지만, 다른점은 문자열안에 없는 문자를 반환할 경우, 반환하는 값이 다른뿐.
print(a.find('b'))                      # 2번째
print(a.find('z'))                      # 문자열 a에 없는 문자일 경우, -1 반환. (=!index)//index와 다른점.

