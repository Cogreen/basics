# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 10:19:30 2018

@author: stu
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 10:40:50 2018

@author: stu
"""

import keyword
keyword.kwlist 

x=10
x
print(x)
type(x)

a = 1
a = a +1
a +=1

a = a-1
a -=1
print(a)

a = a*1
a *=1

a = a/2
a /=2

a = a//2
a //= 2

f = 10.12 #부동소숫점(float)
type(f)

f = 10.4e3 #지수표현 10.4*10**
type(f)

x = 1
y = 2
y > x
y >= x
y <= x
y == x
y != x


2 > 1 and 3 > 2
2 > 1 or 3 >2
not 1 > 2  # and or not 


[문제1] x,y 변수에 있는 값을 기준으로 수행한 결과 입니다. 
x 와 y 변수에 어떤 값이 있어야 하나요.
또한 결과값이 나오기 위해서 어떤 계산식을 만들어야 하는지 계산식을 만들어 보세요.

#result_1~result_8 단순연산자 
result_1 =  7
result_2 =  3
result_3 =  -3
result_4 =  10
result_5 =  0.4
result_6 =  0
result_7 =  2
result_8 =  32
#result_9 복합연산자
result_9 =  7.0
result_10 =  -21
result_11 =  50
result_12 =  29

x= 5
y= 2

result_1= x+y 
print(result_1)
result_2 =x-y 
print(result_2)
result_3 =y-x
print(result_3)
result_4 = x*y
print(result_4)
result_5 = y/x
print(result_5)
result_6 = y//x
print(result_6)
result_7 = y%x
print(result_7) 
result_8 = y**x 
print(result_8)

result_9 = result_5* x + x 
print(result_9)
result_10 = (x+y) * (y-x)
print(result_10)
result_11 = (x*y) * x
print(result_11)
result_12 = x**y+y**y
print(result_12)

result_9 = result_5*x + x
print(result_9)
result_10 = result_1 * result_3
print(result_10)
result_11 = result_4 * x
print(result_11)
result_12 =x**y+y**y
print(result_12)

print("result_1=", result_1)

#변수확인
dir() #선언된 변수 확인
locals()
del(x) #선언된 변수 삭제


문자열 
'대한민국'
"짝짝짝"
"""대한민국
짝짝짝"""


\n
print("오늘 하루도 \n 행복하자")

\t
print("오늘 하루도 \t 행복하자")
print("잘하자\t 파이썬")

\0 #공백문자
print("잘하자\0파이썬")

\\ #표시
print("잘하자\0파이썬\\R")

\\
print("잘하자\'파이썬\'")
print("잘하자'파이썬'")

x = '김현정'
y = '파이썬 개발자'
type(x)
x+y #문자+문자 연결연산자

# 문자에서 *(곱)은 반복연산자(복제)
(x+y)*2

print('='*15)
print("hello world")
print("="*15)


# 포맷팅 코드: %s(문자 포맷) , 들어가야할 값 %( , )
name = "제임스"
music = "클래식"

print("안녕하세요. {}입니다. 즐겨듣는 음악은 {}입니다.".format(name, music))
print("안녕하세요. %s입니다. 즐겨듣는 음악은 %s입니다." %(name, music))

# 포맷팅 코드: %d (정수 포맷)
x = 996
y = 8
result = x % y
print("{}를 {}나누면 {}가 나머지 입니다.".format(x,y,result))

print("%d를 %d 나누면 %d가 나머지 입니다." %(x,y,result))

result1= x//y
result2 = x%y
print("%d를 %d 나누면 %d는 몫이고 %d 나머지입니다." %(x, y, result1, result2))

# divmod
result1, result2 = divmod(x,y)
print("%d를 %d 나누면 %d는 몫이고 %d 나머지입니다." %(x, y, result1, result2))

# %f는 실수를 나타내주는 포맷팅 코드 
print("원주율은 %d 입니다." %3.14159)
print("원주율은 {}입니다.".format(3.14159))
print("원주율은 %f 입니다." %3.14159)

#인덱싱 & 슬라이싱
x = "행복한 하루를 보내자" 
len(x)
x[:]
x[0]
x[1]
x[-1] 
x[0:3] #x[시작요소번호:끝요소번호-1]
x[3:]
x[4:6]
x[4:-5]
x[::2]
x[1:7:2]
x[5::2]
x[::-1]


#
[문제_2] v_str 변수에 이 문자열을 입력하세요. 


v_str = "시간은 멈추지 않습니다. 하루를 유익하게 살아야합니다."

len(v_str)

1. "시간은 멈추지 않습니다." 만 출력해주세요

v_str[0:13]



2. "하루를 유익하게 살아야합니다." 만 출력해주세요

v_str[14:30]
v_str[14::]


3. "살아야합니다."  만 출력해주세요

v_str[-7::]



4. "시추니루하야"  이 글자만 출력해주세요.

v_str[0:30:5]



5. "시간은 멈추지 않습니다. 하루를 유익하게" 만 출력해주세요.

v_str[0:-7]


6. v_str 문자열을 뒤순으로 출력해 주세요.

v_str[::-1]



##
[문제3] R과 달리 인덱스를 바로 변환하지 못하므로 조각조각 내어 문제를 풀어야 한다. 

>>> x = '파리썬'
>>> x
'파리썬'

인덱스를 이용해서 리 -> 이로 변환하세요.
 
x = '파리썬'
x=x[0]+'이'+x[2]
x
      

#문자함수: 함수앞에 변수의 이름이 꼭 와야 한다. 
#replace함수
x = '파리썬'
x.replace('리','이') #함수 미리보기로는 파이썬으로 수정가능 했으나 다시 x를 출력하면 파리썬으로 나오니 변수를 다시 지정해줘야 한다. 
x
x = x.replace('리','이')
x

#startswith: 원본 문자열이 매개변수로 입력한 문자열로 시작되는지를 판단
x = 'hello world'

x.startswith('h')
x.startswith('H')

#endswith: 원본 문자열이 매개변수로 입력한 문자열로 끝나는지를 판단
x.endswith('d')
x.endswith('D')
x.endswith('ld')

#find: 원본 문자열안에 매개변수로 입력한 문자열이 존재하는 위치를 앞에서부터 찾는다. 만약 존재하지 않으면 -1로 나온다.(0이 인덱스를 가지기 때문에)
x.find('w')
x.find('world')
x.find('W')

#count: 원본 문자열 안에 매개변수로 입력한 문자열이 몇번 나오는지에 대한 건수 
x.count('l')

#upper: 원본 문자열을 대문자로 변환 
x.upper()

#lower: 원본 문자열을 소문자로 변환
x.lower()

#capitalize: 원본 문자열을 첫글자를 대문자 변환
x.capitalize()

#title: 단어마다 첫글자를 대문자로 변환
x.title()

# swapcase: 문자끼리 스위칭을 하고 싶을 때
s = "HELLO, world"

s.swapcase()

#center: 원본 문자열을 지정한 공간에서 중앙에 배치 
s.center(20)

#ljust: 원본문자열을 지정한 공간에서 왼쪽에서 배치
s.ljust(20)

#rjust: 원본문자열을 지정한 공간에서 오른쪽에 배치
s.rjust(20)


# 공백제거 함수 
x = '                        hello      '
#strip: 원본문자열 양쪽에 공백을 제거
x.strip()

#lstrip: 원본문자열 왼쪽에 공백을 제거 
x.lstrip()

#rstrip: 원본문자열 왼쪽에 공백을 제거 
x.rstrip()

# strip응용하여 문자제거
x = 'helloh'
#strip: 원본문자열 양쪽에 문자를 제거
x.strip('h')

#lstrip: 원본문자열 왼쪽에 문자를 제거 
x.lstrip('h')

#rstrip: 원본문자열 왼쪽에 문자을 제거 
x.rstrip('h')

#is.alpha: 원본 문자열이 숫자, 기호를 제외한 알파벳, 한글로 이루어졌는지 확인
x = 'hello'
y = 'hello2018'
z = '안녕하세요'

x.isalpha()
y.isalpha()
z.isalpha()

#isalnum(): 원본 문자열이 알파벳, 숫자로 이루어져 있는지 확인 (And 조건이 아닌 OR조건에 해당 )
x.isalnum()
y.isalnum()
z.isalnum()

#isnumeric: 원본 문자열이 수로만 이루어져 있는지 확인 
x.isnumeric()
y.isnumeric()
z.isnumeric()

d = '2018'
d.isnumeric()

#replace: 원본문자열에서 어떤 문자열을 찾아서 새로운 문자열로 변경
x.replace('hello', 'python')


#find: 있으면 인덱스 번호를 return해주고, 없으면 -1의 값으로 return한다. 
x.find('o')
x.find('O')
#index: 있으면 인덱스 번호를 return해주고, 없으면 오류를 냄 
#index: 원본 문자열안에 매개변수로 입력한 문자열이 존재하는 위치를 앞에서부터 찾는다. 없으면 오류
x.index('o')
x.index('O')
#rfind: 원본문자열안에 매개변수로 입력한 문자열이 존재하는 위치를 뒤에서 부터 찾는다 (lfind는 없다.); 뒤에서부터 스캔하느냐 앞에서 부터 스캔하느냐가 다름 
x.rfind('o')

# in 연산자를 이용해서 문자열의 존재여부를 확인
'o' in x

#split: comma를 기준으로 x를 split 하고 싶을 때 사용 
x = 'hello, world'
x.split(',')

#' ' .join: 매개변수에 ' '가 사이에 기입됨 
# join: 원본 글자 사이에 특정한 문자열을 추가한다. 
x = 'abc'
x = ','.join(x)


###############################################################
a = 'a b c d e f g' 변수에 문자열이 들어 있습니다. 다음을 수행하세요.

a = 'a b c d e f g'
[문제4] a 변수에 있는 문자의 갯수를  구하세요.
len(a)

[문제5] a 변수에 공백문자 갯수를 구하세요.
a.count(' ')


[문제6] a 변수 안에 있는 공백문자를 제외한 갯수를 구하세요.
len(a)-a.count(' ')


[문제7] a 변수에 있는 공백문자를 제거한 후 b 변수에 넣어주세요
b = a.replace(' ','')
b


[문제8] a 변수에 있는 문자를 분리한 후 c 변수에 넣어주세요.
c = a.split(' ')

[문제9] c 변수에 있는 문자를 합쳐서 자신의 변수에 다시 넣어주세요.
c = ','.join(c)
c

###############################################################
아래와 같은 문자데이터가 있습니다. 
url = 'http://www.python.org'


[문제10] http:// 제거한 후 url 변수에 넣어 주세요.
url = url.replace('http://','')
url
url = url.lstrip('htttp://')

url

[문제11] url변수에 있는 문자 데이터에 '.'을 기준으로 분리하세요.
url = url.split('.')
url

[문제12] url변수에 있는 문자데이터를 www.python.org 모양으로 만드세요.
url='.'.join(url)
url

[문제13] url변수에 있는 문자데이터를 대문자로 변환하세요.
url.upper()

[문제14] url변수에 있는 문자데이터를 소문자로 변환하세요.
url.lower()



#input: 
x=input()

1234

y=input()

1234

x+y
Out[309]: '12341234'

type(x)

int(x)+int(y)



################################################################3
■ R의 자료형
1. Vector: 같은 데이터 타입을 갖는 1차원배열구조
2. Matrix: 같은 데이터 타입을 갖는 2차원배열구조
3. Array: 같은 데이터 타입을 갖는 다차원배열구조
4. List: 서로 다른 데이터 타입을 갖는 벡터들을 저장하거나 또다른 list를 저장하는 구조
5. Data.frame: 서로 다른 데이터 타입을 갖는 컬럼으로 이루어져 2차원 배열구조 (table)

■ Python의 자료형
1. List
- 서로 다른 데이터 타입을 갖는 1차원 배열 (vector구조, 그러나 서로 다른 데이터 타입을 가짐)
- 데이터의 목록을 다루는 자료형
- [ ]

x= [10,20,30]
x
len(x)
type(x)


#리스트 인덱싱
x[0]
x[-1]

#리스트 슬라이싱 [시작:끝-1]
x[0:2] #0번요소, 1번요소 보기
x[1:]  #1번요소 부터 다 보기
x[:-1]
x[-1:]

#리스트 값 수정
x[0] = 100
x[1:3] = [200, 300]
x

# append: 리스트변수 끝에 값을 추가
x.append(400)
x

# extend: 리스트변수와 리스트변수를 이어붙이기
# extend: 기존 리스트 변수에 다른 리스트 변수를 이어 붙이는 방법
x1 = [600,700]
x1

x.extend(x1)
x

#insert: 인덱스를 사용하여 특정 위치에 값을 추가
x.insert(4, 500)
x

# +를 이용해서 리스트변수 결합하는 방법 
x2 = [800, 900, 1000]
x = x + x2
x

x = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
#리스트변수에 있는 값 중에 마지막값을 제거하는 방법(인덱스 번호를 쓰지 않으면 제일 뒤에 있는 것이 제거 된다.)
x.pop()
x
x.pop(4)
x

#리스트 인덱스 값을 삭제하는 방법
del x[3]
x


#len, find, index 비교하기
drink=['콜라', '사이다', '환타', '콜라', '사이다', '콜라']
len(drink)
drink.count('콜라')
drink.find('콜라')  #오류
drink.index('콜라') #첫번째 ‘콜라’만 찾아줌
drink.index('콜라',1)  #1번방부터 ‘콜라’를 찾아줌
drink.index('콜라',4)  #4번방부터 ‘콜라’를 찾아줌

#리스트 변수에 값을 기준으로 삭제
drink.remove('콜라')
drink


# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 09:54:25 2018

@author: stu
"""

##문제
[문제17] day 변수에 20180905를 입력하세요. 화면 출력은 2018년 09월 05일 출력하세요.

day = "20180905"
print(day[0:4]+'년\0'+day[4:6]+'월\0'+day[6:]+'일')


day = "20180905"
print(day[0:4]+'년 '+day[4:6]+'월 '+day[6:]+'일')


####자료형########중첩리트스
x =[]
type(x)
x = [1,2,3,['a','b','c'], 4, 5]
x[2:5]
x[3]
x[3][0]
x[3][0:2]
x[3][-1]
x[3][2]
x[3].append('d')
x[3]
del x[3][3]
x[3]
x[3][0]=x[3][0].upper()
x[3][1]=x[3][1].upper()
x[3][2]=x[3][2].upper()

x[0]=x[0]*10    #[0]번 인덱스에는 숫자이기 때문에 곱이되고
x
x[3][0]=x[3][0]*2  #[3][0]의 인덱스는 문자이기 때문에 복제가 된다. 
x

# 리스트변수에 값을 다 지운다.
x.clear()
x

#리스트 내의 값을 기준으로 정렬 기본값은 오르참순 
x=[1,5,3,4,2]
x.sort()
x.sort(reverse=True)  #python에서 True도 대소문자 구문을 한다. 
x

#reverse: 리스트 인덱스 순서를 반대로 뒤집을 때 사용 
x=[1,5,3,4,2]
x.reverse()

#sorted: 정렬해서 미리보기
x = sorted(x)
x
x = sorted(x, reverse=True)
x

##문제 18~25
food 변수 아래와 같이 데이터가 들어 있습니다.food변수를 생성하시고 문제를 풀어보세요.

>>> food[0]
['김밥', '라면', '오뎅']
>>> food[1]
['비빔밥', '김치찌게']
>>> food[2]
['자장면', '짬뽕']

[문제18]  1번 index에 청국장 추가 하세요
food = [['김밥', '라면', '오뎅'],['비빔밥', '김치찌게'],['자장면', '짬뽕']]
food[0].append('청국장')
food[0]

[문제19] 2번 index에 탕수육 추가하세요.
food[2].append('탕수육')
food[2]

[문제20] 0번 index에 있는 오뎅 삭제하세요.
del food[0][2]
food[0]
 
#쌤답: food[0].remove('오뎅')

[문제21] 0번 index에 튀김, 튀김, 떡복이 한꺼번에 추가하세요
food1=['튀김','튀김','떡볶이']
food[0]+food1



[문제22] 2번 index에 2번 위치에 유산슬 추가하세요
food[2].insert(2,'유산슬')
food[2]
#쌤답: food[2].insert(2, '유산슬')

[문제23] 튀김 갯수를 세어주세요
food.count('튀김')
food


[문제24] 0번 index만 정렬해주세요# 인덱스 번호를 표현하지 않을 경우, 전체 중에 요소별로 0번 값을 기준으로 정렬한 값으로 표현하게 된다. 
food[0].sort
food[0]

[문제25] 0번 index에 마지막 데이터 삭제하세요
del food[0][-1]
food[0]

#쌤답: food[0].pop()

#중첩 리스트에서 len에 변수값을 바로 넣을 경우 전체값이 아니라 인덱스 갯수를 추출한다. 
len(food)

len(food[0])

len(food[2])


######자료형 #########tuple
리스트자료형과 똑같다. 차이점은 수정, 삭제, 추가 안된다.  cf. 상수처럼 사용되기 때문에 빠르게 처리된다. 
리스트[], 튜플()

list1=[]
type(list1)
tuple1=()
type(tuple1)
tuple2 = 10
type(tuple2)
tuple3 = (1,)
type(tuple3)
tuple4=(1,2,3,4)
type(tuple4)
tuple5=(1,2,3,('a','b'))
tuple5[3][0]
#튜플 변수 값을 수정하려면 오류
tuple5[0]=10

#튜플 변수 값을 삭제하려면 오류
del tuple5[0]

#튜플 변수 값을 추가 하려면 오류
tuple5.append(4)

# tuple을 연산하면 tuple로 결과가 나온다. 따라서 tuple에 변수를 추가하고 싶으면 tuple 자료형을 만들어 추가하면 된다.  
# 이때 사실은 tuple은 추가의 개념이 아니라 새로운 것이 만들어지는 것이다. 

x = (1,2,3)
id(x)
y = (4,5,6)
z = x + y
z
type(z)

# tuple은 append 대신 다음과 같이 추가할 수 있다. (새로운 x를 만들 수 있다.)
x = x +(4,)
x
id(x)
type(x) 

x.index(3)
x.count(1)

# sorted: sort를 하면서 type이 list로 바뀌게 된다. 
x =(2,3,4,1)
x.sort
type(x)
z =sorted(x)
type(z)
z


######자료형 ##■ dictionary
■ dictionary
- key를 가지고 value을 확인하는 자료형 
- {} 중괄호 사용 
- 예시)
key         value
이름        홍길동
전화번호    0101234568
주소        경기도

dic = {'이름':'홍길동', '전화번호':'01012345678','주소':'경기도'}
dic

type(dic)

dic['이름']

sports={'축구':'메시', '농구':'커리','야구':'박찬호'}

sports['축구']
#새로운 key -value값 넣기
sports['컬링']='김영미'
sports['컬링']=['김은정','김경애','김영미','김선영','김초희']
sports

#key값만 보기
sports.keys()
#value값만 보기
sports.values()
#key, value전체 다보기
sports.items()

sports['농구']
sports.get('농구')

#없는 key-value를 none으로 추출하기
sports['봅슬레이']
sports.get('봅슬레이')

# 키 값에 있는지 없는 지 확인 
'컬링' in sports.keys()
'봅슬레이' in sports.keys()

# value 값에 있는지 없는지 확인
'메시' in sports.values()
'호날두' in sports.values()
['김은정', '김경애', '김영미', '김선영', '김초희'] in sports.values()

del sports['야구']
sports

sports['축구']=[]
sports

sports.clear()
sports

sports={'축구':'메시', '농구':'커리','야구':'박찬호'}

x= sports.values()
x
type(x)

x=list(x)
type(x)


######### 자료형 ■ set(집합)
■ set(집합)
List type하고 비슷하다. 차이점은 index가 없다.

x = {1,1,1,2,3,2,3}
x
type(x)

y={2,3,4,5}
 
#합집합
x.union(y)
x|y

#교집합
x.intersection(y)
x&y

#차집합
x.difference(y)
x-y

y.difference(x)
y-x

# x에 있는 원소
1 in x
6 in x

# 인덱스가 없어서 오류
x[0]

#x에 있는 값 제거하기
#집합 변수에 값을 삭제
x.remove(1)
# 집합변수에 값을 입력
x.add(1) 
# 집합변수에 여러개의 값을 추가할 때
x.update([5,6,7])
x

####
a = []
b = ()
c = {}
s = set()
type(a)
type(b)
type(c)
type(s)



###자료형 ■ bool
■ bool
-참(True), 거짓(False)를 나타내는 자료형
-python에서는 대소문자 잘 구분지어서 나타내줘야한다. 
 
x = True
type(x)
y = False
type(y)

x == y
1 == 1
2 > 1
1 != 2

not 1
not -1
not 0
not None

#True 표현방법
bool(1)
bool(-1)
bool('python')
bool([1,2,3])
bool((1,2,3))
bool({1,2})

#False 표현방법
bool(0)
bool([])
bool(())
bool({})
bool(None)
bool('')


####### 조건문
■ if문 
if 조건문:
    수행해야할 문
    
if 1:
    print('참')
    print('오늘 하루도 행복하자')
    
if 0:
    print('참')
    print('오늘 하루도 행복하자')
else:
    print('거짓')
    print('그냥 사는거지 뭐...')

x = []
if x:
    print('참')
    print('오늘 하루도 행복하자')
else:
    print('거짓')
    print('그냥 사는거지 뭐...')

    
# x의 값이 참이면 참을 수행하고, 아니면 거짓을 수행함     
x = 1
if x==1:
    print('참')
    print('오늘 하루도 행복하자')
else:
    print('거짓')
    print('그냥 사는거지 뭐...')
    
#
x = 0
if x > 10 and 1/x :
    print('x는 10보다 크다')
else:
    print('x는 10보다 작다')
    
# x = 0
if 1/x and x>10 :
    print('x는 10보다 크다')
else:
    print('x는 10보다 작다')
 
if x > 10 & 1/x :    
    print('x는 10보다 크다')
else:
    print('x는 10보다 작다')
 
x= 0
if x < 10 or 1/x :    
    print('x는 10보다 크다')
else:
    print('x는 10보다 작다')

x= 0
if 1/x or x < 10:    
    print('x는 10보다 크다')
else:
    print('x는 10보다 작다')
    
    
x= 0
if x < 10 | 1/x :    
    print('x는 10보다 크다')
else:
    print('x는 10보다 작다')


#python에서는 elseif는 elif이다. 
score = 88

if 90 <= score <= 100:
    print('A')
elif 80 <= score <= 90:
    print('B')
elif 70 <= score <= 80:
    print('C')
elif 60 <= score <= 70:
    print('D')    
else:
    print('F')
    
    
# 문제
[문제26] 숫자를 입력값으로 받아서 짝수인지 홀수인지를 출력하는 프로그램을 만드세요.
x = input()

415
type(x)

if int(x)%2 ==1 :
    print('홀수')
else:
    print('짝수')
    
#쌤답
a = int(input('숫자를 입력하세요: ' ))
if a%2 == 0 :
    print('짝수')
else: 
    print('홀수')

[문제27]한글, alphabet만 입력받아야 합니다. 
        만약에 다른 문자가 들어 오면 "한글, alphabet 이외의 문자가 포함되어 있습니다." 라는 문구가 출력해야 하고 아니면 입력받은 문자를 출력하세요.

if x.isalpha():
    print(x)
else:
    print("한글, alphabet 이외의 문자가 포함되어 있습니다.")    


# 쌤답 - 공백문자가 있으면 false로 받는다.
a = input('문자를 입력하세요:')
if a.isalpha():
    print(a)
else: 
    print("한글, alphabet 이외의 문자가 포함되어 있습니다.")
    
[문제28] 숫자를 입력값으로 받습니다. 
   만약 숫자가 이외의 값이 들어 오면 "숫자 이외의 문자가 포함되어 있습니다." 아니면 숫자 출력하세요.

if x.isnumeric():
    print(x)
else:
    print("숫자 이외의 문자가 포함되어 있습니다.")    

#쌤답 
if a.isnumeric():
    print(a)
else: 
    print("숫자 이외의 문자가 포함되어 있습니다.")
    
    
#######################3
리스트 형일 때: False
x = [1,2]
y = [2,1]

if x == y:
    print('참')
else:
    print('거짓')

set형일 때: True    
x = {1,2}
y = {2,1}

if x == y:
    print('참')
else:
    print('거짓')


#################################
▣ 반복문
■ while문
조건이 참인동안에 while문을 반복해서 수행한다.

while 조건문:
    반복수행해야할 문장

# 문제
[문제29] 1부터 100까지 합을 구하세요. #반복 횟수가 중요하다. -> count 알고리즘 필요 # 그 안에서 1씩 증가하는 로직을 구현해야 한다. count 변수의 값을 어디엔가 누적 개념으로 놓아두고 반영해야 한다. 

i = 0   #count변수
result = 0  #누적합을 더하는 변수
while i <= 100:
    result +=i     # result = result + i 
    i +=1          # i= i +1
print(result)
    
i = 0   #count변수
result = 0  #누적합을 더하는 변수
while i <= 100:
    result +=i     # result = result + i 
    i +=1          # i= i +1
print(result)      # print를 들여쓰기 하면 각각의 result값을 출력한다.  
    
    
[문제30]단을 입력값으로 받아서 구구단을 출력하세요. 

dan = int(input('단을 입력해주세요: '))

i = 1
while i < 10:
    print('{}*{}={}'.format(dan,i,dan*i))
    i += 1
    

i = 1
while i < 10:
    print('%s*%s=%s'%(dan,i,dan*i))
    i += 1



# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 09:46:43 2018

@author: stu
"""
# loop 문에서 (while, if) 
break와 continue를 사용한다. 


#break: 무한loop에 빠져버리는 상황을 피하기 위해 사용
# break: 종료하는 보조제어문
i = 0
while 1:
    if i > 10:
        break
    else:    
        i += 1
        print('반복하는 값:%d'%i)

#cf. 무한 loop에 빠짐
i = 0
while 1:
    i += 1
    print('반복하는 값:%d'%i)
    
# 10, 9, 8, 7, .. 반복을 피하기 위해 break를 걸음 
i = 10
while 1: 
    print('반복하는 값: %d' %i)
    i -= 1
    if i == 0: 
        break       

#cf. 무한 loop에 빠짐
i = 10 
while 1:
    print('반복하는 값: %d'%i)
    i -= 1
    
# not i 를 사용하여 true를 만들어 break 걸기 
i = 10
while 1: 
    print('반복하는 값: %d' %i)
    i -= 1
    if not i: 
        break

# continue문은 while문으로 돌아가게 하는 문 
i = 0 
while i < 10:
    i += 1
    if i%2 == 0:  #짝수는 수행하지 않고 계속 while문을 수행하겠음
        continue
    print(i)


################
[문제30] 1부터 100까지의 3의 배수를 출력, 합을 구하세요. while문을 이용하세요.

#답1: 리소스를 많이 잡아 먹음 
i = 0
result = 0
while i < 100:
    i += 1 
    if i%3 == 0:
        print(i)
        result += i
        
print(result)

#답2: break가 없으면 102까지 출력될 수 있다. 
i = 0
result = 0
while i < 100:
    i += 3
    if i > 100:
        break
    else:
        print(i)
        result += i
        
print(result)


[문제31] 조건이 없는 상태에서 1부터 10까지 3,5를 제외한 합을 구하세요.
continue문, break문을 이용하세요.

# 조건이 없는 상태에서 : while 문에서  true를 생각하기 

i = 0
sum = 0

while True:
    i += 1
    if i == 3 or i == 5:
        continue
    if i > 10:
        break
    sum += i 

print(sum)    


[문제32] 리스트 변수에 18,2,3,1,4,5,7,8,9,10,11,15,16 값이 들어 있습니다. 짝수만 합을 구하세요.

i=0
x = [18,2,3,1,4,5,7,8,9,10,11,15,16]
result = 0

while i < len(x):
    if x[i]%2 == 0: 
        result += x[i]
    i += 1
    
print(result)

# 쌤답 
x = [18,2,3,1,4,5,7,8,9,10,11,15,16]
i=0
sum = 0 
while i < len(x):
    if x[i]%2 == 0:
        sum += x[i]
    i += 1

print(sum)


## 구구단을 만들면 subloop 구조로 풀어야 하기 때문에 while문 안에 while 문을 넣어야 함 
[문제33] 구구단을 생성하세요
   
i = 1
j = 1

while i <9:
    i += 1
    print ('---''{}''단---'.format(i))
    while j <= 9:
        print('%s * %s = %s'%(i,j,i*j))
        j += 1
    if j == 10:
       j = 1 
         

#하빈이 씬박한 답 ㅋ center와 /n
i=1
j=1

while i<9:
    i+=1
    x='*%d단*'%i
    print('\n %s'%x.center(6))
    
    while j<=9:
        print('{} * {} = {} '.format(i,j,i*j))
        j+=1
        if j==10:
            j=1
            break


# if 문으로 j를 리셋해줄 필요 없이 메인 while문에서 다시 선언해 주면 된다.
while i<9:
    i+=1
    j=1
    x='*%s단*'%i
    y=x.center(8)
    print('\n %s'%y)
    
    while j<=9:
        print('{} * {} = {} '.format(i,j,i*j))
        j+=1

        
#쌤답 
v_num = 2
while v_num <= 9:
    count = 1
    p_num = 0
    print ('-- %d단 --' %v_num)
    while count <= 9:
        p_num = v_num * count 
        print(v_num, '*', count, '=', p_num)
        count = count + 1 
    v_num = v_num + 1 


while v_nume <=9:
    count = 1
    p_num = 0
    print ('-- %d단 --' %v_num)
    while count <= 9:
        p_num = v_num* count
        print (v_num, '*', count, '=', p_num)
        count = count +1 
    v_num = v_num + 1 
                

####### 오후 시간 #########
[문제34] 리스트 변수에 12,3,21,4,5,7,33,2,18,9,10,31,15,16 값이 들어 있습니다. 최대값을 구하세요.
x = [12,3,21,4,5,7,33,2,18,9,10,31,15,16]
i = 0
j = 0

while not i:
    j+1
    if x[i]-x[j] > 0:
        print(x[i])
    else:
       x[i]-x[j] < 0: 
        i+=1
        print(x[i])
    

큰수-작은수 양수
else 작은수-큰수 음수 

#쌤답1 - 오류 
x = [12,3,21,4,5,7,33,2,18,9,10,31,15,16]
i = 1 
max = x[0]

while i < len(x):
    if max > x[i]:
        max = x[i]
        i +=1

print(max)
  
# 쌤답 2 - 잉? 답이 이상함 
x = [12,3,21,4,5,7,33,2,18,9,10,31,15,16]
i = 0
max = x[0]
cn =len(x)
while i < cn:
    i += 1
    if i == cn:
        break
    else:
        if max < x[i]:
            max = x[i]
        i += 1

print(max)


# 쌤답 3
x = [12,3,21,4,5,7,33,2,18,9,10,31,15,16]
i = 0
max = x[0]
cn =len(x)
while i < cn:
    if max < x[i]:
        max = x[i]
    i += 1 

print(max)


[문제35] 리스트 변수에 12,3,21,4,5,7,33,2,18,9,10,31,15,16 값이 들어 있습니다. 최소값을 구하세요.
x = [12,3,21,4,5,7,33,2,18,9,10,31,15,16]
i = 1 
min = x[0]
while i < len(x):
    if min > x[i]:
        min = x[i]
        
    i += 1

print(min)    

#########################
■ for 문
for 반복변수 in (리스트, 튜플, 문자열):
    반복수행해야할 문장 

for i in [1,2,3,4,5]:
    print(i)

x = [1,2,3,4,5]
for i in x:
    print(i)


x = (1,2,3,4,5)
for i in x:
    print(i)
    
for i in ['a','b','c']:
    print(i)
    
x = ['sql', 'plsql', 'r', 'python']
for i in x:
    print(i)
    
for i in '대한민국':
    print(i)

x = [(1,2), (3,4), (5,6)]    
for (a, b) in x:
    print(a+b)


#############################################333
[문제36] 학생들의 점수가 90,55,63,78,80 점이 있습니다.
60점 이상이면 합격, 60점 미만이면 불합격 출력해 주세요.

x = [90,55,63,78,80]
for i in x:
    if i >= 60:
        print ('합격')
    else:
        i < 60
        print('불합격')

######################################################
■ range 
range(시작점, 끝점-1, 간격)
list(range(1,11,1))
list(range(0,101,1))
list(range(0,101,5))
range 시작점을 쓰지 않으면 0부터 시작한다. 



for i in range(1,11):
    print(i)

for i in range(1,11,2):
    print(i)

[문제37] 1부터 100까지 합을 구하세요.(for 이용)

result =0
for i in range(1,101):
   result += i
print(result) 



[문제38] 1부터 10까지 출력하세요. 단 4, 8은 제외(for 이용)??

for i in range(1,11):   
    if i != 4 and i != 8:
        print(i)

#쌤답
for i in range(1,11):
    if i == 4 or i == 8:
        continue
    print(i)


[문제39] 화면과 같이 출력하세요.(for 이용)

가로의 숫자를 입력하세요 : 5
세로의 숫자를 입력하세요 : 5
★ ★ ★ ★ ★ 
★ ★ ★ ★ ★ 
★ ★ ★ ★ ★ 
★ ★ ★ ★ ★ 
★ ★ ★ ★ ★ 

for i in range(1,6):
    print('★'*5)

#쌤답    
a = int(input('가로의 숫자를 입력하세요: '))
b = int(input('세로의 숫자를 입력하세요: '))
for i in range(b):
    print('★'*a)

   
[문제40] 구구단을 출력하세요.(for 이용)

for i in range(2,10):
    print('\n---',i,'단---')
    for j in range(1,10):
        print('%s * %s = %s'%(i,j,i*j))

#쌤답
for i in range(2,10):
    print("---{}단---".format(i))
    for j in range (1,10):
        print("{} * {} = {}".format(i, j, i*j))

    
        
[문제41] 구구단을 만드세요. 

2단에서 9단까지만 입력하세요, [0은 구구단 전부를 출력합니다.]: 

    # 내 답 다시 확인해보기 
x = input()
range(2,10)

for i in range(2,10):
    if int(x)==0:
        print('\n---',i,'단---')
        for j in range(1,10):
            print('%s * %s = %s'%(i,j,i*j))
    else: 
        print('%s * %s = %s'%(x,i,int(x)*i))


if int(x)==0:
    for i in range(2,10):
        print('\n---',i,'단---')
        for j in range(2,10):
            print('%s * %s = %s'%(i,j,i*j))
elif 2 <= int(x) <= 9:
    print('\n---',x,'단---')
    for j in range(2,10):
        print('%s * %s = %s' %(x,j,int(x),j))


# 쌤답
m = int(input('2단에서 9단까지만 입력하세요. [0은 구구단 전부를 출력합니다.]: '))

if m == 0:
    for i in range(1,10):
        print("---{}단---".format(i))
        for a in range (1,10):
            print(i, "x", a, "=", i*a)
elif 2 <= m <= 9:
    print("---{}단---".format(m))            
    for i in range(1, 10):
        print(m, "x", i, "=", m*i)
        
   
     
[문제42]lst 변수에 a,b,c,d값이 있습니다. for문을 이용하여 아래화면과 같이 출력하세요.


0번 a값이 있습니다.
1번 b값이 있습니다.
2번 c값이 있습니다.
3번 d값이 있습니다.


lst = ['a','b', 'c', 'd']
for i in range(len(lst)):
    print('{}번 {}값이 있습니다.'.format(i,lst[i]))

#별도의 method 
for i, name in enumerate(lst):
    print('{}번 {}값이 있습니다.'.format(i, name))

■ enumerate: list변수 안에 인덱스와 인덱스 값을 바로 리턴해 주는 method 
(range처럼 나오기 때문에 객체형식으로 나온다. 인자값 두개(인덱스, 인덱스값)을 리턴해준다.)


#################
[문제43] 1부터 9까지 x 리스트 변수에 입력하세요.
y변수는 x 변수의 값을 2곱한 값으로 입력해주세요.

x = list(range(1,10,1))
# x= range(1,10) 만 써도 됨
y = []
for i in x:
   y.append(2*i)
y    

    
[문제44] apple, banana, orange 리스트 변수에 값을 입력하시고
         이 값들의 길이를 출력해주세요.

x = ['apple', 'banana', 'orange']
result=0

# 문제를 잘못 이해했네요... 전체 문자숫자를 구하는 줄~
for i in range(len(x)):
    result += len(x[i])
print(result)


for i in range(len(x)):
    print(len(x[i]))



#쌤답
for i in x:
    print (len(i))

[문제45] 변수에 아래와 같이 들어 있습니다. 아래처럼 결과를 출력하세요.

lst1 = [1,2,3]
lst2 = [4,5,6]

출력결과

[4, 5, 6, 8, 10, 12, 12, 15, 18]


lst3=[]

for i in lst1:
    for j in lst2:
        lst3.append(i*j)
     
lst3

#쌤답
for x in lst1:
    for y in lst2:
        print(x*y, end=',')

#end: option으로 사용 가능

lst3=[]

for x in lst1:
    for y in lst2:
        lst3.append(x*y)
     
lst3



###########################################################
#다르게 풀기
[문제43] 1부터 9까지 x 리스트 변수에 입력하세요.
y변수는 x 변수의 값을 2곱한 값으로 입력해주세요.

x = list(range(1,10,1))
# x= range(1,10) 만 써도 됨
y = []
for i in x:
   y.append(2*i)
y    
###################################

■ 리스트 내장객체 
(문제 43번과 관련하여 기존에 리스트 변수를 정의하고, append하지 않고 바로 값을 얻어내는 방법)
[ 표현식  for 반복변수 in 반복가능한 객체]
z = [ i*2 for i in x]
z

# 리스트 내장객체를 통해 문제 44번, 45번풀기 
[문제44] apple, banana, orange 리스트 변수에 값을 입력하시고
         이 값들의 길이를 출력해주세요.

x = ['apple', 'banana', 'orange']

[len(i) for i in x]


[문제45] 변수에 아래와 같이 들어 있습니다. 아래처럼 결과를 출력하세요.

lst1 = [1,2,3]
lst2 = [4,5,6]

출력결과

[4, 5, 6, 8, 10, 12, 12, 15, 18]

lst3 = [i*j for i in lst1 for j in lst2] #for i in lst1 : main for문 / for j in lst2: subfor 문 

################################################ 
[문제 46] 1부터 100까지 값중에 짝수만 x변수에 입력해주세요. 
#1번방법
x = []
for i in range(1,101):
    if i%2 == 0:
        x.append(i)

#2번방법: 리스트 내장객체 안에 if문도 내장할 수 있다. 
z=[i for i in range(1,101) if i%2==0]
z


# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 09:46:23 2018

@author: stu
"""

###################################################################################
[문제47] 튜플변수에 사과, 귤, 오렌지, 배, 포도, 바나나, 자몽, 키위, 딸기, 블루베리, 망고를 입력하시고 
과일이름중에 세글자 이상인 과일만  fruit_lst변수에 입력해주세요.

fruit_lst=()

fruit = ('사과', '귤', '오렌지', '배', '포도', '바나나', '자몽', '키위', '딸기', '블루베리', '망고')

#답1: tuple로 했을 때 
for i in fruit:
    if len(i) >= 3:
        fruit_lst = fruit_lst+(i,)
#답2:
fruit_lst= [i for i in fruit if len(i) >= 3]


#쌤답1
fruit = ('사과', '귤', '오렌지', '배', '포도', '바나나', '자몽', '키위', '딸기', '블루베리', '망고')
fruit_lst = []
for i in fruit:
    if len(i) >= 3:
        fruit_lst.append(i)
print(fruit_lst)

#쌤답2
fruit_lst2 = [i for i in fruit if len(i) >=3]
print(fruit_lst2)


[문제48] 과일판매 현황을 dictionary 변수로 생성하세요. 과일 이름을 키로 하고 수량은 값으로 표현한후
과일이름만 대문자로 출력해주세요.

   
apple  100 , banana  300, orange  300

dictionary = {'apple':'100' , 'banana':'300', 'orange':'300'}
for i in dictionary.keys():
    print(i.upper())

# 쌤답1
dic = {'apple':'100' , 'banana':'300', 'orange':'300'}
for i in dic.keys():
    print(i.upper(), end=',')

# 쌤답2
for i,v in dic.items():
    print(i.upper()+':'+str(v), end=',\0') #format문자 코드를 쓰지 않고 변수에 있는 문자를 붙여서 출력할 경우, 문자와 숫자가 같이 출력 될수 없다. 따라서 현재 문자와 숫자 이기때문에 오류가 난다. 따라서 str(v)를 해서 string으로 변형해야 한다. 

# 쌤답 3
[i.upper() for i in dic.keys()]


# 쌤답 4
[[i.upper(), v] for i, v in dic.items()] # dictionary 모양처럼 해야 오류가 나지 않는다. [i.upeer(), v]


###### 
cf.dictionary형은 빈도수 체크할 때 많이 사용한다. R처럼 table을 만들 수 없기 때문에 dictionary를 이용하여 빈도수를 만들어야 한다. 

▣ 함수
- 기능의 프로그램
- 반복되는 코드를 하나로 묶어서 처리하는 방법 
cf. class: 함수를 모아 놓은 것, /plsql: package는 class와 비슷한 개념으로 함수를 모아 놓은 것을 의미함, 유지,관리,보수가 편리, 오버로드 기능을 지원 

def 함수이름(인수, 인수, 인수...):
    수행할 문장....(수행해야할 로직)
    
    [return 값]
    
        #plsql에서 retrun은 의무적이었지만, r과 python은 return값은 option이다.
        #python의 return문은 종료의 의미 
        #즉, return을 쓰게 되면 값이 없는 return문을 종료하는 의미이다. 
    

예시)
# 예시 1   
함수이름()
    
def message():
    print('오늘 하루도 행복하자')


message()

#예시2
def message(x): #x로 입력값을 만듦
    print('%s 화이팅'%(x))

message('홍창식')

#예시 3
def message():
    print("매일 행복하자")
    return "happy"

word = message()
print(word)


################################################################
[문제49] 함수에 두개의 숫자를 입력값으로 받아서 값을 비교하는 프로그램을 작성하세요.(출력하는 형식으로 만들기) 
#인수값 x, y를 넣었을 때 비교하는 프로그램 

#답1
def num_compare(x,y):
    if x - y == 0:
        print('x와 y는 같다')
    elif x - y > 0:
        print('x가 y보다 크다')
    elif x - y < 0:
        print('x가 y보다 작다')

num_compare(10,5)

#답2 
def num_compare(x,y):  
    if x>y:
        print('{}가 {}보다 크다'.format(x,y))
    elif x<y:
        print('{}가 {}보다 작다'.format(x,y))
    else:
        x==y
        print('{}와 {}는 같다'.format(x,y))


[문제50] 두 인수값을 받아서 합한 값을 리턴해주는 sum함수를 생성하세요.

def sum(x,y):
    return x+y

z = sum(1,2)
z
 
################################################################
■ 함수에서의 가변 인수값: * 
가변으로 변하는 인수값을 어떻게 처리할까? cf.plsql: 가변값을 받을 수 있는 record 변수를 넣어서 package에 넣어 수행함
sum(1,2,3,4,5)
sum(1,2,3) 

형식)
def 함수이름(*인수):
    수행할 문장 

예시) 인수(형식매개변수) x는 가변으로 사용할 수 있음 / x개가 여러개 들어갈 경우 for문을 생각해야 한다. for i in 반복해야할 list변수 
def sum(*x):
    total = 0   #누적되어야 할 값을 넣어야 할 변수가 필요하니 local변수를 선언한다. 
    for i in x:
        total += i
    return total

z=sum(1,2,3,4,5)
print(z)
sum(1,2,3)


################################################################
[문제51]
cal('sum', 1,2,3,4,5)
cal('multiply',1,2,3,4,5)

def cal(arg1, *arg2):    #크게 보면 두개의 인수, arg1에는 sum과 multiply만 들어오고(문자만 들어오고), arg2는 가변으로 받을 경우, arg2앞에 *을 넣어주면 된다.
    if arg1 == 'sum':
        total = 0
        for i in arg2:
            total += i
        return total
    elif arg1 == 'multiply':
        total = 1
        for i in arg2:
            total *= i 
        return total

#쌤답 
def cal(arg1, *arg2):    #크게 보면 두개의 인수, arg1에는 sum과 multiply만 들어오고(문자만 들어오고), arg2는 가변으로 받을 경우, arg2앞에 *을 넣어주면 된다.
    if arg1 == 'sum':
        total = 0
        for i in arg2:
            total += i
    elif arg1 == 'multiply':
        total = 1
        for i in arg2:
            total *= i 
    return total

#쌤답: 혹시 문자열을 대문자로 쓰거나 그럴 경우, lower로 바꿔주어 if에서 비교하는 것이 좋다. 문자값 비교시 주의합시다! 
def cal(arg1, *arg2):    #크게 보면 두개의 인수, arg1에는 sum과 multiply만 들어오고(문자만 들어오고), arg2는 가변으로 받을 경우, arg2앞에 *을 넣어주면 된다.
    if arg1.lower() == 'sum':
        total = 0
        for i in arg2:
            total += i
    elif arg1.lower() == 'multiply':
        total = 1
        for i in arg2:
            total *= i 
    return total

cal('SUM', 1,2,3)


##############################################################################################
[문제52] 여러 숫자를 인수값으로 받아서 합과 평균을 출력하는 aggF함수를 생성하세요.

aggF(1,2,3,4,5,6,7,8,9,10)
  
합 :  55
평균 : 5.5 

def aggF(*x):
    result = 0
    for i in x :
        result += i
    print('합 : ',result)
    print('평균 : ',result/len(x))

##############################################################################################
▣ return문: 


■ #리턴문은 여러 번 쓸 수 있되, 첫번째 return문만 수행하고 끝남
def f1(x,y):
    return x+y
    return x*y

z = f1(2,3)
print(z)

■ 여러 번의 return문을 쓰려면 ,(콤마)를 이용해서 return하고자 하는 값을 연결

def f1(x,y):
    return x+y, x*y

sum, mul = f1(2,3)
print(sum, mul)


# [문제52]을 return으로 풀기 
[문제52] 여러 숫자를 인수값으로 받아서 합과 평균을 출력하는 aggF함수를 생성하세요.

aggF(1,2,3,4,5,6,7,8,9,10)
  
합 :  55
평균 : 5.5 

def aggF(*arg):
    total = 0
    for i in arg:
        total = total+i
    avg = total/len(arg)
    print('sum=%dm avg=%0.2f'%(total, avg))   #format문자 소숫점 제어하기: %0.2f 소수 2번째 자리까지 표시하기 
    return total, avg

sum, avg = aggF(1,2,3,4,5,6,7,8,9,10)
print(sum, avg)


■ 값이 없는 return문은 종료 시킴
def f2(x,y):
    if y == 0:
        return
    print(x/y, " 값 입니다.")

f2(4,2)
f2(4,0) #값이 없는 return문은 종료임


■ 형식매개변수에 기본값 지정 가능    

def f3(name, age, gender='M'):      #gender라는 매개변수에 M이라는 기본값 지정 
    print("이름은 ", name)
    print("나이는 ", age)
    if gender == 'M':
        print("남자")
    else:
        print("여자")

# 원래 형식매개변수에 맞게 매개변수를 넣어야 하는데 넣지 않으면 오류가 발생하지만 기본값을 지정하여 오류를 피할 수 있다.
f3("홍길동", 30)                   #gender값을 입력하지 않으면 기본으로 M
f3("송하빈", 20, "F")

■ 전역변수(global): 프로그램이 종료될때까지 어디서든지 사용할 수 있는 변수(일반적으로 기존에 사용했던 변수들이 global변수에 해당한다.)
■ 지역변수(local): 함수 안에서만 사용하는 변수 

#x: global variable
x = 10

#x: local variable: 이 함수 안에서만 쓰이기 때문에
def f4(x):      # x는 매개변수: f4에서만 사용되는 매개변수 
    print("x 변수 값은", x)     #
    x = 20      #여기서 x는 local 변수
    print("x 변수 값은", x)

f4(x)                           #매개변수, 로컬변수 출력
print(x)                        #10출력(global variable)

#함수 밖에 있는 global 변수(x=10)를 함수안에서 global 키워드를 사용해서 global 변수 값을 x=20으로 변경하는 것 
x = 10
def f5(arg):
    global x                  #global 키워드를 이용해 함수 안에서 global 변수를 바꿔 사용함
    x = 20                    #여기서 x는 global 변수가 된다. 
    print('x 변수 값은', x)

f5(x)
print(x)

#############################################################################
[문제53] 입력값을 누적해서 더하는 함수를 작성하세요.

>>> print(add(2))
2

>>> print(add(8))
10

result = 0
def add(x):
    global result
    result += x
    return result
    
print(add(2))
print(add(8))

#쌤답 
total = 0
def add(arg):
    glbal total
    total += arg
    return total

print(add(2))
print(add(8))

dir()

del total

[문제54] 아래와 같이 변수에 값이 들어 있습니다. 
exchang함수에 x변수에 값을 넣으면 y로 변환하는 함수를 만드세요.

x = ["귀도","반","로섬"]
y = ["Guido","van", "Rossum"]

# 문제를 잘못 이해함.... ;;;
y = []
def exchange(x):
    for i in x: 
        if i == "귀도":
            y.append("Guido")
        elif i == "반":
            y.append("van")
        elif i == "로섬":
            y.append("Rossum")
        

exchange(x)
print(x)

#쌤답   - 문제 이해를 위한 설명 먼저 보고 비교하기와 답을 비교하기
x = ["귀도","반","로섬"]
y = ["Guido","van", "Rossum"]

def exchange(x):
    x = x[:]
    for i in range(len(x)):
        x[i] = y[i]
    print(x)

exchange(x)
print(x)
print(y)

# 비교하기
x = ["귀도","반","로섬"]
y = ["Guido","van", "Rossum"]

def exchange(x):
    x = x
    for i in range(len(x)):
        x[i] = y[i]
    print(x)

exchange(x)
print(x)    # x = x[:]를 안하기 때문에 x[i] = y[i]로 했을 때 y[i]로 반환된 값이 x[i]로 들어가기 때문에 print(x)에서 x가 아닌 y값으로 나오는 것임
print(y)

#54문제 이해를 위해 
◆ copy: 메모리가 같은 (주소값이 같은) 복제: b
a = [1,2,3]
b = a               #변수에 copy를 하면 메모리를 함께 사용하기 때문에 a.append(4)를 한 다음 print(a,b)를 하게 되면 b값도 a값에 4가 붙은 값까지 함께 출력된다. 

print(a,b)
print(id(a),id(b))  #메모리 주소 출력값; 메모리 주소 출력값이 같기 때문에 똑같이 사용하는 것임 
#print(id(a),id(b))
121778376 121778376

a.append(4)     
# print(a,b)
print(id(a),id(b))
[1, 2, 3, 4] [1, 2, 3, 4]
121778376 121778376

◆ deepcopy를 하는 방법(1): 물리적으로 다른 복제: c
c = a[:]            #복제를 하되 물리적으로 복제(따로 복제)하기 위해서는 c = a[:] 를 이용해야 한다. 즉, a에서 인덱싱 전체를 보겠다는 :(콜론)을 사용하여 복제해야 물리적으로 다르게 복제한다. 이래야 바깥쪽에 있는 변수에 영향을 주지 않는다.
print(a,b,c)
print(id(a),id(b),id(c))
#print(a,b,c)
print(id(a),id(b),id(c))
[1, 2, 3, 4] [1, 2, 3, 4] [1, 2, 3, 4]
121778376 121778376 121781000

a.append(5)
print(a,b,c)
print(id(a),id(b),id(c))
#print(a,b,c)
print(id(a),id(b),id(c))
[1, 2, 3, 4, 5] [1, 2, 3, 4, 5] [1, 2, 3, 4]
121778376 121778376 121781000

◆ deepcopy를 하는 방법(2): 물리적으로 다른 복제: d
import copy

d = copy.deepcopy(a)
print(id(a),id(d))
#print(id(a),id(d))
121778376 152096968

a.append(6)
print(a,d)
#print(a,d)
[1, 2, 3, 4, 5, 6] [1, 2, 3, 4, 5]

 
◆ 인덱스에 있는 값을 복제할 때 메모리 주소는 달라진다. 
a = [1,2,3]
b = a[0]    #변수를 0번 인덱스에 있는 값으로 b를 만들라고 했기 때문에 b가 a의 모든 값을 가져가지 않기 때문에 a와 b의 메모리 주소가 다르게 나온다. 
print(id(a),id(b))

#print(id(a),id(b))
152108552 1616276544

#############################################################################
[문제55]약수를 구하는 divisor 함수를 생성하세요.

1이상의 숫자를 입력하세요: 100
[100, 50, 25, 20, 10, 5, 4, 2, 1]

#내답
x = int(input("1이상의 숫자를 입력하세요: "))
def divisor(x):
    x2 = x
    x1 = [] 
    #x1.append(x) --- 나의 오류 
    while x > 0:
        if x2%x == 0:
            x1.append(x)
        x -= 1
    return(sorted(x1))

print(divisor(x))     


# 쌤답 
print("어떤 정수를 나누어 떨어지게 하는, 0이 아닌 정수이다. 음의 정수도 약수가 되지만 일반적으로 양의 약수만 다룬다")

#답1
num1 = int(input("1이상의 숫자를 입력하세요: ") )

def divisor(num1):
    for i in range(1,num1+1):
        if(num1%i == 0):
            print(i,end=" ")
            
divisor(num1)

#답2: 반으로 값을 나누어 약수 구하기
num1 = int(input("1이상의 숫자를 입력하세요: "))

def divisor(num1):
    num2 = int(num1/2)
    num3 = []
    num3.append(num1)
    while num2 >= 1:
        if num1 % num2 == 0:
            num3.append(num2)
        num2 -= 1
    return(sorted(num3))    
    #return(sorted(num3,reverse=False))
 
print(divisor(num1))


# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 09:45:21 2018

@author: stu
"""

[문제56] 여러 값을 동일한 변수에 순차적으로 저장할수 있는 용도의 변수 타입과 부호는 ?
list, []

[문제57] x 리스트 변수에 1, 3, 5, 7, 9 를 입력하세요
x = [1,3,5,7,9]  


[문제58] x 변수에 타입을 확인하세요.
type(x)


[문제59] x변수에 첫번째값을 확인해주세요
x[0]

[문제60] x변수에 제일뒤에 값을 확인해주세요
x[-1] 
x[len(x)-1]

[문제61] x변수에 10를 제일 뒤에 추가해주세요.
x.append(10)
x

[문제62] x변수에 있는 값들중에 10을 삭제해주세요
x.remove(10)
#x.pop()
x


[문제63] x변수에 1번색인위치에 2를 입력하세요.
x.insert(1,2)   #1번색인 위치에 2를 추가 입력 
#x[1]=2 변환임 
x

[문제64] x변수에 1번색인값을 제거해주세요.
x
x.pop(1)
#del x[1]
x


[문제65] x 변수에 첫번째 부터  세번째까지 값을 출력해주세요.
x[0:3]   
x[:3]

[문제66] x 변수에 제일뒤에서 두개 값을 출력해주세요.
x[-2:]
#x[len(x)-2:len(x)]


[문제67] x 변수를 y변수에 대입한 후 y변수에 11을 추가한 후 x값도 확인 한 후 분석해주세요.
x
y = x
y
y.append(11)
x

id(x), id(y) #메모리를 같이 참조하고 있음 / #메모리를 다르게 참조할 경우, :(콜론)을 사용하든지 deepcopy를 사용해야함 


[문제68] x변수를 z변수에 복사하지만 고유한 변수로 생성해주시고 z변수에 13을 추가 해주세요.
z = []
z = x[:]
#z[:] = x
id(z), id(x)
z.append(13)
z

[문제69] 
    x = [1,2,3]
    y = [4,5,6]
    y변수에 값을 x 변수에 넣어주세요.

id(x)
id(y)

x.extend(y)
x    #x변수의 메모리는 달라지지 않는다.
id(x)

#x=x+y     #x변수의 메모리가 달라
x
    
[문제70] x 변수에 1번 인덱스의 값을 제거해주세요.
del x[1]
x

[문제71] x변수에 1번 부터 3번 인덱스를 제거해주세요.
del x[1:4]  
x

[문제72] 중첩리스트를 이용할때 첫번째 항목의 첫번째 항목의 값을 추출해주세요.
x = [[1,2,3],[4,5,6]]
x[0][0]
 

[문제73] 리스트형과 비슷하지만 요소의 값을 변경 할 수 없는 타입과 부호는 ?
tuple, ()

    
[문제74] 키, 값을 저장하는 데이터 타입과 부호는 ?
dictionary {} {'':''}   

#{}은 set형과 같다. set은 중복된 값을 제거해준다.(set: intersection, union, difference)
     
[문제75]  아래와 같은 내용을 변수에 입력해주세요. 변수이름은 dict

           이름 : '홍길동'
           나이 : 30
           직업 : '파이썬개발자'
           
dict = {'이름': '홍길동', '나이':'30', '직업':'파이썬개발자'}
dict
    
[문제76] dict변수 키를 출력하세요.
dict.keys()    


[문제77] dict변수 값을 출력하세요.
dict.values()


[문제78] dict변수의 키, 값을 출력해주세요.
dict.items()
 

[문제79] dict변수의 이름만 출력해주세요.
dict.get('이름')


[문제80] dict변수의 주소 = '서울' 추가해주세요
dict['주소']='서울'
dict
    
[문제81]  dict변수의 나이값을 32 수정하세요.
dict["나이"]=32
dict

#############################################################################################3
▣ 재귀호출
- 자기 자신을 다시 호출한다. 
- 함수 안에서 내 함수를 다시 호출 하는 과정 -> 반복문 필요
- 반복문 + stack 구조 

# que: 집어 넣는대로 들어가는 구조; 처음 들어간 것이 제일 먼저 나가는 구조
# push: stack 구조에 쌓아서 놓는 구조 
# stack구조: 제일 밑에 있는 것을 뽑아내고 싶어도 위에 있는 것부터 pop을 해야함(덜어내야함)

■ stack
FILO(First In Last Out): 제일 처음에 들어간 것이 나중에 나간다. :선입후출
LIFO(Last In First Out): 나중에 들어간 것이 제일 먼저 나간다.: 후입선출 

■ push: push 스택의 구조상 마지막 데이터 위치에 입력된다. 

■ pop: 마지막 데이터 위치에서 데이터를 꺼내는 작업(삭제)

■ 재귀호출의 구조  
-stack []
-push 하면 stack 변수에 값을 넣는다.
-pop 하면 stack 변수에 값을 삭제한다.

stack []
push(1)
push(2)
push(3)

pop(3)    #제일 마지막에 있는 것이 삭제 됨 
pop(2)
pop(1)


stack=[]
def push(n):
    global stack    #어디서나 stack을 사용할 수 있도록 global 변수로 만듦 
    stack.append(n)
    
def pop():
    global stack
    if len(stack)==0:
        return Non 
    return stack.pop()

push(1)    #1이 제일 먼저 들어감
push(2)    #1다음 2가 들어감
push(3)    #2다음 3이 들어감 

pop(3)


# stack을 que를 만들때  - 하노이탑 생각하기 : 새로운 변수를 만들어 stack을 하기 
3을 밑으로 들어가고 2가 그 다음, 1이 마지막으로 들어가게 된다. 

#일상생활에서 stack 알고리즘 
1) 하나의 페이지 안에 지금까지의 페이지가 쌓아였기 때문에 첫번째 페이지 부터 마지막 페이지를 보는 것
2) 문서작업에서 되돌리기 
3) 옷장정리 

#재귀호출: factorial (재귀함수로 쓰이고 있음)

▶ factorial 함수
n! = n * (n-1) * (n-2) *.........* 2 * 1
n! = n * (n-1)!

예시)
5! = 5*4*3*2*1
5! = 5*4!
   = 5*4*3!
   = 5*4*3*2!
   = 5*4*3*2*1!
   = 5*4*3*2*1
0! = 1

factorial 공리                         #함수식이 됨 
             n * factorial(n-1) n>=1   #조건 제어문이 됨 
fatoria(n) = 1                  n =0

- 재귀호출문을 통해서 fatorial 계산 가능     #프로그램이 simple하게 할 수 있음
- 그러나 반복문을 통해서 fatorial 계산 가능  #가끔 재귀함수를 사용하게 될 때 보다 반복문 사용이 더 나을 때도 있다. 
- 재귀호출: 반복문 + stack  
    -> 문제점: 반복문 때문에 무한 loop에 빠질 수 있는 위험이 있다. 
    -> 해결책: 따라서 끝내는 작업(끝내주는 시점)을 해야 한다! 
    

factorial 반복문  
def factorial(n):
    f = 1
    for i in range(n,0,-1):
        f *= i
    return f

factorial(5)
factorial(1)
factorial(0)


factorial 재귀호출
def factorial(n):
    if n == 1 or n == 0 :
        return 1
    return n * factorial(n-1) 


# factorial 재귀호출    
    왜 stack 구조가 될까?  #함수 구조이기 때문에 담아놔야하는 구조가 됨 (stack )
    factorial(5)        <push>: stack에 쌓아놓기 
    5 * facotrial(4)    #1) 곱셈은 상수일 때 가능, 그러나 facotrial(4)에 해당하는 값을 모른다. 할 수 없이 어딘가에 쌓아놔야 함. 
                        #2) factorial(4)는 4*factorial(3) -> factorial(3)을 쌓아 놓음
                        #3) factorial(3)는 3*factorail(2) -> factorial(2)을 쌓아 놓음
                        #4) factorial(2)는 2*factorial(1) -> factorial(1)을 쌓아 놓음
                        #3) factorial(1)는 1*factorail(0) -> factorial(0)을 쌓아 놓음
                        #4) factorial(0) 은 1                                         
                        #5) factorial(0) 은 1 -> 이 값을 받환 -> factorial(1)=1 
                        #6) factorial(1) 은 1 
                        <pop>: 계산
                        #4) f(0) = 1
                        #5) f(1)=1*f(0) 
                        #6) f(1)= 1
                        #7) f(2)=2*1
                        #8) f(3)=3*f(2)
                        #9) f(3)=3*2*1
                        #10) f(4)=4*f(3)
                        #11) f(4)=4*3*2*1
                        #12) f(5)=5*f(4)
                        #13) f(5)=5*4*3*2*1                        
                        

####################################################################################
공약수
18과 24의 공약수 
18 = [1, 2, 3, 6, 9, 18]
24 = [1, 2, 3, 4, 6, 8, 12, 24]
공약수: [1,2,3,6]
최대 공약수: 6

소인수분해
2 | 18   24
3 |  9   12
  -----------   
     3    4
최대공약수: 6
최소공배수: 2 * 3* 3 *4 


■ 유클리드 알고리즘
- 주어진 두 수 사이에 존재하는 최대공약수(GCD(Greatest Common Divisor))를 구하는 알고리즘 
1. 두 수 m, n(m > n) 입력으로 들어온다.
2. n이 0이라면 m을 출력하고 알고리즘은 종료 
3. m이 n으로 나누어 떨어지면, n을 출력하고(최대공약수) 알고리즘은 종료
4. 그렇지 않으면 m을 n으로 나눈 나머지를 새롭게 m에 대입하고 m과 n을 바꾸고 다시 3번으로 돌아간다.

[문제82] 최대공약수를 재귀함수로 구현해보세요.
def gcd(m, n):
    if n == 0 :
        return m
    elif m%n ==0:
        return n
    elif m%n != 0 :
        return gcd(n, m%n)
    
gcd(6,3)
gcd(24,18)

#아름이 답
def gcd(m, n):
    if n == 0 :
        return m
    elif m%n ==0:
        return n
    else:
        m= m%n
        return gcd(n,m)
######################
# 쌤답: 
def gcd(x,y):
    if (x<y):
        x, y = y, x    #switching: 기존의 x값을 y로, y값을 x로 바꾸는 방법
    while (y!=0):
        n = x%y
        x = y;
        y = n;
    return x

# 쌤답; 재귀호출 단계    
gcd(24,18)
    24%18 -> 6, x=18, y=6 (18,6)
    18%6 -> 0,  x=6, y=0 (6,0)


# 쌤답- 재귀호출 사용
def gcdFn(x,y):
    if y==0:
        return x
    return gcdFn(y, x%y)

    18%6  (6,0)  
    24%18 (18,6) ↑
24  18%24 (24,18)↑
gcdFn(18,24)     ↑


############################################################################
[문제83] stddev(2,3,1,7) 표준편차를 구하세요. stddev함수를 생성하세요.

평균 = 관측값의 합 / 데이터수
편차 = 관측값 - 평균
편차 제곱합 = (편차**2)+(편차**2)
분산 = 편차제곱합/데이터수(자유도)
표준편차 = math.sqrt(분산)

import math
math.sqrt(분산)

#method 안에 method 가능함 

def stddev(*x) :
    total = 0
    for i in x:
        total += i 
        avg =total/len(x)
        dev_total = 0
    for i in x:
        dev_total += ((i - avg)**2)
        dev = dev_total/len(x)
    return math.sqrt(dev)
            
        
# 쌤답 - method 안에 method 사용 가능 / 밖에서 method mean, variance를 사용할 수 없음 
def stddev(*arg):
    def mean ():
        return sum(arg)/len(arg)
    
    def variance(m):
        total = 0
        for i in arg: 
            total += (i-m)**2
        return total/(len(arg)-1)   #R에서도 자유도 n-1 
    v = variance(mean())
    return math.sqrt(v)


■ module만들기 
# ==> 계속 써야 하는 함수는 object 단위로 호출하여 사용하면 편리하다. 
# ==> 즉, script를 복사-붙여넣기를 하지 않고 file로 떨어뜨려 놓고 import하는 것이 편리하다. (object단위로 호출 가능)
# c:\python\stddev.py 로 stddev script를 object단위로 떨어뜨려 놓기 (메모장에 복사하기 붙여넣기)

# path가 걸려져 있는 것을 확인하기 
물리적인 directory를 사용할 수 있도록 path를 걸어야 한다. 
import sys
sys.path
# 내가 만든 directory를 path에 추가하기 
sys.path.append('c:\\python')
sys.path
# stddev 파일을 불러 들이기 
import stddev
# import된 것 확인하기 
dir()
# stddev: module 이름이 됨 
# module 사용하기 : module이름.method이름 
stddev.stddev(2,3,1,7)

#항상 module 이름을 사용하기 귀찮다면 파일이름 중에 stddev라는 모듈을 import해서 계속 사용한다는 의미
from stddev import *
stddev(2,3,1,7) #method만 사용하면 됨.

#내가 만든 directory에 path만들기 
import sys
sys.path.append('C:\\mypython')
sys.path

#잘못된 path 지우기
sys.path.remove('C:\\mypython')

#########################################
[문제84] stats 모듈에 평균, 분산, 표준편차함수를 사용할수 있는 프로그램을 생성하세요.

>>> import stats
>>> stats.mean(1,2,3,4,5)
3.0
>>> stats.variance(1,2,3,4,5)
2.5
>>> stats.stddev(1,2,3,4,5)
1.5811388300841898

#stats에 각 함수를 포함하도록 하기

########## c:\python\stats.py 답
import math

def mean (*arg):
    return sum(arg)/len(arg)

def variance(*arg):
    total = 0
    m = mean(*arg)
    for i in arg: 
        total += (i-m)**2
    return total/(len(arg)-1)


def stddev(*arg):
    return math.sqrt(variance(*arg))

#cf. 만약에 *arg 로 넣기 싫다면 
def mean(arg):
    return sum(arg)/len(arg)

가변형식일 때는 하나하나 인수값을 넣어야 한다. 
mean(1,2,3,4,5)

하지만 인수값을 가변형식으로 넣지 않을 경우 list형으로 전달해주거나 tuple형, dictionary형 으로 전달해 줘야한다. 
mean([1,2,3,4,5])
mean((1,2,3,4,5))
mean({1,2,3,4,5})


###############################    

import stats

stats.mean(1,2,3,4,5)

stats.variance(1,2,3,4,5)

stats.stddev(1,2,3,4,5)



# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 09:48:47 2018

@author: stu
"""

    
▣ 탐욕알고리즘
- 거리구하기
- 수강신청하기
- 화폐계산하기 

[문제85] 프로그램을 생성하세요.

액수입력 : 362
화폐단위를 입력하세요 : 100 50 1
1원 : 12개
50원 : 1개
100원 : 3개

    
#쌤답 
def coinGreedy(money, cash_type):
    cash_type.sort(reverse=True)  #cash_type이 1,50,100으로 입력됐을 때, 큰 단위로 먼저 나누기 위해서 reverse를 함
    remain = money                #remain이 money로 되어야 함
    res = {}                  
    for cash in cash_type:        #cash_type이 100,50,1
        dvmd = divmod(remain,cash)
        res[cash] = dvmd[0]       #res[cash]키에  dvdm[0]값을 넣음 
        remain = dvmd[1] 
    return res

money = int(input('액수입력 : '))
cash_type = [int(x) for x in input('화폐단위를 입력하세요 : ').split(' ')]
res = coinGreedy(money,cash_type)
for k,v in res.items():          #res.items 를 통해 key value를 확인할 수 있다 
    print('{0}원 : {1}개'.format(k,v))


#cf. 
    
import operator			# dictionary에 대한 정렬을 위해 필요한 moduel 

#키를 기준으로 오름차순 정리
for k,v in sorted(res.items(), key=operator.itemgetter(0)):    
    print('{0}원 : {1}개'.format(k,v))

#value를 기준으로 오름차순 정리
for k,v in sorted(res.items(), key=operator.itemgetter(1)):
    print('{0}원 : {1}개'.format(k,v))

#키를 기준으로 내림차순 정리
for k,v in sorted(res.items(), key=operator.itemgetter(0), reverse=True):
    print('{0}원 : {1}개'.format(k,v))

#value를 기준으로 내림차순 정리
for k,v in sorted(res.items(), key=operator.itemgetter(1), reverse=True):
    print('{0}원 : {1}개'.format(k,v))


#operator 모듈을 불러들인 다음 sorted(정렬에 대한 미리보기), dictionary에 대한 key와 value값을 정렬 

#itemgetter()
itemgetter(0) 여기서 0이 key를 의미
itemgetter(1) 여기서 1은 value절을 의미  


▣ exception처리
- try와 except가 필요하다. 
- exception: 미리 정의된 예상(오류이름)을 알아 놓는 것이 좋다.
def divide(x,y):
    return x/y

divide(10,2)
divide(10,0)
divide(10,'둘')

1)
try:
    z = divide(10,2)
    print(z)
except: 
    print("오류가 발생했습니다.")

2)
#오류 발생했지만 정상적으로 종료하고 메시지를 출력함 
try:
    z = divide(10,0)
    print(z)
except: 
    print("오류가 발생했습니다.")
    

cf. plsql exception이름을 만들어 exception을 처리함 / when others 절은 위에 exception처리에 걸리는 게 없을 때 사용
    1) 미리 정의된 예상(오류 이름), 2) 오류번호는 있는데 이름이 없을 때 이름을 붙여주고 처리, 3) user define- raise문을 만나는 즉시 exception처리 

cf. python에서는 오류 번호가 없음/ 대신 오류 이름은 있음: ZeroDivisionError, TypeError
    => exception처리를 하려면 exception이름을 알고 있어야 한다. 

3) type error 가 났을 때, 등 except가 발생할 때 logic을 하나씩 쓸 수 있음 
try:
    z = divide(10,2)
    print(z)
except TypeError:
    print("인수값을 숫자로 입력하세요.")
except ZeroDivisionError:
    print("0값으로 나눌 수 없습니다.")
except:
    print("오류가 발생했습니다.")
   
4) else: optional한 것으로 else:를 사용하면 except가 없으면 else를 처리하고 끝난다.
try:
    z = divide(10,2)
    print(z)
except TypeError:
    print("인수값을 숫자로 입력하세요.")
except ZeroDivisionError:
    print("0값으로 나눌 수 없습니다.")
except:
    print("오류가 발생했습니다.")
else: 
    print("결과: {0}".format(z)) #0:위치포인터로서 쓰지 않아도 된다.
    
5) finally: 오류가 나도 finally를 수행하고 종료 됨
try:
    z = divide(10,0)
    print(z)
except TypeError:
    print("인수값을 숫자로 입력하세요.")
except ZeroDivisionError:
    print("0값으로 나눌 수 없습니다.")
except:
    print("오류가 발생했습니다.")
else: 
    print("결과: {0}".format(z)) #0:위치포인터로서 쓰지 않아도 된다.   
finally: 
    print("프로그램종료")
    
6) raise exception: rasie절에 만든 오류를 유발 하기 위해서 raise exception(keyword)과 except exception as error(꼭 error를 사용하지 않아도 됨)를 사용 
def func(arg):
    try:
        if arg < 1 or arg > 10:
            raise Exception("유효하지 않는 숫자입니다.:{}".format(arg))
        else:
            print("입력한 수는 {})입니다.".format(arg))
    except Exception as error:
        print("오류가 발생했습니다.{}".format(error))

func(100)            
#as error부분이 raise exception으로 감 

    


################################################################################################
[문제86] 숫자를 입력값으로 받은 후 짝수인지 홀수 인지를 출력한후 그 숫자값을 기준으로
짝수면 짝수형식의 증가값으로 10개 출력, 홀수면 홀수형식의 증가값으로 10개 출력합니다.
만약에 숫자가 들어 오지 않으면 예외사항처리하세요.

숫자를 입력해주세요 : 10
짝수
10
12
14
16
18
20
22
24
26
28
>>> 

숫자를 입력해주세요 : 11
홀수
11
13
15
17
19
21
23
25
27
29

숫자를 입력해주세요 : 이십
invalid literal for int() with base 10: '이십'
숫자를 입력하세요
 

try:   
    number = int(input("숫자를 입력해주세요: "))
    if number%2 == 1:
        print("홀수")
    else: 
        print("짝수")
    count = 1
    while count <= 10:
        print(number)
        number += 2
        count += 1
except ValueError as error:
    print(error)
    print("숫자를 입력하세요")

# 무한루프 발생: number로만 변수를 설정하여 입력하니.... +2가 무한반복... 망... 
try:   
    number = int(input("숫자를 입력해주세요: "))
    if number%2 == 1:
        print("홀수")
    else: 
        print("짝수")
    while number <= (number+20):
        print(number)
        number += 2
except ValueError as error:
    print(error)
    print("숫자를 입력하세요")


#쌤답1
try:
    num = int(input("숫자를 입력해주세요 : "))
    if (num%2) ==0:
        print("짝수")
    else:
        print("홀수")
    count =1
    while count <= 10:
        print(num)
        num += 2
        count += 1
except ValueError as error:
    print(error)
    print('숫자를 입력하세요')

#쌤답2
try: 
    num = int(input("숫자를 입력해주세요 : "))
    if (num%2) ==0:
        print("짝수")
    else:
        print("홀수")
    count =1
    while count <= 10:
        print(num)
        num += 2
        count += 1
except Exception as error:
    print(error)
    print('숫자를 입력하세요')



■ 오류와 실제 오류 정보 파악하기 
lst = [1,2,3]

1)
try:
    print(lst[3])
except:
    print('오류가 발생했습니다.')
    
2) 실제 오류 정보 파악하기   
try:
    print(lst[3])
except Exception as error:
    print(error)

3)
try:
    print(lst[3])
except IndexError as error:
    print(error)
    

###################################################################################################################333
▣ 날짜 
datetime 패키지에서는 
날짜 시간을 제공하는 datetime class, 
날짜만 제공하는 date class, 
시간만 제공하는 time class, 
일수, 시간, 분, 초 구간제공하는 timedelta class

#datetime package
import datetime

#date에 today라는 method가 있음
datetime.date.today()
datetime.date.today().year
datetime.date.today().month
datetime.date.today().day

d=datetime.date.today()
d.year
d.month
d.day


#now moethod는 시, 분, 초도 나옴
datetime.datetime.now()
datetime.datetime.now().year
datetime.datetime.now().month
datetime.datetime.now().day
datetime.datetime.now().hour
datetime.datetime.now().minute
datetime.datetime.now().second

n = datetime.datetime.now()
n.year
n.microsecond   #백만분의 1초: 10**(-6) = μ
n.date()
n.time()
#weekday도 method이기 때문에 ()사용하기 
n.weekday()  0:월 ~ 6:일

cf. sql sysdate를 통해 to_character 해서 날짜를 뽑아냄

###########################################################################
[문제87] 오늘이 무슨 요일인지 출력해주세요
import datetime

days = ['월요일','화요일','수요일','목요일','금요일','토요일','일']
days[datetime.datetime.now().weekday()]

##########################################################################
#년도를 int로 뽑아냄
d = datetime.datetime.now()
type(d.year)


■ strftime: date -> char 
d.strftime('%Y %m %d %B')
d.strftime('%Y') #년도만 str(문자형식)으로 뽑아냄 
d.strftime('%x') #월/ 일/ 년도
d.strftime('%X') #시:분:초
d.strftime('%A') 
d.strftime('%a') 
d.strftime('%c') #날짜, 시간정보
d.strftime('%p')
d.strftime('%j') #누적날짜
d.strftime('%U') 
d.strftime('%W') 
type(d.strftime('%Y %m %d'))

%Y 년도 4자리
%m 달
%d 일
%B 영어 달 이름
%H 시간 24시간으로 환산
%I 시간 12시간으로 환산
%M 분
%S 초
%x 현재 날짜 정보 #월/ 일/ 년도
%X 현재 시간 #시:분:초
%A 요일
%a 요일(축약요일)
%c 날짜시간정보
%p AM, PM
%j 누적 날짜
%U 누적주 (일요일 시작)
%W 누적주 (월요일 시작)
%w 요일 (0~6)
%z 시간대 (+부호 시간대) #datetime.datetime.now()가 시간대를 가지고 있지 않기 때문에 지금 값이 return되지 않음 
d.strftime('%z') 

■ strptime: char -> date
datetime.datetime.strptime('2018-09-11 14:50:00','%Y-%m-%d %H:%M:%S')

d = datetime.date(2018, 9, 11)
t = datetime.time(14,52,00)

#날짜 정보와 시간정보를 합침 
datetime.datetime.combine(d,t)

#날짜정보 계산하기 
datetime.datetime(2018,5,24)-datetime.datetime(2018,11,22)

#날짜정보에 날짜더하기 계산
datetime.datetime(2018, 9, 11) + datetime.timedelta(days=72)

#
datetime.timedelta(days=72)
#초로 환산됨
datetime.timedelta(hours=1)
datetime.timedelta(minutes=1)

# 날짜정보 계산하기
datetime.datetime(2018, 9, 11) + datetime.timedelta(days=72, seconds=3600)

#현재날짜정보 return 
datetime.date.today()


##########################################################################
[문제88] 함수에 인수값으로 현재날짜, 일수 정보를 입력 받아서 더한 날짜정보를 리턴하는 next_day함수를 생성하세요.

#답
def next_day(x):
    return datetime.date.today()+ datetime.timedelta(days=x)

next_day(72)

#쌤답 
def next_day(arg1, arg2):
    return (arg1 + datetime.timedelta(days=arg2))
print(next_day(datetime.date.today(), 72))
##########################################################################


■ 구간계산: delta값에 대한 초단위 계산 
start = datetime.datetime.now()
end = datetime.datetime.now()
delta = end - start
delta.total_seconds()


##########################################################################
[문제89] 아래와 같은 결과가 출력될수 있도록 프로그램을 생성하세요


1에서 천만까지 짝수합, 홀수합 구합니다
1에서 천만까지 짝수합: 24999995000000
1에서 천만까지 홀수합: 25000000000000
처리시간 : 0:00:01.950003
처리시간 millisecond(1/1000)  : 1950ms

#답1
import datetime
start = datetime.datetime.now()
print('1에서 천만까지 짝수합, 홀수합 구합니다')
result_even = 0
result_odd = 0
i = 1
while  i <= 10000000:
    if i%2 == 0:
        result_even += i
        i += 1
    else:
        result_odd += i
        i += 1
print('1에서 천만까지 짝수합: %d'%result_even)
print('1에서 천만까지 홀수합: %d'%result_odd)
end = datetime.datetime.now()        
delta = end -start
delta.total_seconds()
print("처리시간 %d"%delta.total_seconds())
delta_ms = int(delta.total_seconds()*1000)
print("처리시간 millisecond(1/1000) : %dms"%delta_ms)



#답2
import datetime
start = datetime.datetime.now()
print('1에서 천만까지 짝수합, 홀수합 구합니다')
result_even = 0
result_odd = 0
for i in range(1,10000001):
    if i%2 == 0:
        result_even += i
    elif i%2 == 1:
        result_odd += i
print('1에서 천만까지 짝수합: %d'%result_even)
print('1에서 천만까지 홀수합: %d'%result_odd)
end = datetime.datetime.now()        
delta = end -start
delta.total_seconds()
print("처리시간 %d"%delta.total_seconds())
delta_ms = int(delta.total_seconds()*1000)
print("처리시간 millisecond(1/1000) : %dms"%delta_ms)



#쌤답
from datetime import datetime
start = datetime.now()
print('1에서 천만까지 짝수합, 홀수합 구합니다')
even_result = 0
odd_result = 0
for i in range(10000000):
    if i % 2 == 0:
        even_result += i
    else:
        odd_result += i
print('1에서 천만까지 짝수합: %d'%even_result)
print('1에서 천만까지 홀수합: %d'%odd_result)
end = datetime.now()
delta = end - start
print("처리시간 : ",delta)
delta_ms = int(delta.total_seconds() * 1000)
print("처리시간 millisecond(1/1000)  : %dms"%delta_ms)



##########################################################################
■ import time

1970년 1월 1일 0시 0분 0초를 기준으로 지난 시간을 초단위로 리턴해주는 함수
UTC(Universal Time Coordinated 세계협정표준시)를 이용해서 실수 형태로 반환

time.time()
time.localtime()
time.localtime().tm_year
time.localtime().tm_mon
time.localtime().tm_wday #현재요일(0~6)
time.localtime().tm_yday  #누적일수(1~365(366))
time.localtime().tm_isdst  #서머타임일 경우 1, 아닐경우 0, 모를경우 -1


time.gmtime()   #UTC 기준의 현재 시간 (local time)
time.asctime()
time.ctime()

■ time -> char : 
    strftime 여기에도 있지만 형식이 조금 다름 
time.strftime('%Y', time.localtime())
time.strftime('%Y %z', time.localtime())

■ time.sleep(2): 2초 간격으로 for문 돌리기 
for i in range(10):
    print(i)
    time.sleep(2)


▣ import calendar
import calendar
print(calendar.calendar(2018))
calendar.calendar(2018)

calendar.prcal(2019)

calendar.prmonth(2018,9)

calendar.weekday(2018,9,11)

calendar.monthrange(2018, 9)





# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 09:44:41 2018

@author: stu
"""

▣ 파일 입출력

■ 파일생성

■  파일객체 = open("c:/data/test.txt".mode)

■ mode
r : 읽기
w : 쓰기(파일 안에 원본 데이터는 지우고 작성된다.-overwrite)
a : 추가

■ 파일객체.close

f = open("c:/data/test.txt", "w")   #파일 객체 먼저 선언해야함 ex) f = open("물리적 위치정보", "모드정보")

for i in range(1,11):
    txt = "%d 오늘하루도 행복하자\n"%i
    f.write(txt)

f.close()

#test.txt 출력
1 오늘하루도 행복하자
2 오늘하루도 행복하자
3 오늘하루도 행복하자
4 오늘하루도 행복하자
5 오늘하루도 행복하자
6 오늘하루도 행복하자
7 오늘하루도 행복하자
8 오늘하루도 행복하자
9 오늘하루도 행복하자
10 오늘하루도 행복하자

#append
f = open("c:/data/test.txt", "a")   #파일 객체 먼저 선언해야함 ex) f = open("물리적 위치정보", "모드정보")

for i in range(11,21):
    txt = "%d 오늘하루도 행복하자\n"%i
    f.write(txt)

f.close()                           #꼭 파일을 닫아줘야함! (close작업을 안하면 계속 열려있음)

# text.txt 출력
1 오늘하루도 행복하자
2 오늘하루도 행복하자
3 오늘하루도 행복하자
4 오늘하루도 행복하자
5 오늘하루도 행복하자
6 오늘하루도 행복하자
7 오늘하루도 행복하자
8 오늘하루도 행복하자
9 오늘하루도 행복하자
10 오늘하루도 행복하자
11 오늘하루도 행복하자
12 오늘하루도 행복하자
13 오늘하루도 행복하자
14 오늘하루도 행복하자
15 오늘하루도 행복하자
16 오늘하루도 행복하자
17 오늘하루도 행복하자
18 오늘하루도 행복하자
19 오늘하루도 행복하자
20 오늘하루도 행복하자


▣ import os
■ 파일 존재 여부 확인
import os
os.path.exists("c:/data/test.txt")
# 존재하면 True, 존재하지 않으면 False

■ 파일 읽기
- readline(): 라인 하나씩 읽어들인다. 
#첫문장만 읽어들이기
file = open("c:/data/test.txt","r")
data = file.readline()
print(data)
file.close

#전체 문장을 읽어들이기
file = open("c:/data/test.txt","r")
while True:
    data = file.readline()      #더이상 파일에서 읽어올 라인이 없으면 None값을 리턴함 (None은 False임)
    if not data:    #not data: data가 없으면
        break
    print(data)
file.close()

#전체 문장 읽어들일 때 공백 줄 없애기
file = open("c:/data/test.txt","r")
while True:
    data = file.readline()
    if not data:    #not data: data가 없으면
        break
    print(data, end='') #end='': 공백줄 없애기
file.close()

#
- readlines(): 모든 라인을 읽어서 리스트에 저장  -> #변수는 리스트가 됨  -> 따라서 하나씩 하나씩 for문을 이용해서 읽어들여야 함 
file = open("c:/data/test.txt","r")
data = file.readlines()
print(data, end='')
file.close

# 
file = open("c:/data/test.txt","r")
data = file.readlines()
for i in data:
    print(i,end='')
file.close()

#
- read():파일전체를 문자열로 리턴한다.
file = open("c:/data/test.txt","r")
data = file.read()
print(data)
file.close

# cf. sql-  with문: 가상결과 집합을 테이블 모양으로 만들어 놓은 것, inline view(제약: 가상집합을 다시 호출할 때 사용이 안됨)

- with: close를 자동으로 하는 방법 
with open("c:/data/test.txt","w") as file:
    for i in range(1,101):
          txt = '%d 오늘하루도 행복하자\n'%i
          file.write(txt)


#
txt = ['야!! 가을이다', '오늘 하루 신나게 놀아보자']

with open('c:/data/test_new.txt','w') as file:
    for i in txt:
        file.write(i)

with open('c:/data/test_new.txt','w') as file:
    for i in txt:
        file.write(i+'\n')
        
with open('c:/data/test_new.txt','w') as file:
    for i in txt:
        file.write('{}\n'.format(i))
        
# 위의 파일을 읽기 모드로 만들기
with open('c:/data/test_new.txt','r') as file:    
    txt=file.readlines()
    for i in txt:
        print(i,end='')


▣import csv
# csv 파일: ,(comma)로 구분되어 있는 파일
import os
os.path.exists("c:/data/emp.csv")

import csv
file = open("c:/data/emp.csv.","r")
csv.reader(file)   #저장된 주소만 보이고 내용확인이 안됨 

# csv파일 읽어드리기 
emp_csv = csv.reader(file)
emp_csv

# 내용 확인을 위해서는 다음과 같이 for문을 사용해서 읽어들여야 한다. 
for emp_list in emp_csv:
    print(emp_list)


    
# dataframe이 아닌 list 값으로 출력된다. 
# next(emp_csv)를 통해 컬럼정보를 제거할 있다. 
file = open("c:/data/emp.csv","r")
emp_csv = csv.reader(file)
#next(emp_csv)
for emp_list in emp_csv:
    print(emp_list)
    
[문제90] emp.csv파일의 last_name, salary를 출력해주세요. 
# last name, salary 출력하기 
file = open("c:/data/emp.csv","r")
emp_csv = csv.reader(file)
next(emp_csv)
for emp_list in emp_csv:
    print(emp_list[2], emp_list[7])  #2번 인덱스 정보만 출력해 줌 

########################################################################
[문제91] last_name, last_name 길이를 출력해주세요.
file = open("c:/data/emp.csv", "r")
emp_csv = csv.reader(file)
next(emp_csv)
for emp_list in emp_csv:
    print(emp_list[2], len(emp_list[2]))
                     
[문제92] employee_id, last_name, salary*12 달 곱한값을 출력해주세요.
# 문자열이기 때문에 숫자형식으로 바꿔줘야 한다. int로 할 경우
file = open("c:/data/emp.csv", "r")
emp_csv = csv.reader(file)
next(emp_csv)
for emp_list in emp_csv:
    print(emp_list[0], emp_list[2], (int(emp_list[7])*12))
file.close()    

# 문자열이기 때문에 숫자형식으로 바꿔줘야 한다. 그러나 int할 때 소수점이 있으면 오류가 남으로 float을 사용해야 한다. 
file = open("c:/data/emp.csv", "r")
emp_csv = csv.reader(file)
next(emp_csv)
for emp_list in emp_csv:
    print(emp_list[0], emp_list[2], (float(emp_list[7])*12))
file.close()    

[문제93] last_name, commission_pct를 출력하는데 commission_pct값이 ''이면 0으로 출력해주세요.
#답1
file = open("c:/data/emp.csv", "r")
emp_csv = csv.reader(file)
next(emp_csv)
for emp_list in emp_csv:
    if emp_list[-3] =='':
        emp_list[-3] = 0
        print(emp_list[2], emp_list[-3])
    else: 
        print(emp_list[2], emp_list[-3])
file.close()  

#답2
file = open("c:/data/emp.csv", "r")
emp_csv = csv.reader(file)
next(emp_csv)
for emp_list in emp_csv:
    if emp_list[-3] =='':
        print(emp_list[2], emp_list[-3].replace('','0'))
    else: 
        print(emp_list[2], emp_list[-3])
file.close()  

#쌤답
def ifnull(var1, var2):
    if var1 =='':
        return var2
    return var1

file = open("c:/data/emp.csv", "r")
emp_csv = csv.reader(file)
next(emp_csv)
for emp_list in emp_csv:
    print(emp_list[2], ifnull(emp_list[8],0))
file.close()


[문제94] last_name을 대문자로 job_id 소문자로 출력해주세요.
file = open("c:/data/emp.csv","r")
emp_csv = csv.reader(file)
next(emp_csv)
for emp_list in emp_csv:
    print(emp_list[2].upper(), emp_list[6].lower())
file.close()

[문제95] last_name을 첫글자만 추출해서 소문자로 출력해주세요.
file = open("c:/data/emp.csv", "r")
emp_csv = csv.reader(file)
next(emp_csv)
for emp_list in emp_csv:
    print(emp_list[2][0].lower())
file.close()

[문제96] last_name을 두번째 부터 마지막까지만 추출해서 대문자로 출력해주세요.
#답1
file = open("c:/data/emp.csv","r")
emp_csv = csv.reader(file)
next(emp_csv)
for emp_list in emp_csv:
    print(emp_list[2][1:-1].upper())
file.close()

#답2
file = open("c:/data/emp.csv","r")
emp_csv = csv.reader(file)
next(emp_csv)
for emp_list in emp_csv:
    print(emp_list[2][1:].upper())
file.close()

[문제97] 이름을 입력하면 첫글자는 대문자 나머지는 소문자를 출력하는 initcap함수를 이용해서 이름을 출력하세요.
def initcap(x):
    return(x[0].upper()+x[1:].lower())    

   
initcap("kimhyunjung")

import csv
file = open("c:/data/emp.csv",'r')
emp_csv = csv.reader(file)
next(emp_csv)
for emp_list in emp_csv:
    print(initcap(emp_list[2]))
file.close()


[문제98] 이름을 입력하면 제일 뒤에 있는 철자는 대문자 앞의 문자는 소문자로 출력하는 talicap함수를 생성하세요. 
def tailcap(x):
    return(x[:-1].lower()+x[-1].upper())
    
tailcap("hyunjungKim")

import csv
file = open("c:/data/emp.csv",'r')
emp_csv = csv.reader(file)
next(emp_csv)
for emp_list in emp_csv:
    print(tailcap(emp_list[2]))
file.close()

[문제99] 이름과 급여를 출력하는데 급여를 출력할 때에 0대신 *를 출력하세요.
#답1
def zero(x):
    return(x.replace("0","*"))

import csv
file = open("c:/data/emp.csv",'r')
emp_csv = csv.reader(file)
next(emp_csv)
for emp_list in emp_csv:
    print(emp_list[2], zero(emp_list[7]))
file.close()

#답2
file = open("c:/data/emp.csv",'r')
emp_csv = csv.reader(file)
next(emp_csv)
for emp_list in emp_csv:
    print(emp_list[2], emp_list[7].replace("0","*"))
file.close()


[문제100] 이름, salary*12 + commission_pct결과를 출력해주세요. 

"""
def commission(x):
    if x == '':
        return x=0
    else:
        return x

import csv
file = open("c:/data/emp.csv",'r')
emp_csv = csv.reader(file)
next(emp_csv)
for emp_list in emp_csv:
    print(emp_list[2], float(emp_list[7]*12)+commission(float(emp_list[-3])))


file = open("c:/data/emp.csv", "r")
emp_csv = csv.reader(file)
next(emp_csv)
for emp_list in emp_csv:
    if emp_list[-3] =='':
        emp_list[-3] = 0
        print(emp_list[2], math.trunc(int(emp_list[7]*12))+(float(emp_list[-3])))
    else: 
        print(emp_list[2], math.trunc(int(emp_list[7]*12))+(float(emp_list[-3])))
file.close()  
"""

# 쌤답
import math
    
def ifnull(var1, var2):
    if var1 =='':
        return var2
    return var1

file = open("c:/data/emp.csv", "r")
emp_csv = csv.reader(file)
next(emp_csv)
for emp_list in emp_csv:
    print(emp_list[2], math.trunc(int(emp_list[7])*12+float(ifnull(emp_list[8],0))))
file.close()

#ifnull: nvl함수를 만듦
#trunc: sql의 trunc함수와 다름 
#round는 그냥 내장되어 있는 함수
#trunc: math라는 함수를 불러야 함 


[문제101] 이름, 입사한 요일(한글)을 출력해주세요.

import datetime

def day(x):
    days = ['월요일','화요일','수요일','목요일','금요일','토요일','일요일']
    return days[datetime.datetime.strptime(x,'%Y%m%d').weekday()]

file = open("c:/data/emp.csv", "r")
emp_csv = csv.reader(file)
next(emp_csv)
for emp_list in emp_csv:
    print(emp_list[2], day(emp_list[5]))
file.close()

#쌤답 :문자 -> 날짜 
import datetime
import csv
file = open("c:/data/emp.csv",'r')
days = ['월요일','화요일','수요일','목요일','금요일','토요일','일요일']
emp_csv = csv.reader(file)
next(emp_csv)
for emp_list in emp_csv:
    a = datetime.datetime.strptime(emp_list[5],'%Y%m%d')
    print(emp_list[1], days[a.weekday()])
file.close()

[문제102] 이름, 입사한 날짜부터 오늘까지 총 몇일 근무했는지 출력하세요. 

import datetime
import csv

def workdays(x):
    return datetime.datetime.today()-datetime.datetime.strptime(x, '%Y%m%d')

file = open("c:/data/emp.csv", "r")
emp_csv = csv.reader(file)
next(emp_csv)
for emp_list in emp_csv:
    print(emp_list[2], workdays(emp_list[5]).days)   #.days시간정보 없애기 
file.close()


#쌤답1
import datetime
import csv
file = open("c:/data/emp.csv",'r')
emp_csv =csv.reader(file)
next(emp_csv)
for emp_list in emp_csv:
    a = datetime.datetime.now()- datetime.datetime.strptime(emp_list[5],'%Y%m%d')
    print(emp_list[1], a.days)
file.close()

#cf. 날짜는 날짜의 모양을 만들어줘야 한다. now()는 datetime형식 today()는 date형식
#쌤답2
import datetime
import csv
file = open("c:/data/emp.csv",'r')
emp_csv =csv.reader(file)
next(emp_csv)
for emp_list in emp_csv:
    a = datetime.date.today()- datetime.datetime.strptime(emp_list[5],'%Y%m%d').date()  #날짜형식인 date형식을 맞추기
    print(emp_list[1], a.days)
file.close()


[문제103]오늘 부터 이번달 말일까지 몇일 남았는지 출력하세요.
import datetime 
import calendar

day = calendar.monthrange(2018, 9) 

day[1] - datetime.date.today().day

#쌤답
from datetime import date
from calendar import monthrange

monthrange(2018,9)[1]-date.today().day


[문제104] 사원번호가 100번 사원의 사원이름과 급여를 출력하세요.
import csv
file = open("c:/data/emp.csv",'r')
emp_csv =csv.reader(file)
next(emp_csv)
for emp_list in emp_csv:
    if emp_list[0] == "100":
        print(emp_list[1], emp_list[7])
file.close()

#쌤답
import csv

file = open("c:/data/emp.csv",'r')
emp_csv = csv.reader(file)
next(emp_csv)
for emp_list in emp_csv:
    if int(emp_list[0])==100:
        print(emp_list[2], emp_list[7])
file.close()
        
[문제105] 급여가 10000 이상인 사원들의 이름과 급여를 출력하세요.
import csv
file = open("c:/data/emp.csv",'r')
emp_csv =csv.reader(file)
next(emp_csv)
for emp_list in emp_csv:
    if int(emp_list[7]) >= 10000:        #where의 조건절    
        print(emp_list[1], emp_list[7])  #select 절의 column 
file.close()

#쌤답
import csv
file = open("c:/data/emp.csv",'r')
emp_csv =csv.reader(file)
next(emp_csv)
for emp_list in emp_csv:
    if float(emp_list[7]) >= 10000:        #where의 조건절    
        print(emp_list[2], emp_list[7])  #select 절의 column 
file.close()

[문제106] 2001-01-13일에 입사한 사원의 이름과 입사일을 출력하세요
#답1: 날짜형으로 비교
import csv
import datetime
file = open("c:/data/emp.csv",'r')
emp_csv =csv.reader(file)
next(emp_csv)
for emp_list in emp_csv:
    if datetime.datetime.strptime(emp_list[5],'%Y%m%d') == datetime.datetime.strptime('2001-01-13','%Y-%m-%d'):
        print(emp_list[1], emp_list[5])
file.close()

#답2: 문자형으로 비교
import csv
import datetime
file = open("c:/data/emp.csv",'r')
emp_csv =csv.reader(file)
next(emp_csv)
for emp_list in emp_csv:
    if emp_list[5] == "20010113":
        print(emp_list[1], emp_list[5])
file.close()

#쎔답
import csv
import time
file = open("c:/data/emp.csv",'r')
emp_csv =csv.reader(file)
next(emp_csv)
for emp_list in emp_csv:
    if time.strptime(emp_list[5],'%Y%m%d') == time.strptime('20010113','%Y%m%d'):
        print(emp_list[1], emp_list[5])
file.close()

#sql: to_date : 문자 -> 날짜

[문제107] 2002 년도에 입사한 사원들의 이름과 입사일을 출력하세요.
#답1
import csv
import datetime
file = open("c:/data/emp.csv",'r')
emp_csv =csv.reader(file)
next(emp_csv)
for emp_list in emp_csv:
    if datetime.datetime.strptime('2002-01-01', '%Y-%m-%d') <= datetime.datetime.strptime(emp_list[5],'%Y%m%d') < datetime.datetime.strptime('2003-01-01', '%Y-%m-%d'):
        print(emp_list[1], emp_list[5])
file.close()

#답2
import csv
file = open("c:/data/emp.csv",'r')
emp_csv =csv.reader(file)
next(emp_csv)
for emp_list in emp_csv:
    if int(emp_list[5][0:4])==2002:
        print(emp_list[1], emp_list[5])
file.close()

#쌤답1
import csv
file = open("c:/data/emp.csv",'r')
emp_csv =csv.reader(file)
next(emp_csv)
for emp_list in emp_csv:
    if emp_list[5][:4]=='2002':
        print(emp_list[2], emp_list[5])
file.close()

#쌤답2
import csv
import time

file = open("c:/data/emp.csv",'r')
emp_csv =csv.reader(file)
next(emp_csv)
for emp_list in emp_csv:
    if time.strptime(emp_list[5],'%Y%m%d').tm_year == time.strptime('2002', '%Y').tm_year:
        print(emp_list[2], emp_list[5])
file.close()


########################################################################

[문제108] job이 ST_CLERK 이고 월급 3000 이상인 사원들의 이름과 job, 급여 출력하세요
import csv
file = open("c:/data/emp.csv",'r')
emp_csv=csv.reader(file)
next(emp_csv)
for emp_list in emp_csv:
    if emp_list[6]=="ST_CLERK" and int(emp_list[7])>=3000:
        print(emp_list[2], emp_list[6], emp_list[7])


[문제109] 급여가 2500 에서 3000 사이인 사원들의 이름과 급여를 출력하세요
import csv
file = open("c:/data/emp.csv",'r')
emp_csv=csv.reader(file)
next(emp_csv)
for emp_list in emp_csv:
    if 2500 <= int(emp_list[7]) <= 3000:
        print(emp_list[2], emp_list[7])

#쌤답
file = open("c:/data/emp.csv",'r')
emp_csv=csv.reader(file)
next(emp_csv)
for emp_list in emp_csv:
    if 2500 <= float(emp_list[7]) and 3000>=float(emp_list[7]):
         print(emp_list[2], emp_list[7])   
    
[문제110] job AD_VP , AD_PRES 인 사원들의 이름과 월급과 직업을 출력하세요
import csv
file = open("c:/data/emp.csv",'r')
emp_csv=csv.reader(file)
next(emp_csv)
for emp_list in emp_csv:
    if emp_list[6] == "AD_VP" or emp_list[6]=="AD_PRES":
        print(emp_list[2], emp_list[7], emp_list[6])

#쌤답
import csv
file = open("c:/data/emp.csv",'r')
emp_csv=csv.reader(file)
next(emp_csv)
cn = 0
for emp_list in emp_csv:
    if emp_list[6] in ["AD_VP", "AD_PRES"]:
        print(emp_list[2], emp_list[7], emp_list[6])
        cn += 1
print ('총건수 %d'%cn)

[문제111] 직업이 AD_VP , AD_PRES 이 아닌 사원들의 이름과 월급과 직업을  출력하세요
import csv
file = open("c:/data/emp.csv",'r')
emp_csv=csv.reader(file)
next(emp_csv)
count = 0 
for emp_list in emp_csv:
    if emp_list[6] != "AD_VP" and emp_list[6] !="AD_PRES":
        print(emp_list[2], emp_list[7], emp_list[6])
        count +=1
print(count)

#쌤답
import csv
file = open("c:/data/emp.csv",'r')
emp_csv=csv.reader(file)
next(emp_csv)
cn = 0
for emp_list in emp_csv:
    if emp_list[6] not in ["AD_VP", "AD_PRES"]:
        print(emp_list[2], emp_list[7], emp_list[6])
        cn += 1
print ('총건수 %d'%cn)



# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 09:46:49 2018

@author: stu
"""
##############################################################################
import csv
file = open("c:/data/emp.csv","r")          
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    print(emp_list)
    

[문제112] 커미션이 null 인 사원의 이름, 급여, 커미션을 출력하세요.
          전체 인원수, 커미션 null의 수, 비율도 출력하세요.

import csv
file = open("c:/data/emp.csv","r")          
emp_csv = csv.reader(file)
next(emp_csv)
cn_total = 0
cn_null = 0
for emp_list in emp_csv:
    cn_total += 1
    if emp_list[-3] == "":
        emp_list[-3] = 0
        print(emp_list[2], emp_list[7], emp_list[-3])
        cn_null += 1
ratio=round((cn_null/cn_total*100),2)

print('전체 인원수: ', cn_total,'명')
print('커미션 null의 수 :',cn_null,'명')
print('비율: ', ratio)


#쌤답
import csv
import math

import csv
file = open("c:/data/emp.csv","r")          
emp_csv = csv.reader(file)
next(emp_csv)
cn1 = 0
cn2 = 0
for emp_list in emp_csv:
    if emp_list[8] =='':
        print(emp_list[2], emp_list[7], emp_list[8])
        cn1 +=1
    cn2 += 1
print('전체 수: {}'.format(cn2))
print('조건의 수: {}'.format(cn1))
print('조건의 비율: {}'.format(math.trunc(cn1*100/cn2)))



[문제113]커미션이 null 이 아닌 사원들의 이름,급여,커미션을 출력하세요.
전체 인원수, 커미션 null의 수, 비율도 출력하세요.

import csv
file = open("c:/data/emp.csv","r")          
emp_csv = csv.reader(file)
next(emp_csv)
cn_total = 0
cn_null = 0
for emp_list in emp_csv:
    cn_total += 1
    if emp_list[-3] != "":
        print(emp_list[2], emp_list[7], emp_list[-3])
        cn_null += 1
ratio=round((cn_null/cn_total*100),2)

print('전체 인원수: ', cn_total,'명')
print('커미션 null의 수 :',cn_null,'명')
print('비율: ', ratio)


#쌤답
import csv
import math

import csv
file = open("c:/data/emp.csv","r")          
emp_csv = csv.reader(file)
next(emp_csv)
cn1 = 0
cn2 = 0
for emp_list in emp_csv:
    if emp_list[8] !='':
        print(emp_list[2], emp_list[7], emp_list[8])
        cn1 +=1
    cn2 += 1
print('전체 수: {}'.format(cn2))
print('조건의 수: {}'.format(cn1))
print('조건의 비율: {}'.format(math.trunc(cn1*100/cn2)))


[문제114] last_name의 첫번째 철자가 S 로 시작하는 사원들의 이름과 급여를 출력하세요.
전체 인원수, 커미션 null의 수, 비율도 출력하세요.

import csv
file = open("c:/data/emp.csv","r")          
emp_csv = csv.reader(file)
next(emp_csv)
cn_total = 0
cn_s = 0
for emp_list in emp_csv:
    cn_total += 1
    if emp_list[2][0].upper() == 'S':
        print(emp_list[2], emp_list[7])
        cn_s += 1
ratio=round((cn_s/cn_total*100),2)

print('전체 인원수: ', cn_total,'명')
print('last_name의 첫번째 철자가 S 로 시작하는 사원의 수 :',cn_s,'명')
print('비율: ', ratio)

#쌤답
import csv
import math

import csv
file = open("c:/data/emp.csv","r")          
emp_csv = csv.reader(file)
next(emp_csv)
cn1 = 0
cn2 = 0
for emp_list in emp_csv:
    if emp_list[2][0].upper() == 'S':
        print(emp_list[2], emp_list[7])
        cn1 +=1
    cn2 += 1
print('전체 수: {}'.format(cn2))
print('조건의 수: {}'.format(cn1))
print('조건의 비율: {}'.format(math.trunc(cn1*100/cn2)))


[문제115] last_name의 두번째 철자가 i 인 사원들의 이름과 월급을 출력하세요. 
전체 인원수, 커미션 null의 수, 비율도 출력하세요.

import csv
file = open("c:/data/emp.csv","r")          
emp_csv = csv.reader(file)
next(emp_csv)
cn_total = 0
cn_i = 0
for emp_list in emp_csv:
    cn_total += 1
    if emp_list[2][1].lower() == 'i':
        print(emp_list[2], emp_list[7])
        cn_i += 1
ratio=round((cn_i/cn_total*100),2)

print('전체 인원수: ', cn_total,'명')
print('last_name의 두번째 철자가 i 인 사원의 수 :',cn_i,'명')
print('비율: ', ratio)

#쌤답
import csv
import math

import csv
file = open("c:/data/emp.csv","r")          
emp_csv = csv.reader(file)
next(emp_csv)
cn1 = 0
cn2 = 0
for emp_list in emp_csv:
    if emp_list[2][1].lower() == 'i':
        print(emp_list[2], emp_list[7])
        cn1 +=1
    cn2 += 1
print('전체 수: {}'.format(cn2))
print('조건의 수: {}'.format(cn1))
print('조건의 비율: {}'.format(math.trunc(cn1*100/cn2)))


[문제116] 50번부서 사원들의 이름, 급여 출력하는데 이름을 오름차순으로 출력하세요.

#
import csv
file = open("c:/data/emp.csv","r")          
emp_csv = csv.reader(file)
next(emp_csv)
dept_50 = []

for emp_list in emp_csv:
    if emp_list[-1]=="50":
        dept_50.append('{},{}'.format(emp_list[2], emp_list[7]))
        
dept_50.sort()
print(dept_50)

# 쌤답
from operator import itemgetter #operator 모듈 제공

file = open("c:/data/emp.csv","r")          
emp_csv = csv.reader(file)
next(emp_csv)
emp_list = []
for i in emp_csv:
    if i[-1]=="50":
        emp_list.append(i)
        
emp_list_sorted = sorted(emp_list, reverse=False, key=itemgetter(2))  #sorted는 미리보기 #key=itemgetter(): list 정렬; method가 없다면 몇번 인덱스를 기준으로 할 것인지 만들면 된다.
for i in emp_list_sorted:
    print(i[2],i[7])



cf. 확인해보기: emp_list
cf. emp_list_sorted 
print(emp_list_sorted)

#쌤답 응용하기 method를 직접만들자! sort_check라는 함수를 만들어 key=itemgetter를 만들어 보기     
import csv
def sortCheck(data):
    return(data[2])            #sorted(emp_list, reverse=False, key=itemgetter(2))
    
file = open("c:/data/emp.csv","r")          
emp_csv = csv.reader(file)
next(emp_csv)
emp_list = []
for i in emp_csv:
    if i[-1]=="50":
        emp_list.append(i)

emp_list_sorted = sorted(emp_list, reverse=False, key= sortCheck)        

for i in emp_list_sorted:
    print(i[2],i[7])


#######################################################################
#쌤답 굳이 method를 위에 만들지 않고 key값에 람다함수로 만드려면?
▣ lambda(람다)함수
-이름이 없는 한줄짜리 함수
-가독성을 위해서

예시) 
# method
def f(x,y):
    return x*y

f(2,3)

# 한줄짜리 함수 
(lambda x,y: x*y)(2,3)

# 한줄짜리 함수 
f = lambda x,y: x*y    
f(2,3)        

#######################################################################
[문제116] 50번부서 사원들의 이름, 급여 출력하는데 이름을 오름차순으로 출력하세요.
# 람다함수 이용 
import csv
def sortCheck(data):
    return(data[2])            #sorted(emp_list, reverse=False, key=itemgetter(2))
    
file = open("c:/data/emp.csv","r")          
emp_csv = csv.reader(file)
next(emp_csv)
emp_list = []
for i in emp_csv:
    if i[-1]=="50":
        emp_list.append(i)

emp_list_sorted = sorted(emp_list, reverse=False, key=(lambda x:x[2]))        

for i in emp_list_sorted:
    print(i[2],i[7])




#이상해1
import csv
file = open("c:/data/emp.csv","r")          
emp_csv = csv.reader(file)
next(emp_csv)
dept_50 = []

for emp_list in emp_csv:
    if emp_list[-1]=="50":
        dept_50.extend([print(emp_list[2]),print(emp_list[7])])

#이상해2
import csv
file = open("c:/data/emp.csv","r")          
emp_csv = csv.reader(file)
next(emp_csv)
dept_50 = []
        
for emp_list in emp_csv:
    if emp_list[-1]=="50":
        dept_50.extend([print(emp_list[2], emp_list[7])])
        

[문제117] job이 ST_CLERK인 사원들의 이름과 입사일과 job을 출력하는데 가장 최근에 입사한 사원부터 출력하세요.
#람다함수 이용
import csv

file = open("c:/data/emp.csv",'r')
emp_csv = csv.reader(file)
next(emp_csv)
job_ST_CLERK = []

for i in emp_csv:
    if i[6] == "ST_CLERK":
        job_ST_CLERK.append(i)

job_sorted = sorted(job_ST_CLERK , reverse=True, key=(lambda x:x[5]))
   
for i in job_sorted:
    print(i[2],i[5],i[6])
    
# operator module이용 
import csv
from operator import itemgetter 

file = open("c:/data/emp.csv",'r')
emp_csv = csv.reader(file)
next(emp_csv)
job_ST_CLERK = []

for i in emp_csv:
    if i[6] == "ST_CLERK":
        job_ST_CLERK.append(i)
job_sorted = sorted(job_ST_CLERK , reverse=True, key=itemgetter(5))
for i in job_sorted:
    print(i[2],i[5],i[6])


[문제118] 부서별 급여의 총액을 구하세요.
import csv
file = open("c:/data/emp.csv",'r')
emp_csv = csv.reader(file)
next(emp_csv)

dept_sum={}

for emp_list in emp_csv:
    if emp_list[10] in dept_sum:
        dept_sum[emp_list[10]]=int(dept_sum[emp_list[10]])+int(emp_list[7])
    else:
        dept_sum[emp_list[10]]=int(emp_list[7])

for k,v in dept_sum.items():
    print(k,v)


[문제119] 부서별 급여의 총액을 구하세요. 부서별로 오름차순 정렬하세요. 

10 4400
20 19000
30 24900
40 6500
50 156400
60 28800
70 10000
80 304500
90 63040
100 51608
110 20308
non 7000


#119번
        
import csv
file = open("c:/data/emp.csv",'r')
emp_csv = csv.reader(file)
next(emp_csv)

dept_sum={}
for emp_list in emp_csv:
    if emp_list[10] in dept_sum:
        dept_sum[emp_list[10]]=int(dept_sum[emp_list[10]])+int(emp_list[7]) #key - value 값: 만약에 부서코드에 null이 없었으면 int로 바꿔 풀기 
    else:
        dept_sum[emp_list[10]]=int(emp_list[7])   # key - value값
        
def sortCheck(x):
    try:
        return int(x[0])   #key를 기준으로 하여 integer 바꾸기
    except:
        return 999         #na는 999가 되어 맨 밑으로 정렬됨 

dept_sum_sort = sorted(dept_sum.items(), reverse=False, key=sortCheck) #정렬시킨 key-value값 

for k, v in dept_sum_sort:
    if k=='':
        print('non',v)
    else: 
        print(k,v)
        
        
[문제120] 단어, 알파벳을 입력값으로 넣어서 단어 안에 알파벳 수를 출력하세요

<화면예>

wordF('happy','p')
2

def wordF(x,y):
    print(x.count(y))
    
def wordF(x,y):
    result = 0
    for i in range(len(x)):
        if x[i] ==y:
            result += 1 
    print(result)

#쌤답
def wordF(arg1, arg2):
    cn = 0
    for i in arg1:
        if i == arg2:
            cn += 1
    print(cn)
    

 [문제121] 단어를 입력값으로 넣어서 알파벳을 출력하는데 중복되는 알파벳은 하나만 출력하세요.

alphaF('happy')
['h', 'a', 'p', 'y']

alphaF('intelligence')
['i', 'n', 't', 'e', 'l', 'g', 'c']
   

def alphaF(x):
    list = []
    for i in range(len(x)):
        if x[i] not in list:
            list.append(x[i])
    print(list)        


#쌤답
def alphaF(arg):
    freq = []
    for c in arg:
        if c not in freq:   #freq에 없으면 append
            freq.append(c)
                            #freq에 있으면 if는 끝남 
    print(freq)


[문제122] 단어 철자의 빈도수를 출력하세요.


alphaF('intelligence')
{'i': 2, 'n': 2, 't': 1, 'e': 3, 'l': 2, 'g': 1, 'c': 1}

alphaF('happy')
{'h': 1, 'a': 1, 'p': 2, 'y': 1}
   
#다시 해보기    
def alphaF(x):
    alpha_sum={}
    for i in range(len(x)):
        if x[i] in alpha_sum:
            alpha_sum['x[i]'] = 'x.count(x[i])'
    for k,v in alpha_sum.items():
        print(k,v)


# 쌤답 
def alphaF(arg):
    freq={}
    for c in arg:
        if c in freq:
            freq[c] += 1
        else:
            freq[c] = 1
    print(freq)
    

#######################################################################
    
▣ pandas
- 데이터 분석 기능을 제공하는 라이브러리
- 1차원 배열: Series
- 2차원 배열: DataFrame

import pandas as pd 
from pandas import Series, DataFrame (pandas.Series 계속 써는 것을 방지하기 위해 이렇게 import할 수 있음)

■ Series
- 1차원 배열
- 인덱스(색인) 배열의 데이터에 연관된 이름을 가지고 있다. 

s = Series([10,20,30,40,50])
s.index    #색인의 인덱스를 볼 수 있음 
s.values   #값을 보여주면서 자료형을 보여줌
s.index = ['a','b','c','d','e']   #기존의 인덱스 번호를 수정 
s
# R의 vector형처럼 계산할 수 있다. 
s + 10
s - 10
s * 10
s / 3
s//3
s %3

# index를 바로 설정할 수 있음
s2 = Series([10,20,30,40], index=['a','b','c','d'])
s2
s2['a','b'] #오류
s2[['a','b']] #두개의 인덱스를 보려고 할 경우 -> 두개의 대괄호가 필요

# 기존의 인덱스를 보는 방법을 사용할 수 있음 
s2[0]
s2[0:3]
s2[-1]

s2[s2>20]   #20보다 큰 값 확인가능 

#인덱스가 있는지 확인하기 
'a' in s2
'e' in s2

#인덱스 값 수정, 추가, 삭제
s2['a'] = 100   #수정
s2
s2['e'] = 50    #추가
s2
del s2['e']     #삭제
s2['a'] = ''
s2
del s2          #변수삭제: del 변수이름 -> 변수이름 삭제

□ dictionary 형을 series로 생성(key : index/  value: 내용)
dict = {'a':10, 'b':20, 'c':30, 'd':40}
dict
s3 = Series(dict)
s3

dict = {'a':10, 'b':20, 'c':30, 'd':40}
ix = {'a','b','c','d'}      #내가 원하는 index 값(ix)만 가져옴; 그대로 참조함 
s4 = Series(dict, index=ix)
s4

dict = {'a':10, 'b':20, 'c':30, 'd':40}
ix = {'a','b','c','z'}          #z라는 index는 만들어졌지만 dict z값은 없음 -> NaN ; sequence한 배열이 원래 아님 #NaN이 있기 때문에 type도 바뀜
s5 = Series(dict, index=ix)
s5  #NaN(Not a Number): 인덱스 값을 찾을 수 없기 때문에 NaN저장


dict = {'a':10, 'b':20, 'c':30, 'd':40}
ix = {'a','b'}   
s6 = Series(dict, index=ix)
s6

□ pandas에서 null인 값 찾기 
import pandas as pd 
pd.isnull(s5)       #NaN가 있으면 True
pd.notnull(s5)      #NaN가 있으면 False

dict = {'서울':100, '부산':200, '광주':300, '제주':400}
s7 = Series(dict)
s7

city=['서울', '광주', '제주', '인천']

s8 = Series(dict, index=city)
s8

■ DataFrame
- 2차원 배열
- 표현식의 자료구조
- 각 컬럼은 서로 다른 종류의 값(문자, 숫자, 불리언)
- R언어 data.frame
- DataFrame([[],[],[]])

df1 = DataFrame([[1,2,3],[4,5,6],[7,8,9]]) #대괄호 안에 
df1

#dictionary
data = {'도시':['광주','부산','강원','인천'],'인구수':[100,200,50,300]}
data

df2 = DataFrame(data)
df2

df3 = DataFrame({'도시':['광주','부산','강원','인천'],'인구수':[100,200,50,300]})
df3

#컬럼 수정
df3.columns = ['지역','가구수']
df3

# 컬럼 정보 추출
df3.지역
df3.가구수

df3['지역']
df3['가구수']


# 연산작업(series에서와 같이 연산작업이 가능하다.)
df3['가구수']*100

#인덱스 확인
df3.index
#인덱스 수정
df3.index=['one', 'two', 'three','four']
df3

#행보기: ix 메소드 이용 
#데이트프레임.ix[인덱스이름]
df3.ix['one']
df3.ix[0]
df3.ix[1]

#series로 열을 추가
v = Series([1000,2000,3000,4000], 
           index=['one', 'two', 'three', 'four'])
v

df3['부채'] = v
df3

#직접 리스로 열을 추가
df3['인구수']=[10000,20000,300000,5000]
df3

#열 삭제
del df3['부채']
df3

# 
data = {'서울':{2001:200,2002:300},'부산':{2000:10,2001:20,2002:30}}

df4 = DataFrame(data)
df4
# 컬럼이름이 인덱스로, 인덱스가 컬럼이름쪽으로 방향을 바꿈
df4.T
#컬럼 확인
df4.columns
#인덱스 확인
df4.index
#value값 확인 
df4.values

□ reindex(재색인): 새로운 색인에 맞도록 객체를 새로 생성하는 기능
#series 생성: 인덱스가 sequence하지 않음 
obj = Series([10,20,30,40], index=['c','d','a','b'])

# 리인덱스를 통해서 sequence하게 만들 수 있음
obj2 = obj.reindex(['a','b','c','d'])
obj2

# 새로운 인덱스를 더할시에 그 값은 NaN이 됨 
obj3 = obj.reindex(['a','b','c','d','z'])
obj3

#필요한 것만 뽑아낼 때 reindex 응용하기 
obj4 = obj.reindex(['a','b','c'])
obj4




# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 09:46:58 2018

@author: stu
"""

import pandas as pd
from pandas import Series, DataFrame

Series
- 1차원배열

DataFrame
- 2차원배열 

□ .reindex() 
- 인덱스 배열을 변형하고자 할 때 사용
- 새로운 인덱스를 만들 때 사용
- NaN 값을 fill_value=0으로 만들 때 사용

obj = Series([10, 20, 30, 40], index =['c','d','a','b'])
obj


obj2 = obj.reindex(['a','b','c','d'])
obj2

# 'f' 인덱스는 없음 -> field 값은 NaN 으로 나타남
obj3 = obj.reindex(['a','b','c','d','f']) 
obj3

# fill_value=0 : NaN값을 0으로 바꿈 (직접 바꾸고 싶은 값으로 바꿀 때 fill_value사용)
obj4 = obj.reindex(['a','b','c','d','f'],fill_value=0)
obj4


▣ import numpy as np
import numpy as np

■ np.arange(): array 생성 #행렬을 만들 수 있음 
# array 생성
np.arange(4)

■ np.arange().reshape(,): 행렬생성
# 행렬 생성
np.arange(4).reshape(2,2)
np.arange(9).reshape(3,3)
np.arange(12).reshape(3,4)

df = DataFrame(np.arange(9).reshape(3,3), index=['a','b','c'], columns=['x','y','z'])
df

#d 인덱스가 없기 때문에 d는 NaN으로 만들어짐(적용됨)
df2 = df.reindex(['a','b','c','d'])
df2

□ method = 'ffill'/ method = 'pad'는 앞의 값으로 NaN을 채운다.
# method = 'ffill': NaN값이 앞에 있는 데이터가 채워짐 
df3 = df.reindex(['a','b','c','d'], method ='ffill')
df3 = df.reindex(['a','b','c','d'], method ='pad')
df3

obj = Series(['sql','r','python'], index=[0,2,4])
obj2 = obj.reindex(range(6))
obj2 = obj.reindex(range(6), method='ffill')
obj2

#method='bfill' 또는 'backfill'는 뒤의 값으로 NaN을 채운다.
obj2= obj.reindex(range(6), method='bfill')
obj2
obj2= obj.reindex(range(6), method='backfill')
obj2
obj2[5] = 'sql'
obj2

□ 행삭제 
obj = Series(np.arange(5), index=['a','b','c','d','e'])
obj
#행삭제: 꼭 적용을 시켜줘야 함
obj.drop('e') #미리보기만 해 줌
obj

obj = obj.drop('e')
obj

# 여러개의 값을 지울 수 있음
obj = obj.drop(['c','d'])
obj

#dataframe 삭제적용하기
df = DataFrame(np.arange(16).reshape(4,4), 
               index=['w','x','y','z'], 
               columns=['one','two','three','four'])
#삭제 미리보기
df.drop('x',axis=0) #axis=0:행
df.drop('four',axis=1) #axis=1:열

# 삭제 적용
df = df.drop(['w','y'], axis=0)
df

df = df.drop(['one','two'], axis=1)
df

□ 인덱스 보기
obj = Series([10,20,30,40], index=['a','b','c','d'])
obj
# indexing
obj['a']
obj[0]
obj[1:3]  #인덱스 번호
obj['b':'c'] #인데스 
# a하고 c만 보고 싶을 때: 안에 대괄호 필요 
obj['a','c'] #오류
obj[['a','c']]
obj[[0,2]]
# 30미만인 데이터 보기 
obj<30 #boolean 형식으로 데이터를 추출 
obj[obj<30] #30미만 데이터 추출

# dataframe 인덱스 보기
df = DataFrame(np.arange(16).reshape(4,4), 
               index=['w','x','y','z'], 
               columns=['one','two','three','four'])
df
df['one']
df[['one','two']]
df[2:]
df < 5
df[df<5]
df[df['one']<5]

#x행만 보여주기 
df.ix['x'] # .ix[]: 이름, 번호 모두 쓸 수 있음 
df.ix[0] # 번호로 인덱스 보기
df.loc['x'] # loc[]: 인덱스 이름, 컬럼이름만 가능 
df.loc[0] # error #loc[]인덱스 번호를 사용할 수 없
df.iloc[0] # iloc[]:인덱스 번호, 컬럼번호만 사용가능

df.ix['x','one']
df.ix['x',['one','two']]
#두개값을 보려고 할 때는 꼭 리스트 형으로 만들어서 표현해야한다.
df.ix[['x','y']]
df.ix[['x','y'],['one','two']]
#열에도 순번이 있기 때문에 리스트 모양으로 순번을 표현할 수 있다.
df.ix[['x','y'],[0,1]]
df.ix[0,'one']
df.ix[[0,2],[0,1]]

df.ix[:]
df.ix[0:2]
df.ix[0:2, 0:2]
df.ix[:,0:2]
df.ix[-1]
df.ix[:,-1]


##############################################################################################
※ 행과 열을 추출하는 방법: 매우 중요합니다. ※

[문제123] 아래와 같은 모양의 표를 생성하세요. 

      PYTHON   R  SQL
2014      60  90   50
2015      80  65   75
2016      70  75   85

#dictionary형을 먼저 만들어 생각해보기 
df = DataFrame({'PYTHON':[60,80,70],'R':[90,65,75],'SQL':[50,75,85]}, 
                index=['2014','2015','2016'])
df


[문제124] 'PYTHON' 열을 선택하세요
df.ix[:,'PYTHON']
df['PYTHON']

[문제125] '2014' 행 정보를 출력하세요.
df.ix['2014']
df.iloc[0]


[문제126] 인덱스번호를 기준으로 1부터 2번까지 출력하세요.
df.ix[1:3]
df[1:3]
df.iloc[1:3]

[문제127] PYTHON의 값을 기준으로 60보다 큰값을 가지고 있는 행 정보를 출력하세요.
df[df.ix[:,'PYTHON']>60]
df[df['PYTHON']>60]

[문제128] PYTHON의 값을 기준으로 60 보다 큰값을 가지고 있는 PYTHON 정보만 출력하세요.
df1 = df.ix[df['PYTHON']>60]
df1['PYTHON']

df.ix[df['PYTHON']>60, 'PYTHON']  #df['PYTHON']>60:행정보,/'PYTHON' 뒤에 열 정보를 추가하면 PYTHON정보만 추출한다.
df.ix[df['PYTHON']>60,'PYTHON'] 
df.loc[df['PYTHON']>60, 'PYTHON']
df['PYTHON'][df['PYTHON']>60]  #[df['PYTHON']>60]: 행제한

#SQL로 생각하기 'PYTHON'] , 'PYTHON'] ,'PYTHON'] : Select절 / df['PYTHON']>60: where절이라고 할 수 있음 

[문제129] '2015' 행값 중에 PYTHON 정보만 출력하세요
df.ix['2015','PYTHON']

[문제130] '2015' 행값 중에 PYTHON, R 정보 출력하세요 
df.ix['2015',['PYTHON','R']]

[문제131] 'R' 열 정보를 출력하세요.
df['R']
df.loc[:,'R']
df.ix[:,'R']

##############################################################################################

□ .at[열(인덱스 이름), 행(columns)]=값: 새로운 행 추가 
새로운 행을 추가: 2013년도 PYTHON: 70, SQL:90, R=85 추가한다.

df.at['2013','PYTHON'] = 70
df.at['2013','SQL'] = 90
df.at['2013','R'] = 85
df

#2013년도 정보 삭제
df=df.drop('2013')

#deprecated (곧 사라질 문법)
#cf. 예전 버전: .set_value(인덱스 이름,행,값)
df.set_value('2013','PYTHON',70)
df.set_value('2013','SQL',90)
df.set_value('2013','PYTHON',85)


#plsql 열을 추가해야 한다.
df.at['2013','PLSQL']=50
df.at['2014','PLSQL']=60
df.at['2015','PLSQL']=70
df.at['2016','PLSQL']=80

#삭제시: axis=0(행), axis=1(열)에 대해 신경쓰기
# axis=0 #행- 쓰지않으면 axis=0이 기본값으로 지정
df =df.drop('PLSQL',axis=1) #열 삭제



#행,열 추가 되면  밑,옆에 추가가 된다 -> 원하는 형식으로 행, 열을 정렬하기
df.at['2013','PYTHON'] = 70
df.at['2013','SQL'] = 90
df.at['2013','R'] = 85
df

df.at['2013','PLSQL']=50
df.at['2014','PLSQL']=60
df.at['2015','PLSQL']=70
df.at['2016','PLSQL']=80
df

# 원하는 행을 정렬하기
df = df.reindex(['2013','2014','2015','2016'])
df

# 열(column) 정렬하기
df = df.reindex(columns=['SQL','PLSQL','R','PYTHON'])
df

####################################################################################3
[문제132]PYTHON 점수가 80 이상 또는 SQL 점수가 90 이상인 데이터 출력하세요.
df[(df['PYTHON']>=80)|(df['SQL']>=90)]


[문제133] PYTHON 점수가 80 이상 이고 SQL 점수 90 이상인 데이터 출력하세요.
df[(df['PYTHON']>=80)&(df['SQL']>=90)]

#df[(df['PYTHON']>=80)&(df['SQL']>=70)]
####################################################################################3

□ pandas로 로드시키기
# 기존의 데이터 출력
import csv
file=open("c:/data/emp.csv",'r')
emp_csv = csv.reader(file)
next(emp_csv)

for emp_list in emp_csv:
    if emp_list[0] == "100": 
        print(emp_list[7])
 
#판다스로 데이터 로드시키기     
import pandas as pd       
emp = pd.read_csv("c:/data/emp.csv")        
emp


#데이터 정보 알아보기- 컬럼이름, 데이터 정보
emp.dtypes

#데이터 정보보기 - 전체건수, 컬럼이름, 데이터 정보, 메모리사용량
emp.info()
#cf. R에서 DATA정보를 알아보기 위해서는 str()

#100사원의 SALARY구하기
emp.ix[emp['EMPLOYEE_ID']==100, 'SALARY']
emp['SALARY'][emp['EMPLOYEE_ID']==100]


###############################################################################
[문제134] 직업이 ST_CLERK인 사원의 LAST_NAME, SALARY, JOB_ID를 출력해주세요.

emp[['LAST_NAME','SALARY','JOB_ID']][emp['JOB_ID']=="ST_CLERK"]

emp.ix[emp['JOB_ID']=="ST_CLERK",['LAST_NAME','SALARY','JOB_ID']]


###############################################################################
#student 데이터프레임만들
student = DataFrame([[60,80,70],[50,70,85],[90,80,95]],
                    index=['홍길동','박찬호','손흥민'],
                    columns=['영어','수학','국어'])
student

#데이터 추가하기
제임스 영어 100 수학 50 국어 80

student.at['제임스','영어'] = 100
student.at['제임스','수학'] = 50
student.at['제임스','국어'] = 80

student

#student_new 데이터프레임만들기
student_new = DataFrame([[60,70,80,],[50,75,85],[90,80,85]], 
                        index=['윤건','김건모','이문세'],
                        columns=['영어','수학','국어'])
student_new

# student1 데이터프레임만들기
student1 = DataFrame([[60,70,80,],[50,75,85],[90,80,85]], 
                        index=['싸이','나얼','윤상'],
                        columns=['영어','수학','국어'])

#기존 데이터프레임과 새로운 데이터프레임을 합치기
student = student.append(student_new)
student

□ pd.concat:기존 데이터프레임과 새로운 데이터프레임을 합치기
student = pd.concat([student,student1])
student

#컬럼정보, 데이터건수 확인 
student.info()
#열추가
student['과학'] = [100, 80, 90, 60, 50, 60, 70, 80, 70, 60]
student
#공통적으로 데이터 넣기(열추가)
student['한국사'] = '조선'
student
#과목만 추가하기(열만 추가)
student['음악'] = ''
student


##지우기
#열 지우기
del student['음악']
student

#축으로 지우기
student = student.drop('제임스',axis=0)
student

#열지우기 
student = student.drop('한국사',axis=1)
student

#데이터 찾기
student.ix['윤건']
student.loc['윤건']
student.xs('윤건', axis=0)
student.xs('영어') #error
student.xs('영어', axis=1)
student['영어']

#인덱스 이름 바꾸기 (딕셔너리 모양처럼 만들기)
student.rename(index={'윤상':'김상'}) #미리보기임 
student = student.rename(index={'윤상':'김상'})
student

#컬럼 이름 바꾸기
student =student.rename(columns={'과학':'물리'})
student


■ series끼리 연산하기
obj1 = Series([10,5,3,7],index=['a','b','c','d'])
obj2 = Series([2,4,6,8,10], index=['a','b','c','d','e'])

#series 사칙연산
obj1 *100

#더하기
#series 끼리 연산하기 - 인덱스 이름을 기준으로 연산한다. 
obj1 + obj2

#series 끼리 연살 할 때, 인덱스가 없는 것은 0으로 계산 작업을 하기
obj1.add(obj2, fill_value=0)

# 빼기
obj1-obj2
obj1.sub(obj2, fill_value=0)

# 곱하기
obj1*obj2
obj.mul(obj,fill_value=1)

#나누기
obj1/obj2
obj1.div(obj, fill_value=1)

■ dataframe 사칙연산: 인덱스를 기준으로 사칙연산
df1 = DataFrame(np.arange(6).reshape(2,3), 
                index=['2015','2016'], 
                columns=['python','sql','plsql'])
df1

df2 = DataFrame(np.arange(12).reshape(3,4),
                index=['2014','2015','2016'],
                columns = ['python','r','sql','plsql'])
df2

#
df1 + df2
df1.add(df2, fill_value=0)

#
df1.sub(df2, fill_value=0)

#
df1.mul(df2, fill_value=1)

#
df1.mul(df2, fill_value=1)


■ 브로드캐스팅(broadcasting): 하나의 값을 계속 중개해줌 
obj1 = np.arange(15).reshape(5,3)
obj1
obj2 = np.arange(3)
obj2


#브로드캐스팅: obj2 값은 [0,1,2]이므로 이 값이 계속 obj1의 다른 행에도 계속 돌아가면서 계산된다. 
#obj2가 obj1에 맞게 모양을 바꾼다. 
obj1 + obj2
obj1 - obj2
obj1 * obj2
obj1 / obj2


■자동으로  브로드캐스팅(broadcasting)이 안될 때 
#
obj2.repeat(5)
obj2.repeat(5).reshape(5,3)
obj2.repeat(5).reshape(3,5)
obj2.repeat(5).reshape(3,5).T

# 결과 값 같음 
obj1 + obj2.repeat(5).reshape(3,5).T
obj1 + obj2

■ 리스트 내장객체
df1 = DataFrame(np.arange(15).reshape(5,3),
                index=[str(i) for i in range(2012,2017)],
                columns = ['a','b','c'])
df1
type(df1)

#
s = df1.ix[0]
s
type(s)

# broadcasting이 여기서도 돌아감 
df1 + s

##연산작업을 할 때는 일반적으로 type을 일치시켜야 하지만 꼭 일치하지 않아도 broadcasting이 돌아가 연산이 된다. 

■ 정렬 
□ .sort_index(): 인덱스를 기준으로 오름차순 정렬 
obj = Series([2,3,5,6], index=['d','c','b','a'])
obj
obj.sort_index()
obj.sort_index(ascending=False)

□ .sort_values(): value를 기준으로 오름차순 정렬
obj.sort_values()
obj.sort_values(ascending=False)


□ dataframe정렬: sort.index() 
df = DataFrame(np.arange(8).reshape(2,4), 
               index=['two','one'],
               columns=['d','a','c','b'])
df               
#
df.sort_index()
df.sort_index(ascending=False)
df.sort_index(axis=0)
df.sort_index(axis=1) # 0: row, 1:column
df.sort_index(ascending=False, axis=1)

□ dataframe정렬: sort.values() 
# b라는 열을 기준으로 오름차순 정렬 
df.sort_values(by = 'b')

# b라는 열을 기준으로 내림차순 정렬 
df.sort_values(by = 'b', axis=0 , ascending=False)

#one이라는 행을 기준으로 열들의 내림차순 정렬
df.sort_values(by = 'one', axis=1 , ascending=False)




# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 09:40:05 2018

@author: stu
"""
###############################################################################################################
[문제134] emp.csv 파일의 데이터를 판다스를 이용해서 읽어 들인 후 급여가 10000 이상인 사원들의 이름, 급여, 입사일을 출력해주세요.

import pandas as pd

emp = pd.read_csv("c:/data/emp.csv")
emp.head()
emp.tail(10)
emp.info()

#답1
emp[['LAST_NAME','SALARY', 'HIRE_DATE']][emp['SALARY']>=10000]

#답2 
emp.ix[emp['SALARY']>=10000, ['LAST_NAME', 'SALARY', 'HIRE_DATE']] #보편적으로 없어질 method 

#답3
emp.loc[emp['SALARY']>=10000, ['LAST_NAME', 'SALARY', 'HIRE_DATE']]


[문제135] 급여 10000 이상인 사원들의 이름과 급여, 입사일를 출력하세요. 급여를 기준으로 내림차순하세요.

#답1
emp[['LAST_NAME','SALARY', 'HIRE_DATE']][emp['SALARY']>=10000].sort_values(by='SALARY', ascending=False)

#답2
emp.ix[emp['SALARY']>=10000, ['LAST_NAME', 'SALARY', 'HIRE_DATE']].sort_values(by='SALARY', ascending=False)

#답3
emp.loc[emp['SALARY']>=10000, ['LAST_NAME', 'SALARY', 'HIRE_DATE']].sort_values(by='SALARY', ascending=False)

# sort_values(by=['SALARY', 'HIRE_DATE'])와 같이 sort.vlaue에 해당하는 열은 리스트 모양으로 여러개 넣을 수 있다. 
# emp.loc[emp['SALARY']>=10000, ['LAST_NAME', 'SALARY', 'HIRE_DATE']].sort_values(by=['SALARY', 'HIRE_DATE'], ascending=False)


###############################################################################################################

obj = Series([78, 88, 92, 79, 67, 91, 70, 86, 90, 90])

#값을 기준으로 오름차순 정렬
obj.sort_values()

#값을 기준으로 내림차순 정렬
obj.sort_values(ascending=False)

#rank 구하기  (cf. sql의 분석함수 같이 공부하기)
#동일한 순위일 경우 일 경우 평균값으로 할지, 최소값으로 할지, 최대값으로 할지 결정할 수 잇다. 
# 오름차순 순위: eg. 67이 있는 위치(4)에 1로 표기됨, 78이 있는 위치(6)에 2로 표기됨
# 기본값: 동일한 순위일 경우 일 경우 평균값으로 표현
obj.rank() 

obj.rank(ascending=False)

#동일값일 때 평균으로 출력함 (기본값)
obj.rank(ascending=False, method='average')

#최소값인 동일한 순위로 나옴 (4등은 없음)
obj.rank(ascending=False, method='min')

#최대값인 동일한 순위로 나옴 (3등은 없음)
obj.rank(ascending=False, method='max')

#동일한 동률일 경우 index가 앞을 경우 먼저 순위를 줌 (e.g.90점이 8인덱스를 가진 경우 3위, 9인덱스를 가진경우 4위)
obj.rank(ascending=False, method='first')


#sql의 기존의 rank와 같음(e.g, 1,2,3,3,5 로 표현)
obj.rank(ascending=False, method='min')


#sql의 dense_rank와 같음: 연이은 정수로 표현(e.g., 1,2,3,3,4... 로 표현)
obj.rank(ascending=False, method='dense')

#series를 하나의 열로 들어가고, 순위도 하나의 열로 들어가 dataframe으로 만들기
obj1= DataFrame({'순위':obj.rank(ascending=False, method='dense'),
            '점수':obj})

#순위로 정렬하기
obj1.sort_values(by='순위')


import numpy as np
#NaN값 만들기 
obj2 = Series([70,60,80,np.nan,90])
obj2

#정렬을 하면 오름차순, 내림차순 모두 null값이 맨 뒤에 출력된다.
obj2.sort_values()
obj2.sort_values(ascending=False)
#cf. sql의 null값은 -> 오름차순: 제일 밑에/ 내림차순: 제일 위에


#NaN값을 제일 앞으로
obj2.sort_values(ascending=False, na_position='first')

#NaN값을 제일 뒤로
obj2.sort_values(ascending=False, na_position='last')


# NaN은 순위를 적용해도 무시됨 
obj2.rank()
obj2.rank(ascending=False)
#NaN값이 순위를 적용해도 무시됨: 기본값 na_option='keep'
obj2.rank(na_option='keep')
#na_option='top': NaN값이 1등으로 출력됨 
obj2.rank(na_option='top')
obj2.rank(ascending=False, na_option='top')
#na_option='bottom': NaN값이 꼴등으로 출력됨 
obj2.rank(na_option='bottom')
obj2.rank(ascending=False, na_option='bottom')



#
df = DataFrame({'영어':[60,80,70], '수학':[50,72,86]},
                index=['홍길동','박찬호','손흥민'])
df
#수학을 기준으로 정렬
df.sort_values(by='수학')
df.sort_values(by='수학', ascending=False)
#수학 데이터만 보기 
df['수학'].sort_values(ascending=False)
# rank 구하기 (과목별로 순위값이 자동으로 만들어짐)
 df.rank(ascending=False)
# 각 학생이 잘하는 과목에 대해 rank를 해줌  (axis=1 열이기 때문에 영어, 수학을 두 기준으로 순위를 구함)
df.rank(ascending=False, axis=1)
#영어에 대한 rank보기
df['영어'].rank(ascending=False)
# 홍길동에 대한 rank만 보기
df.ix['홍길동'].rank(ascending=False)


########################################################################################
[문제136] 급여를 많이 받는 순으로 10위 까지를 구하세요. 


import pandas as pd
emp.info()
emp = pd.read_csv("c:/data/emp.csv")
emp['SALARY'].rank(ascending=False, method='min').sort_values()[0:10]

DataFrame({'사원명':emp['LAST_NAME'], 
               '급여':emp['SALARY'],
               '순위':emp['SALARY'].rank(ascending=False, method='min')}).sort_values(by='순위')[0:10]

#좀 더 생각해보기 
s=DataFrame({'사원명':emp['LAST_NAME'],
           '급여':emp['SALARY'],
           '순위':emp['SALARY'].rank(ascending=False, method='dense')})
s.sort_values(by='순위')


#쌤답
emp[emp['SALARY'].rank(ascending=False, method='dense')<=10][['EMPLOYEE_ID', 'LAST_NAME', 'SALARY']]    
또는 

emp['rank'] = emp['SALARY'].rank(ascending=False, method='dense')
emp[emp['rank']<=10].sort_values('rank')
########################################################################################

□ pandas에서의 in 연산자

df = DataFrame({'영어':[60,80,70], '수학':[50,72,86]},
                index=['홍길동','박찬호','손흥민'])
df

# in 연산자: 이 조건의 값을 출력
df[df['수학'].isin([72,86])] #행을 제한하는 부분

# ~: not in 연산자의 의미로, 이 조건의 반대를 의미
df[~df['수학'].isin([72,86])]


########################################################################################
[문제137] 직업이 AD_VP, AD_PRES 인 사원들의 이름, 급여, 직업을 출력하세요.

import pandas as pd
emp.info()
emp = pd.read_csv("c:/data/emp.csv")

emp[emp['JOB_ID'].isin(['AD_VP','AD_PRES'])][['LAST_NAME','SALARY','JOB_ID']] #제한을 먼저 한 다음, 열을 가져옴 

emp[['LAST_NAME','SALARY','JOB_ID']] [emp['JOB_ID'].isin(['AD_VP','AD_PRES'])]



[문제138] 직업이 AD_VP ,AD_PRES 아닌 사원들의 이름, 급여, 직업을 출력하세요.
import pandas as pd
emp.info()
emp = pd.read_csv("c:/data/emp.csv")
emp[~emp['JOB_ID'].isin(['AD_VP','AD_PRES'])][['LAST_NAME','SALARY','JOB_ID']]

emp[['LAST_NAME','SALARY','JOB_ID']][~emp['JOB_ID'].isin(['AD_VP','AD_PRES'])]
########################################################################################

# NaN을 넣는 방법 
obj = Series([1,2,3,None,5])
obj

import numpy as np
obj = Series([1,2,3,np.nan,5])
obj

from numpy import nan as NA
obj = Series([1,2,3,NA, 5])
obj


#NaN에 0으로 채우기
obj.fillna(0) #미리보기임 (적용은 아님)

#NaN이 값을 True로 출력
obj.isnull()

#NaN이 값을 True로 출력 by Pandas
pd.isnull(obj)

#NaN 아닌 값을 True로 출력
obj.notnull()

#NaN값만 출력하기
obj[obj.isnull()]

#NaN아닌 값만 출력하기
obj[obj.notnull()]
obj.dropna()


# (from numpy import nan as NA로 만들어 놨기 때문에 NA사용 가능)
df = DataFrame([[1,2,3],[1,None,NA],[NA,NA,NA],[NA,2,3]])
df
#NaN이 하나라도 있으면 제외가 됨 
df.dropna()
df.dropna(how='all')
df.dropna(how='all', axis=0)  #0은 행을 기준
df.dropna(how='all', axis=1)  #1은 열을 기준
df.dropna(axis=0)
df.dropna(axis=1)

df[4] = NA
df.dropna(how='all', axis=1)


#NaN을 0으로 채움 
df.fillna(0)

#0번 열에만 0을 채움
df[0].fillna(0)

#1번 컬럼에는 0을, 1번 컬럼에는 1, 2번 컬럼에는 2, 4번컬럼에는 4를 채우고자 함
df.fillna({0:0, 1:1, 2:2, 4:4})

# NaN을 0으로 채우는 것이 적용됨
df.fillna(0, inplace=True)
df

#앞에 있는 내용으로 NaN를 채움
df.fillna(method='ffill')
df.fillna(method='pad')

#뒤에 있는 내용으로 NaN을 채움
df.fillna(method='bfill')
df.fillna(method='backfill')

########################################################################################
[문제139] 커미션이 null인 사원의 이름, 커미션을 출력하세요.
import pandas as pd
emp = pd.read_csv("c:/data/emp.csv")

#답1
emp[['LAST_NAME','COMMISSION_PCT']][emp['COMMISSION_PCT'].isnull()]

#답2
emp[emp['COMMISSION_PCT'].isnull()][['LAST_NAME','COMMISSION_PCT']]

#답3
emp.ix[emp['COMMISSION_PCT'].isnull(),['LAST_NAME','COMMISSION_PCT']]

#답4
emp.loc[emp['COMMISSION_PCT'].isnull(),['LAST_NAME','COMMISSION_PCT']]

[문제140] 커미션이 null아닌 사원의 이름, 커미션을 출력하세요.
import pandas as pd
emp = pd.read_csv("c:/data/emp.csv")
#답1
emp[['LAST_NAME','COMMISSION_PCT']][emp['COMMISSION_PCT'].notnull()]

#답2
emp[emp['COMMISSION_PCT'].notnull()][['LAST_NAME','COMMISSION_PCT']]

#답3
emp.ix[emp['COMMISSION_PCT'].notnull(),['LAST_NAME','COMMISSION_PCT']]

#답4
emp.loc[emp['COMMISSION_PCT'].notnull(),['LAST_NAME','COMMISSION_PCT']]
########################################################################################
▣ apply 함수
- apply함수는 행, 열값을 인수값으로 받아서 반복하여 그 함수를 적용한다. 

#series
s1 = Series([1,2,3])

def square(x):
    return x**2

#함수사용 
square(s1)
#error
s1.square()
#apply사용
s1.apply(square)
#lambda 사용
s1.apply(lambda x:x**2)


#dataframe
df = DataFrame([[1,2,3],[4,5,6]])
df
df.apply(square)
df.apply(square, axis=0)
df.apply(square, axis=1)

#행을 기준으로 열을 합함
df.apply(sum, axis=0)
#열을 기준으로 행을 합함
df.apply(sum, axis=1)
#
df.apply(lambda x:x**2)




########################################################################################
[문제141] last_name 첫글자가 S로 시작되는 사원들의 last_name을 출력하세요.

#답1
def ini(x):
    for i in range(len(x)):
        if x[i][0]=='S':
            print(x[i])

ini(emp['LAST_NAME'])

#답2
emp[emp['LAST_NAME'].apply(lambda x:x[0]=='S')]['LAST_NAME']

#답3
def start(x):
    for i in range(len(x)):
        if x[i].startswith('S'):
            print(x[i])
            
start(emp['LAST_NAME'])


#쌤답
def first_character(w):
    if w[0] == 'S':
        return True
    return False

emp['LAST_NAME'][emp['LAST_NAME'].apply(first_character)]
emp[emp['LAST_NAME'].apply(first_character)]['LAST_NAME']
emp.ix[emp['LAST_NAME'].apply(first_character),'LAST_NAME']

emp.ix[emp['LAST_NAME'].apply(lambda x:x[0]=='S'),'LAST_NAME']
emp.ix[emp['LAST_NAME'].apply(lambda x:x[0])=='S','LAST_NAME']
emp.ix[emp['LAST_NAME'].apply(lambda x:x.startswith('S')),'LAST_NAME']


[문제142] last_name g로 끝나는 사원들의 이름, 급여 출력하세요.
#답1
def last(x, y):
    for i in range(len(x)):
        if x[i][-1] == 'g':
            print(x[i],y[i])
            
last(emp['LAST_NAME'],emp['SALARY'])     
       
#답2
def last_character(w):
    if w[-1] == 'g':
        return True
    return False

emp[['LAST_NAME','SALARY']][emp['LAST_NAME'].apply(last_character)]

#답3
emp.ix[emp['LAST_NAME'].apply(lambda x:x[-1]=='g'),['LAST_NAME','SALARY']]
#답4
emp.ix[emp['LAST_NAME'].apply(lambda x:x.endswith('g')),['LAST_NAME','SALARY']]


[문제143] 110번 사원의 급여보다 많이 받는 사원들의 이름, 급여를 출력하세요.
#일반적인 data인 scalar형식에서 가져왔다면 문제가 되지 않지만, dataframe은 series형식으로 가져오기 때문에 이 부분을 고려해야하는 문제이다. 
import pandas as pd
emp = pd.read_csv("c:/data/emp.csv")
emp.info()

#답1
emp101 = emp['SALARY'][emp['EMPLOYEE_ID']==110]
emp[['LAST_NAME','SALARY']][emp['SALARY']> int(emp101)]

#답2
emp[['LAST_NAME','SALARY']][emp['SALARY']>int(emp['SALARY'][emp['EMPLOYEE_ID']==110])]

#쌤답 
-int를 함수를 이용하면 scalar 값으로 return함
-v_110.values[0]을 사용하면 값을 추출함 

v_110 = emp[emp['EMPLOYEE_ID']==110]['SALARY']
type(v_110)
emp[emp['SALARY'] > int(v_110)][['LAST_NAME','SALARY']]
emp[emp['SALARY'] > v_110.values[0]][['LAST_NAME','SALARY']]


[문제144] 관리자 사원의 이름, 입사일, 급여를 출력하세요.
#답1
emp[['LAST_NAME','HIRE_DATE','SALARY']][emp['EMPLOYEE_ID'].isin(emp['MANAGER_ID'])]

#답2
file = open("c:/data/emp.csv",'r')
emp_csv = csv.reader(file)
next(emp_csv)
manager_id=[]
for emp_list in emp_csv: 
    manager_id.append(emp_list[-2])
print(set(manager_id))
file.close()  

file = open("c:/data/emp.csv",'r')
emp_csv = csv.reader(file)
next(emp_csv)
for emp_list in emp_csv:
    if emp_list[0] in manager_id:
        print(emp_list[2], emp_list[5], emp_list[7])
file.close()  

#답3 #유일값만 넣기 위해 
file = open("c:/data/emp.csv",'r')
emp_csv = csv.reader(file)
next(emp_csv)
v_mgr = []
for emp_list in emp_csv:
    if (not emp_list[9] in v_mgr) & (emp_list[9] != ''):
        v_mgr.append(emp_list[9])
print(len(v_mgr))
file.close()

file = open("c:/data/emp.csv",'r')
emp_csv = csv.reader(file)
next(emp_csv)
for emp_list in emp_csv:
    for mgr in v_mgr:
        if emp_list[0]==mgr:
            print(emp_list[2], emp_list[5], emp_list[7])
file.close()


 
 # -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 09:45:21 2018

@author: stu
"""

#################################################################################################
[문제145] 101번 사원의 관리자 이름, 입사일, 급여정보를 출력하세요.
1. pandas를 이용해서 해결

import pandas as pd
emp = pd.read_csv('c:/data/emp.csv')
emp[['LAST_NAME','HIRE_DATE','SALARY']][emp['EMPLOYEE_ID'].isin(emp['MANAGER_ID'][emp['EMPLOYEE_ID']==101])]

# 쌤답
import pandas as pd
emp = pd.read_csv('c:/data/emp.csv')
mgr =emp[emp['EMPLOYEE_ID']==101]['MANAGER_ID']
emp[emp['EMPLOYEE_ID']==mgr.values[0]][['LAST_NAME','HIRE_DATE', 'SALARY']]
emp[emp['EMPLOYEE_ID']==int(mgr)][['LAST_NAME','HIRE_DATE', 'SALARY']]

2. 일반적으로 csv 파일을 읽어서 해결

import csv
file = open('c:/data/emp.csv','r')
emp_csv =csv.reader(file)
next(emp_csv)
for emp_list in emp_csv:
    if emp_list[0]=='101':
       manager_id = emp_list[-2]
file.close()
        
file = open('c:/data/emp.csv','r')
emp_csv = csv.reader(file)
next(emp_csv)
for emp_list in emp_csv:
    if emp_list[0] == manager_id:
        print(emp_list[2], emp_list[5], emp_list[7])
file.close()        



#쌤답
import csv
file = open('c:/data/emp.csv','r')
emp_csv =csv.reader(file)
next(emp_csv)
v_mgr = []
for emp_list in emp_csv:
    if emp_list[0] == '101':  #sql문장시 full scan유발 ->  filter 술어 체크 : index가 중요함 
        v_mgr.append(emp_list[9])
file.close()

#filter 술어: 어느 위치에 문장이 있는지 모르기 때문에 모두 스캔 해야함 -> full scan유발 
#aceess술어: rawid를 알고 어느 위치에 있는지 찾아가는 형태의 scan -> 

import csv
file = open('c:/data/emp.csv','r')
emp_csv =csv.reader(file)
next(emp_csv)
for emp_list in emp_csv:
    if emp_list[0] == v_mgr[0]:  #list 변수이기 대문에 v_mgr[0]으로 표시
        print(emp_list[2], emp_list[5], emp_list[7])
file.close()


#################################################################################################

■ pandas에서 그룹함수 적용

import numpy as np

from pandas import Series, DataFrame

s = Series([2, 4, 8, np.nan, 6])

s.sum()
s.sum(skipna=True)
s.sum(skipna=False)


# skipna= True가 돌아가고 있음 
s.mean()
s.var()   #표본집단인기 때문에 n-1로 나눔
s.std()
s.max()
s.min()
#누적의 합 
s.cumsum()  
#최소값의 인덱스
s.idxmin()
s[s.idxmin()]
#최대값의 인덱스
s.idxmax()
s[s.idxmax()]


s = Series([2, 4, 8, np.nan, 6, 8, 2]) #최소값 2개, 최대값 2개
# 최소값이 2개 이지만 최소값의 처음 값의 인덱스만 return, 뒤의 인덱스는 return하지 않음
s.idxmin()

# 최대값이 2개 이지만 최대값의 처음 값의 인덱스만 return, 뒤의 인덱스는 return하지 않음
s.idxmax()

# 최소값, 최대값 인덱스 모두 구하기 
s[s==s.min()]
s[s==s.max()]

#인덱스만 보겠음
s[s==s.min()].index
#value값만 보겠음 -> array형으로 나옴 
s[s==s.min()].values

#4분위수를 포함하여 요약
s.describe()
#NaN을 포함하지 않은 갯수가 나옴
s.count()
#NaN을 포함하여 갯수가 나옴 
len(s)

#
df = DataFrame([[60,80,70],[50,75,83],[90,83,81]],
               index=['홍길동', '박찬호', '손흥민'],
               columns=['영어','수학','국어'])
df
#과목별로 sum이 됨: axis= 0
df.sum()
# 행단위로 sum
df.sum(axis=0)
df.sum(axis='rows')
#열단위로 sum
df.sum(axis=1)
df.sum(axis='columns')

#
df.mean()
df.mean(axis=1)

# df의 dataframe에 한 행을 추가하기 
제임스 영어: 100, 수학: np.nan, 국어:90
df.at['제임스','영어']= 100
df.at['제임스', '수학']=np.nan
df.at['제임스', '국어'] = 90

#
df.sum()
df.mean()
df.mean(skipna=False)
df.mean(axis=1, skipna=False)

#
df.idxmin()
df.idxmax()
df.cumsum()

#
df['영어'].sum()
df['영어'].mean()
df['영어'].var()
df['영어'].std()
df['영어'].max()
df['영어'].min()
# 홍길동 학생의 점수 합
df.loc['홍길동'].sum()
# 데이터 요약 
df.describe()


#################################################################################################

[문제146] 최고 급여, 최저 급여 출력하세요.

#pandas이용
import numpy as np
from pandas import Series, DataFrame

print(emp['SALARY'].max())
print(emp['SALARY'].min())

#import csv 사용 -최대값 
import csv
file = open('c:/data/emp.csv','r')
emp_csv = csv.reader(file)
next(emp_csv)
max_sal = 0
for emp_list in emp_csv:
    if int(emp_list[7]) > max_sal:
            max_sal = int(emp_list[7])
print(max_sal)
   
#import csv 사용 -최소값 
import csv
file = open('c:/data/emp.csv','r')
emp_csv = csv.reader(file)
next(emp_csv)
min_sal = 1000000000  #고민해보기 
for emp_list in emp_csv:
    if int(emp_list[7]) < min_sal:
            min_sal = int(emp_list[7])
print(min_sal)

#
import csv
file = open('c:/data/emp.csv','r')
emp_csv = csv.reader(file)
next(emp_csv)
for emp_list in emp_csv:
    for i in range(len(emp_list)):
        print(emp_list[i][7]]])
    
    if int(emp_list[7]) < min_sal:
            min_sal = int(emp_list[7])
print(min_sal)


#
import csv

file = open("c:/data/emp.csv","r")
emp_csv = csv.reader(file)
next(emp_csv)
sal_max, sal_min = next(emp_csv)[7], next(emp_csv)[7]
print(sal_max)
print(sal_min)
for emp_list in emp_csv:
    if int(emp_list[7]) >= sal_max:
        sal_max = int(emp_list[7])
    if int(emp_list[7]) <= sal_min:
        sal_min = int(emp_list[7])
print("최고 급여 : {}, 최저 급여 : {}".format(sal_max,sal_min))

file.close()
#
import csv
sal_max, sal_min = int(next(emp_csv)[7]), int(next(emp_csv)[7])
file = open("c:/data/emp.csv","r")
emp_csv = csv.reader(file)
next(emp_csv)

for emp_list in emp_csv:
    if int(emp_list[7]) >= sal_max:
        sal_max = int(emp_list[7])
    if int(emp_list[7]) <= sal_min:
        sal_min = int(emp_list[7])
print("최고 급여 : {}, 최저 급여 : {}".format(sal_max,sal_min))



     
#쌤답-최대값 
import csv
file = open('c:/data/emp.csv','r')
emp_csv = csv.reader(file)
next(emp_csv)
sal = 0
for emp_list in emp_csv:
    if int(emp_list[7]) > int(sal):
        sal = emp_list[7]
print(sal)

#쌤답-최소값 
import csv
file = open('c:/data/emp.csv','r')
emp_csv = csv.reader(file)
next(emp_csv)
sal = 10000000000
for emp_list in emp_csv:
    if int(emp_list[7]) < int(sal):
        sal = emp_list[7]
print(sal)

#참고 
import csv
file = open('c:/data/emp.csv','r')
emp_csv = csv.reader(file)
next(emp_csv)
sal = []
for emp_list in emp_csv:
    sal.append(int(emp_list[7]))
print(max(sal))  
print(min(sal))
# max, min은 python에 있는 내장객체 



[문제147] 20번 부서 사원들의 급여 합을 구하세요.

#pandas이용
import numpy as np
from pandas import Series, DataFrame
emp['SALARY'][emp['DEPARTMENT_ID']==20].sum()

#import csv 파일 
import csv
file = open('c:/data/emp.csv','r')
emp_csv = csv.reader(file)
next(emp_csv)
sal = 0
for emp_list in emp_csv:
    if emp_list[10]=='20':
        sal += int(emp_list[7])
print(sal)


# emp_new 파일 
import pandas as pd
emp = pd.read_csv('c:/data/emp_new.csv', names=['empid','name','job','mgr','hire_date','sal','comm','deptno'])
print(emp['sal'][emp['deptno']==20].sum())


import csv
file = open('c:/data/emp_new.csv','r')
emp_csv = csv.reader(file)
sal = 0
for emp_list in emp_csv:
    if emp_list[7]=='20':
        sal += float(emp_list[5])
print(sal)


[문제148] 부서번호를 입력하면 그 부서의 급여 총액을 구하는 함수를 생성하세요.

dept_sum_sal()

부서번호를 입력하세요 :  20

19000.0


dept_sum_sal()

부서번호를 입력하세요 :  30

24900.0


import numpy as np
from pandas import Series, DataFrame

# 답
def dept_sum_sal():
    x=int(input('부서번호를 입력하세요 : '))
    print(emp['SALARY'][emp['DEPARTMENT_ID']==x].sum())
dept_sum_sal()

#쌤답1
def dept_sum_sal():
    emp=pd.read_csv('c:/data/emp_new.csv',names=['empid','name','job','mgr','hire_date','sal','comm','deptno'])
    id = input('부서를 입력하세요: ' )
    print(emp.loc[emp['deptno']==int(id),'sal'].sum())
dept_sum_sal()

#쌤답2
def dept_sum_sal():
    import csv
    file = open('c:/data/emp_new.csv','r')
    emp_csv = csv.reader(file)
    sal = 0
    id = input('부서번호를 입력하세요 : ')
    for emp_list in emp_csv:
        if emp_list[7] == id:
            sal += int(emp_list[5])
    print(sal)
    file.close()
    
dept_sum_sal()

[문제149] 직업을 물어보게하고 직업을 입력하면 해당 직업의 최고 급여를 출력되게하는데 아무것도 입력하지 않으면 계속 물어보게하는
프로그램을 작성하세요.

job_max_sal()

직업을 입력하세요 ?  ST_CLERK
3600.0

job_max_sal()

직업을 입력하세요 ? sa_rep
11500.0

job_max_sal()

직업을 입력하세요 ? 

직업을 입력하세요 ? 

직업을 입력하세요 ? 

job_max_sal()

직업을 입력하세요 ? sales
해당 직업의 사원은 없습니다.

import pandas as pd
emp=pd.read_csv('c:/data/emp.csv')
job = input("직업을 입력하세요 ? ")
if 'job.upper()' in (emp['JOB_ID']):
    print(max(emp['SALARY'][emp['JOB_ID']=='job.upper']))
elif 'job.upper()' not in (emp['JOB_ID']):
    print('해당 직업의 사원은 없습니다.)
elif 'job' = '':
    print("직업을 입력하세요?")

while jo
    print("직업을 입력하세요?") 
    

import pandas as pd
emp=pd.read_csv('c:/data/emp.csv')
max(emp['SALARY'][emp['JOB_ID']=='ST_CLERK'])

import pandas as pd
emp=pd.read_csv('c:/data/emp.csv')
emp['JOB_ID']

if ST_CLEKR in emp['JOB_ID']:
    print('ST_')

# try -except: 한 쌍 -> excetpion 처리
# user define  -> raise 문 
#쌤답1
import pandas as pd 
def job_max_sal():
    try:
        emp =pd.read_csv('c:/data/emp_new.csv',names=['empid','name','job','mgr','hire_date','sal','comm','deptno'])
        name = ''
        while name =='':
            name = input('직업을 입력하세요? ' )
        maxsal = emp['sal'][emp['job']==name.upper()].max()
        if pd.isnull(maxsal):   #pd의 null값 검출 
            raise Exception
        return maxsal
    except Exception as err:
        print('해당 직업의 사원은 없습니다.')

job_max_sal()

#쌤답2
def job_max_sal():
    try:
        import  csv
        file = open("c:\data\emp_new.csv",'r')
        emp_csv = csv.reader(file)
        name = ''
        sal = []
        while name =='':
            name = input('직업을 입력하세요 ? ')
        
        for emp_list in emp_csv:
            if emp_list[2] == name.upper():
                sal.append(int(emp_list[5]))
        maxsal = max(sal)
        if maxsal=='':   #null값 검출 
            raise Exception
        return maxsal
    except Exception as err:
        print ('해당 직업의 사원은 없습니다.')

job_max_sal()




[문제150]부서번호,급여를 기준으로 내림차순 정렬해서 아래 화면처럼 컬럼정보를 출력하세요.


     deptno  empid         name      sal
105   110.0    205      Higgins  12008.0
106   110.0    206        Gietz   8300.0
8     100.0    108    Greenberg  13208.8
9     100.0    109       Faviet   9900.0
10    100.0    110         Chen   8200.0
12    100.0    112        Urman   7800.0
11    100.0    111      Sciarra   7700.0
13    100.0    113         Popp   6900.0

#답
import pandas as pd 
emp =pd.read_csv('c:/data/emp_new.csv',names=['empid','name','job','mgr','hire_date','sal','comm','deptno'])
emp[['deptno','empid','name','sal']].sort_values(by=['deptno', 'sal'], ascending=False)


[문제151] index 번호 0부터 50까지 부서번호, 급여를 기준으로 내림차순 정렬한 후 아래결과처럼 출력하세요.


    deptno  empid         name      sal
8    100.0    108    Greenberg  13208.8
9    100.0    109       Faviet   9900.0
10   100.0    110         Chen   8200.0
12   100.0    112        Urman   7800.0
11   100.0    111      Sciarra   7700.0
13   100.0    113         Popp   6900.0

#답 
import pandas as pd 
emp =pd.read_csv('c:/data/emp_new.csv',names=['empid','name','job','mgr','hire_date','sal','comm','deptno'])
print(emp.ix[0:50][['deptno','empid','name','sal']].sort_values(by=['deptno', 'sal'], ascending=False))
#emp.ix[0:50] 행제한 


[문제152] 50번 부서 사원들의 정보를 급여를 기준으로 내림차순 정렬해서 해서 아래 화면처럼 컬럼정보를 출력하세요.

   empid         name  deptno     sal
21    121        Fripp    50.0  8200.0
20    120        Weiss    50.0  8000.0
22    122     Kaufling    50.0  7900.0
23    123      Vollman    50.0  6500.0
24    124      Mourgos    50.0  5800.0
84    184     Sarchand    50.0  4200.0


#답
import pandas as pd
emp = pd.read_csv("c:\data\emp_new.csv", names = ['empid','name','job','mgr','hire_date','sal','comm','deptno'])
print(emp[emp[['deptno','empid','name','sal']]["deptno"]==50].sort_values(by=['deptno','sal'],ascending=False))



[문제153] 10,20,30,40,50번 부서 사원들의 급여의 총액을 출력하세요.

<화면출력>

10 4400.0
20 19000.0
30 24900.0
40 6500.0
50 156400.0

import pandas as pd 
emp =pd.read_csv('c:/data/emp_new.csv',names=['empid','name','job','mgr','hire_date','sal','comm','deptno'])
for i in [10,20,30,40,50]:
    print (i, emp.loc[emp['deptno']==i, 'sal'].sum())
#emp.loc    


[문제154] s 변수에 값들 중에 unique한 값만 s_uniuqe변수에 넣어주세요.
s = [1,2,3,4,1,2,3,4,5,1,2,3,4,5,6,'']

#답
s_unique = []
for i in s:
    if i not in s_unique:
        s_unique.append(i)
    elif i in (s_unique):
        pass
print(s_unique)

#쌤답
s_unique = []
for s_list in s:
    if not s_list in s_unique:
        s_unique.append(s_list)
print(s_uniuqe)



# null값을 제외하기 
s_unique = []
for s_list in s:
    if (not s_list in s_unique) and (s_list != ''):
        s_unique.append(s_list)
print(s_unique)


s 변수에 값들의 빈도수 구해주세요.  #dictionary 형 생각하기 

s = [1,2,3,4,1,2,3,4,5,1,2,3,4,5,6,'']

freq = {}
for i in s:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
print(freq)

#null 빼기
freq = {}
for i in s:
    if i in freq:
        freq[i] += 1
    else:
        if i != '':
            freq[i] = 1
print(freq)

########################################################################################################

import numpy as np
from pandas import Series,DataFrame
s = Series([1,2,3,4,1,2,3,4,5,1,2,3,4,5,6,np.nan])

#Series에서 유일값 출력하기
#unique(): series에서 유일값 뽑기 
ss = s.unique()
ss
#자료형이 array인되서  dropna로 nan값을 지울 수 없음 
ss.dropna()
#NaN 지우기 - data유형을 series로 바꿔서 만들어 주면 dropna를 사용할 수 있음
ss= Series(s.unique())
ss.dropna()

#값이 인덱스가 되고, 건수가 형성됨(sort를 통해 인덱스를 정렬할 수 있음)
s.value_counts()
s.value_counts(sort=True)
s.value_counts(sort=False)

#기술통계값으로 상대비율(값이 전체중에 몇 프로인지 출력함)
s.value_counts(normalize=True)

#dictionary값에 대해 상대 비율을 출력하기 
freq = {}
for i in s:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
print(freq)

t = len(s)
for k,v in freq.items():
    print(k,v/t)


# null 값 뺀 dictionary 값에 대해 상대비율을 출력하기
freq = {}
for i in s:
    if i in freq:
        freq[i] += 1
    else:
        if i != '':
            freq[i] = 1
print(freq)

t = len(s)
for k,v in freq.items():
    print(k,v/(t-1))

#dataframe에서 유일값 출력하기
df = DataFrame({'a':['a1','a1','a1','a2','a2','a2','a3'],
                'b':['b1','b1','b1','b2','b2','b3',np.nan]})

#유일값 출력하기(nan도 출력)
df['a'].unique()
df['b'].unique()
#유일값 출력하기(nan빼고 출력)
ddf=Series(df['b'].unique())
ddf.dropna()

#빈도수 체크하기(null값이 빠짐)
df['a'].value_counts()
df['b'].value_counts()
df['b'].value_counts(dropna=True) #기본값 
df['b'].value_counts(dropna=False) 

#################################################################################################
[문제155] 부서별로 급여 총액을 출력하세요.

<화면 출력>

10 4400.0
20 19000.0
30 24900.0
40 6500.0
50 156400.0
60 28800.0
70 10000.0
80 304500.0
90 58000.0
100 53708.8
110 20308.0


#nan값 포함하지 않음 
import pandas as pd 
emp =pd.read_csv('c:/data/emp_new.csv',names=['empid','name','job','mgr','hire_date','sal','comm','deptno'])
emp_deptno=Series(emp['deptno'].unique())
dept = emp_deptno.dropna().sort_values()
for i in dept:
    print (int(i), emp.loc[emp['deptno']==i, 'sal'].sum())

#
import pandas as pd 
emp =pd.read_csv('c:/data/emp_new.csv',names=['empid','name','job','mgr','hire_date','sal','comm','deptno'])
emp_deptno=Series(emp['deptno'].unique())
dept = emp_deptno.dropna()
for i in dept.sort_values():
    print (int(i), emp.loc[emp['deptno']==i, 'sal'].sum())
    
#쌤답
import pandas as pd 
emp =pd.read_csv('c:/data/emp_new.csv',names=['empid','name','job','mgr','hire_date','sal','comm','deptno'])

deptno_unique = Series(emp['deptno'].unique())
deptno_unique = deptno_unique.dropna()

for i in deptno_unique.sort_values():
    print(int(i), emp.loc[emp['deptno']==i,'sal'].sum())



# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 09:47:35 2018

@author: stu
"""
###############################################################################

[문제156]부서별로 급여 총액을 출력하세요.

<화면 출력>

10 4400.0
20 19000.0
30 24900.0
40 6500.0
50 156400.0
60 28800.0
70 10000.0
80 304500.0
90 58000.0
100 53708.8
110 20308.0
nan 7000.0

# pandas에서 제공하는 isnull() 생각해서 풀기!

import pandas as pd
import numpy as np
from pandas import Series,DataFrame

emp = pd.read_csv("c:/data/emp.csv")
deptno = Series(emp['DEPARTMENT_ID'].unique())
deptno=deptno.sort_values()
deptno
for i in deptno:
    if pd.isnull(i):
        print(i, emp.loc[emp['DEPARTMENT_ID'].isnull(), 'SALARY'].sum())
    else:
        print (int(i), emp.loc[emp['DEPARTMENT_ID']==i, 'SALARY'].sum())



###############################################################################
   
▣ pandas      
■ groupby: pandas에서 grouping을 통한 집계값 구하기 

import pandas as pd
import numpy as np
from pandas import Series,DataFrame
import pandas as pd 
emp =pd.read_csv('c:/data/emp_new.csv',names=['empid','name','job','mgr','hire_date','sal','comm','deptno'])

# sql select 문
select deptno,sum(al)
from emp
group by deptno

# groupby 를 통한 함수
emp['sal'].groupby(emp['deptno']).sum()
emp['sal'].groupby(emp['deptno']).mean()
emp['sal'].groupby(emp['deptno']).var()
emp['sal'].groupby(emp['deptno']).std()
emp['sal'].groupby(emp['deptno']).count()
emp['sal'].groupby(emp['deptno']).max()
emp['sal'].groupby(emp['deptno']).min()

#grouping만 적용
deptno_group = emp['sal'].groupby(emp['deptno'])
#객체정보만 보여줌 
deptno_group
#
deptno_group.sum()
deptno_group.mean()

# 동일한 부서 안에서도 job이 다른 사원들의 결과값을 정리해줌 
#sql select문장
select deptno, job, sum(sal)
from emp
group by deptno, job
#pandas의 groupby사용 
emp['sal'].groupby([emp['deptno'], emp['job']]).sum()

dept_group = emp['sal'].groupby([emp['deptno'], emp['job']])
dept_group.sum()
dept_mean = dept_group.mean()
dept_mean

#unstack(): corsstable 모양으로 결과값이 출력됨
dept_mean.unstack()

#
emp.groupby(['deptno','job'])['sal'].sum()
#unstack(): corsstable 모양으로 결과값이 출력됨
emp.groupby(['deptno','job'])['sal'].sum().unstack()

#부서별로 data를 분리하여 바라보기  -> for문을 통해 출력 
#object 정보만 보임
emp.groupby('deptno')
# for 문을 통해 출력
for name, group in emp.groupby('deptno'):
    print(name)
    print(group)

★★★★★ # name1, name2.. 
for (name1, name2), gorup in emp.groupby(['deptno','job']):
    print(name1, name2)
    print(group)
    
        
#groupby는 NaN은 누락됨 -> 따라서 fillna와 같은 method를 사용하여 데이터를 정제한다음 적용하는 것이 좋다.
emp['sal'].groupby(emp['deptno'].fillna(0)).sum()


###############################################################################
[문제157] 년도별로 입사한 인원수 결과를 출력해주세요.
import pandas as pd
import numpy as np
from pandas import Series,DataFrame
import pandas as pd 
emp =pd.read_csv('c:/data/emp_new.csv',names=['empid','name','job','mgr','hire_date','sal','comm','deptno'])

import datetime


emp['hire_date']>='2005'
for name, group in emp.groupby(['hire_date']).count():
    print(name)
    print(group)


emp['hire_date'].dstrftime('%Y')
emp['hire_date']

emp.groupby(['hire_date']).count()

for i in emp['hire_date']:
   y = datetime.datetime.strptime(i, '%Y-%m-%d')  #char -> date
   print((y.strftime('%Y')))
   
   for j in year:
       if emp['hire_date'] == j: 
         
#답 
emp['empid'].groupby([i[0:4] for i in emp['hire_date']]).count()


[문제157] emp.csv 파일에 데이터 중에 년도별로 입사한 인원수 결과를 출력해주세요.

from pandas import Series, DataFrame
import pandas as pd
import numpy as np

#쌤답: 기존의 datatime을 사용할 수 없음 
# str.slice(,): 문자의 slicing 
emp = pd.read_csv("c:\data\emp_new.csv", names = ['empid','name','job','mgr','hire_date','sal','comm','deptno'])
emp.dtypes
#답1: str.slice 이용
print(emp.groupby(emp['hire_date'].str.slice(0,4))['empid'].count()) #문자이기 때문에 slicingㅇ르 할 수 있음 
#답2: .dt: pandas에서 제공하는 날짜 형을 바꿔주는 함수 (object만 보임)
# .dt.year: 년도를 뽑아냄
# .dt.month: 달을 뽑아냄

print(emp.groupby(pd.to_datetime(emp['hire_date']).dt.year)['empid'].count())
pd.to_datetime(emp['hire_date']).dt
pd.to_datetime(emp['hire_date']).dt.year
pd.to_datetime(emp['hire_date']).dt.month
pd.to_datetime(emp['hire_date']).dt.day
pd.to_datetime(emp['hire_date']).apply(lambda x: x.year)
pd.to_datetime(emp['hire_date']).apply(lambda x: x.month)

#format의 기본값: '2018-09-19 11:01:30', '20180919 11:01:30'
pd.to_datetime(Series('2018-09-19 11:01:30')).dt.year
pd.to_datetime(Series('2018-09-19 11:01:30')).dt.month
pd.to_datetime(Series('2018-09-19 11:01:30')).dt.day
pd.to_datetime(Series('2018-09-19 11:01:30')).dt.hour
pd.to_datetime(Series('2018-09-19 11:01:30')).dt.minute
pd.to_datetime(Series('2018-09-19 11:01:30')).dt.second
pd.to_datetime(Series('2018-09-19 11:01:30')).dt.quarter #분기
pd.to_datetime(Series('2018-09-19 11:01:30')).dt.dayofweek #(월요일=0, 일요일=6)
pd.to_datetime(Series('2018-09-19 11:01:30')).dt.dayofyear
pd.to_datetime(Series('2018-09-19 11:01:30')).dt.date
pd.to_datetime(Series('2018-09-19 11:01:30')).dt.time
pd.to_datetime(Series('2018-09-19 11:01:30')).dt.week
pd.to_datetime(Series('2018-09-19 11:01:30')).dt.days_in_month

# format을 사용하여 날짜의 형식을 새로 제공할 수 있음 
pd.to_datetime(Series('09192018 11:01:30'),format='%m%d%Y %H:%M:%S').dt.year



[문제158] emp_new.csv 를 emp리스트 변수안에 아래 모양과 같은 딕셔너리 데이터 유형에 데이트를 입력한 후 출력하세요.
# -> 앞으로 join과 관련된 문제를 풀기위해 필요한 부분임 
# list 변수안에 dictionary 형을 만들기 ;key -value 값
{'empno': 100, 'ename': King, 'job': AD_PRES, 'mgr': '', 'hiredate': 2003-06-17, 'sal': 24000, 'comm': '', 'deptno': 90}


100 King AD_PRES  2003-06-17 24000  90
101 Kochhar AD_VP 100 2005-09-21 17000  90
102 De Haan AD_VP 100 2001-01-13 17000  90
103 Hunold IT_PROG 102 2006-01-03 9000  60
104 Ernst IT_PROG 103 2007-05-21 6000  60

import csv
file = open("c:/data/emp_new.csv", 'r')
emp_csv =csv.reader(file) 
emp = []
for emp_list in emp_csv:
    emp.append({'empno':emp_list[0], 
    'ename':emp_list[1], 
    'job':emp_list[2], 
    'mgr':emp_list[3],
    'hiredate':emp_list[4],
    'sal':emp_list[5], 
    'comm':emp_list[6], 
    'deptno':emp_list[7]})
    
for e in emp:
    print(e['empno'], e['ename'], e['job'], e['mgr'],e['hiredate'], e['sal'], e['comm'], e['deptno'])
file.close()

# 잘못된 내답 ㅠ
import csv
file = open("c:/data/emp_new.csv", 'r')
emp_csv =csv.reader(file) 
emp={}
for emp_list in emp_csv:
    emp['empno']=emp_list[0], 
    emp['ename']=emp_list[1], 
    emp['job']=emp_list[2], 
    emp['mgr']=emp_list[3],
    emp['hiredate']=emp_list[4],
    emp['sal']=emp_list[5], 
    emp['comm']=emp_list[6], 
    emp['deptno']=emp_list[7]
    print(emp)



[문제159] emp_new.csv, dept_new.csv 파일을 읽어서 사원의 이름, 부서 이름을 출력하세요.
import csv
file1 = open("c:/data/emp_new.csv", 'r')
emp_csv =csv.reader(file1) 
emp = []
for emp_list in emp_csv:
    emp.append({'empno':emp_list[0], 
    'ename':emp_list[1], 
    'job':emp_list[2], 
    'mgr':emp_list[3],
    'hiredate':emp_list[4],
    'sal':emp_list[5], 
    'comm':emp_list[6], 
    'deptno':emp_list[7]})
file2 = open("c:/data/dept_new.csv", 'r')   
dept_csv = csv.reader(file2)
dept = []
for dept_list in dept_csv:
    dept.append({'deptno':dept_list[0],
                 'dname':dept_list[1],
                 'mgrid':dept_list[2],
                 'locid':dept_list[3]})      

for i in dept:
    for j in emp:
        if dept[i]['deptno']==emp[j]['deptno']:
            print(emp[j]['ename'], dept[i]['dname'])


import csv
file1 = open("c:/data/emp_new.csv", 'r')
emp_csv =csv.reader(file1) 
file2 = open("c:/data/dept_new.csv", 'r')   
dept_csv = csv.reader(file2)
for i in emp_csv:
    print(i)
    
    
    for j in dept_csv:
        if emp_list[][7]==dept_list[0]:
            print(emp_list[1], dept_list[1])
    

#쌤답
import csv
file1 = open("c:/data/emp_new.csv", 'r')
file2 = open("c:/data/dept_new.csv", 'r')   
emp_csv =csv.reader(file1)        
dept_csv = csv.reader(file2)
 
emp = []
dept = []

for i in dept_csv:
    dept.append({'deptno':i[0], 'dname':i[1], 'mgrid':i[2], 'locid':i[3]})

for j in emp_csv:
    emp.append({'empno':j[0], 
    'ename':j[1], 
    'job':j[2], 
    'mgr':j[3],
    'hiredate':j[4],
    'sal':j[5], 
    'comm':j[6], 
    'deptno':j[7]})
    
for d in dept:
    for e in emp:
        if e['deptno']==d['deptno']:
            print(e['ename'], d['dname'])
            
empfile.close()
deptfile.close()



[문제160] 사원들의 이름, 부서 이름을 출력하면서 소속부서가 없는 사원도 출력해주세요. 마지막에는 총건수도 출력하세요. 
import  csv
empfile = open("c:\data\emp_new.csv",'r')
deptfile = open("c:\data\dept_new.csv",'r')
emp_csv = csv.reader(empfile)
dept_csv = csv.reader(deptfile)

emp = []  
dept =[]

for i in  dept_csv:
    dept.append({'deptno':i[0],'dname':i[1],'mgr':i[2],'loc':i[3]})

for j in emp_csv:
    emp.append({'empno':j[0],'ename':j[1],'job':j[2],'mgr':j[3], 'hiredate':j[4],'sal':j[5],'comm':j[6],'deptno':j[7]})

cn = 0   # outer 조인 (driving 고정 +반대쪽이 driving 고정  cf. right outer join => left가 드라이빙 / left otuer join= > right이 드라이빙 )
for e in emp:
    if e['deptno'] == '':
        print(e['ename'])
        cn += 1
    else:
        for d in dept:
            if e['deptno'] == d['deptno']:
               print ( e['ename'], d['dname'])
               cn += 1

print(cn)

empfile.close()
deptfile.close()


#sql의 select 문장
select e.ename, d.dname
from emp e, dept d
where e.deptno = d.deptno:
    
select e.ename, d.dname
from emp e, dept d
where e.deptno = d.deptno(+):
    
select e.ename, d.dname
from emp e left otuer join dept d
where e.deptno =  d.deptno(+):
###############################################################################

from pandas import Series, DataFrame
import pandas as pd
import numpy as np

emp = pd.read_csv("c:/data/emp_new.csv", names=['empid','name','job','mgr','hire_date', 'sal','comm','deptno'])
dept = pd.read_csv("c:/data/dept_new.csv", names=['deptno','dname', 'mgr','loc'])

#몇개의 row와 몇개의 coulmn이 있는지 확인 
emp.shape
#columns 확인
emp.columns
#data type
emp.dtypes

■ pd.merge: pandas의 merge 
(#sql: merge는 dml 문장을 한꺼번에 실행할 수 있는 것)

#동일한 column이름(key값)이 존재하기 때문에 원하는 join결과가 나오지 않을 수 있음 -> deptno, mgr
#-> 이럴경우 먼저 나열 되어 있는 mgr을 기준으로 joind을 함
pd.merge(emp, dept)

#on 절을 통함 merge on에 쓴 것이 컬럼의 기준이 됨
pd.merge(emp, dept, on='deptno')

# on='deptno'을 기준으로 name, deptno, dname을 출력  (on절에 이름이 같을 경우 이렇게 실행하면 된다.)
pd.merge(emp[['name', 'deptno']],dept[['deptno','dname']], on='deptno')

# merge하고자 하는 컬럼의 이름이 다른 경우 left_on과 right_on을 사용하면 된다.  
# e.g., selfjoin시에 키 컬럼 이름이 달라지므로 selfjoin시 사용할 수 있다. 
pd.merge(emp[['name', 'deptno']],dept[['deptno','dname']],
         left_on='deptno', right_on='deptno')

# inner join(equijoin)  -> data 1개가 출력되지 않음 : 106건 
pd.merge(emp[['name','deptno']],dept[['deptno','dname']], on='deptno', how='inner')
# 왼쪽 데이터 프레임은 다 출력
pd.merge(emp[['name','deptno']],dept[['deptno','dname']], on='deptno', how='left')
# 오른쪽 데이터 프레임은 다 출력 
pd.merge(emp[['name','deptno']],dept[['deptno','dname']], on='deptno', how='right')
# full outer join: 모든 양쪽의 내용을 다 출력 
pd.merge(emp[['name','deptno']],dept[['deptno','dname']], on='deptno', how='outer')


###############################################################################
[문제161] emp_new.csv, dept_new.csv 파일 데이터에서 50번 부서 사원의 중에 급여가 5000 이상인 사원의 이름, 부서 이름을 출력하세요.

from pandas import Series, DataFrame
import pandas as pd
import numpy as np

#답1
emp = pd.read_csv("c:/data/emp_new.csv", names=['empid','name','job','mgr','hire_date', 'sal','comm','deptno'])
dept = pd.read_csv("c:/data/dept_new.csv", names=['deptno','dname', 'mgr','loc'])

pd.merge(emp[['name','sal','deptno']],dept[['deptno','dname']], on='deptno')
new=pd.merge(emp[['name','sal','deptno']],dept[['deptno','dname']], on='deptno')
  
new= new[['name','dname','sal']][new['deptno']==50]
new[['name','dname','sal']][new['sal']>=5000]

#답2
emp = pd.read_csv("c:/data/emp_new.csv", names=['empid','name','job','mgr','hire_date', 'sal','comm','deptno'])
dept = pd.read_csv("c:/data/dept_new.csv", names=['deptno','dname', 'mgr','loc'])

(pd.merge(emp[['name','sal','deptno']],dept[['deptno','dname']], on='deptno')[emp['deptno']==50])[['name','dname','sal']][emp['sal']>=5000]

#쌤답
emp = pd.read_csv("c:/data/emp_new.csv", names=['empid','name','job','mgr','hire_date', 'sal','comm','deptno'])
dept = pd.read_csv("c:/data/dept_new.csv", names=['deptno','dname', 'mgr','loc'])

pd.merge(emp[(emp['deptno']==50)&(emp['sal']>=5000)][['name','sal','deptno']],dept[['deptno','dname']], on='deptno')

[문제162] 2002년도에 근무한 사원들의 이름, 급여, 입사일, 부서코드,부서이름을 출력하세요.

from pandas import Series, DataFrame
import pandas as pd
import numpy as np

#답1
pd.merge(emp[['name','sal', 'hire_date','deptno']],dept[['deptno','dname']], on='deptno', how='left')[['name','sal','hire_date','deptno','dname']][emp['hire_date'].str.slice(0,4)=='2002']

#답2
new2=pd.merge(emp[['name','sal', 'hire_date','deptno']],dept[['deptno','dname']], on='deptno')
new2[['name','sal','hire_date','deptno','dname']][new2['hire_date'].str.slice(0,4)=='2002']

#쌤답1
pd.merge(emp[emp['hire_date'].str.slice(0,4)=='2002'][['name','sal','hire_date','deptno']], dept[['deptno','dname']], on='deptno')

#쌤답2
from datetime import datetime
pd.merge(emp[pd.to_datetime(emp['hire_date']).dt.year==datetime.strptime('2002','%Y').year][['name','sal','hire_date','deptno']],dept[['deptno','dname']],on='deptno')


[문제163] 직업이 AD_VP, AD_PRES 인 사원들의 이름, 급여, 직업, 부서코드, 부서이름 을 출력하세요.
emp = pd.read_csv("c:/data/emp_new.csv", names=['empid','name','job','mgr','hire_date', 'sal','comm','deptno'])
dept = pd.read_csv("c:/data/dept_new.csv", names=['deptno','dname', 'mgr','loc'])

#답1
import pandas as pd 
pd.merge(emp[(emp['job']=='AD_VP')|(emp['job']== 'AD_PRES')][['name','sal','job','deptno']],dept[['deptno','dname']], on='deptno')

#답2
import pandas as pd 
pd.merge(emp[emp['job'].isin(['AD_VP','AD_PRES'])][['name','sal','job','deptno']],dept[['deptno','dname']], on='deptno')



###############################################################################\
dept = DataFrame({'dname':['관리팀', '마케팅팀','구매팀','인사팀','경영지원팀','기술지원팀','홍보팀','영업팀','기획팀','재무팀','회계팀']},
                  index=[10,20,30,40,50,60,70,80,90,100,110])
dept

# right index/ left index: index를 이용할 때
pd.merge(emp[['name','sal','deptno']], dept, left_on='deptno', right_index=True)


###############################################################################
[문제164] 부서이름별 총액 급여를 출력하세요.  

#답1 
import pandas as pd 
emp = pd.read_csv("c:/data/emp_new.csv", names=['empid','name','job','mgr','hire_date', 'sal','comm','deptno'])
dept = DataFrame({'dname':['관리팀', '마케팅팀','구매팀','인사팀','경영지원팀','기술지원팀','홍보팀','영업팀','기획팀','재무팀','회계팀']},
                  index=[10,20,30,40,50,60,70,80,90,100,110])

m=pd.merge(emp[['name','sal','deptno']], dept, left_on='deptno', right_index=True)
dname_unique = Series(m['dname'].unique())
m

for i in dname_unique.sort_values():
    print(i, m.loc[m['dname']==i, 'sal'].sum())

#답2
    import pandas as pd 
emp = pd.read_csv("c:/data/emp_new.csv", names=['empid','name','job','mgr','hire_date', 'sal','comm','deptno'])
dept = DataFrame({'dname':['관리팀', '마케팅팀','구매팀','인사팀','경영지원팀','기술지원팀','홍보팀','영업팀','기획팀','재무팀','회계팀']},
                  index=[10,20,30,40,50,60,70,80,90,100,110])

# dataframe만 join이 가능하다, 따라서 처리를 한뒤 join을 해야함 
m=pd.merge(emp[['name','sal','deptno']], dept, left_on='deptno', right_index=True)
dname_unique = Series(m['dname'].unique())

m['sal'].groupby(m['dname']).sum()

# 쌤답1
from pandas import Series, DataFrame
import pandas as pd
emp = pd.read_csv("c:\data\emp_new.csv", names = ['empid','name','job','mgr','hire_date','sal','comm','deptno'])
dept = pd.read_csv("c:\data\dept_new.csv", names = ['deptno','dname','mgr','loc'])

#먼저 grouping 한 뒤에 -> join 함
dept_sal = emp['sal'].groupby(emp['deptno']).sum() #series형이어서 merge할수 없음 
dept_sal = DataFrame(dept_sal) #따라서 dataframe형을 바꿈 
dept_sal.reindex([10,20,30,40,50,60,70,80,90,100,110]) #다시 reindex가 필요함 
pd.merge(dept[['deptno','dname']], dept_sal, left_on = 'deptno', right_index=True)


# 쌤답2 
# 먼저 join 한 뒤 -> grouping의 집계값 구함
from pandas import Series, DataFrame
import pandas as pd
emp = pd.read_csv("c:\data\emp_new.csv", names = ['empid','name','job','mgr','hire_date','sal','comm','deptno'])
dept = pd.read_csv("c:\data\dept_new.csv", names = ['deptno','dname','mgr','loc'])
m = pd.merge(emp[['deptno','sal']], dept[['deptno','dname']])
m
m['sal'].groupby(m['dname']).sum()


#쌤답3 
dept= DataFrame({'dname':['관리팀','마케팅팀','구매팀','인사팀','경영지원팀','기술지원팀','홍보팀',
'영업팀','기획팀','재무팀','회계팀']},
index=[10,20,30,40,50,60,70,80,90,100,110])
pd.merge(dept, dept_sal, left_index = True, right_index=True)




# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 09:45:20 2018

@author: stu
"""
###############################################################################

[문제165] emp_new.csv 파일  데이터에 커미션 정보를 분석하려 합니다.
커미션에 null값들의 수, null이 아닌값들의 수를 구하세요.

1. 일반적으로 csv file을 읽어서 해결
import csv
file = open("c:/data/emp_new.csv",'r')
emp_csv = csv.reader(file)
comm = 0
for emp_list in emp_csv:
    if emp_list[-2] == '':
        comm +=1
print(comm)
        
import csv
file = open("c:/data/emp_new.csv",'r')
emp_csv = csv.reader(file)
comm = 0
for emp_list in emp_csv:
    if emp_list[-2] != '':
        comm +=1 
print(comm)
                
                
#쌤답
import csv

file = open("c:/data/emp_new.csv",'r')
emp_csv = csv.reader(file)
cn1 = 0
cn2 = 0
for emp_list in emp_csv:
    if emp_list[6] == '':
        cn1 += 1
    else:
        cn2 += 1
print('null의 수:' , cn1)
print('null이 아닌 수:' , cn2)
file.close()
        
                
                
2. pandas를 이용해서 해결
#답1 - null
import pandas as pd
emp = pd.read_csv("c:\data\emp_new.csv", names = ['empid','name','job','mgr','hire_date','sal','comm','deptno'])
emp[emp['comm'].isnull()]['empid'].count()
#답2
emp[(emp['comm']).isnull()]['comm'].fillna(0).count()

    
#답1 - notnull
import pandas as pd
emp = pd.read_csv("c:\data\emp_new.csv", names = ['empid','name','job','mgr','hire_date','sal','comm','deptno'])
emp[emp['comm'].notnull()]['comm'].count()


#쌤답 
#
import pandas as pd
emp = pd.read_csv("c:\data\emp_new.csv", names = ['empid','name','job','mgr','hire_date','sal','comm','deptno'])
print('null 수: ', emp[emp['comm'].isnull()]['empid'].count())
print('null 아닌 수: ', emp[emp['comm'].notnull()]['empid'].count())

[문제166] emp_new.csv, dept_new.csv 파일 데이터를 이용해서  조인된 결과를 보려고 합니다.
조인 함수를 생성하세요.

join(emp,'deptno','ename', dept,'deptno','dname')

join(emp,'mgr','ename', emp,'empno','ename') 

#답xxxxxx 잘못된 답! 근데 merge되는 순서 다시 확인하기 위해서 남겨둠 
from pandas import Series, DataFrame
import pandas as pd
emp = pd.read_csv("c:\data\emp_new.csv", names = ['empno','ename','job','mgr','hire_date','sal','comm','deptno'])
dept = pd.read_csv("c:\data\dept_new.csv", names = ['deptno','dname','mgr','loc'])
def join(x, x1, x2, y, y1, y2):
    print(pd.merge(x[[x1,x2]],y[[y1,y2]]))
    
#동일한 column이름(key값)이 존재하기 때문에 원하는 join결과가 나오지 않을 수 있음 -> deptno, mgr
#-> 이럴경우 먼저 나열 되어 있는 mgr을 기준으로 joind을 함

#답 1
from pandas import Series, DataFrame
import pandas as pd
emp = pd.read_csv("c:\data\emp_new.csv", names = ['empno','ename','job','mgr','hire_date','sal','comm','deptno'])
dept = pd.read_csv("c:\data\dept_new.csv", names = ['deptno','dname','mgr','loc'])
def join(x, x1, x2, y, y1, y2):
    print(pd.merge(x[[x1,x2]],y[[y1,y2]], left_on = x1, right_on = y1))


#쌤답2
import csv
empfile = open("c:/data/emp_new.csv",'r')    
deptfile = open("c:/data/dept_new.csv",'r')
emp_csv = csv.reader(empfile)
detp_csv = csv.reader(deptfile)
emp = []
dept = []

for j  in emp_csv:
    emp.append({'empno':j[0], 'enanme':j[1], 'job': j[2], 'mgr':j[3], 'hiredate':j[4], 'sal':j[5], 'comm':j[6], 'deptno':j[7]})

def join (outer_table, outer_column1, outer_column2, inner_table, inner_coulmn1, inner_coulmn2):
    for o in outer_table:
        for i in inner_table:
            if o[outer_column1] == i[inner==column1]:
                print(o[outer_column2], i[inner_coulmn2])

#쌤답2
import  pandas  as  pd

emp = pd.read_csv("c:\data\emp_new.csv", names = ['empid','ename','job','mgr','hire_date','sal','comm','deptno'])
dept = pd.read_csv("c:\data\dept_new.csv",names = ['deptno','dname','mgr','loc'])

def join(outer_table,outer_column1,outer_column2,inner_table,inner_column1,inner_column2):
    print(pd.merge(outer_table[[outer_column1,outer_column2]],inner_table[[inner_column1,inner_column2]],left_on=outer_column1,right_on=inner_column1))

join(emp,'deptno','ename', dept,'deptno','dname')

join(emp,'mgr','ename', emp,'empid','ename')    



###############################################################################
#하나씩 인덱싱을 함수에 넣음 
def f(arg):
    result=[]
    for i in arg:
        result.append(i*2)
    return result

f([1,2,3,4,5])
id(f)

#한통으로 [1,2,3,4,5]를 넣음
def f1(arg)  :
    return arg*2

f1([1,2,3,4,5])

■ map 함수는 입력받는 자료형의 각 요소가 함수에 수행된 결과를 묶어서 리턴하는 함수
#map 정보만 추출
map(f1,[1,2,3,4,5])
#list로 만들어줌 
list(map(f1,([1,2,3,4,5])))

#람다함수 이용
list(map(lambda x: x*2,[1,2,3,4,5]))


###############################################################################
[문제167] x변수에는 1,2,3,4,5  y변수에는 6,7,8,9,10 들어 있다. f(x,y) = x2 + y 를 구하세요.(lambda, map 함수를 이용하세요)

#답1
f = lambda x, y : x*2 +y
x = [1,2,3,4,5]
y = [6,7,8,9,10]
result = map(f,x,y)
print(list(result))

#답2
x = [1,2,3,4,5]
y = [6,7,8,9,10]
print(list(map(lambda x,y: x*2+y, x,y)))

###############################################################################
□ 한쪽의 value값과 한쪽의 index값을 붙이는 작업
from pandas import Series, DataFrame
import pandas as pd
import numpy as np

x = Series([1,2,3],index=['one','two','three']) #값, 인덱스 
y = Series(['하나','둘','셋'], index=[1,2,3]) #값, 인덱스 

#series에서는 pd.merge가 안됨 -> dataframe형으로 만들어야 함  
x1=DataFrame(x)
y1=DataFrame(y)

# merge: merge는 작업후 필요없 열을 버려줘야함
pd.merge(x1,y1, left_on = 0, right_index=True)

# map을 통해 pandas에서도 한쪽의 값과 한쪽의 index를 붙이는 작엄을 함 
#꼭 항상 value, index순서로 쓰지 않아도 됨 
x.map(y)

###############################################################################
[문제168] emp_new.csv는 pandas로 읽고  dept_new.csv는 일반 csv로 읽어 들인 후 조인을 수행하세요.

#답1
#한쪽은 DataFrame
import  pandas  as  pd
emp = pd.read_csv("c:\data\emp_new.csv", names = ['empid','ename','job','mgr','hire_date','sal','comm','deptno'])

import csv
file = open("c:\data\dept_new.csv",'r')


#dictionary형으로 만들기
import csv
file = open("c:\data\dept_new.csv",'r')
dept = csv.reader(file)
d = {}
for dept_list in dept:
    if dept_list[0] != d:
        d[int(dept_list[0])] = dept_list[1]
d

emp['dname']=emp['deptno'].map(d) 
print(emp[['empid','deptno','dname']])


#
import csv
file = open("c:\data\dept_new.csv",'r')
dept = csv.reader(file)
d = {}
for dept_list in dept:
    d[int(dept_list[0])] = dept_list[1]

d
emp['dname']=emp['deptno'].map(d)
print(emp[['empid','deptno','dname']])

#쌤답

#한쪽은 DataFrame
import  pandas  as  pd
emp = pd.read_csv("c:\data\emp_new.csv", names = ['empid','ename','job','mgr','hire_date','sal','comm','deptno'])

import csv
deptfile = open("c:\data\dept_new.csv",'r')
dept_csv = csv.reader(deptfile)
dept = {}

for i in dept_csv:
    if i[0] != dept:
        dept[int(i[0])] = i[1]
dept  

for k,v in dept.items():
    print(k,v)

# merge하지 않아도 join된 결과를 얻을 수 있다. 
emp['dname']=emp['deptno'].map(dept) 
print(emp[['empid','deptno','dname']])



[문제169] happiness 변수에 문장이 있습니다. 행복이란 단어가 몇개 나오는지 분석하시고, 위치정보도 출력해주세요.



happiness = '우리나라 「헌법」 제10조는 “모든 국민은 인간으로서의 존엄과 가치를 가지며, 행복을 추구할 권리를 가진다”라고 규정하고 있다.행복추구권은 근대 입헌민주주의의 핵심인 개인주의·자유주의를 그 사상적 기반으로 하고 있다. 행복추구권에 있어서 행복은 다의적인 개념으로, 각자의 생활조건이나 가치관에 따라 다르게 이해될 수 있으나, 최소한 인간적인 고통이 없는 상태 내지 만족감을 느낄 수 있는 행복한 상태를 의미한다.'

#답: 행복 단어 개수
cn=0
i=0
for i in range(len(happiness)):
    i += 1
    if happiness[i:i+2]=='행복':
        cn += 1
print(cn)    

#답2
cn = happiness.count('행복')
print('단어의 수:', cn)


#단어의 위치찾기- 다시 시도 해보기 
cn=0
i=0
loc=[]
for i in range(len(happiness)):
    i += 1
    if happiness[i:i+2]=='행복':
        cn += 1
        loc.append(happiness.find('행복'))       
print(loc)
print(cn)    

#답1
print('단어의 위치:', happiness.find('행복',44))
print('단어의 위치:', happiness.find('행복',71))
print('단어의 위치:', happiness.find('행복',122))
print('단어의 위치:', happiness.find('행복',133))
print('단어의 위치:', happiness.find('행복',217))

#답2: find: 있으면 인덱스 번호를 return해주고, 없으면 -index1의 값으로 return한다. 
a =1 
while happiness.find('행복',a) != -1:
    a = happiness.find('행복', a)
    print('단어의 위치: ', a)
    a += 1
    
happiness.find('행복') != -1





[문제170] emp1.csv, emp2.csv파일을 읽어서 부서별 총액급여를 구하세요.

import pandas as pd 

#답1
import pandas as pd 
emp1 = pd.read_csv("c:\data\emp1.csv", names = ['empid','name','hire_date','sal','deptno'])
emp = emp1
for i in range(2,3):
    emp = emp.append(pd.read_csv("c:\data\emp{}.csv".format(i), names = ['empid','name','hire_date','sal','deptno']))
emp['sal'].groupby(emp['deptno']).sum()



#답2
import pandas as pd 
emp=emp1.append(emp2)
    
emp1 = pd.read_csv("c:\data\emp1.csv", names = ['empid','ename','hire_date','sal','deptno'])
emp2 = pd.read_csv("c:\data\emp2.csv", names = ['empid','ename','hire_date','sal','deptno'])

emp['sal'].groupby(emp['deptno']).sum()
emp1['sal'].groupby(emp1['deptno']).sum()
emp2['sal'].groupby(emp2['deptno']).sum()

#답3
emp = pd.DataFrame(index = ['empid','name','hire_date','sal','deptno'])
for i in range(1,3):
    emp = emp.append(pd.read_csv("c:\data\emp{}.csv".format(i), names = ['empid','name','hire_date','sal','deptno']))
emp['sal'].groupby(emp['deptno']).sum()


#쌤답1
import pandas as pd
emp = pd.DataFrame()
for i in range(1,3):
    file = 'c:/data/emp{}.csv'.format(i)
    temp = pd.read_csv(file, names = ['empid','name','hire_date','sal','deptno'])
    emp = emp.append(temp)
    
print(emp['sal'].groupby(emp['deptno']).sum())


#쌤답2
■ import glob
glob.glob(): 동일이름이지만 번호만 달라지는 파일명을 불러들일때 사용하는 method, *가 키워드임

import glob
import pandas as pd

file = 'C:/python_data/emp*.csv'
file_list = glob.glob(file)
print(file_list)
emp = pd.DataFrame()

for i in file_list:
    temp = pd.read_csv(i, names =  ['empid','name','hire_date','sal','deptno'])
    emp = emp.append(temp)

print(emp['sal'].groupby(emp['deptno']).sum())



[문제171] 2016년도에 태어난 아이들의 정보가 들어 있는 year2016파일을 분석해야 합니다. 총 출생수를 출력해주세요.

#txt파일에서 ,로 구분자가 되어있기 때문에 csv로 읽어들일 수 있다. 
#총 출생수 
import pandas as pd
data = pd.read_csv('c:/data/yob2016.txt', names = ['name','gender','num'])

data['num'].sum()

# pandas를 사용하지 않을 때
readlines


#쌤답1: csv객체로 읽어들임 
import csv
import os 

count=0
file = 'c:\data\yob2016.txt'
name = os.path.basename('c:\data\yob2016.txt')  #물리적인 절대적경로를 빼고, 파일이름.확장자
name = name.split('.')[0]   #.을 기준으로 split [0]인덱스의 값만 뽑아내면 파일 이름만 뽑아내게 됨 
with open(file,'r') as f: #with를 사용하면 file.close()를 안해도 됨 
    data=csv.reader(f)
    for d in data:
        count += int(d[2]) #2번 index값을 intger형으로 바꾼후 count 변수에 누적 
print(name,count) #파일이름과 총출생수 출력 

#쌤답2 : readlines로 읽어들일 때 ★★★★★★★ 주의하기 
import csv
import os

count=0
file = 'c:\data\yob2016.txt'
name = os.path.basename('c:\data\yob2016.txt')
name = name.split('.')[0]
with open(file,'r') as f:
    data=f.readlines()
    for d in data:
        birth = d.split(',')[2] #split 을 해야함 
        count += int(birth)
print(name,count)



import pandas as pd 
import os

file = 'c:/data/yob2016.txt'
name = os.path.basename(file)
name = name.split('.')[0]

#쌤답3
yob = pd.read_csv('c:\data\yob2016.txt', names=['name','gender','birth'])
print(name,yob['birth'].sum())




[문제172] 2016년도에 태어난 아이 이름 상위 10까지 보여주세요. 성별 상위 5까지 보여주세요.
import pandas as pd
data = pd.read_csv('c:/data/yob2016.txt', names = ['name','gender','num'])


data[data['gender']=='F']
data[data['gender']=='M']

#답: 아이 이름 상위 10까지
total = DataFrame({'순위':data['num'].rank(ascending=False, method='dense'), '이름':data['name'], '성별':data['gender'], '인원수':data['num']})
total[['순위','이름','성별','인원수']][total['순위']<= 10]


#답: 성별 상위 5까지 
f= data[data['gender']=='F']
total_f= DataFrame({'순위':f['num'].rank(ascending=False, method='dense'), '이름':f['name'], '성별':f['gender'], '인원수':f['num']})
total_f[['순위','이름','성별','인원수']][total_f['순위']<= 5]

m= data[data['gender']=='M']
total_m= DataFrame({'순위':m['num'].rank(ascending=False, method='dense'), '이름':m['name'], '성별':m['gender'], '인원수':m['num']})
total_m[['순위','이름','성별','인원수']][total_m['순위']<= 5]



# 답22
import pandas as pd
name=pd.read_csv("c:/data/yob2016.txt", names = ['name','gender','count'])
a=name.sort_values(by='count',ascending=False)[0:10]
a

female=name[name['gender']=='F']
male=name[name['gender']=='M']

f=female.sort_values(by='count', ascending=False)[0:10]
f
m=male.sort_values(by='count', ascending=False)[0:10]
m


#쌤답
import pandas as pd 

yob2016 = pd.read_csv('c:\data\yob2016.txt', names=['name','gender','birth'])

def top(df, n=5, column='birth'):   # 넣지 않으면 n=5, column='birth' -> default값으로 설정할 수 있음 
    return df.sort_values(by=column, ascending=False)[:n]  #[:n]은 slicing ; 기억하기!! sort.values로 상위 몇 개만 뽑아내기! 

print(top(yob2016 , n=10))

print(yob2016.groupby('gender').apply(top))


#rank를 이용해서 출생수가 동일하게 counting된 아이들의 이름을 누락시키지 않게 하기 위해 




# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 09:45:39 2018

@author: stu
"""

###############################################################################

#sort_value는 같은 값이 없을 때 순위를 구하는 것이 가능하지만 같은 값이 있게 되면 누락되는 상황이 발생되기 때문에 순위를 구할때는 rank를 사용해야 한다. 
#rank안의 option의 dense를 사용해서 
#sql에는 inline view를 통해서 바깥쪽에서 제한을 함,(select 문장에서 rank구하기 확인하기-> 순위를 구하되 10위까지 구한 것을 dataframe을 하나 만들어 넣어놔야한다. 그런다음 제한하면 됨)
[문제173] emp1.csv 데이터를 이용해서 급여를 많이 받는 순으로 10위까지 구하세요.

import pandas as pd
from pandas import Series, DataFrame


emp = pd.read_csv('c:/data/emp1.csv', names=['empid','name','hire_date', 'sal', 'deptno']) 

emprank = DataFrame({ 'rank':emp['sal'].rank(ascending=False, method='desne')})

emprank = DataFrame({'empid':emp['empid'], 'name':emp['name'], 'hire_date':emp['hire_date'], 'sal':emp['sal'], 'rank':emp['sal'].rank(ascending=False, method='dense'), 'deptno':emp['deptno']})
rank=emprank[['empid','name','hire_date','sal','rank','deptno']][emprank['rank']<=10].sort_values('rank')
rank

#쌤답
emp['rank'] = emp['sal'].rank(ascending=False, method='dense')
emp[emp['rank']<=10] .sort_values('rank')


[문제174] emp1.csv 데이터를 이용해서 부서별로 급여를 많이 받는 순으로 5위까지 구하세요.
#답1
import pandas as pd
from pandas import Series, DataFrame

emp = pd.read_csv('c:/data/emp1.csv', names=['empid','name','hire_date', 'sal', 'deptno']) 
emp['dept_rank'] = emp['sal'].groupby(emp['deptno']).rank(ascending=False, method='dense')

for i in emp[emp['dept_rank'] <= 5].sort_values(['dept_rank']).groupby('deptno'):
    print(i)


#답2
import pandas as pd
from pandas import Series, DataFrame

emp = pd.read_csv('c:/data/emp1.csv', names=['empid','name','hire_date', 'sal', 'deptno']) 

emp['dept_rank'] = emp['sal'].groupby(emp['deptno']).rank(ascending=False, method='dense')
emp[emp['dept_rank']<=5].sort_values(['deptno','dept_rank'])


###############################################################################


[문제175] yob2016.txt 데이터를 이용해서 아기 이름 순위 10위까지 구하세요.

import pandas as pd
data = pd.read_csv('c:/data/yob2016.txt', names = ['name','gender','num'])

data['rank'] = data['num'].rank(ascending=False, method='dense')
data[['name','gender','num','rank']][data['rank']<=10].sort_values('rank')



[문제176] yob2016.txt 데이터를 이용해서 성별 아기 이름 순위 5위까지 구하세요.

import pandas as pd
data = pd.read_csv('c:/data/yob2016.txt', names = ['name','gender','num'])
data['gender_rank'] = data['num'].groupby(data['gender']).rank(ascending=False, method='dense')
data[data['gender_rank']<=5].sort_values(['gender','gender_rank'])

import pandas as pd
data = pd.read_csv('c:/data/yob2016.txt', names = ['name','gender','num'])
data['gender_rank'] = data['num'].groupby(data['gender']).rank(ascending=False, method='dense')

for i in data[data['gender_rank']<=5].sort_values(['gender_rank']).groupby('gender'):
    print(i)
    
    
[문제177] 2000 ~ 2016년도 년도별 출생수

https://catalog.data.gov/dataset/baby-names-from-social-security-card-applications-national-level-data

def countName():
    counting = []
    for i in range(2000,2017):
        count = 0
        filename = 'c:\python_data\yob\yob%d.txt'%i
        with open(filename,'r') as f:
            data=f.readlines()
            for j in data:
                birth = j.split(',')[2]
                count += int(birth)
            counting.append((j,count))
    return counting

result = countName()            
for year, cn in result:
    print(year, cn)
    
#쌤답1
def countBirths():
    ret=[]
    for y in range(2000,2017):
        count=0
        filename='c:python_data\yob\yob%d.txt'%y
        with open(filename,'r') as f:
            data=f.readlines()
            for d in data:
                birth = d.split(',')[2]
                count += int(birth)
            ret.append((y,count))
    return ret



result = countBirths()
for year, cn in result:
    print(year,cn)

##오답: 누적합이 되어버림 
import os
from pandas import Series, DataFrame
import pandas as pd
import numpy as np

year_cn=[]
all_data = pd.DataFrame()
for y in range(2000,2017):
    filename='c:\python_data\yob\yob%d.txt'%y
    name = os.path.basename(filename)
    name = name.split('.')[0]
    df = pd.read_csv(filename, names=['name','gender','birth'])
    #all_data = all_data.append(df)    -> 필요없는 부분 
    year_cn.append((name[3:],all_data['birth'].sum()))
    print(name[3:],all_data['birth'].sum())

#답
import os
from pandas import Series, DataFrame
import pandas as pd
import numpy as np

year_cn=[]
all_data = pd.DataFrame()
for y in range(2000,2017):
    filename='c:\python_data\yob\yob%d.txt'%y
    name = os.path.basename(filename)
    name = name.split('.')[0]
    df = pd.read_csv(filename, names=['name','gender','birth'])
    year_cn.append((name[3:], df['birth'].sum()))
    print(name[3:], df['birth'].sum())


#답
        
import pandas as pd

for i in range(2000,2017):
    temp = pd.read_csv('c:/python_data/yob/yob{}.txt'.format(i), names = ['name', 'gender', 'cnt'])
    print(i,temp['cnt'].sum())
    
[문제178]  2000 ~ 2016년도 년도별 출생수 결과를 year.txt 파일에 저장하세요.

import os
import glob
from pandas import Series, DataFrame
import pandas as pd
import numpy as np

#답1
#write 대상을 만들기 
year_cn=[]                                          #append 하여 만드는 작업
all_data = pd.DataFrame()
for f in glob.glob("c:\python_data\yob\yob*.txt"):   #물리적 확장자 주소
    name = os.path.basename(f)      # (물리적 확장자 주소가 아닌) file이름만 뽑아내기 -> 나중에 년도만 뽑아내기 위해서 
    name = name.split('.')[0]       # 파일 이름의 년도 정보 뽑아내기 
    df = pd.read_csv(f, names=['name','gender','birth'])   
    year_cn.append((name[3:],df['birth'].sum()))  #name[3:] :yob을 제거하고 연도만 넣기: 200x, 출생수 저장
    print(name[3:],df['birth'].sum())             #출력


# 이제부터 파일로 떨어뜨리기 ; 
#기존 데이터를 저장할때는 하나씩 저장하여 ,를 써주면서 형식을 저장해야함 (밑의 writer= csv.writer(f, delimiter=','와 다름))
with open('c:\python_data\yob\year.txt','w') as f:      #'w' :write정보 , f별칭 
    for year, birth in year_cn:                     #year_cn에서 year와 birth를 가져옴
        data = '%s,%s\n'%(year,birth)               #%s를 통해 year, birth를 넣음, \n 줄바꿈
        print(data)         
        f.write(data)                               #data 차곡차곡 정리



#답2 - append 하지 않고 한번에 작업하기 

import os
from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import csv

with open('c:/python_data/yob/year_total.csv','w') as f:
    writer = csv.writer(f, delimiter=',')   #csv.writer : csv로 저장, / 구분자: delimiter=',' 
    for y in range(2000,2017):
        filename='c:/python_data/yob/yob%d.txt'%y   #for문을 사용하여 data읽어들이기 
        name = os.path.basename(filename)
        name = name.split('.')[0]
        df = pd.read_csv(filename, names=['name','gender','birth'])
        writer.writerow([name[3:],df['birth'].sum()])   #writerow(): 결과물 ()부분을 행단위로 저장하겠다. :writerow([name[3:],df['birth'].sum()]) 


#답3

import pandas as pd

f = open("c:/python_data/yob/year2.txt", "w")

for i in range(2000,2017):
    temp = pd.read_csv('c:/python_data/yob/yob{}.txt'.format(i), names = ['name', 'gender', 'cnt'])
    txt = "{},{}\n".format(i,temp['cnt'].sum())
    f.write(txt)

f.close()





[문제179] 2010 ~ 2016  년도까지 성별 출생 현황을
year_gender_total.csv 파일로 생성해주세요.

# 덥
import pandas as pd

f = open("c:/data/year_gender_total.csv", "w")

f.write('year,M,F\n')

for i in range(2000,2017):
    temp = pd.read_csv('c:/python_data/yob/yob{}.txt'.format(i), names = ['name', 'gender', 'cnt'])
    M = temp[temp['gender']=='M']['cnt'].sum()
    F = temp[temp['gender']=='F']['cnt'].sum()
    txt = "{},{},{}\n".format(i,M,F)
    f.write(txt)

f.close()



#이상한 답

import pandas as pd

f = open("c:/python_data/yob/year_gender_total2.csv", "w")

for i in range(2000,2017):
    temp = pd.read_csv('c:/python_data/yob/yob{}.txt'.format(i), names = ['name', 'gender', 'cnt'])
    temp1 = temp.groupby(temp['gender']).sum()
    f_cnt = temp1.loc['F']
    m_cnt = temp1.loc['M']
    txt = "{},{},{}\n".format(i,f_cnt, m_cnt)
    f.write(txt)

f.close()


#답

import os
from pandas import Series, DataFrame
import pandas as pd
import numpy as np

with open('c:/python_data/year_gender_total.csv','w') as f:
    writer = csv.writer(f, delimiter=',')
    writer.writerow(['년도','여자','남자'])
    for y in range(2000,2017):
        filename='c:\python_data\yob%d.txt'%y
        name = os.path.basename(filename)
        name = name.split('.')[0]
        df = pd.read_csv(filename, names=['name','gender','birth'])
        gender_cn = df['birth'].groupby(df['gender']).sum()
        f_cn = gender_cn.loc['F']
        m_cn = gender_cn.loc['M']
        writer.writerow([name[3:],f_cn, m_cn])
        


#writing시 영어 외의 문자열은 utf-8로 encoding 을 해야 문자가 깨지지 않는다. option으로 encoding='utf-8'을 사용하기! 
with open('c:/python_data/year-gender_total.csv','w',encoding='utf-8') as f:
    
    
###############################################################################

▣ matplotlib: 시각화 패키지

import matplotlib as mpl
import matplotlib.pylab as plt

plt.plot([1,5,10,15,20])
#graph격자
plt.grid(True)  
#plot을 show 해줘
plt.show

#x축: [100,200,300,400,500], y축: [1,5,10,15,20]
plt.plot([100,200,300,400,500],[1,5,10,15,20])
#web에서는 show를 하지 않으면 출력하지 않기 때문에 plt.show를 하면 출력된다. (spider에서는 plt.show를 쓰지 않아도 plot이 제공되지만 그래프 정보만 나오는 경우는 plt.show를 해줘야 그래프를 볼 수 있다.)
plt.show


plt.plot([100,200,300,400,500],[1,5,10,15,20], color='blue')
plt.plot([100,200,300,400,500],[1,5,10,15,20], color='c')  #rgbcmyk
plt.plot([100,200,300,400,500],[1,5,10,15,20], color='r')
plt.plot([100,200,300,400,500],[1,5,10,15,20], color='b')
plt.plot([100,200,300,400,500],[1,5,10,15,20], color='g')
plt.plot([100,200,300,400,500],[1,5,10,15,20], color='m')
plt.plot([100,200,300,400,500],[1,5,10,15,20], color='y')
plt.plot([100,200,300,400,500],[1,5,10,15,20], color='k')
plt.show

#회색조
plt.plot([100,200,300,400,500],[1,5,10,15,20], color='0.75') #0~1 회색조
plt.show

#linestyle -solid, dashed, dashdot
plt.plot([100,200,300,400,500],[1,5,10,15,20], color='blue', linestyle='dotted')
plt.show

plt.plot([100,200,300,400,500],[1,5,10,15,20], color='blue', linestyle='solid')
plt.show

plt.plot([100,200,300,400,500],[1,5,10,15,20], color='blue', linestyle='dashed')
plt.show

plt.plot([100,200,300,400,500],[1,5,10,15,20], color='blue', linestyle='dashdot')
plt.show

#
plt.plot([100,200,300,400,500],[1,5,10,15,20], '--r') #dashed red
plt.show

plt.plot([100,200,300,400,500],[1,5,10,15,20], '.r')
plt.show

plt.plot([100,200,300,400,500],[1,5,10,15,20], '-g') #solid green
plt show

plt.plot([100,200,300,400,500],[1,5,10,15,20], '--c') #dashed cyan
plt.show 

plt.plot([100,200,300,400,500],[1,5,10,15,20], '-.k') #dashdot black
plt.show

plt.plot([100,200,300,400,500],[1,5,10,15,20], ':r') #dotted red 
plt.show


# anaconda propmt에서 jupyter notebook 실행

clrl +enter: 실행
alt + enter: command line 생성 


# 
data = {'홍길동':[15,13,11],
        '윤건' : [13,14,15],
        '나얼': [10,9,12]}
data

df = DataFrame(data, index=['2015','2016','2017'])
df.rank()

x = df.rank()
x

plt.plot(x)
plt.show()


#한글은 깨짐 -> font를 불러와야 함 
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/windows/fonts/malgun.ttf").get_name()
rc('font', family=font_name)


#범례만들기: label 
plt.plot(x.ix[:,0], label='나얼')
plt.plot(x.ix[:,1], label='윤건', linestyle='--')
plt.plot(x.ix[:,2], label='홍길동', linestyle=':')
plt.title('기록 순위 비교 그래프', fontsize=15)
plt.xlabel('년도', fontsize=10)
plt.ylabel('순위',fontsize=10)
plt.legend() 
#yticks: 기존의 레벨을 다른 형식으로 변환해 주는 method
plt.yticks([1,2,3],['1등','2등','3등'])
#xticks:
plt.xticks(['2015','2016','2017'],['2015년', '2016년', '2017년'])

plt.xlim([2015.9,2017.9])


#y축의 범위: ylim
plt.ylim([1,2,3])
#x축의 범위: xlim
plt.xlim([2015.9,2017.9])


#범례출력하기 

#수평막대그래프
df.plot(kind='barh')
df.plot(kind='barh', stacked=True)

#수직막대그래프
df.plot(kind='bar')
df.plot(kind='bar', stacked=True)



##############################################################################
[문제180] 2010 ~ 2016  년도까지 성별 출생 현황을 그래프를 그리세요.

#module import 
import csv
from pandas import Series,DataFrame
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)
%matplotlib inline

with open('c:/python_data/year_gender_total.csv','w',encoding="utf-8") as f:
    writer = csv.writer(f, delimiter=',')
    writer.writerow(['년도','여자','남자'])
    for y in range(2000,2017):
        filename='c:\python_data\yob\yob%d.txt'%y
        name = os.path.basename(filename)
        name = name.split('.')[0]
        df = pd.read_csv(filename, names=['name','gender','birth'])
        gender_cn = df['birth'].groupby(df['gender']).sum()
        writer.writerow([name[3:],gender_cn.loc['F'],gender_cn.loc['M']])
      


df = pd.read_csv('c:/python_data/year_gender_total.csv')
df
#여자만 뽑아내어 그래프를 그리고 싶다면 df['여자']로 해서 Data를 뽑아낸 다음 
df['여자']

#set_index : '년도'를 index로 표현하고 싶을 때 사용 
df = df.set_index("년도")
df
df.plot()
df.plot(kind="bar")
df.plot(kind="barh")

plt.plot(df.ix[:,0], label="여자", color="r", linestyle="--")
plt.plot(df.ix[:,1], label="남자", color="b", linestyle=":")
plt.title("성별 출생 현황", fontsize=15)
plt.xlabel("년도",fontsize=10)
plt.ylabel("출생수",fontsize=10)
plt.legend()
plt.grid()



# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 15:36:46 2018

@author: stu
"""

import sqlite3

# 메모리에다가 db를 구성
conn = sqlite3.connect(":memory:")

# conn에 cursor 생성
c = conn.cursor() 

c.execute("create table contact(name, mobile, email, address)")

c.execute("insert into contact(name, mobile, email, address) values('홍길동','010','100@','100')")

c.execute("select*from contact")

c.fetchone()

c.fetchone()

c.execute("insert into contact(name, mobile, email, address) values('박찬호','010','103','102')")

c.execute("select*from contact")

c.fetchone()

c.fetchone()

c.fetchall()

#영구히 저장되는 것이 아니라서 rollback 수행시 사라짐
conn.rollback()

#영구히 저장
conn.commit()


#커서닫기
c.close()
#connect(메모리)닫기
coon.close()

conn=sqlite3.connect(":memory:")

c = conn.cursor()
# 커서와 메모리를 close했기 때문에 안의 내용(table) 사라짐
c.exectue("select*from contact")

c.close()

conn.close()

# 파일로 떨어뜨리면 close한 이후에도 계속사용 가능
conn=sqlite3.connect("c:/data/insa.db")

c = conn.cursor()

c.execute("create table emp1(id integer, name text, sal integer)")

c.execute("insert into emp1(id,name,sal) values(1,'권아름',1000)")

c.execute("insert into emp1(id,name,sal) values(2,'박찬호',2000)")

c.execute("select * from emp1")

c.fetchall()

conn.commit()

c.close()

conn.close()

#
conn=sqlite3.connect("c:/data/insa.db")

c = conn.cursor()

#내가 만든 테이블 보기
c.execute("select name from sqlite_master where type='table'")

c.fetchall()

#PRAGMA table_info(테이블명) : 테이블의 정보 확인 (sql에서 desc)
c.execute("PRAGMA table_info(emp1)")

c.fetchall()
# values를 ?,?,?로 두고 후에 입력값 처리
c.execute("insert into emp1(id,name,sal) values(?,?,?)",(3,'나얼',3000))	

c.execute("select * from emp1")

c.fetchall()

#입력값 처리
insert_sql="insert into emp1(id,name,sal) values(?,?,?)"	
c.execute(insert_sql,(4,'윤건',4000))

c.execute("select * from emp1")

c.fetchall()


conn.commit()

c.execute("select * from emp1")

#fetchmany(4) : 4개만 보기
c.fetchmany(4)

c.execute("update emp1 set sal=6000 where id=1")

c.execute("select * from emp1 where id=1")

c.fetchone()

conn.rollback()

c.execute("select * from emp1 where id=1")

c.fetchone()

c.execute("delete from emp1 where id=2")

c.execute("select * from emp1")

c.fetchall()

#컬럼 추가
c.execute("alter table emp1 add column deptno integer")		

c.fetchall()

c.execute("select * from emp1")

c.fetchall()

c.execute("drop table emp1")

c.execute("create table emp(id integer,name text,sal integer,deptno integer)")

c.execute("insert into emp(id,name,sal,deptno) values(1,'홍길동',1000,10)")

c.execute("insert into emp(id,name,sal,deptno) values(2,'박찬호',2000,20)")

c.execute("insert into emp(id,name,sal,deptno) values(3,'나얼',3000,30)")

c.execute("insert into emp(id,name,sal,deptno) values(4,'윤건',4000,40)")

conn.commit()

c.execute("select * from emp")

c.fetchall()

c.execute("create table dept(deptno integer, dname text)")

c.execute("insert into dept(deptno,dname) values(10,'총무부')")

c.execute("insert into dept(deptno,dname) values(20,'영업1')")

c.execute("insert into dept(deptno,dname) values(30,'영업2')")

c.execute("insert into dept(deptno,dname) values(40,'분석팀')")

conn.commit()

c.execute("select * from dept")

c.fetchall()

c.execute("insert into emp(id,name,sal,deptno) values(5,'김건모',5000,null)")

c.execute("insert into dept(deptno,dname) values(50,'인사팀')")

conn.commit()

c.execute("select * from emp")

c.fetchall()

c.execute("select * from dept")

c.fetchall()

#join은 ANSI표준으로 지원함
c.execute("select emp.id,emp.name,emp.deptno,dept.dname from emp inner join dept on emp.deptno=dept.deptno")	

#emp.deptno가 null인 김건모는 출력되지 않음
c.fetchall()



#20180928 - 아름 필기
20180928


# Anaconda Prompt에서
pip install beautifulsoup4


# Spyder에서
from bs4 import BeautifulSoup

html="""
<html>								html은 트리형식
	<body>
		<h1> 스크래핑 </h1>
			<p> 웹페이지 분석하기 </p>
			<p> 데이터 정제작업하기 </p>
 			<p> 데이터 정제작업하기2 </p>
	</body>
</html>
"""

soup=BeautifulSoup(html,"html.parser")		parser라는 분석기를 돌려야함

soup
Out[6]: 

<html>
<body>
<h1> 스크래핑 </h1>
<p> 웹페이지 분석하기 </p>
<p> 데이터 정제작업하기 </p>
</body>
</html>


# 원하는 태그 내용을 가져오기
h1=soup.html.body.h1				h1 내용을 긁어오기

h1
Out[9]: <h1> 스크래핑 </h1>

h1.string					변수.string : 태그는 제거하고 문자만 출력
Out[10]: ' 스크래핑 '

p1=soup.html.body.p				첫번째 p 내용을 긁어오기

p1.string
Out[13]: ' 웹페이지 분석하기 '

p2=p1.next_sibling				태그와 태그 사이에는 \n이 내부적으로 있음
						따라서 두번째 태그 내용을 보고싶으면 next_sibling 두번해야 함
p2.string
Out[21]: '\n'					

p2=p1.next_sibling.next_sibling			첫번째.next_sibling.next_sibling : 두번째 p 내용을 긁어오기
										   p2는 p1의 형제
p2.string
Out[19]: ' 데이터 정제작업하기 '

p3=p2.next_sibling.next_sibling			세번째 p 내용 긁어오기, 두번째 p를 기준으로 next_sibling.next_sibling

p3.string
Out[33]: ' 데이터 정제작업하기2 '


html="""
<html>
<body>
<h1 id='title'> beautifulsoup </h1>			id라는 속성을 부여
<p id='subtitle'> 스크래핑 </p>
<p> 데이터 추출하기 </p>
</body>
</html>
"""

soup=BeautifulSoup(html,"html.parser")

soup.find(id='title').string
Out[56]: ' beautifulsoup '

title=soup.find(id='title')

title.string
Out[58]: ' beautifulsoup '

soup.find(id='subtitle').string
Out[59]: ' 스크래핑 '


html="""
<html>
	<body>
		<ul>
			<li> <a href="http://www.itwill.com"> 아이티윌 </a> </li>		링크를 생성하는 태그
			<li> <a href="http://www.naver.com"> 네이버 </a> </li>
	</body>
</html>
"""

soup=BeautifulSoup(html,"html.parser")

a1=soup.html.body.ul.li.a

a1.string
Out[49]: ' 아이티윌 '

soup.find('a')							find : 해당 태그의 첫번째 것만 찾아줌
Out[63]: <a href="http://www.itwill.com"> 아이티윌 </a>

soup.find('a').string
Out[64]: ' 아이티윌 '

soup.find_all('a')						find_all : 해당 태그의 모든 내용을 찾아줌
Out[65]: 
[<a href="http://www.itwill.com"> 아이티윌 </a>,
 <a href="http://www.naver.com"> 네이버 </a>]

a=soup.a

a								첫번째 것만 보여줌
Out[72]: <a href="http://www.itwill.com"> 아이티윌 </a>

a.attrs								a안의 속성의 값을 보여줌
Out[70]: {'href': 'http://www.itwill.com'}

'href' in a.attrs						href라는 key가 a.attrs에 존재하는가
Out[71]: True

a['href']							href의 values만 보기
Out[75]: 'http://www.itwill.com'

a.attrs['href']
Out[76]: 'http://www.itwill.com'


link=soup.find_all('a')						find_all을 통해 'a'속성의 값을 출력하면 list 형태이므로 string이 바로 안됨

link
Out[79]: 
[<a href="http://www.itwill.com"> 아이티윌 </a>,
 <a href="http://www.naver.com"> 네이버 </a>]

for i in link:
    print(i.attrs['href'])
    print(i.string)
    
http://www.itwill.com
 아이티윌 
http://www.naver.com
 네이버 

for i in link:
    print(i.attrs['href'])
    print(i.get_text())
    
http://itwill.co.kr
 아이티윌 
http://www.naver.com
 네이버 

link=soup.findAll('a')

for i in link:
    print(i.attrs['href'])
    print(i.string)
    
http://itwill.co.kr
 아이티윌 
http://www.naver.com
 네이버 

for i in link:
    print(i.attrs['href'])
    print(i.get_text())
    
http://itwill.co.kr
 아이티윌 
http://www.naver.com
 네이버



<html>
<head>
	<title> 나의 홈페이지 </title>
</head>
	
<body>
<p align ='center'> 환영합니다 </p>
<p align ='left'> 이름 : 권아름 <br> 나이 : 25 <br> 취미 : 음악감상 </p>
<p align ='right'> 오늘 하루도 행복하세요...</p>
<a href = 'http://itwill.co.kr' class='cafe1' id='link1'> 아이티윌 </a>
<a href = 'http://www.naver.com' class='cafe2' id='link2'> 네이버 </a>
<a href = 'http://www.google.com' class='cafe3' id='link3'> 구글 </a>
</body>
</html>

위의 내용을 c:/data에 a.html로 저장 (파일형식 : 모든파일, 인코딩 : UTF-8)


with open("c:/data/a.html",encoding='UTF8') as html:				a.html파일을 불러와서 분석하기
    soup=BeautifulSoup(html,'html.parser')
  
soup.find('title').string
Out[91]: ' 나의 홈페이지 '

soup.find('body')
Out[92]: 
<body>
<p align="center"> 환영합니다 </p>
<p align="left"> 이름 : 권아름 <br/> 나이 : 25 <br/> 취미 : 음악감상 </p>
<p align="right"> 오늘 하루도 행복하세요...</p>
<a class="cafe1" href="http://itwill.co.kr" id="link1"> 아이티윌 </a>
<a class="cafe2" href="http://www.naver.com" id="link2"> 네이버 </a>
<a class="cafe3" href="http://www.google.com" id="link3"> 구글 </a>
</body>

p=soup.find_all('p')

p
Out[95]: 
[<p align="center"> 환영합니다 </p>,
 <p align="left"> 이름 : 권아름 <br/> 나이 : 25 <br/> 취미 : 음악감상 </p>,
 <p align="right"> 오늘 하루도 행복하세요...</p>]

for i in p:
    print(i.string)
    
 환영합니다 
None						p라는 태그안에 글자열을 변경하는 태그가 사용된 경우 None으로 출력
 오늘 하루도 행복하세요...

for i in p:
    print(i.get_text())				get_text() : text를 모두 출력
    
 환영합니다 
 이름 : 권아름  나이 : 25  취미 : 음악감상 
 오늘 하루도 행복하세요...

p=soup.findAll('p')

for i in p:
    print(i.get_text())
    
 환영합니다 
 이름 : 권아름  나이 : 25  취미 : 음악감상 
 오늘 하루도 행복하세요...

soup.find('body')
Out[104]: 
<body>
<p align="center"> 환영합니다 </p>
<p align="left"> 이름 : 권아름 <br/> 나이 : 25 <br/> 취미 : 음악감상 </p>
<p align="right"> 오늘 하루도 행복하세요...</p>
<a class="cafe1" href="http://itwill.co.kr" id="link1"> 아이티윌 </a>
<a class="cafe2" href="http://www.naver.com" id="link2"> 네이버 </a>
<a class="cafe3" href="http://www.google.com" id="link3"> 구글 </a>
</body>

soup.find('body').string			아무것도 안나옴

soup.find('body').get_text()			\n으로 구분되서 text 출력
Out[106]: '\n 환영합니다 \n 이름 : 권아름  나이 : 25  취미 : 음악감상 \n 오늘 하루도 행복하세요...\n 아이티윌 \n 네이버 \n 구글 \n'

soup.find('body').get_text(strip=True)		모두 붙여서 출력
Out[107]: '환영합니다이름 : 권아름나이 : 25취미 : 음악감상오늘 하루도 행복하세요...아이티윌네이버구글'

body=soup.find('body')

for i in body:
    print(i.string)
    
 환영합니다 


None


 오늘 하루도 행복하세요...


 아이티윌 


 네이버 


 구글 

for i in body:
    print(i.get_text())							get_text()는 find_all / findAll에서만 되는 메소드
AttributeError: 'NavigableString' object has no attribute 'get_text'

body=soup.find_all('body')

for i in body:
    print(i.get_text())
    

 환영합니다 
 이름 : 권아름  나이 : 25  취미 : 음악감상 
 오늘 하루도 행복하세요...
 아이티윌 
 네이버 
 구글 

body=soup.findAll('body')

for i in body:
    print(i.get_text())
    

 환영합니다 
 이름 : 권아름  나이 : 25  취미 : 음악감상 
 오늘 하루도 행복하세요...
 아이티윌 
 네이버 
 구글


soup.find('a')
Out[114]: <a class="cafe1" href="http://itwill.co.kr" id="link1"> 아이티윌 </a>

a=soup.find_all('a')

for i in a:
    print(i.get_text())
    
 아이티윌 
 네이버 
 구글 

a=soup.findAll('a')

for i in a:
    print(i.get_text())
    
 아이티윌 
 네이버 
 구글


a1=soup.findAll('a',{'class':'cafe1'})				같은 레벨의 a태그가 여러개 있을 경우 class 또는 id 속성을 통해서 찾기

a1
Out[128]: [<a class="cafe1" href="http://itwill.co.kr" id="link1"> 아이티윌 </a>]

for i in a1:
    print(i.attrs['href'])
    print(i.get_text())
    
http://itwill.co.kr
 아이티윌 

a2=soup.findAll('a',{'class':'cafe2'})

a2
Out[131]: [<a class="cafe2" href="http://www.naver.com" id="link2"> 네이버 </a>]

for i in a2:
    print(i.get_text())
    
 네이버 

a3=soup.findAll('a',{'class':'cafe3'})

a3
Out[133]: [<a class="cafe3" href="http://www.google.com" id="link3"> 구글 </a>]

for i in a3:
    print(i.get_text())
    
 구글


a1=soup.find('a',{'class':'cafe1'})

for i in a1:
    print(i.get_text())					find에서는 get_text()를 쓸 수 없음
    
AttributeError: 'NavigableString' object has no attribute 'get_text'

for i in a1:
    print(i.string)					find를 쓸 때는 string를 사용해야함
    
 아이티윌 

for i in a1:
    print(i.attrs['href'])				find에서는 attrs를 쓸 수 없음
    print(i.string)

AttributeError: 'NavigableString' object has no attribute 'attrs'


a1=soup.findAll('a',{'id':'link1'})			id라는 속성을 이용해서 찾기

for i in a1:
    print(i.attrs['href'])
    print(i.get_text())
    
http://itwill.co.kr
 아이티윌 

a2=soup.findAll('a',{'id':'link2'})

for i in a2:
    print(i.attrs['href'])
    print(i.get_text())
    
http://www.naver.com
 네이버 

for i in soup.findAll('a',{'id':'link3'}):
    print(i.attrs['href'])
    print(i.get_text())
    
http://www.google.com
 구글 


soup.findAll(class='cafe1')
                     ^
SyntaxError: invalid syntax			오류남, class_ 꼭 해줘야함

soup.findAll(class_='cafe1')
Out[152]: [<a class="cafe1" href="http://itwill.co.kr" id="link1"> 아이티윌 </a>]

for i in soup.findAll(class_='cafe1'):
    print(i.attrs['href'])
    print(i.get_text())
    
http://itwill.co.kr
 아이티윌 

for i in soup.findAll(id='link1'):		id는 _하면 안됨
    print(i.attrs['href'])
    print(i.get_text())
    
http://itwill.co.kr
 아이티윌


for i in soup.findAll('a'):
    print(i.get('href'))			href 속성의 값을 출력
    
http://itwill.co.kr
http://www.naver.com
http://www.google.com

soup.findAll(['a','p'])				여러 태그를 동시에 보고자 할 때는 [] 사용
Out[159]: 
[<p align="center"> 환영합니다 </p>,
 <p align="left"> 이름 : 권아름 <br/> 나이 : 25 <br/> 취미 : 음악감상 </p>,
 <p align="right"> 오늘 하루도 행복하세요...</p>,
 <a class="cafe1" href="http://itwill.co.kr" id="link1"> 아이티윌 </a>,
 <a class="cafe2" href="http://www.naver.com" id="link2"> 네이버 </a>,
 <a class="cafe3" href="http://www.google.com" id="link3"> 구글 </a>]

for i in soup.findAll(['a','p']):
    print(i.get_text())
    
 환영합니다 
 이름 : 권아름  나이 : 25  취미 : 음악감상 
 오늘 하루도 행복하세요...
 아이티윌 
 네이버 
 구글 



import urllib.request as req						BeautifulSoup은 다운로드 기능이 없어서 urllib.request사용

url="http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp"

res=req.urlopen(url)

res
Out[166]: <http.client.HTTPResponse at 0x8c278d0>

soup=BeautifulSoup(res,'html.parser')

soup.find('title').string
Out[170]: '기상청 육상 중기예보'

http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp
인터넷 화면에서 오른쪽버튼 - 소스보기
크롬으로 들어가면 자동으로 태그가 보임 (오른쪽 버튼 - 검사)



# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 09:49:43 2018

@author: stu
"""

from bs4 import BeautifulSoup

#html 가상으로 만들기

html="""
<html>
<body>
<div id = 'lecture1'>
<h1> 데이터 과학 </h1>
</div>
<div id = 'lecture2'>
<h1> 빅데이터분석 </h1>
<ul class = 'subject'>
<li> SQL </li>
<li> R </li>
<li> PYTHON </li>
</ul> 
</div>
</body>
</html>
"""

#분석기를 돌려야하고, 분석기는 저장해 둬야함 eg. soup

soup = BeautifulSoup(html, 'html.parser')


#h1 찾기: body는 생략가능 
##방법1
soup.html.div.h1.string                                                        
##방법2
soup.find('h1').string

#태그 모두 제거
soup.find('h1').get_text()
soup.find('h1').text

#변수에 h1 담기
h1 = soup.find('h1')
h1.string

#두번째 h1찾기
h2 = soup.find(id='lecture2')
h2.find('h1').string                                                            

#Python 찾기 (webpage에서 출력되는것;li목록이 다른 것에도 있을 것이라는 가정하에 뽑아내야함) 
#class_
soup.find('ul', class_='subject').string
#li가 여러개이기 때문에 get_text로 찾아야 함 -> 그러나 \n도 출력되기 때문에 다음 번과 같이 한다.
soup.find('ul', class_='subject').get_text()

ul = soup.find('ul', class_='subject')
for i in ul:
    print(i.string)
 
ul = soup.find('ul', class_='subject')                                          # 오류  
for i in ul:
    print(i.get_text())

for i in ul:                                                                   # 오류 
    print(i.text)
    
#find_all : 다 찾는 것  -> string으로는 찾아지지 않는다. : 따라서 get_text()를 이용해야함!
ul = soup.find_all('ul', class_='subject')
for i in ul:
    print(i.stirng)

ul = soup.find_all('ul', class_='subject')
for i in ul:
    print(i.get_text())

# 위와 유사한 method findAll
ul = soup.findAll('ul', class_='subject')
for i in ul:
    print(i.text)
    
# class 속성을 찾아야할 때는 꼭 class_로 넣어주거나 dictonary 모양으로 만들어 {'class':'subject'} 찾거나 하면 된다. (방법2가지)
ul = soup.find_all('ul', {'class':'subject'})
for i in ul:
    print(i.text)
    
    
■ css(cascading stylesheets)    
#stylesheets(eg. div..) 들에 대해서 편하게 분석하는 제공 툴 
□  select_one은 css 선택자 요소 하나를 추출   #find와 같은 역할을 한다. 

soup.select_one('div > h1').string      #>은 계층에 대한 표현

#두번째 h1을 찾기 -> id의 속성을 통해서 찾을 수 있음 
#div안에 id값을 표시할 때는 #(기호 샵)을 사용한다. 
soup.select_one('div#lecture1 > h1').string 

soup.select_one('div#lecture2 > h1').string 

                
# div.content 
-> .(점)은 그 안에 들어 있는 class를 의미한다. 


□ select는 css 선택자로 요소 여러개를 리스트로 추출한다. (기호의 의미 #:id, .:class를 의미)
s = soup.select('div#lecture2 > ul.subject > li')
for i in s:
    print(i.string)



■ 매번 url이 바뀔 경우에 crawling을 할 경우 
환율 정보 예시> 
https://finance.naver.com/marketindex/?tabSel=exchange#tab_section
https://finance.naver.com/marketindex


예를 들어 미국 환율만 뽑아 낼 경우 -> F12 -> 요소검사 -> span.value -> class가 value해당하는 string 값을 뽑아 내면 된다. 
<span class="value">1,111.80</span>

□url 내용을 가져오기 
from bs4 import BeautifulSoup
import urllib.request as req 

url = "https://finance.naver.com/marketindex"
res = req.urlopen(url)  #url에 있는 site내용을 가져옴 

#분석하기
soup = BeautifulSoup(res,"html.parser")
dollar = soup.select_one('div.head_info > span.value').string
print('USD/KRW', dollar)

□ copy> copy selector 으로 상위 정보와 함께 가져오기 ; 
1) #exchangeList > li.on > a.head.usd > div > span.value
2) soup.select_one을 통해서 span.vaule 뽑아내기 

1)    
#달러 찾기 
soup.select_one("#exchangeList > li.on > a.head.usd > div > span.value").string

#엔화 찾기
soup.select_one("a.head.jpy > div > span.value").string
soup.select_one("div.head_info.point_dn > span.value").string

#중국 원화 찾기
soup.select_one("a.head.cny > div > span.value").string


■ naver 실시간 검색
url1 = "https://datalab.naver.com/keyword/realtimeList.naver"
res = req.urlopen(url1)

soup = BeautifulSoup(res,"html.parser")
soup

막히네요.. 


#content > div > div.keyword_carousel > div > div > div:nth-child(1) > div > div > ul
ul = soup.find('ul', class_='rank_list')                                          # 오류  
for i in ul:
    print(i.text)


# =============================================================================
# 오후 수업 시작
# =============================================================================
html = """
<ul id = '조선왕'>
<li id = '태조'> '이성계' </li>
<li id = '정조'> '이방과' </li>
<li id = '태종'> '이방원' </li>
<li id = '세종'> '이도' </li>
<li id = '문종'> '이향' </li>
</ul>
"""

soup = BeautifulSoup(html, "html.parser")

#세종의 이름 뽑아내기; 세종의 id 속성 뽑아내기
soup.select_one("#세종").string
soup.select_one("#세종").text
soup.select_one("li#세종").string
soup.select_one("ul > li#세종").string
soup.select_one("#조선왕 #세종").string
soup.select_one("ul#조선왕 > li#세종").string
soup.select_one("li[id=세종]").string
#li:nth-of-type: li의 순서를 제한하여 id 속성 뽑아내기
soup.select_one("li:nth-of-type(4)").string
soup.select('li')

# list 형식으로 되어있는 text를 추출하기
for i in soup.select('li'):
    print(i.text)
    
soup.select('li')[0].string
soup.select('li')[3].string

#환율정보 nth-of-type 사용하기 (여러번 사용할 경우, 오류가 발생한다.-> 그땐 변수에 담아놓고 다시 시작하는 방법을 사용할 수 있다.)
url = "https://finance.naver.com/marketindex"
res = req.urlopen(url)
soup = BeautifulSoup(res,"html.parser")
l = soup.select_one('div.market1 > div.data > ul.data_lst > li:nth-of-type(1)')
l.select_one("span:nth-of-type(2)").string

#li:nth-of-type(2)
l = soup.select_one('div.market1 > div.data > ul.data_lst > li:nth-of-type(2)')
l.select_one("span:nth-of-type(2)").string

#li:nth-of-type(3)
l = soup.select_one('div.market1 > div.data > ul.data_lst > li:nth-of-type(3)')
l.select_one("span:nth-of-type(2)").string

#market2
l = soup.select_one('div.market2 > div.data > ul.data_lst > li:nth-of-type(1)')
l.select_one("span:nth-of-type(2)").string

#market3
l = soup.select_one('div.market3 > div.data > ul.data_lst > li:nth-of-type(1)')
l.select_one("span:nth-of-type(2)").string



# =============================================================================
# 개인실습: 네이버 부동산
# =============================================================================
url_reals = "https://land.naver.com/article/articleList.nhn?rletNo=97&rletTypeCd=A01&tradeTypeCd=A1"
real_state = req.urlopen(url_reals)
soup = BeautifulSoup(real_state, "html.parser")

#홀수만 매물 정보 검색가능
info = soup.select_one('tbody > tr:nth-of-type(1)')
info

price = info.select_one('td:nth-of-type(7)')
test = price.select_one('td > div> strong#')
test
                 
price.select_one('td > div > strong')


e.select_one('td:nth-of-type(7) > div > strong title')



# sale 타입
info.select_one('td:nth-of-type(1)')
info.select_one('td:nth-of-type(1) > div#inner')

# 특징
info.select_one('td:nth-of-type(2)')
# 단지정보 
info.select_one('td:nth-of-type(3)')
# 면적 
info.select_one('td:nth-of-type(4)')
# 동정보
info.select_one('td:nth-of-type(5)')
# 층수 정보
info.select_one('td:nth-of-type(6)')
# 중개업소 
info.select_one('td:nth-of-type(8)')


# =============================================================================
# 동아일보로 부터 인공지능 링크값 가져오기 
# =============================================================================
#contents > div:nth-child(9) > div > div:nth-child(2) > div.t > p.tit > a


url_ai = "http://news.donga.com/search?check_news=1&more=1&sorting=1&range=1&search_date=&query=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5"
ai = req.urlopen(url_ai)
soup = BeautifulSoup(ai, "html.parser")
soup

#
a = soup.select_one('.searchCont > div:nth-of-type(3) > div.t > p.tit > a')

#url 불러오기
lst = []
for i in soup.select('div.searchList > div.t > p.tit'):
    print(i.select_one('a')['href'])
    lst.append(i.select_one('a')['href'])


#본문 기사 정보 긁어오기 
lst    

cn = 0
txt = []
for i in lst:
    print(i)
    res = req.urlopen(i).read().decode('utf-8')
    soup = BeautifulSoup(res, 'html.parser')
    result = soup.select('div.article_txt')
    
    
    for i in result:
        #print(i.text)
       txt.append(i.text)
 txt
    
new_txt = []

for i in range(0,15):
    new_txt.append(txt[i][0:txt[i].find('Copyright')])
     

# =============================================================================
# 설치하기 : konlpy 
# =============================================================================
Anaconda Prompt 
-설치 pip install konlpy 
- Java base 로 구현되어 있음 
- Java base 설치가 되어있어야 구현이 가능함 

- konlpy 실행이 안될 경우: pip install jpype1
- pip install jpype1 도 안될 경우: 밑의 step3개를 따르세요.
 
#step1
https://konlpy-ko.readthedocs.io/ko/v0.4.3/install/

#step2
https://www.lfd.uci.edu/~gohlke/pythonlibs/#jpype
JPype allows full access to Java class libraries. 

python 버전 확인 -> 3.6이기 때문에 / 운영체제 64bit이므로 
다운로드 : JPype1‑0.6.3‑cp36‑cp36m‑win_amd64.whl 
저장: c드라이브에 

#step3 
anaconda prompt을 관리자 권한으로 실행 
-> command line에서 cd c:\로 만들고 다시 설치 
-> dir *.whl # 파일이 있는지 확인

pip install JPype1‑0.6.3‑cp36‑cp36m‑win_amd64.whl

# =============================================================================
# konlpy 실행시키기
# =============================================================================
#java 경로 설정 
1) jdk의 위치 확인 후 
2) 시스템 고급 설정 > 환경변수
3) stu에 대한 사용자 변수 > 새로만들기
    -변수이름: JAVA_HOME
    -변수값: jdk 위치
4) 시스템 변수
    ;JAVA_HOME

#konlpy 실행 
from konlpy.tag import Twitter

twitter = Twitter()

malist = twitter.pos("아버지 가방에 들어가신다.", norm=True, stem=True)

print(malist)

pos: 형태소 분석
norm : 그래욬ㅋㅋㅋㅋ -> 그래요 로 바꿔줌
stem : 그렇다 원형을 찾아 준다

# 그래욬ㅋㅋㅋ 분석 
slang = twitter.pos('그래욬ㅋㅋㅋ', norm=True,  stem = True)
print(slang)

#txt분석 
txt = "텍스트 마이닝은 텍스트 형태의 데이터를 수학적 알고리즘에 기초하여 수집 , 처리 분석, 요약하는 연구 기법을 통칭하는 용어이다."

twitter.nouns(txt)



# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 09:45:42 2018

@author: stu
"""

# =============================================================================
# KoNLPY(코엔엘파이) : 한국어 정보처리를 위한 파이썬 패키지
# =============================================================================

▣ KoNLPY(코엔엘파이) : 한국어 정보처리를 위한 파이썬 패키지

■ 형태소(morpheme)
- 언어학에서 일정한 의미가 있는 가장 작은 말의 단위를 뜻함 
- 자연어 처리에서 토큰으로 형태소를 이용한다. 

■ 형태소 분석(morphological analysis)
- 단어로 부터 어근, 접두사, 접미사, 품사 등 다양한 언어적 속성을 파악하고 이를 이용하여 형태소를 찾아내거나 처리하는 작업

■ KoNLPy
- 형태소 분석을 하기위해서 필요한 라이브러리를 모아 놓은 패키지이다.

■ 형태소 분석기 종류
    □ Twitter
    - 트위터 코리아에서 개발 
    - https://github.com/twitter/twitter-korean-text
    
    □ Kkma(꼬꼬마)
    - 서울대학교 개발
    - http://kkma.snu.ac.kr
    
    □ Hannaum(한나눔)
    - KAIST
    - http://semanticweb.kaist.ac.kr/hannanum
    
    □ Mecav(매카브)
    - 일어용 형태소 분석기를 한국어를 사용할 수 있도록 수정
    - http://bitbucket.org/eunjeon/mecab-ko
    
    □ Komoran(코모란)
    - shineware에서 개발 
    - http://github.com/shin285/KOMORAN

■ 설치 
pip install konlpy
pip install jpype1

■ 꼬꼬마 실행
from konlpy.tag import Kkma
kkma = Kkma() 

txt = '통찰력은 사물이나 현상의 원인과 결과를 이해하고 간파하는 능력이다. 통찰력을 얻는 좋은 방법은 독서이다'
txt1 = '통찰력은 사물이나 현상의 원인과 결과를 이해하고 간파하는 능력이고 통찰력을 얻는 좋은 방법은 독서이다'

#문장을 분석 
kkma.sentences(txt)
kkma.sentences(txt1)

#형태소 분석
kkma.pos(txt)

#명사 분석
kkma.nouns(txt)

■ Twitter 실행
from konlpy.tag import Twitter
twitter = Twitter()

#형태소 분석
twitter.pos(txt)

#명사 분석
twitter.nouns(txt)

#트위터에서 추가적으로 제공하는 부분: 맞춤법, 원형
txt = '그래욬ㅋㅋㅋㅋ'
twitter.pos(txt, norm=True, stem=True)
norm: '그래욬ㅋㅋㅋ -> 그래요'
stem: 그렇다 원형으로 찾아준다.

#꼬꼬마와 트위터 비교하기
txt = '텍스트 마이닝은 텍스트 형태의 데이터를 수학적 알고리즘에 기초하여 수집, 처리, 분석, 요약하는 연구기법을 통칭하는 용어이다.'

kkma.pos(txt)
twitter.pos(txt)

#konlpy의 corpus위치 정보
C:\Users\stu\Anaconda3\Lib\site-packages\konlpy\data\corpus

■ nltk 설치/실행: 
pip install nltk

import nltk

from konlpy.corpus import kolaw
#kolaw 디렉토리에 있는 내용을 보여줌 
kolaw.fileids()
#파일 읽어 들이기 
doc_ko = kolaw.open('constitution.txt').read()
#twitter로 명사를 뽑아내고 별도의 변수에 저장
tokens_ko = twitter.nouns(doc_ko)
tokens_ko
# 단어의 수를 세기 -> dictonary형으로 자료형으로 만들어 없으면 새로운 방을 만들어 counting, 있으면 누적해서 counting
# 단어의 수를 세기: nltk method 이용하기
ko = nltk.Text(tokens_ko)
# token이 만들어짐
ko.tokens
#단어개수를 뽑아줌
len(ko.tokens) 
#단어의 중복제거
len(set(ko.tokens))
#단어의 빈도수 
ko.vocab()

■ plot 만들기 -> 한국어를 깨지지 않게 하기 위해 폰트를 불러와야 함 
import matplotlib.pyplot as plt
from matplotlib import font_manager ,rc
font_name = font_manager.FontProperties(fname="c:\windows\Fonts\malgun.ttf").get_name()
rc('font',family=font_name)

# plot 만들기 
plt.figure(figsize=(12,6))
ko.plot(50) #상위 50개만 보여주기
plt.show()

#빈도 상위 10개 단어 보여주기 
ko.vocab().most_common(10)


■ 분석해야할 문서는 임의로 절대적 경로를 불러들일 수 없고, corpus위치 정보에 넣어야 함
- 문재인 대통령 취임사를 바탕으로 다시 분석하기
kolaw.fileids()

doc_ko = kolaw.open('moon_speech.txt').read()
#twitter로 명사를 뽑아내고 별도의 변수에 저장
tokens_ko = twitter.nouns(doc_ko)
tokens_ko
# 단어의 수를 세기 -> dictonary형으로 자료형으로 만들어 없으면 새로운 방을 만들어 counting, 있으면 누적해서 counting
# 단어의 수를 세기: nltk method 이용하기
ko = nltk.Text(tokens_ko)
# token이 만들어짐
ko.tokens
#단어개수를 뽑아줌
len(ko.tokens) 
#단어의 중복제거
len(set(ko.tokens))
#단어의 빈도수 
ko.vocab()


import matplotlib.pyplot as plt
from matplotlib import font_manager ,rc
font_name = font_manager.FontProperties(fname="c:\windows\Fonts\malgun.ttf").get_name()
rc('font',family=font_name)

# plot 만들기 
plt.figure(figsize=(12,6))
ko.plot(20) #상위 20개만 보여주기
plt.show()

#빈도 상위 10개 단어 보여주기 
ko.vocab().most_common(10)

■ 불용어(필요없는글자;stopword) 제거하기 
#리스트 변수에 불용어 만들기 
stopword=['.',',','(',')','의','지','에','간','것','곳','달','저','이','과','향']
#리스트 내장객체 생각해보기  (eachword가 stopword에만 없어야 ko안에서 eachwod를 리스트로 만들기)
ko = [eachword for eachword in ko if eachword not in stopword]
#토큰작업
ko = nltk.Text(ko)
# token이 만들어짐
ko.tokens
#단어개수를 뽑아줌
len(ko.tokens) 
#단어의 중복제거
len(set(ko.tokens))
#단어의 빈도수 
ko.vocab()
ko.vocab().most_common(10)

■ 다양한 method 
#특정단어 개수 세기
ko.count('국민')
#특정단어와 연관있는 단어(특정단어 side에 있는 단어)
ko.concordance('약속')
ko.concordance('문재인')

■ wordcloud install하기/ 실행하기
#Anaconda Prompt에 설치하기
pip install wordcloud
# 실행하기 (spyder에서 )
from wordcloud import WordCloud
#data 변수에 상위 30개 단어 담기
data = ko.vocab().most_common(30)
#wordcloud 만들기
wordcloud = WordCloud(font_path="c:\Windows\Fonts\malgunbd.ttf", background_color='white', width=1000, height=800).generate_from_frequencies(dict(data))
plt.figure(figsize=(10,10))
plt.imshow(wordcloud)
plt.axis("off")
plt.show()

# =============================================================================
# 꼬꼬마로 문재인 취임사 분석하기 (twitter로 분석한 부분 kkma로만 바꾸고 다시 실행)
# =============================================================================
■ 꼬꼬마로 분석하기 
doc_ko = kolaw.open('moon_speech.txt').read()
#kkoma로 명사를 뽑아내고 별도의 변수에 저장
tokens_ko = kkma.nouns(doc_ko)
tokens_ko
# 단어의 수를 세기 -> dictonary형으로 자료형으로 만들어 없으면 새로운 방을 만들어 counting, 있으면 누적해서 counting
# 단어의 수를 세기: nltk method 이용하기
ko = nltk.Text(tokens_ko)
# token이 만들어짐
ko.tokens
#단어개수를 뽑아줌
len(ko.tokens) 
#단어의 중복제거
len(set(ko.tokens))
#단어의 빈도수 
ko.vocab()


import matplotlib.pyplot as plt
from matplotlib import font_manager ,rc
font_name = font_manager.FontProperties(fname="c:\windows\Fonts\malgun.ttf").get_name()
rc('font',family=font_name)

# plot 만들기 
plt.figure(figsize=(12,6))
ko.plot(20) #상위 20개만 보여주기
plt.show()

#빈도 상위 10개 단어 보여주기 
ko.vocab().most_common(10)

■ 불용어(필요없는글자;stopword) 제거하기 
#리스트 변수에 불용어 만들기 
stopword=['.',',','(',')','의','지','에','간','것','곳','달','저','이','과','향']
#리스트 내장객체 생각해보기  (eachword가 stopword에만 없어야 ko안에서 eachwod를 리스트로 만들기)
ko = [eachword for eachword in ko if eachword not in stopword]
#토큰작업
ko = nltk.Text(ko)
# token이 만들어짐
ko.tokens
#단어개수를 뽑아줌
len(ko.tokens) 
#단어의 중복제거
len(set(ko.tokens))
#단어의 빈도수 
ko.vocab()
ko.vocab().most_common(10)

■ 다양한 method 
#특정단어 개수 세기
ko.count('국민')
#특정단어와 연관있는 단어(특정단어 side에 있는 단어)
ko.concordance('약속')
ko.concordance('문재인')

■ wordcloud install하기/ 실행하기
#Anaconda Prompt에 설치하기
pip install wordcloud
# 실행하기 (spyder에서 )
from wordcloud import WordCloud
#data 변수에 상위 30개 단어 담기
data = ko.vocab().most_common(30)
#wordcloud 만들기
wordcloud = WordCloud(font_path="c:\Windows\Fonts\malgunbd.ttf", background_color='white', width=1000, height=800).generate_from_frequencies(dict(data))
plt.figure(figsize=(10,10))
plt.imshow(wordcloud)
plt.axis("off")
plt.show()

# =============================================================================
# [문제185]동아일보 검색을 토대로 nlp분석
# =============================================================================

from bs4 import BeautifulSoup

#url가져오기
import urllib.request as req 

url_ai = 'http://news.donga.com/search?check_news=1&more=1&sorting=1&range=1&search_date=&query=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5'
ai = req.urlopen(url_ai)

#분석하기
soup_ai = BeautifulSoup(ai,"html.parser")
soup_ai


a_ai = soup_ai.select_one('.searchCont > div:nth-of-type(3) > div.t > p.tit > a')
a_ai

#url 불러오기
lst = []
for i in soup_ai.select('div.searchList > div.t > p.tit'):
    print(i.select_one('a')['href'])
    lst.append(i.select_one('a')['href'])
    
#본문 기사 정보 긁어오기 
lst   

cn = 0
txt = []
for i in lst:
    print(i)
    res = req.urlopen(i).read().decode('utf-8')
    soup = BeautifulSoup(res, 'html.parser')
    result = soup.select('div.article_txt')
    
    
    for i in result:
        #print(i.text)
       txt.append(i.text)
txt
    
new_txt = []

for i in range(0,15):
    new_txt.append(txt[i][0:txt[i].find('Copyright')])

#converting to list to string 1st way
news = ''
for i in new_txt :
    news +=i

news

#converting list to string 2nd way
str_ai =''.join(new_txt)
str_ai

■ twitter로 분석하기
from konlpy.tag import Twitter
twitter = Twitter()

#token작업 
ai_tokens = twitter.nouns(str_ai)
ai_tokens

# 단어의 수를 세기: nltk method 이용하기
ai = nltk.Text(ai_tokens)
# token이 만들어짐
ai.tokens
#단어개수를 뽑아줌
len(ai.tokens) 
#단어의 중복제거
len(set(ai.tokens))
#단어의 빈도수 
ai.vocab()


import matplotlib.pyplot as plt
from matplotlib import font_manager ,rc
font_name = font_manager.FontProperties(fname="c:\windows\Fonts\malgun.ttf").get_name()
rc('font',family=font_name)

# plot 만들기 
plt.figure(figsize=(12,6))
ai.plot(10) #상위 20개만 보여주기
plt.show()

#빈도 상위 10개 단어 보여주기 
ai.vocab().most_common(10)

■ 불용어(필요없는글자;stopword) 제거하기 
#리스트 변수에 불용어 만들기 
stopword=['.',',','(',')','의','것','등','또','고','수','곳','이','간엔','창','며','명','개','박','원', '때문', '더', '중', '은', '그', '건', '도', '를', '로','라며','위해']
#리스트 내장객체 생각해보기  (eachword가 stopword에만 없어야 ko안에서 eachwod를 리스트로 만들기)
ai = [eachword for eachword in ko if eachword not in stopword]
#토큰작업
ai = nltk.Text(ai)
# token이 만들어짐
ai.tokens
#단어개수를 뽑아줌
len(ai.tokens) 
#단어의 중복제거
len(set(ai.tokens))
#단어의 빈도수 
ai.vocab()
ai.vocab().most_common(1000)


■ wordcloud install하기/ 실행하기
#Anaconda Prompt에 설치하기
pip install wordcloud
# 실행하기 (spyder에서 )
from wordcloud import WordCloud
#data 변수에 상위 30개 단어 담기
data = ai.vocab().most_common(50)
#wordcloud 만들기
wordcloud = WordCloud(font_path="c:\Windows\Fonts\malgunbd.ttf", background_color='white', width=1000, height=800).generate_from_frequencies(dict(data))
plt.figure(figsize=(10,10))
plt.imshow(wordcloud)
plt.axis("off")
plt.show()



#[문제 185] 쌤답 - kkma사용
    #주의해야할 부분
        #기사형식에서 버려야 할 것을 버리고 string으로 저장 (1)
        #파일로 떨어뜨려 저장한 뒤, 파일로 읽어들여 분석하기 (2)

import urllib.request
from bs4 import BeautifulSoup

params = []
for i in range(1,50,15):
    list_url = "http://news.donga.com/search?p="+str(i)+"&query=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5&check_news=1&more=1&sorting=1&search_date=1&v1=&v2=&range=1"

    url = urllib.request.Request(list_url)
    res = urllib.request.urlopen(url, timeout=100).read().decode("utf-8")
    soup= BeautifulSoup(res, "html.parser")
    for link in soup.findAll('p', class_='tit'):
        params.append(link.find('a').get('href'))


txt= []
for i in params:
    #print(i)
    url = urllib.request.Request(i)
    res = urllib.request.urlopen(url).read().decode("utf-8")
    soup= BeautifulSoup(res, "html.parser")
    result = soup.find_all('div',{'class':'article_txt'})
    
    
    for i in result:
        #print(i.text)
       txt.append(i.text)


#기사형식에서 버려야 할 것을 버리고 string으로 저장 (1)
new_text =''
for i in range(0,60):
    new_text = new_text + txt[i][0:txt[i].find('Copyright')] + '\n'
    

import nltk
from konlpy.tag import Kkma
kkma = Kkma()

tokens_ko = kkma.nouns(new_text)
tokens_ko

ko = nltk.Text(tokens_ko)
len(ko.tokens)
len(set(ko.tokens))
ko.vocab()
ko.vocab().most_common(50)


#파일로 떨어뜨려 저장한 뒤, 파일로 읽어들여 분석하기 (2)
with open("c:/data/new_text.txt","w",encoding="utf-8") as file:
    for i in range(0,60):
        file.write(txt[i][0:txt[i].find('Copyright')])


with open("c:/data/new_text.txt","r",encoding="utf-8") as file:
    news = file.read()          #file.read(): 하나의 문서로 그대로 가져옴/ -> readlines으로 하면 안됨; list형식으로 가져오기 때문에 


import nltk
from konlpy.tag import Kkma
kkma = Kkma()

tokens_ko = kkma.nouns(news)
ko = nltk.Text(tokens_ko)
ko.vocab()



# =============================================================================
# wordcloud - 그림 넣기;  파일 참조 wordcloud.txt
# =============================================================================

#설치한 library 목록을 보여줌 
pip.exe list 

#공학쪽 library: scipy 
- scipy 확인하기 


from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

#UTF-8이 오류가 나서 ANSI 표준으로 바꿔 불러왔음 
with open("c:/data/moon.txt","r") as file:
	text = file.read()



from scipy.misc import imread

heart_mask = imread("c:/data/heart.jpg")

#공백 줄바꿈을 기준으로 Wordcloud를 만듦 
wordcloud = WordCloud(font_path = "c://Windows//Fonts//malgunbd.ttf", 
		stopwords=STOPWORDS,              #불용어 내부적으로 내장되어 있음; option; 
		background_color="white",
		width=1000,
		height=800,
		mask=heart_mask).generate(text)  #mask라는 변수에 heart_mask를 지정 

plt.figure(figsize=(10,10))
plt.imshow(wordcloud)
plt.axis("off")
plt.show()


# =============================================================================
# wordcloud2 - imageio.imread 로 이용하기
# =============================================================================
pip.exe list


from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

with open("c:/data/moon.txt","r") as file:
	text = file.read()


## from scipy.misc import imread 

## heart_mask = imread("c:/data/heart.jpg") # deprecated

import imageio

heart_mask = imageio.imread("c:/data/heart.jpg")


wordcloud = WordCloud(font_path = "c://Windows//Fonts//malgunbd.ttf", 
		stopwords=STOPWORDS,
		background_color="white",
		width=1000,
		height=800,
		mask=heart_mask).generate(text)

plt.figure(figsize=(10,10))
plt.imshow(wordcloud)
plt.axis("off")
plt.show()

# =============================================================================
# 웹페이지의 이미지를 컴퓨터에 저장
# =============================================================================

■ 웹페이지의 이미지를 컴퓨터에 저장

한겨례신문 - 더보기 - 만화 - 메인의 10월 2일 한겨레 그림판의 그림 긁어오기

from bs4 import BeautifulSoup
import urllib.request as req

url = "http://www.hani.co.kr/arti/cartoon/home01.html"
res = req.urlopen(url)
soup = BeautifulSoup(res, "html.parser")

lnk=soup.select_one('div.today-comic > a > img').get('src')

print(lnk)
http://img.hani.co.kr/imgdb/resize/2018/1001/53_1538392461_00503455_20181001.JPG


from urllib import request

request.urlretrieve(lnk,'c:/data/20181002.jpg')            #lnk위치의 파일을 c:/data에 20181002.jpg로 저장

Out[14]: ('c:/data/20181002.jpg', <http.client.HTTPMessage at 0x9de5b00>)



# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 09:51:04 2018

@author: stu
"""


# =============================================================================
# [문제186] http://www.skwyverns.com/Wyverns/Players/picther/picther_list.asp
이미지를 다운로드하세요.
# =============================================================================
#img가 full address로 안 보일 경우 

from bs4 import BeautifulSoup
import urllib.request as req

params = []
url = "http://www.skwyverns.com/Wyverns/Players/picther/picther_list.asp"
res = req.urlopen(url).read()
soup = BeautifulSoup(res, 'html.parser')
#전체 가져옴
lnk = soup.select('div.sell > div.sum > a > img')

#실제 물리적인 주소를 만드는 방법
for i in lnk:
    params.append('http://www.skwyverns.com' + i['src'])

type(params)

#파일 저장 
for p in params:
    splitStr = p.split('/')
    name = splitStr[len(splitStr)-1]
    fullPath = 'c:/sk_picther/' + name
    req.urlretrieve(p, fullPath)


#사용처에 대해 고민해보기 
select vs. select_one
find vs. find_all
###############################################################################

#성복이꺼 
    

from bs4 import BeautifulSoup
import urllib.request as req
from urllib import request

url = "http://www.skwyverns.com/Wyverns/Players/picther/picther_list.asp"
res = req.urlopen(url)
res

## 이미
head ='http://www.skwyverns.com'

soup = BeautifulSoup(res,'html.parser')

img=soup.select_one('#content > div > div.entrie_list > div.list_group')
                    
img = img.select('.sell > .sum > a > img')
img

cn=0
cn
name=''
for i in img:
    cn+=1
    print(i.attrs['src'])
    print(i.attrs['alt'])
    
    img_url=head+i.attrs['src']
    name=i.attrs['alt']
    
    request.urlretrieve(img_url,"c:/data/"+name+".jpg")
    

#아루미꺼
from bs4 import BeautifulSoup
import urllib.request as req

url = "http://www.skwyverns.com/Wyverns/Players/picther/picther_list.asp"
res = req.urlopen(url)
soup = BeautifulSoup(res, "html.parser")

src=[]
name=[]

for i in soup.select('div.sell > div.sum > a > img'):
    src.append('http://www.skwyverns.com'+i.get('src'))
    name.append(i.get('alt'))


from urllib import request

for i in range(len(src)):
    request.urlretrieve(src[i],'c:/data/skwyverns_{}.jpg'.format(name[i]))
    

# =============================================================================
# 오전수업
# =============================================================================
▣ selenium
- 웹브라우저를 컨트롤하여 웹 UI(User Interface)를 자동화하는 도구
- dynamic한 웹페이지를 웹크롤링하기 위한 도구 (user id/ user pw를 필요로 하는 경우)

■ selenium client 설치
pip install selenium

■ selenium driver를 설치 (control할 수 있는 driver)
firefox driver: https://github.com/mozilla/geckodriver/releases
chrome driver: https://sites.google.com/a/chromium.org/chromedriver/downloads
panthomsJS: http://phantomjs.org


■ 사용 
from selenium import webdriver
url = 'http://www.naver.com'

#phantomJS가 웹브라우저를 제어함
driver = webdriver.PhantomJS('c:/data/phantomjs.exe')
#3초동안 대기
driver.implicitly_wait(3)
driver.get(url)
#스크린샷 저장
driver.save_screenshot('c:/data/naver.png')
#나가기
driver.quit()


##login하여 쇼핑-장부구니같은 내용을 스크롤링하고 싶을 경우 

#step1 login을 하는 페이지를 첫페이지로 간다    
https://nid.naver.com/nidlogin.login

# 숨어서 로그인하게, -> 클릭이 필요함: 이를 짜야함 


# =============================================================================
# 오후 수업
# =============================================================================

from selenium import webdriver
from bs4 import BeautifulSoup

#입력창에 id와 pw넣기
user = "kimhj139"
mypass = "wmfrjdnsgkfn"

#driver
driver= webdriver.PhantomJS("c:/data/phantomjs.exe")
driver.implicitly_wait(3)
#접속해야 될 사이트에 접속하기
url_login = 'http://nid.naver.com/nidlogin.login'
driver.get(url_login)
# id를 입력하는  input 요소를 찾는다. 
# find_element_by_id(id): id속성으로 요소를 하나 추출한다.
inputid = driver.find_element_by_id("id")
#입력박스에 있는 텍스트 지우기; (이전에 혹시 inputid값이 있다면 지워주기)
inputid.clear()
#send_keys: 입력박스에 아이디 입력
inputid.send_keys(user)
#비밀번호 입력하는 input 요소를 찾는다.
inputpw = driver.find_element_by_id("pw")
#기존 input값에 pw가 있는 경우 지우기
inputid.clear()
#
inputpw.send_keys(mypass)

#로그인하기- 요소 선택을 통해서 로그인 부분을 찾기
<input type="submit" title="로그인" alt="로그인" value="로그인" class="btn_global" onclick="nclks('log.login',this,event)">
# find_element_by_css_selector(""): css선택자로 요소 하나 추출  (#class는 input.btn_global로 찾고, type에 submit을 넣어주기, 속성은 꼭 써줄 필요는 없으나 어떤 페이지에서는 class이름이 동일할 경우 type을 찾아 써줘야한다.)
loginbn = driver.find_element_by_css_selector("input.btn_global[type=submit]")

#로그인 버튼 클릭 하기: 아이디와 비밀번호 전송
loginbn.submit()



#예시- 네이버 페이> 쇼핑 > 디지털/가전 
#주소
driver.get("https://pay.naver.com/introduction/merchant/list?searchMerchantCategoryCode=50000003&searchTapType=merchant&searchSortType=payOrderCount&searchType=merchantName&searchKeyword=")
# 페이지의 element를 모두 가지고 옮
html = driver.page_source
#BeautifulSoup가 내용을 가져오지 못하기 때문에 panthomJS가 가져오는 역할을 한다.
soup = BeautifulSoup(html, "html.parser")
#태그 안에서 원하는 부분만 추출하기 
notice = soup.find_all('table', class_="tb_list tb_store")

for n in notice:
    print(n.text)
    
driver.quit()


#예시 - 쇼핑목록 가져오기
from selenium import webdriver
from bs4 import BeautifulSoup

#입력창에 id와 pw넣기
user = "kimhj139"
mypass = "wmfrjdnsgkfn"

#driver
driver= webdriver.PhantomJS("c:/data/phantomjs.exe")
driver.implicitly_wait(3)
#접속해야 될 사이트에 접속하기
url_login = 'http://nid.naver.com/nidlogin.login'
driver.get(url_login)
# id를 입력하는  input 요소를 찾는다. 
# find_element_by_id(id): id속성으로 요소를 하나 추출한다.
inputid = driver.find_element_by_id("id")
#입력박스에 있는 텍스트 지우기; (이전에 혹시 inputid값이 있다면 지워주기)
inputid.clear()
#send_keys: 입력박스에 아이디 입력
inputid.send_keys(user)
#비밀번호 입력하는 input 요소를 찾는다.
inputpw = driver.find_element_by_id("pw")
#기존 input값에 pw가 있는 경우 지우기
inputid.clear()
#
inputpw.send_keys(mypass)

#로그인하기- 요소 선택을 통해서 로그인 부분을 찾기
<input type="submit" title="로그인" alt="로그인" value="로그인" class="btn_global" onclick="nclks('log.login',this,event)">
# find_element_by_css_selector(""): css선택자로 요소 하나 추출  (#class는 input.btn_global로 찾고, type에 submit을 넣어주기, 속성은 꼭 써줄 필요는 없으나 어떤 페이지에서는 class이름이 동일할 경우 type을 찾아 써줘야한다.)
loginbn = driver.find_element_by_css_selector("input.btn_global[type=submit]")

#로그인 버튼 클릭 하기: 아이디와 비밀번호 전송
loginbn.submit()


#주소
driver.get("https://order.pay.naver.com/home")

# 페이지의 element를 모두 가지고 옮
html = driver.page_source

#BeautifulSoup가 내용을 가져오지 못하기 때문에 panthomJS가 가져오는 역할을 한다.
soup = BeautifulSoup(html, "html.parser")
#태그 안에서 원하는 부분만 추출하기 
notice = soup.find_all 
('#_rowLi20181002104236CHK2018100275436881 > div.p_inr')                
notice

                     
for n in notice:
    print(n.text)
    
driver.quit()

#_listContentArea > div:nth-child(2)

# =============================================================================
# chrome driver
# =============================================================================

from selenium import webdriver
from bs4 import BeautifulSoup

#입력창에 id와 pw넣기
user = "kimhj139"
mypass = "wmfrjdnsgkfn"

#driver
#driver= webdriver.PhantomJS("c:/data/phantomjs.exe")
driver = webdriver.Chrome("c:/data/chromedriver.exe")
driver.implicitly_wait(3)
#접속해야 될 사이트에 접속하기
url_login = 'http://nid.naver.com/nidlogin.login'
driver.get(url_login)
# id를 입력하는  input 요소를 찾는다. 
# find_element_by_id(id): id속성으로 요소를 하나 추출한다.
inputid = driver.find_element_by_id("id")
#입력박스에 있는 텍스트 지우기; (이전에 혹시 inputid값이 있다면 지워주기)
inputid.clear()
#send_keys: 입력박스에 아이디 입력
inputid.send_keys(user)
#비밀번호 입력하는 input 요소를 찾는다.
inputpw = driver.find_element_by_id("pw")
#기존 input값에 pw가 있는 경우 지우기
inputid.clear()
#
inputpw.send_keys(mypass)

#로그인하기- 요소 선택을 통해서 로그인 부분을 찾기
#<input type="submit" title="로그인" alt="로그인" value="로그인" class="btn_global" onclick="nclks('log.login',this,event)">
# find_element_by_css_selector(""): css선택자로 요소 하나 추출  (#class는 input.btn_global로 찾고, type에 submit을 넣어주기, 속성은 꼭 써줄 필요는 없으나 어떤 페이지에서는 class이름이 동일할 경우 type을 찾아 써줘야한다.)
loginbn = driver.find_element_by_css_selector("input.btn_global[type=submit]")



#로그인 버튼 클릭 하기: 아이디와 비밀번호 전송
loginbn.submit()



#예시- 네이버 페이> 쇼핑 > 디지털/가전 
#주소
driver.get("https://pay.naver.com/introduction/merchant/list?searchMerchantCategoryCode=50000003&searchTapType=merchant&searchSortType=payOrderCount&searchType=merchantName&searchKeyword=")
# 페이지의 element를 모두 가지고 옮
html = driver.page_source
#BeautifulSoup가 내용을 가져오지 못하기 때문에 panthomJS가 가져오는 역할을 한다.
soup = BeautifulSoup(html, "html.parser")
#태그 안에서 원하는 부분만 추출하기 
notice = soup.find_all('table', class_="tb_list tb_store")

for n in notice:
    print(n.text)
    
driver.quit()

# =============================================================================
# 다음 로그인 - 웹크롤러
# =============================================================================
from selenium import webdriver
from bs4 import BeautifulSoup

#입력창에 id와 pw넣기
user = "kimhj139"
mypass = "cnfqkf!7"

#driver
#driver= webdriver.PhantomJS("c:/data/phantomjs.exe")
driver = webdriver.Chrome("c:/data/chromedriver.exe")
driver.implicitly_wait(3)
#접속해야 될 사이트에 접속하기
url_login = 'https://logins.daum.net/accounts/loginform.do?url=https%3A%2F%2Fmember.daum.net%2Ffind%2Fid.do%3Faction%3Dhome'
driver.get(url_login)
# id를 입력하는  input 요소를 찾는다. 
# find_element_by_id(id): id속성으로 요소를 하나 추출한다.
inputid = driver.find_element_by_id("id")
#입력박스에 있는 텍스트 지우기; (이전에 혹시 inputid값이 있다면 지워주기)
inputid.clear()
#send_keys: 입력박스에 아이디 입력
inputid.send_keys(user)
#비밀번호 입력하는 input 요소를 찾는다.
inputpw = driver.find_element_by_id("pw")
#기존 input값에 pw가 있는 경우 지우기
inputpw.clear()
#
inputpw.send_keys(mypass)

#로그인하기- 요소 선택을 통해서 로그인 부분을 찾기
#<input type="submit" title="로그인" alt="로그인" value="로그인" class="btn_global" onclick="nclks('log.login',this,event)">
# find_element_by_css_selector(""): css선택자로 요소 하나 추출  (#class는 input.btn_global로 찾고, type에 submit을 넣어주기, 속성은 꼭 써줄 필요는 없으나 어떤 페이지에서는 class이름이 동일할 경우 type을 찾아 써줘야한다.)
loginbn = driver.find_element_by_css_selector("button.loginBtn[type=submit]")
# button
<button id="loginBtn" type="submit" class="btn_comm" onclick="_tiq.push(['__trackEvent', 'loginform_pc', 'login_daum']);">로그인</button>
#로그인 버튼 클릭 하기: 아이디와 비밀번호 전송
loginbn.submit()



#예시- 네이버 페이> 쇼핑 > 디지털/가전 
#주소
driver.get("https://pay.naver.com/introduction/merchant/list?searchMerchantCategoryCode=50000003&searchTapType=merchant&searchSortType=payOrderCount&searchType=merchantName&searchKeyword=")
# 페이지의 element를 모두 가지고 옮
html = driver.page_source
#BeautifulSoup가 내용을 가져오지 못하기 때문에 panthomJS가 가져오는 역할을 한다.
soup = BeautifulSoup(html, "html.parser")
#태그 안에서 원하는 부분만 추출하기 
notice = soup.find_all('table', class_="tb_list tb_store")

for n in notice:
    print(n.text)
    
driver.quit()

###############################################################################
# naver
<input type="submit" title="로그인" alt="로그인" value="로그인" class="btn_global" onclick="nclks('log.login',this,event)">
#태그 안에서 원하는 부분만 추출하기 
notice = soup.find_all('table', class_="tb_list tb_store")
###############################################################################


# =============================================================================
# 이미지 검색만 하기
# =============================================================================

#기본적인 step#################################################################
# 네이버> 검색 > 이미지
# 이미지 검색창을 알아야 함 
https://search.naver.com/search.naver?where=image&sm=tab_jum&query=


# 입력창 태그보기
# <input type="text" id="nx_query" name="query" class="box_window" maxlength="255" accesskey="s" value="" autocomplete="off" title="검색어 입력">

# img url
#<img src="https://search.pstatic.net/common/?src=http%3A%2F%2Fpost.phinf.naver.net%2FMjAxNzEyMDdfMjIy%2FMDAxNTEyNjQ0NDEyODAy.tWSXo2z5dNjQe_VMhffKFR7dwxrR4u7YypsOi7VYNrwg.c5EgFgAEWov-QJhwRRVXjPd_uvZHGCbQQtqrBNw2-b8g.JPEG%2FIJhr12cKveg86zwOBerfBe69yccY.jpg&amp;type=b400" class="_img" alt="아이언맨 슈트 총정리-마크1부터 48까지  | 포스트" onerror="var we=$Element(this); we.addClass('bg_nimg'); we.attr('alt','이미지준비중'); we.attr('src','data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7');" data-width="526" data-height="969" style="height: 150.654px; width: 81.7792px; left: 0px; top: 0px; zoom: 1; opacity: 1;">

#검색된 이미지를 더 많이 보기 위해서는 end key나, scroll bar를 내리거나, 밑의 화살키를 누르거나 하는 작업을 반복해서 해야 함 

import urllib.request as req
from bs4 import BeautifulSoup
from selenium import webdriver
#end key를 제어하는 모듈 
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome("c:/data/chromedriver.exe")

#이미지 검색해야할 창 
browser.get("https://search.naver.com/search.naver?where=image&sm=tab_jum&query=")
#id 속성으로 입력창 값을 찾음 # 입력창 태그보기
# <input type="text" id="nx_query" name="query" class="box_window" maxlength="255" accesskey="s" value="" autocomplete="off" title="검색어 입력">
elem = browser.find_element_by_id("nx_query")
#검색어 검색창에 검색어 넣기,+ 검색하기
elem.send_keys("아이언맨")
elem.submit()
#html tag 분석
brower.find_element_by....
#웹페이지에 있는 정보를 다 가져오기  => body만 가져온 다음 -> 이미지만 세세하게 들어

#body 태그 안에 있는 것을 기준으로 end 키를 내부적으로 돌리겠다.
browser.find_element_by_tag_name("body").send_keys(Keys.END)
#
time.sleep(5)
#end키를 한번 만 돌릴 경우 이미지를 다 볼 수 없기 때문에 반복문을 생성한다.
for i in range(1,2):
    browser.find_element_by_tag_name("body").send_keys(Keys.END)
    

# END키를 누르면 계속해서 tag가 바뀌게 됨

html = browser.page_source    
soup = BeautifulSoup(html, "html.parser")

#img를 찾아야 함
# <img src="https://search.pstatic.net/common/?src=http%3A%2F%2Fpost.phinf.naver.net%2FMjAxNzEyMDdfMjIy%2FMDAxNTEyNjQ0NDEyODAy.tWSXo2z5dNjQe_VMhffKFR7dwxrR4u7YypsOi7VYNrwg.c5EgFgAEWov-QJhwRRVXjPd_uvZHGCbQQtqrBNw2-b8g.JPEG%2FIJhr12cKveg86zwOBerfBe69yccY.jpg&amp;type=b400" class="_img" alt="아이언맨 슈트 총정리-마크1부터 48까지  | 포스트" onerror="var we=$Element(this); we.addClass('bg_nimg'); we.attr('alt','이미지준비중'); we.attr('src','data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7');" data-width="526" data-height="969" style="height: 196.568px; width: 106.702px; left: 0px; top: 0px; zoom: 1; opacity: 1;">

params = []

imglist = soup.find_all("img", class_="_img")

for im in imglist:
    params.append(im['src'])
    
params

a = 1
for p in params:
    req.urlretrieve(p, "c:/data/pictest/"+str(a)+".jpg")
    a += 1 
    
browser.quit()

###############################################################################
#스크롤 되다가 끊어지는 모양으로 나오게 될 경우 range값을 조정해본다. 
import urllib.request as req
from bs4 import BeautifulSoup
from selenium import webdriver
#end key를 제어하는 모듈 
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome("c:/data/chromedriver.exe")

#이미지 검색해야할 창 
browser.get("https://search.naver.com/search.naver?where=image&sm=tab_jum&query=")
#id 속성으로 입력창 값을 찾음 # 입력창 태그보기
# <input type="text" id="nx_query" name="query" class="box_window" maxlength="255" accesskey="s" value="" autocomplete="off" title="검색어 입력">
elem = browser.find_element_by_id("nx_query")
#검색어 검색창에 검색어 넣기,+ 검색하기
elem.send_keys("아이언맨")
elem.submit()

#body 태그 안에 있는 것을 기준으로 end 키를 내부적으로 돌리겠다.
browser.find_element_by_tag_name("body").send_keys(Keys.END)
#
time.sleep(5)

#time.sleep을 늘려서 모든 태그 주소값 가져와보기
for i in range(1,2):
    time.sleep(40)
    browser.find_element_by_tag_name("body").send_keys(Keys.END)
    time.sleep(40)
    
html = browser.page_source    
soup = BeautifulSoup(html, "html.parser")


params = []

imglist = soup.find_all("img", class_="_img")

for im in imglist:
    params.append(im['src'])
    

a = 1
for p in params:
    req.urlretrieve(p, "c:/data/pictest/"+str(a)+".jpg")
    a += 1 
    
    
browser.quit()

# =============================================================================
# google 이미지 웹크롤링
# =============================================================================
import urllib.request as req
from bs4 import BeautifulSoup
from selenium import webdriver
#end key를 제어하는 모듈 
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome("c:/data/chromedriver.exe")

browser.get("https://www.google.co.kr/imghp?hl=ko&tab=wi")

#id 속성으로 입력창 값을 찾음 # 입력창 태그보기
# naver: <input type="text" id="nx_query" name="query" class="box_window" maxlength="255" accesskey="s" value="" autocomplete="off" title="검색어 입력">
# google: <input class="gsfi" id="lst-ib" maxlength="2048" name="q" autocomplete="off" title="검색" type="text" value="" aria-label="검색" aria-haspopup="false" role="combobox" aria-autocomplete="list" dir="ltr" spellcheck="false" style="border: none; padding: 0px; margin: 0px; height: auto; width: 100%; background: url(&quot;data:image/gif;base64,R0lGODlhAQABAID/AMDAwAAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw%3D%3D&quot;) transparent; position: absolute; z-index: 6; left: 0px; outline: none;">
elem = browser.find_element_by_id("lst-ib")
#검색어 검색창에 검색어 넣기,+ 검색하기
elem.send_keys("아이언맨")
elem.submit()



#body 태그 안에 있는 것을 기준으로 end 키를 내부적으로 돌리겠다.
browser.find_element_by_tag_name("body").send_keys(Keys.END)

#
time.sleep(5)

#time.sleep을 늘려서 모든 태그 주소값 가져와보기
for i in range(1,2):
    time.sleep(5)
    browser.find_element_by_tag_name("body").send_keys(Keys.END)
    time.sleep(5)
    
html = browser.page_source    
soup = BeautifulSoup(html, "html.parser")


params = []

# naver: <img src="https://search.pstatic.net/common/?src=http%3A%2F%2Fpost.phinf.naver.net%2FMjAxNzEyMDdfMjIx%2FMDAxNTEyNjQ0NDE1NzE2.OPs8ezLyVGnCYm__ukqwZWmNvFTdpQKcKaVK6KeXJF4g.2NIe1RpaB-yuEshhbdJ75iqWaaWsDntQe-uXONbJfcog.JPEG%2FIQDWQKddg_ynSbDTKmWU42inVob8.jpg&amp;type=b400" class="_img" alt="아이언맨 슈트 총정리-마크1부터 48까지  | 포스트" onerror="var we=$Element(this); we.addClass('bg_nimg'); we.attr('alt','이미지준비중'); we.attr('src','data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7');" data-width="271" data-height="499" style="height: 177.154px; width: 96.2097px; left: 0px; top: 0px; zoom: 1; opacity: 1;">
#naver-  class="_img" 
# <img class="rg_ic rg_i" id="eYn1yvL47yOQmM:" jsaction="load:str.tbn" alt="아이언맨에 대한 이미지 검색결과" onload="typeof google==='object'&amp;&amp;google.aft&amp;&amp;google.aft(this)" src="data:image/jpeg;base64,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" style="width: 300px; height: 168px; margin-left: -2px; margin-right: -6px; margin-top: 2px;">


imglist = soup.find_all("img", class_="rg_ic rg_i")

for im in imglist:
    params.append(im['src'])
    
imglist


a = 1
for p in params:
    req.urlretrieve(p, "c:/data/pictest/"+str(a)+".jpg")
    a += 1 
    
    
browser.quit()


# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 09:52:16 2018

@author: stu
"""

# =============================================================================
# 정규표현식(Regular Expression) 
# =============================================================================

▣ 정규표현식(Regular Expression)

import re

source = "Data Science"

■ re.match
- boolean 형식의 값을 return문 
- 조건 제어문에서 사용하는 것이 유리하다.

# Da’라는 글자가 source에서 처음부터 어디까지 있는지 match하자
m = re.match('Da',source)

# 대소문자를 구분함 -> 현재 값: None
re.match('da',source)
print(re.match('da',source))

#
if m:
    print('패턴이 일치한다.')
else: 
    print('패턴이 불일치한다.')
    

#
if re.match('da',source):
    print("패턴이 일치한다.")
else:
    print("패턴이 불일치한다.")
    
# re.I : 대소문자 구분 하지 않기
if  re.match('da', source, re.I):
    print("패턴이 일치한다.")
else:
    print("패턴이 불일치한다.") 

#group, start, end, span에 대한 method 의미
source = "Data Science"
m = re.match('da', source, re.I)
if  m:
    print("패턴이 일치한다.")
    print(m.group())
    print(m.start())
    print(m.end())
    print(m.span())
else:
    print("패턴이 불일치한다.") 
    
■ re.match : 앞의 패턴을 찾는 것을 의미
#re.match에 대한 boolean return을 확인하기    
bool(re.match('D','Data'))
#[0-9]숫자의 패턴으로 되어있는지 확인하기
# *의 의미확인하기
bool(re.match('[0-9]th', '2th'))
bool(re.match('[0-9]th', '21th'))
bool(re.match('[0-9][0-9]th', '21th'))
bool(re.match('[0-9]*th', '21th'))
bool(re.match('[0-9]*th', '2th'))
bool(re.match('[0-9]*th', 'th'))
bool(re.match('[0-9]th', 'th'))
bool(re.match('[0-9]*th', '212th'))
#\d: [0-9]를 의미(숫자 패턴 확인)
bool(re.match('\d\dth', '21th'))
bool(re.match('\d*th', '21th'))

#메타문자
- a.b: .위치에 모든 문자 온다, aab, acb, aob
- .은 한글자 한글자를 의미한다. 
bool(re.match('D.','Data'))
bool(re.match('D...','Data'))
bool(re.match('D.b','Data'))
bool(re.match('D.t','Data'))
#[.]:.이 한글자 한글자가 아닌 dot .로 찾을 때는 대괄호로 사용하게 된다. 즉, dot을 문자로 의미하게 된다.
- a[.]b: .은 문자로 인식해서 찾는다. 
bool(re.match('D[.]','D.ata'))
# *: 앞의 패턴이 0번, 1번, 몇번이상 나올지 상관없다.
a*b: aaaaab, aab
bool(re.match('D*','Data'))
bool(re.match('D*a','Data'))
bool(re.match('D*a','DData'))
bool(re.match('A*','DData'))
bool(re.match('AA*','DData'))
# +: +앞에 글자가 최소 한번 이상 반복
a+b : +앞에 글자가 최소 한번 이상 반복
bool(re.match('c+','ccat'))
bool(re.match('c+','cat'))
bool(re.match('c+','at'))
bool(re.match('c*','at'))  #+와 *비교하기
#?: ?앞에 글자가 0번, 1번 반복되는 경우 (*, +, ?를 꼭 같이 고려하기)
a?b: ?앞에 글자가 0번, 1번 반복되는 경우  
bool(re.match('c?','ccat')) #cc가 두번 나온경우이지만 두번째 c도 있기 때문에 true로 반환
bool(re.match('c?','cat'))
bool(re.match('c?','at'))
bool(re.match('c?a','ccat')) #cc가 두번 나온경우
bool(re.match('c?a','cat')) 
bool(re.match('c?a','at'))
#a{2}b: a가 2번 반복 aab
bool(re.match('c{2}a', 'ccat'))
bool(re.match('c{2}a', 'cat'))
bool(re.match('c{2}a', 'cccat'))
#a{2,3}b: a가 2번 또는 3번 반복 aab, aaab
bool(re.match('c{2,3}a', 'ccat'))
bool(re.match('c{2,3}a', 'cat'))
bool(re.match('c{2,3}a', 'cccat'))
bool(re.match('c{2,3}a', 'ccccat'))
#a|b: a또는 b
bool(re.match('c|a', 'ccat'))
bool(re.match('c|a', 'cat'))
bool(re.match('c|a', 'aat')) 
bool(re.match('c|a', 'bat')) 
#[a-zA-Z]: 알파벳 모두
# [0-9]: 숫자 모두
# \d: 숫자 모두 [0-9]
# \D: 숫자가 아닌 것과 매치, [^0-9]
# \s: 공백문자와 매치
# \S: 공백문자가 아닌 것과 마치 
# \w: 문자, 숫자와 매치, [a-zA-Z0-9]
# \W: 문자, 숫자가 아닌 문자, [^a-zA-Z0-9]


source = "Data Science"
m = re.match('Science', source, re.I)
if  m:
    print("패턴이 일치한다.")
    print(m.group())
    print(m.start())
    print(m.end())
    print(m.span())
else:
    print("패턴이 불일치한다.") 
    
    
source = "Data Science"
m = re.match('\w* Science', source, re.I)
if  m:
    print("패턴이 일치한다.")
    print(m.group())
    print(m.start())
    print(m.end())
    print(m.span())
else:
    print("패턴이 불일치한다.") 
# .*: .은 임의의 문자 -> .가 여러개일경우
source = "Data Science"
m = re.match('.*Science', source, re.I)
if  m:
    print("패턴이 일치한다.")
    print(m.group())
    print(m.start())
    print(m.end())
    print(m.span())
else:
    print("패턴이 불일치한다.") 
# .+     
source = "Data Science"
m = re.match('.+Science', source, re.I)
if  m:
    print("패턴이 일치한다.")
    print(m.group())
    print(m.start())
    print(m.end())
    print(m.span())
else:
    print("패턴이 불일치한다.") 
# .? 
source = "Data Science"
m = re.match('.?Science', source, re.I)
if  m:
    print("패턴이 일치한다.")
    print(m.group())
    print(m.start())
    print(m.end())
    print(m.span())
else:
    print("패턴이 불일치한다.") 

■ re.search
- search는 전체를 대상으로 검색
- boolean형식으로 값을 return함 
(match는 앞의 패턴을 찾는 것이지만 search는 상관없이 전체를 대상으로 검색한다.)
#
bool(re.search('Science', source, re.I))

#
m = re.search('Science', source, re.I)
if  m:
    print("패턴이 일치한다.")
    print(m.group())
    print(m.start())
    print(m.end())
    print(m.span())
else:
    print("패턴이 불일치한다.") 
    

■ re.findall
- findall은 정규식에 일치하는 문자열을 리스트로 반환한다.

source = "Data Science"
# a라는 글자를 source에 있으면 찾기
re.findall('a', source)
# A라는 글자를 source에 있으면 찾기
re.findall('A', source)
# a라는 글자를 대소문자를 가리지 않고 source에 있으면 찾기
re.findall('A', source, re.I)

#a와 a다음 뒤에 글자 찾기
re.findall('a.', source)
#a와 a앞의 글자 찾기
re.findall('.a', source)
#0또는 1
re.findall('a.?', source)
#1이상 
re.findall('a.+', source)
#0이상
re.findall('a.*', source)
# 숫자만 찾아내기
re.findall('[0-9]', '오늘은 2018년 10월 5일 입니다.')
re.findall('\d', '오늘은 2018년 10월 5일 입니다.')
re.findall('[0-9]+', '오늘은 2018년 10월 5일 입니다.')
re.findall('\d+', '오늘은 2018년 10월 5일 입니다.')
# 문자만 찾아내기
re.findall('\D+', '오늘은 2018년 10월 5일 입니다.')
re.findall('[^0-9]+', '오늘은 2018년 10월 5일 입니다.')
re.findall('[a-zA-Z]+', '오늘은 2018년 10월 5일 입니다.') # 알파벳 문자이기 때문에 반환하는 것이 없음
re.findall('[가-힣]+', '오늘은 2018년 10월 5일 입니다.') #한글을 찾기 위해서는 [가-힇]를 사용하여 찾기

# =============================================================================
# 오후수업
# =============================================================================

source = "Data Science"

#replace: old -> new로 바꾸기: 미리보기이기 때문에 변수에 넣어주기
source = source.replace('Science', 'Scientist')

■ re.sub: old -> new로 바꾸기: 미리보기이기 때문에 변수에 넣어주기(적용)
- 메타문자들을 쓸 경우는 re.sub을 사용해서 바꿔주는 것이 용이 
- sub: 일치하는 패턴 대체하기 함수
source = re.sub('Scientist', 'Science', source )

■ re.split: 입력된 패턴을 구분자로 분리
 # : 콜론을 기준으로 split하겠다는 의미
re.split('[:]','python:progarmming')    
re.split('[\:]','python:programming')    
re.split('[,]','python,programming')    
#분리시킬 구분자를 나열하면 됨
re.split('[,:]','python,programming:R')   
re.split('[\,\:]','python,programming:R')   
#공백문자를 구분으로 분리하기
re.split('[ ]','python programming R')   
re.split('[\s]','python programming R')  
#,를 기준으로, 공백문자를 기준으로 분리하기
re.split('[,\s]','python,programming R')  
# \를 기준으로 구분하기
re.split('[\\\]','python\programming R') 


#주민등록번호가 있을 때 뒷부분을 *로 바꾸기
010101-1234567 -> 010101-******
#group: 교체시 그룹을 만들어 기존의 일부 데이터를 유지하며, 새로운 데이터에 적용하기
    #( ):를 통해 그룹 만들기 e.g. (\d{6})
    #\g<1>: 첫번째 그룹을 의미

re.sub('(\d{6})[-]\d{7}','\g<1>-*******','010101-1234567')

■ re.compile
- 정규식 표현식을 미리 compile한 것을 사용하기
p = re.compile(r"(\w+)\s+((\d+)[-]\d+[-]\d+)")
            (\w+): 첫번째 그룹 
            ((\d+)[-]\d+[-]\d+): 두번째 그룹
            (\d+): 세번째 그룹
            (\w+) 문자, 숫자
            \s+공백이 하나, 두개
p.sub("\g<1> \g<2>", "James 010-1234-1234")

# group의 순서가 바뀜 (이것이 없으면 위치를 바꾸고자 할때, split를 하고 변수에 넣어주고 인덱스를 통해 바꿔주는 작업을 해야한다.)
p.sub("\g<2> \g<1>", "James 010-1234-1234")

m = p.search("James 010-1234-1234")

m.group(0) #전체
m.group(1) #이름
m.group(2) #전화번호

# group의 이름을 임의로 만들 수 있음
p = re.compile(r"(\w+)\s+((\d+)[-]\d+[-]\d+)")
# (?P<name>\w+): 그룹 1, name이라는 그룹
# (?P<phone>(\d+)[-]\d+[-]\d+): 그룹2, phone이라는 그룹
p = re.compile(r"(?P<name>\w+)\s+(?P<phone>(\d+)[-]\d+[-]\d+)")
m = p.search("james 010-1234-1234")
m.group("name")
m.group("phone")

#
txt = "of the people, by then people, for the people"
re.findall('people', txt)
re.findall('of|by|for', txt)
re.findall('^of',txt) # ^은 시작의 의미  cf. [^0-9] :^은 not의 의미
re.findall('people$', txt) #$은 끝의 의미

#the 이전에 나오는 for를 찾는다. (the 문자 이전에 for가 있으면 보여주고 없으면 보여주지 않는다.)
re.findall('for (?=the)', txt)
#the 다음에 나오는 people을 찾는다. (the 문자 다음에 people이 있으면 보여주고 없으면 보여주지 않는다.)
re.findall('(?<=the) people', txt)


p = re.compile(r"(\w+)\s+((\d+)[-]\d+[-]\d+)")
p = re.compile(r"(\w+)\s+(\d+[-]\d+[-]\d+)")


p = re.compile(r"(\w+)\s+((\d+)[-]\d+[-]\d+)")
            (\w+): 첫번째 그룹 
            (\d+): 두번째 그룹
            (\w+) 문자, 숫자
            \s+공백이 하나, 두개
p.sub("\g<1> \g<2>", "James 010-1234-1234")

# =============================================================================
# group의 의미를 알기 위해 ()를 다시 설정하여 혼자 공부해 봄
# =============================================================================
# group의 순서가 바뀜 (이것이 없으면 위치를 바꾸고자 할때, split를 하고 변수에 넣어주고 인덱스를 통해 바꿔주는 작업을 해야한다.)
p.sub("\g<2> \g<1>", "James 010-1234-1234")

m = p.search("James 010-1234-1234")

m.group(0) #전체
m.group(1) #이름
m.group(2) #전화번호

p = re.compile(r"(?P<name>\w+)\s+(?P<phone>\d+[-]\d+[-]\d+)")
m = p.search("james 010-1234-1234")
m.group("name")
m.group("phone")


# =============================================================================
#  다시 수업으로 돌아가서
# =============================================================================

print("우리 행복하게 살자")
print('우리 "행복"하게 살자')
#\사용법: 문자로 인식하도록 하기 
print("우리 \"행복\"하게 살자")
#\: :만 사용하면 가끔 인식이 안될 수 있어서 \:를 사용하기도 함

정규식 표현식으로 나타내기 
txt = "Let's live happily"
p = re.compile('\w+')
p.findall(txt) #['Let', 's', 'live', 'happily']

p = re.compile('\w')
p.findall(txt)  #['L', 'e', 't', 's', 'l', 'i', 'v', 'e', 'h', 'a', 'p', 'p', 'i', 'l', 'y']

#'를 문자로 인식하기 때문에 앞에  \를 붙여 \'로 쓰도록 한다.
# [\']뒤에는 문자 하나만 나오면 되기 때문에 .을 사용하면 됨다.
p = re.compile('\w+[\'].')
p.findall(txt)  #["Let's"]
#굳이 \를 안해도 되는 경우는 ""를 사용하여 literal 문자로 나타내면 된다.
p = re.compile("\w+['].")
p.findall(txt)

p = re.compile('Physical | Computer') #둘 중에 하나 또는 둘 다 data를 바꿈
p.sub('Data', 'Physical Science and Computer Science') #replace함 
#p.subn: replace하면서 바뀐 정보에 대한 갯수를 return해줌 
p.subn('Data', 'Physical Science and Computer Science')


#group 다시 정확하게 공부
(정규식에서 tuple모양이 여기서는 group을 의미하다)
p = re.compile(r"(\w+)\s+((\d+)[-](\d+)[-](\d+))")
            r: literal 문자 안에 "를 사용할 경우 \을 또 해줘야 하기 때문에 계속 \를 사용하지 않고 사용하게 해줘도 된다는 의미로 쓰임 
            (\w+): 첫번째 그룹 
            (\d+): 두번째 그룹
            (\w+) 문자, 숫자
            \s+공백이 하나, 두개
p.sub("\g<1> \g<2>", "James 010-1234-1234")

# group의 순서가 바뀜 (이것이 없으면 위치를 바꾸고자 할때, split를 하고 변수에 넣어주고 인덱스를 통해 바꿔주는 작업을 해야한다.)
p.sub("\g<2> \g<1>", "James 010-1234-1234")

m = p.search("James 010-1234-1234")

m.group(0) #전체 (r"(\w+)\s+(\d+[-]\d+[-]\d+)")
m.group(1) #이름 (\w+)
m.group(2) #전화번호 (\d+[-]\d+[-]\d+)
m.group(3) #첫번째(\d+)
m.group(4) #두번째(\d+)
m.group(5) #세번째(\d+)


# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 09:53:55 2018

@author: stu
"""

# =============================================================================
# 오전 수업
# =============================================================================
cf. 
package: global 변수를 편하기 사용하기 위해서 이용

module식 개발: 작은 단위로 개발해서 끼워맞는 작업


▣ class - variable, method 로 구성 
■ 구조적인 프로그램(structured language/ procedural language)
- 프로그램은 순서대로 흐르는 언어(전방참조만 가능함)
■ 객체지향 프로그램(object-oriented language)
- 필요한 프로그램을 호출해서 사용하는 언어 
- 

###############################################################################

▣ 절차(구조적) 지향 프로그램(procedural language )
    - c언어 
    - 물이 위에서 아래로 흐르는 것처럼 순차적인 순차적인 처리가 중요시 되며 프로그램 전체가 유기적으로 연결 되도록 만드는 프로그래밍 기법
    - 단점
        : 재사용할 수 없다. 
        : 확장성이 떨어진다.(overload기능을 할 수 없음)
        : 유지보수가 어렵다. 
        
#누적합 구하기
(글로벌 변수)        
adder(3)
adder(4)
결과는 7일 출력되도록 함수를 만드세요.

x=0
def adder(y):  
    global x
    x+=y
    return x

a
adder(3)
adder(4)


b
adder(5)
adder(5)

a와 b가 따로따로 adder의 누적합을 구하고자 하는데 절차지향 프로그램은 이 경우는 a,b와 상관없이 합이 누적된다. 그래서 a와 b에 대한 함수를 따로 따로 개발해야한다.
그러나 객체지향 프로그램을 이용하여 하나의 프로그램을 가지고 둘이서 따로따로 사용할 수 있는 효과를 줄 수 있음 

▣ 객체지향 프로그램(object oriented language)
    - java, c++, c#, python 
    (cf. r은 구조적 언어이며, script 언어이다.)
    - 구조적프로그래밍과 다르게 큰 문제를 작게 쪼개는 것이 아니라 먼저 작은 문제들을 해결할 수 있는 객체들을 만든 뒤 이 객체들을 조합해서 큰 문제를 해결하는 방법
    - 객체: 사물 개념 중에서 명사로 표현할 수 있는 것을 의미한다.
            사람, 건물 학생
    - 클래스: 객체를 설명해 놓은 것(객체의 설계도)
    - 인스턴스: 클래스를 메모리에 만들어서 사용하도록 하는 의미

객체 = 사람 
속성(Attribute, field) = 변수: 팔, 다리, 머리, 눈, 코 , 입, 이름, 키, 나이, 주민번호, 주소, 학번, 성적, 성격
=> 수치, 값으로 표현 
메소드(method) = 함수 : 기능의 프로그램 처리, 조작하는 것, 속성의 값을 변경하는 기능

#클래스를 표현하는 방법 
class Calculator:
    def __init__(self):
        self.result = 0
        
    def adder(self, num):
        self.result += num
        return self.result

# __init__: 초기화 시키는 method, 꼭 필수사항은 아님
# self 는 자기자신 (이 클래스를 사용하고 있는 자기 자신 )
# 초기화 시키는 작업
# class Calculator:
#    def __init__(self):
#        self.result = 0
        
# adder 에 대한 method 
#    def adder(self, num):
#       self.result += num
#        return self.result
        

#하나의 프로그램을 다르게 사용하고 있음 
#class를 만들었으니 인스턴스instance를 해야함 
<<홍길동>>        
cal1 = Calculator() # 인스턴스 
print(cal1.adder(3))
print(cal1.adder(4))
print(cal1.adder(2))

<<박찬호>>
cal2 = Calculator() # 인스턴스 
print(cal2.adder(5))
print(cal2.adder(5))
print(cal2.adder(1))

class myClass:
    pass   #함수, 클래스에서 아무 작업하지 않을 때 사용 

#pass : 아무것도 수행하지 않겠다.; 함수, 클래스에서 아무 작업하지 않을 때 사용 
    
class Person:
    name = '홍길동'
    age = 20
    
    def myPrint(self):
         print("이름은 {}".format(self.name))
         print("나이는 {}".format(self.age))
#   name = '홍길동'
    age = 20
    위의 두개는 global 변수 처럼 어떤 인스턴스에서도 공통적으로 사용됨

#self: 이 함수를 쓰고 있는 자기 자신을 의미  ()
        홍길동이 이것을 쓰면 홍길동이 쓰고 있다는 것을 의미
# cf. java, c에서는 self를 this로 사용함

# 클래스를 기반으로 인스턴스 생성
p1 = Person()

# 인스턴스화한 method를 사용해야 함 
p2 = Person()
p2.myName()
p2.myAge()

p3=Person()
p3.name = '박찬호'
p3.age = 30
p3.myName()
p3.myAge()
#내 인스턴스 안에서는 속성을 추가할 수 있다. 
p3.job = '프로그래머'
print('직업은',p3,job)

#내 인스턴스 안에서 만큼은 변경 작업이 가능하다. 
#class 장점: 재사용이 가능함

#
class Person:
    def __init__(self):
        self.info=""
    def showinfo(self, name, age):
        self.info += "이름 :" +name+","+" 나이:"+str(age)+"\n"

# self.info대입연산자 + self. 이름 + self.age  그리고 \n 밑으로 한 줄 내리기로 append하게 생성한다.(누적함) 
# str(age)를 쓰지 않으면 오류가 남: 왜냐하면 숫자는 문자랑 같이 사용할 수 없기 때문에 

# init 무조건 인스턴스할 때 생성하고 초기화시킴, 이 클래스에서만 사용할수 있는 변수를 만듦
    name = '홍길동'
    age = 20
와 달리 init은 local변수처럼 적용된다. init에서 생성한 변수는 꼭 self를 붙여야 한다. 

#Person()을 수행시키자 마자 init이 돌아가고 self.info=""가 생성된다. self.info는 null값으로 값을 선언함 
man = Person()
man.showinfo("최유진", 26)
man.showinfo("구동매", 25)
print(man.info)

#woman이라는 인스턴스가 만들어짐, 새로운 info가 선언됨   
woman = Person()
woman.showinfo("고애신", 20)
woman.showinfo("이양화", 21)
woman.showinfo("김현정", 23)
print(woman.info)

name = "제임스"
class myName:
    def mySet(self, setname):
        self.name = setname
    def myPrint(self):
        print(name)
        print(self.name)

p1 = myName()     
p1.mySet("홍길동")        
p1.myPrint()
#self.name: 내 클래스 안에 있는 변수를 쓰겠다는 의미
#name: 클래스 밖에 잇는 변수를 쓰겠다는 의미

class Employee:
    empCount = 0
    
    def __init__(self, name, salary):       # __init__(self) : __init__에 self는 꼭 써야 한다!
        self.name = name                    # 일반적으로 init에 지정해놓은 변수를 self.이름에 같이 사용한다. (self.n = name이라고 해도 되지만)
        self.salary = salary
        Employee.empCount += 1
    def displayCount(self):                 #displayCount(self): self를 꼭 써줘야 한다. -문법임
        print('전체 종업원수는 %d'%Employee.empCount)
    def displayEmployee(self):              #displayEmployee(self): self를 꼭 써줘야 한다. 
        print("이름: ", self.name, ", 급여: ", self.salary)
    
#(기존에는 변수에 호출한 다음 넣었으나)    
# init의 생성자에 변수가 나열되어있으면 class를 인스턴스화 할때 값은 꼭 넣어야 함
emp1 = Employee("홍길동", 1000)
emp1.displayCount()
emp1.displayEmployee()

#Employee.empCount(클래스이름.변수이름 ) :진정한 글로벌 변수가 됨, init은 초기화 되지만 글로벌 변수는 초기화 되지 않는다. 어떤 인스턴스간에 공통으로 사용되는 변수가 됨 
emp2 = Employee("제임스", 2000)
emp2.displayCount()
emp2.displayEmployee()

emp3 = Employee("박찬호", 3000)
emp3.displayCount()
emp3.displayEmployee()


#비교후기. employee.empCount -> self.empCount 로 바꿨을 경우
class Employee:
    empCount = 0
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.empCount += 1
    def displayCount(self):
        print('전체 종업원수는 %d'%self.empCount)
    def displayEmployee(self):
        print("이름:", self.name, ", 급여: ", self.salary)
 
# self.empCount는 empCount가 자기자신의 인스턴스만이 되게 된다.        
# emp1.displayCount()가 계속 1이 됨 
emp1 = Employee("홍길동", 1000)
emp1.displayCount()
emp1.displayEmployee()

emp2 = Employee("제임스", 2000)
emp2.displayCount()
emp2.displayEmployee()

emp3 = Employee("박찬호", 3000)
emp3.displayCount()
emp3.displayEmployee()


# =============================================================================
# 오후수업
# =============================================================================

# 클래스 만들고 -> 인스턴스 생성 -> 클래스 변수를 만듦 (Employee.name);class에서는 맨처음에 변수가 만들지 않았지만 이로 인해 변수가 생성됨 -> 
class Employee:
    pass

#똑같은 class를 사용하지만 인스턴스는 다르게 생성함을 보여준다. id가 다르게 출력되기 때문에 이를 확인할 수 있다.
emp1 = Employee()
emp2 = Employee()

print(id(emp1)) #id는 물리적 메모리 주소
print(id(emp2))

#__class__: 인스턴스의 class 정보확인하기(인스턴스가 어떤 class에 있는지 확인하기)
print(emp1.__class__)
print(emp2.__class__)

#class에 대한 메모리 정보는 같은 값으로 출력된다. 
print(id(emp1.__class__))
print(id(emp2.__class__))

print(id(Employee))

#클래스 변수가 만들어짐 (클래스 변수는 어떤 인스턴스 간에 사용할 수 있다.)
Employee.name = "홍길동"
emp1.name #클래스 변수를 사용
emp2.name #클래스 변수를 사용

emp1.name = "박찬호"
emp1.name #인스턴스 변수가 됨 

emp2.name #클래스 변수르 사용 (자기의 인스턴스가 없기 때문에 클래스 변수를 사용함)

emp1.salary = 2000  
emp1.salary         #인스턴스 변수
emp2.salary         #오류: 자기안에 인스턴스 변수가 없기 때문에


<<요약>>
- 클래스를 사용할 때는 인스턴스화 해야한다. 
- 무조건 처음 사용해야할 method는 __init__이다. : 인스턴스를 초기화시키기 위한 method -> 이는 입력값을 그대로 사용하기 위한 방법이다.
- self지시자로 선언된 변수가 없으면 값이 출력이 되지 않는다. (e.g., self.name = name 변수 선언을 함)
- 모든 인스턴스에서 사용하기 위해서는 class변수로 선언해야 한다. 

# =============================================================================
# [문제187] 생성자에 이름, 핸드폰번호, 메일, 주소 변수를 생성합니다. 
print_info 메소드를 생성한 후  출력하는 Contact 클래스를 생성하세요.
인스턴스는 set_contact 함수를 이용해서 만드시고 이름, 핸드폰번호,메일, 주소는 입력값으로 받아서 출력하세요.
# =============================================================================
생성자 : __init__

#답1 - 잘못됨 
class contact:
    def __init__(self):
        self.name = ""
        self.mobile = ""
        self.email = ""
        self.address = ""
    def print_info(self):
        self.name = input("이름을 입력하세요: ")
        self.mobile = input("핸드폰번호를 입력하세요: ")
        self.email = input("메일을 입력하세요: ")
        self.address = input("주소를 입력하세요: ")  
    def set_contact(self):
        print("이름:",self.name)
        print("핸드폰번호:",self.mobile)
        print("메일:",self.email)
        print("주소:",self.address)

#답2  - 잘못됨
class contact:   
    def __init__(self):
        pass
    def print_info(self):
        self.name = input("이름을 입력하세요: ")
        self.mobile = input("핸드폰번호를 입력하세요: ")
        self.email = input("메일을 입력하세요: ")
        self.address = input("주소를 입력하세요: ")    
    def set_contact(self):
        print("이름:",self.name)
        print("핸드폰번호:",self.mobile)
        print("메일:",self.email)
        print("주소:",self.address)        

emp1 = contact()
emp1.print_info()
emp1.set_contact()


#답2 수정
class contact:   
    def __init__(self,name, mobile, email, address):
        self.name = name
        self.mobie = mobile
        self.email = email
        self.address = address

    def print_info(self):
        print("이름: %d"%self.name)
        print("핸드폰번호: %d"%self.mobile)
        print("메일: %d"%self.email)
        print("주소: %d"%self.address)    
        
def set_contact():
    name = input("이름을 입력하세요: ")
    mobile = input("핸드폰번호를 입력하세요: ")
    email = input("메일을 입력하세요: ")
    address = input("주소를 입력하세요: ")    
    info = Contact(name, mobile, email, address)
    info.print_info()

set_contact()

'홍길동', '010-1000-1004', 'hong@aaa.com', '서울시 강남구 삼성로'

#쌤답 
class Contact:
    def __init__(self,name, pn, email, addr):
        self.name = name
        self.pn = pn
        self.email = email
        self.addr = addr

    def print_info(self):
        print("이름 : {} ".format(self.name))
        print("핸드폰번호 : {} ".format(self.pn))
        print("메일 : {} ".format(self.email))
        print("주소 : {} ".format(self.addr))


def set_contact():
    name = input("이름을 입력하세요 : ")
    pn = input("핸드폰번호를 입력하세요 : ")
    email = input("메일을 입력하세요 : ")
    addr = input("주소를 입력하세요 : ")
    conIns = Contact(name, pn, email, addr)
    conIns.print_info()

set_contact()


# =============================================================================
# [문제188] Contact 클래스 이용해서 입력 들어 온 값들을 c:/data/contact.db 에
	저장해서 관리하세요.
# =============================================================================


import sqlite3

conn = sqlite3.connect(":memory:")

c = conn.cursor()

c.execute("create table contact(name, pn, email, addr)")

class Contact:
    def __init__(self,name, pn, email, addr):
        self.name = name
        self.pn = pn
        self.email = email
        self.addr = addr

    def print_info(self):
        print("이름 : {} ".format(self.name))
        print("핸드폰번호 : {} ".format(self.pn))
        print("메일 : {} ".format(self.email))
        print("주소 : {} ".format(self.addr))

    def input(self):
        self.conn = sqlite3.connect('c:/data/contact.db')
        self.c = self.conn.cursor()
        self.c.execute("insert into contact(name, pn, mail, addr) values(?,?,?,?)",(self.name,self.pn,self.email,self.addr))
        self.c.execute('select * from contact')
        print(self.c.fetchall())
    
    def commit(self):
        self.conn.commit()
       
    def rollback(self):
        self.conn.rollback()
    def close(self):
        self.c.close()
        self.conn.close()


def set_contact():
    name = input("이름을 입력하세요 : ")
    pn = input("핸드폰번호를 입력하세요 : ")
    email = input("메일을 입력하세요 : ")
    addr = input("주소를 입력하세요 : ")
    conIns = Contact(name, pn, email, addr)
    conIns.print_info()
    conIns.input()
    conIns.commit()
    conIns.close()

set_contact()

c.execute("drop table contact")

c.close()
info.close()
import sys
import os.path
sys.data.append('c:\data')
from Contact import *

#c:\data 에 모든파일형식으로 하되 확장자를 .py로 해주기, encoding은 utf-8로 하기 (utf-8로 하지 않으면 불러들일 때 )
# pacakage이름.py로 저장




# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 09:45:17 2018

@author: stu
"""

cf. 변수함수가 모여있는 것이 class라고 할 수 있다.
class Person:
    hobbys = []                 #habbys:클래스 변수: 인스턴스간의 값이 공유
    def add_hobby(self, hobby):  #hobby:매개변수: add_hobby에서만 사용하는 변수
        self.hobbys.append(hobby) #self.hobbys 클래스 변수이기때문에 self이후에도 사용
        
#p1 인스턴스를 생성
p1 = Person()
#'노래부르기' hobby에 추가
p1.add_hobby("노래부르기")
print(p1.hobbys)

#p2 인스턴스 생성 
p2 = Person()
p2.add_hobby("글쓰기")
print(p2.hobbys)

#class 변수는 인스턴스 간에 공유가 되기 때문에, 클래스 변수를 잘 넣어야 한다. 
#위의 경우에는 클래스 변수로 넣으면 p1, p2에 계속 클래스 변수가 공유되어 쌓이기 때문에 hobby를 인스턴스 변수로 만들어야 한다. 

#클래스 변수 호출하는 방법 (#클래스 변수는 p1, p2나 상관없기 때문에 )
print(Person.hobbys)


#hobbys를 인스턴스 변수로 넣기 
class Person:
   def add_hobby(self, hobby): 
        self.hobbys = []   #hobbys는 인스턴스 변수 -> 인스턴스에서만 사용되는 변수로 사용됨
        self.hobbys.append(hobby)

p1 = Person()
p1.add_hobby("노래부르기") 
print(p1.hobbys)

p2 = Person()
p2.add_hobby("글쓰기")
print(p2.hobbys)


#? 다시 확인하기
#1) 클래스 변수인지, 인스턴스 변수인지
#2) add_hobby(self.hobby)/ self를 인스턴스 안에서만 사용하겠다 하더라도 class 변수로 사용될 경우 인스턴스에서만 사용되지 않는다.
class Person:
    def add_hobby(self, hobby): 
        self.hobbys = []   #list 변수이기때문에 출력하면 안됨 
        self.hobbys.append(hobby)
    def show(self):
        print("내 취미는 "+self.hobbys)

p1 = Person()
p1.add_hobby("노래부르기")
print(p1.hobbys)
p1.show() #Error: list변수이기 때문에 

p2 = Person()
p2.add_hobby("글쓰기")
print(p2.hobbys)


#list변수로 고치기 
class Person:
    def add_hobby(self, hobby): 
        self.hobbys = ""   
        self.hobbys = hobby
    def show(self):
        print("내 취미는 "+self.hobbys)

p1 = Person()
p1.add_hobby("노래부르기")
p1.show()

#인스턴스를 사용할 때 만들 때 값을 넣을지, 메소드를 사용할 때 값을 넣을지 고민해야 한다. 
#지금 여기서는 인스턴스를 만들 때 값을 넣을 수 없다.  --> __init__(초기생성자)가 필요하다.
class Person:
    def add_hobby(self, hobby): 
        self.hobbys = hobby
    def show(self):
        print("내 취미는 "+self.hobbys)

#초기 생성자 사용
#초기 생성자를 만들 때, 인스턴스화를 할 때 name을 꼭 입력값으로 받아야 함.
class Person:
    def __init__(self, name):
        self.name = name
        self.hobbys =[]
    def add_hobby(self, hobby): 
        self.hobbys.append(hobby)

#인스턴스는 이름만 넣고, 초기화 됨 
#이름을 넣고, self.name = name 리스트 변수 생성
#add.hobby 메소드를 사용할 때 값을 생성 
p1 = Person('홍길동')
p1.add_hobby('음반수집')
p1.add_hobby('노래부르기')
print(p1.hobbys)

p2 = Person('박찬호')
p2.add_hobby('글쓰기')
print(p2.hobbys)


# =============================================================================
# [문제_189]초기 생성자에는 이름, 주소, 급여를 입력값으로 받고 아래와 같이 출력되는 클래스를 생성하세요. 
인스턴스 생성될때 마다 건수를 출력해주세요.
# =============================================================================
사원수 : 1
이름 : 홍길동 , 주소 : 덴마크,  급여 : 1000

사원수 : 2
이름 : 홍아들 , 주소 : 노르웨이,  급여 : 2000

#sal을 숫자로 받음 
class Emp:
    cn = 0
    def __init__(self, name, addr, sal):
        self.name = name
        self.addr = addr
        self.sal = sal
        Emp.cn += 1
        print('사원수 : %d' %Emp.cn)
        print('이름 :'+self.name+', 주소:'+self.addr+', 급여: %d'%self.sal)

p1 = Emp('홍길동', '덴마크', 1000)
p2 = Emp('홍아들', '노르웨이', 2000)

#sal을 함수에서 str으로 변환해서 입력하기; 숫자로 입력가능 
class Emp:
    cn = 0
    def __init__(self, name, addr, sal):
        self.name = name
        self.addr = addr
        self.sal = sal
        Emp.cn += 1
        print('사원수 : %d' %Emp.cn)
        print('이름 :'+self.name+', 주소:'+self.addr+', 급여: '+str(self.sal))

p1 = Emp('홍길동', '덴마크', 1000)
p2 = Emp('홍아들', '노르웨이', 2000)

#sal을 string으로 받음
class Emp:
    cn = 0
    def __init__(self, name, addr, sal):
        self.name = name
        self.addr = addr
        self.sal = sal
        Emp.cn += 1
        print('사원수 : %d' %Emp.cn)
        print('이름 :'+self.name+', 주소:'+self.addr+', 급여: '+self.sal)

p1 = Emp('홍길동', '덴마크', '1000')
p2 = Emp('홍아들', '노르웨이', '2000')

#함수 추가했을 때 output 
class Emp:
    cn = 0
    def __init__(self, name, addr, sal):
        self.name = name
        self.addr = addr
        self.sal = sal
        Emp.cn += 1
    def add_emp(self):
        print('사원수 : %d' %Emp.cn)
        print('이름 :'+self.name+', 주소:'+self.addr+', 급여: '+self.sal)

p1 = Emp('홍길동', '덴마크', '1000')
p1.add_emp()
p2 = Emp('홍아들', '노르웨이', '2000')
p2.add_emp()


#쌤답
class Employee:
   
   empCn = 0    #class변수

   def __init__(self, name, addr, salary): #형식 매개변수임 (NOT 인스턴스 변수) #__init__안에 있는 것들은 인스턴스를 생성할 때 초기화 된다.
      self.name = name   #인스턴스변수
      self.addr = addr   #인스턴스변수
      self.salary = salary  #인스턴스변수
      Employee.empCn += 1   #class이름.변수이름이 코드해석에 편리함
   
   def printCount(self):                   # 메소드 안에는 꼭 self를 포함하도록 한다.
     print("사원수 : %d" %Employee.empCn)   #class 변수값 출력

   def printEmployee(self):                # 메소드 안에는 꼭 self를 포함하도록 한다.
      print( "이름 : {} , 주소 : {},  급여 : {}".format(self.name, self.addr, self.salary)) #인스턴스 변수는 self.을 사용하도록 한다.


emp1 = Employee("홍길동","덴마크", 1000)
emp1.printCount()
emp1.printEmployee()


emp2 = Employee("홍아들","노르웨이", 2000)
emp2.printCount()
emp2.printEmployee()


# =============================================================================
# [문제 190]

id_number1 = "010101-3234567"
id_number2 = "990202-2123456"

2001 01 01 남성
1999 02 02 여성

# =============================================================================

#방법 
#1)인덱스 기준으로
#2) -split하여 

#답1
# -를 기준으로 split하기 
def id_process(id):
    first, second = id.split("-")  #split하여 first, second로 받을 수 있음
    gender = second[0]
    
    if gender == "1" or gender =="2":
        year = "19"+first[0:2]   #first[:2]까지 slicing해도 됨   
    else:
        year = "20"+first[0:2]
    
    if gender == "2" or gender == "4":
        gender = "여성"
    else:
        gender = "남성"
    
    month = first[2:4]
    day = first[4:6]
    
    return year, month, day, gender

id_process(id_number1)
id_process(id_number2)    
     
#답2
def id(i):     
    if i[7]=="1": 
        print('19'+i[0:2]+' '+i[2:4]+' '+i[4:6] + '남성')
    elif i[7]=="2":
        print('19'+i[0:2]+' '+i[2:4]+' '+i[4:6], '여성')
    elif i[7]=="3":
        print('20'+i[0:2]+' '+i[2:4]+' '+i[4:6], '남성')
    elif i[7]=="4":
        print('20'+i[0:2]+' '+i[2:4]+' '+i[4:6], '여성')       


id_number1 = "010101-3234567"    
id(id_number1)
id(id_number2)


# =============================================================================
# 다시 수업으로
# =============================================================================
class Employee:
    empCount = 0        #class 변수
    raise_ratio = 1.1   #rasie_ratio는 클래스변수인가? 인스턴스 변수인가? -> 인스턴스로 만들어짐!
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1
        
    def showCount(self):
        print("전체 종업원의 수는 {}".format(Employee.empCount))
    
    def showEmp(self):
        print("이름 {}, 급여{}".format(self.name, self.salary))
    
    def raise_salary(self):
        print(self.raise_ratio)
        self.salary = int(self.salary * self.raise_ratio)

    
emp1 = Employee("홍길동", 1000)
emp1.showCount()
emp1.showEmp()
emp1.raise_salary()
emp1.showEmp()

emp1 = Employee("홍길동", 1000)
emp1.showCount()
emp1.showEmp()
emp1.raise_ratio = 1.2
emp1.raise_salary()
emp1.showEmp()

emp2 = Employee("박찬호", 2000)
emp2.showCount()
emp2.showEmp()
emp2.raise_salary()
emp2.showEmp()


#self.raise_ratio를 -> Employee.raise_ratio로 바꾸기 
class Employee:
    empCount = 0        
    raise_ratio = 1.1   
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1
        
    def showCount(self):
        print("전체 종업원의 수는 {}".format(Employee.empCount))
    
    def showEmp(self):
        print("이름 {}, 급여{}".format(self.name, self.salary))
    
    def raise_salary(self):
        print(Employee.raise_ratio)
        self.salary = int(self.salary * Employee.raise_ratio)

emp1 = Employee("홍길동", 1000)
emp1.showCount()
emp1.raise_salary()
emp1.showEmp()
Employee.raise_ratio = 1.2
emp1.raise_salary()
emp1.showEmp()

emp2 = Employee("박찬호", 2000)
emp2.showCount()
emp2.showEmp()
emp2.raise_salary()
emp2.showEmp()

# =============================================================================
# 오후 수업
# =============================================================================
class Person:
    hobbys = [] #클래스 변수처럼 선언 
    def __init__(self, name):
        self.name = name
    def add_hobby(self, hobby):
        self.hobbys.append(hobby)  #hobbys에 hobby를 추가함/self가 있어도 클래스 변수가 될 수 있다.
    def show_info(self):
        print(self.name, self.hobbys)

p1 = Person("홍길동")
p1.add_hobby("음반수집")
p1.show_info()

p2 = Person("박찬호")
p2.show_info()   
p2.add_hobby("글쓰기")
p2.show_info()

#hobbys =[]를 __init__에 넣으면 클래스 변수가 아니라 인스턴스 변수가 될 수 있다.
class Person:
    #hobbys = [] #클래스 변수처럼 선언 
    def __init__(self, name):
        self.name = name
        self.hobbys = [] 
    def add_hobby(self, hobby):
        self.hobbys.append(hobby)  #hobbys에 hobby를 추가함/self가 있어도 클래스 변수가 될 수 있다.
    def show_info(self):
        print(self.name, self.hobbys)

p1 = Person("홍길동")
p1.add_hobby("음반수집")
p1.show_info()

p2 = Person("박찬호")
p2.show_info()   
p2.add_hobby("글쓰기")
p2.show_info()


#raise_ratio 중심으로 살펴보기 
class Employee:
    raise_ratio = 1.1  #클래스변수처럼 선언되어있더라도 이 변수는 인스턴스 변수로 사용될 수 있다. 
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def emp_info(self):                 #인스턴스 메소드
        print("이름 : ",self.name,"급여 : ",self.salary)
    
    def rasie_salary(self):             #인스턴스 메소드
        self.salary = int(self.salary*self.raise_ratio)

emp1 = Employee("홍길동", 1000)
emp1.emp_info()
print(emp1.raise_ratio) 
emp1.raise_ratio = 1.2 #인스턴스 변수 -> 자기영역에서만 1.2로 사용됨
print(emp1.raise_ratio)  #인스턴스 변수
emp1.rasie_salary()
emp1.emp_info()

emp2 = Employee("박찬호", 2000)
emp2.emp_info()
print(emp2.raise_ratio)  #인스턴스변수
emp2.rasie_salary()      #1.1인상
emp2.emp_info()


#클래스 메소드: 모든 인스턴스가 그 메소드를 적용해서 사용하는 것
# raise_ratio를 변경시 다른 인스턴스에서도 계속 적용되도록 만들기
class Employee:
    raise_ratio = 1.1  
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def emp_info(self):                 
        print("이름 : ",self.name,"급여 : ",self.salary)
    
    def rasie_salary(self):             
        self.salary = int(self.salary*self.raise_ratio)
    @classmethod    #@classmethod: 바로 밑에는 클래스 메소드라는 지시자        
    def change_raise_ratio(cls, ratio): #클래스 메소드에서는 cls.매개변수를 만들어야 함
        cls.raise_ratio = ratio #cls.매개변수를 만들어야 함 / #classmethod를 이용하여 위의 raise_ratio=1.1의 변경작업을 함
        print("인상률", round((ratio-1)*100), "%")

#@classmethod: 바로 밑에는 클래스 메소드라는 지시자        
#cls: 클래스 메소드를 의미하는 매개변수(self대신)
#이용: 온라인 게임시 내가 죽었을 때 상대방도 내가 죽은 것으로 나와야하기 때문에 클래스 메소드로 적용하여야 한다.        
emp1 = Employee("홍길동", 1000)     #1
emp1.emp_info()                     #2
print(emp1.raise_ratio)             #3
emp1.change_raise_ratio(1.2)        #4      #내 인스턴스에서 rasie_ratio를 1.2로 변경함 (원래 인스턴스 메소드 변수였으니, cls.를 사용하면서 class 변수로 적용된다.)
print(emp1.raise_ratio)             #5
emp1.rasie_salary()
emp1.emp_info()
print(emp1.raise_ratio)             #11
Employee.change_raise_ratio(1.6)    #12
print(emp1.raise_ratio)             #13

emp2 = Employee("박찬호", 2000)     #6
emp2.emp_info()                     #7
print(emp2.raise_ratio)             #8  #홍길동에서 변경된 raise_ratio 1.2로 변경되어서 나옴 
emp2.rasie_salary()      
emp2.emp_info()

emp2.change_raise_ratio(1.5)        #9
print(emp2.raise_ratio)             #10 #나만 적용되는 것이 아니라 다른 인스턴스 안에서도 적용된다.
print(emp2.raise_ratio)             #14


인스턴스 메소드: 인스턴스를 통해 호출되고 인수값은 인스턴스 자신을 자동으로 전달하는 self를사용해야 한다. 

클래스 메소드: 클래스를 통해 호출되고 @classmethod 데코레이터로 정의하고 클래스 자신을 자동으로 전달하는 인자 cls사용 

스택틱 메소드: 인자를 받지 않는다. (인수값을 받지 않는다.), 함수를 그냥 모아놓을 때 사용하는 것이 좋다. 
(예를들어 math라는 class를 만들고 여러 수학함수를 만들어 놓을 때 그때마다 @staticmethod 를 사용하면 인자값을 넣지 않아도 함수로써 이용이 가능하다.)


class test:
    num = 0
    @staticmethod       #호출하면서 값을 넣는다. /굳이 인스턴스화를 안해도 된다. 
    def add(x,y):
        return x+y
    
t = test
#인스턴스를 통해서 호출
t.add(1,1)
# 클래스를 통해서 호출
test.add(10,20)


class test:
    num = 0            #num=0과 num=x+y의 num은 서로 다른 num이다. 
    @staticmethod    
    def add(x,y):
        num = x+y
        return num
    
t.add(1,2)
test.add(10,21)


# count_viva = classmethod(count_viva)는 @classmethod(데코레이터 classmethod)와 같다. 
##classmethod
#방법1) classmethod로 재적용한다. count_viva = classmethod(count_viva) 
#방법2) 데코레이터 classmethod를 사용한다. 
class Viva:
    cnt = 0                     #클래스 변수
    def __init__(self, name):
        self.name = name #self.name 인스턴스 변수
        print("{}님이 게임방에 들어왔습니다.".format(self.name))
        Viva.cnt += 1
    
    #@classmethod    
    def count_viva(cls):                #인스턴스 상관없이 적용되고 있음
        print("현재{}명이 남았습니다.".format(cls.cnt))  #cls.cnt는 class 변수 / 클래스이름.변수이름(Viva.cnt)라고 해도 된다.
    count_viva = classmethod(count_viva) #classmethod로 재적용 
    
    def __del__(self):  #__del__생성자: 소멸자  # __init__밑에 적용해도 된다. #소멸자는 del하면 돌아가게 된다.
        print("{}님이 게임방에서 나갔습니다.".format(self.name))
        Viva.cnt -=1
        
        
man1 = Viva("홍길동")   #1
man1.count_viva()       #2 #Error남 -> 확인해서 고쳐야함 ㅠㅠ
del man1                #5 #del 인스턴스이름 
man1.count_viva()       #7

man2 = Viva("박찬호")    #3
man2.count_viva()       #4
del man2                #6


class Viva:
    cnt = 0                     #클래스 변수
    def __init__(self, name):
        self.name = name #self.name 인스턴스 변수
        print("{}님이 게임방에 들어왔습니다.".format(self.name))
        Viva.cnt += 1
    
    @classmethod    
    def count_viva(cls):                #인스턴스 상관없이 적용되고 있음
        print("현재{}명이 남았습니다.".format(cls.cnt))  #cls.cnt는 class 변수 / 클래스이름.변수이름(Viva.cnt)라고 해도 된다.
    
    def __del__(self):  #__del__생성자: 소멸자  # __init__밑에 적용해도 된다. #소멸자는 del하면 돌아가게 된다.
        print("{}님이 게임방에서 나갔습니다.".format(self.name))
        Viva.cnt -=1

 
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 09:51:07 2018

@author: stu
"""
# =============================================================================
# 오전 수업
# =============================================================================

#
id_number1 = "010101-3123456"
id_number2 = "990101-2123456"

def id_process(id):
    gender = id[7]
    if gender == "1" or gender == "2":
        year = "19"+id[:2]
    else:
        year = "20"+id[:2]
    
    if gender == "2" or gender == "4":
        gender = "여성"
    else:
        gender = "남성"
    
    month = id[2:4]
    day = id[4:6]
    
    return year, month, day, gender

id_process(id_number1)
id_process(id_number2)   


#__str__: print라는 기능, 즉 인스턴스를 호출하게 되면 무조건 출력하게 됨 
#굳이 함수를 만들어 불러들여 출력하지 않아도 __str__을 통해 출력이 가능하다. 
class Person:
    
    def __init__(self, year, month, day, gender):
        self.year = year
        self.month = month
        self.day = day
        self.gender = gender 

    def __str__(self):
        return"{}년 {}월 {}일 성별은 {}입니다.".format(self.year, self.month, self.day, self.gender)

p = Person(2018, 10, 11, "남")
print(p)

#밑의 인수값을 넣어서 위의 클래스에서 정의된 함수를 통해서 return값을 출력하고 싶을 때 
id_number1 = "010101-3123456"
id_number2 = "990101-2123456"

#Error발생
p1 = Person(id_process(id_number1)) 
# *을 붙여 가변문자임을 명시한다. ; 함수앞에는 *을 꼭 넣어준다.
p1 = Person(*id_process(id_number1))
print(p1)


#클래스 메소드로 호출 하기
# 클래스 메소드 밖에서 클래스 변수를 선언하고자 한다면 cls.를 붙여야 한다. 
# 하지만    @classmethod안에서 선언되면 각각의 변수들에 굳이 cls.를 붙일 필요가 없다. 

class Person:
    
    def __init__(self, year, month, day, gender):
        self.year = year
        self.month = month
        self.day = day
        self.gender = gender 

    def __str__(self):
        return"{}년 {}월 {}일 성별은 {}입니다.".format(self.year, self.month, self.day, self.gender)
   
    @classmethod  #클래스 메소드로 바꾸기: 인스턴스 메소드로 사용하면 안된다. -> 이때는 클래스 메소드로 사용해야한다. 왜냐하면 모든 인스턴스에 메소드가 적용되기 위해서 / 클래스 메소드는 self대신 cls를 사용해야한다.
    def id_process(cls,id):                 #id_process(cls, id)
        gender = id[7]
        if gender == "1" or gender == "2":
            year = "19"+id[:2]
        else:
            year = "20"+id[:2]
        
        if gender == "2" or gender == "4":
            gender = "여성"
        else:
            gender = "남성"
        
        month = id[2:4]
        day = id[4:6]
        
        return cls(year, month, day, gender) #cls(변수들)
    
p1 = Person.id_process(id_number1)
print(p1)

p2 = Person.id_process(id_number2)
print(p2)



#상속
재사용의 방법

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("{}객체를 만드는 중".format(self.name))
    def show_info(self):
        print("이름은 {}, 나이는 {}세이다.".format(self.name, self.age))
        
p1 = Person("홍길동", 20)
p1.show_info()


# 중복되는 코드는 따로 class에 만들어 놓고 상속받으면 유용하다.
# 학생이라는 class는 Person이라는 class를 상속받음
class Student(Person):  #class Student(Person): Person이라는 class를 상속받음
    def __init__(self, name, age, hakbun): 
        Person.__init__(self, name, age)  #생성자에서도 Person의 class를 받고자 할 때 
        self.hakbun = hakbun
        
    def show_info(self): 
        Person.show_info(self) #Person 클래스에서의 함수 show_info도 사용하고자 할때
        print("학번은 {}입니다.".format(self.hakbun))

s1 = Student("홍길동", 20, 20181011)
s1.show_info()

# 
class Professor(Person):
    def __init__(self, name, age, years):
        Person.__init__(self, name, age)
        self.years = years
    
    def show_info(self):
        Person.show_info(self)
        print("근무연수가 {}년 입니다.".format(self.years))
        
p1 = Professor("정교수", 40, 10)
p1.show_info()


# =============================================================================
# [문제191] Person 클래스를 생성하세요. 생성자는 이름, 나이, 성별을 만드세요.
Person 클래스 에는 printMe 메소드를 생성하셔서 이름, 나이 성별을 출력합니다.

Employees클래스를 생성한후 Person상속받습니다.
생성자는 이름, 나이, 성별, 주소, 생일입니다.
단 이름, 나이, 성별은 person에서 상속받으세요.
Employees 클래스에 printMe를 재구성하셔서 주소, 생일을 출력하세요.


myPerson = Person("홍길동","10", "남")
myPerson.printMe()

myEmployee = Employee("송준기", "2", "남", "서울", "2016년 01월 01일")
myEmployee.printMe()



이름은 홍길동 ,  나이는 10살 이고, 성별은 남 입니다.
이름은 송준기 ,  나이는 2살 이고, 성별은 남 입니다.
집 주소는  서울  생일은  2016년 01월 01일 입니다. 
# =============================================================================

#답1
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def printMe(self):
        print("이름은 {}, 나이는 {}살 이고, 성별은 {}입니다.".format(self.name, self.age, self.gender))
        #print( + + + ), +로  만들경우 인스턴스를 만들 때 꼭 문자열("")로 만들어 줘야한다. 

myPerson = Person("홍길동","10", "남")
myPerson.printMe()

class Employee:
    def __init__(self, name, age, gender, addr, birth):
        Person.__init__(self, name, age, gender)
        self.addr = addr
        self.birth = birth
        
    def printMe(self):
        Person.printMe(self)
        print("집 주소는 {} 생일은 {} 입니다.".format(self.addr, self.birth))
        
myEmployee = Employee("송준기", "2", "남", "서울", "2016년 01월 01일")
myEmployee.printMe()


#print( + + + ), +로  만들경우 인스턴스를 만들 때 꼭 문자열("")로 만들어 줘야한다. 

# =============================================================================
# 수업 
# =============================================================================
# Person의 int의 매개변수를 그대로 사용하고자 할 때 pass를 그냥 써주면 된다.
class Emp(Person):
    pass

e = Emp("홍길동", 10, "남")
e.printMe()



# 상속은 여러개를 받을 수 있다. 여러개의 상속을 받을 경우 괄호 안에 상속할 클래스를 나열하면 된다. 
class Emp(Person1, Person2):
    
    
# =============================================================================
# [문제192] Add 클래스에 두수를 더하는 값을 리턴하는 add 메소드 생성
Multiply 클래스에 두수를 곱한값을 리턴하는 multiply 메소드 생성
Divide 클래스에 두수를 나눈값을 리턴하는 divide메소드 생성
Calculator클래스에는 Add, Multiply, Divide 상속받고 두수를 뺀값을 리턴하는 sub 메소드 생성하세요.

# =============================================================================

class Add:
    def add(self, x, y):
        result = 0
        self.x = x
        self.y = y
        self.result = x + y
        return self.result

 
class Multiply:
    def multiply(self, x, y):   
        result = 1
        self.x = x
        self.y = y
        self.result = x * y
        return self.result
        
class Divide:
    def divide (self, x, y):   
        result = 1
        self.x = x
        self.y = y
        self.result = x / y
        return self.result
        
class Calculator(Add, Multiply, Divide):
    def sub(self, x, y):
        result = 0
        self.x = x
        self.y = y 
        self.result = x-y
        return(self.result)
    

                

cal = Calculator()
print(cal.add(10,20))
print(cal.multiply(10,20))


#쌤답
class Add:
    def add(self, x, y):
        return x + y
 
class Multiply:
    def multiply(self, x, y):
        return x*y
        
class Divide:
    def divide(self, x, y):
        return x/y      
        
class Calculator(Add, Multiply, Divide):
    def sub(self, x, y):
        return x-y

cal = Calculator()
print(cal.add(10,20))
print(cal.multiply(10,20))

# =============================================================================
# 오후수업
# =============================================================================

#인스턴스 함수임 (self, x, y)
class Calculator:
    def add(self, x, y):
        return x + y
    
    def sub(self, x, y):
        return x-y
    
    def multiply(self, x, y):
        return x*y    

    def divide(self, x, y):
        return x/y  
    


Calculator.add(1,2)     #오류
#Calculator.add(1,2)가 error가 난다.
#인스턴스 메소드이기 때문에 인스턴스화를 먼저 해야한다.
c = Calculator()
c.add(1,2)

■ staticmethod
#클래스 메소드, 인스턴스 메소드 모두 적용될 수 있는 것은 스태틱 메소드이다. 
#1) 클래스이름.메소드 가능(어떤 인스턴스에 상관없이 같이 사용할 수 있음) 2)인스턴스이름.메소드 가능 -> 클래스 또는 인스턴스로 모두 접근(access)이 가능하다.
# self, cls를 넣으면 안된다.
class Calculator:
    @staticmethod
    def add(x, y):
        return x + y
    @staticmethod
    def sub(x, y):
        return x-y
    @staticmethod
    def multiply(x, y):
        return x*y    
    @staticmethod
    def divide(x, y):
        return x/y  


# =============================================================================
# 모듈 만들고 이용하기
# =============================================================================
■ 모듈 만들고 이용하기
#클래스 메소드로 사용 가능
Calculator.add(1,2)     
#인스턴스 메소드로 사용 가능 
c = Calculator()
c.add(1,2)

■ 모듈식으로 저장하기
- 내가 만든 클래스나 메소드를 모듈로 만들기 
- 예시> c:\data\cal.py로 저장하기

-설정 
파일 형식: 모든파일
파일확장자: .py
인코딩: utf-8 

- import하기
import sys
#path확인
sys.path
#path가 안걸려 있을 경우 추가하기
sys.path.append("c:\data")

#cal 모듈 import하기
import cal
#cal이라는 모듈안에 클래스와 메소드 확인하기 
dir(cal)

#calculator를 인스턴스화하기  :모듈이름.클래스이름
c=cal.Calculator()
c.add(1,2)

#바로 클래스 이름을 쓰고 싶을 때 (from 모듈 import *)
from cal import *
c = Calculator()

#잘 안됨 ㅠ
a = add(1,2)
a.add()


# 모듈 이름으로 불러들이기
PI = 3.141592
class Math:
    def cal(self, r):
        return PI*(r**2)

def mySum(i,j):
    return i+j

#if __name__ =="__main__":   이 조건문은 import할 때 if이하의 로직이 돌아가지 않는다.
if __name__ =="__main__":
    print(PI)
    m = Math()
    print(m.cal(10))
    print(mySum(PI,10))
    
# import 하기
import math_1
math_1.PI
math_1.mySum(1,2)


#모듈안에 무엇이 들어있는지 확인하기
dir(math_1)

print(math_1.PI)
m = math_1.Math()
m.cal(10)
math_1.mySum(math_1.PI,10)

from math_1 import *
print(PI)
m1 = Math()
m1.cal(10)
mySum(PI, 10)


# =============================================================================
# 다중상속
# =============================================================================
■ 다중상속

class mother:
    def talk(self):
        print("대화를 합니다.")

class father:
    def running(self):
        print("달리기를 합니다.")
        
class child(mother, father):
    def play(self):
        print("난 노는게 제일 좋아")
        
m = mother()
m.talk()
f = father()
f.running()
c = child()
c.talk()
c.running()
c.play()
#child가 무슨 상속을 받았는지 확인하기
print(child.__mro__)


class Person:
    country = "한국" #country는 클래스 변수이면서 인스턴스 변수가 될 수 있다.
    def __init__(self, name):
        self.name = name
    def myPrint(self):
        print(self.name + "은 " + self.country+"사람이다")

p1 = Person("홍길동")
p1.myPrint()

p2 = Person("제임스")
p2.country = "핀란드" #인스턴스가 다르기 때문에 다르게 적용된다.
p2.myPrint()

Person.country = "영국" #클래스 변수가 된다. 
p2.myPrint()
p1.myPrint()

#
class Person:
    country = "한국" #country는 클래스 변수이면서 인스턴스 변수가 될 수 있다.
    def __init__(self, name):
        self.name = name
    def myPrint(self):
        print(self.name + "은 " + self.country+"사람이다")

p1 = Person("홍길동")    #1
p1.myPrint()             #4

p2 = Person("제임스")    #2
p2.country = "핀란드"    #6  #인스턴스가 다르기 때문에 다르게 적용된다.
p2.myPrint()            #7

Person.country = "영국" #3 #클래스 변수가 된다. 
p2.myPrint()            #5
p1.myPrint()

#country를 한국으로 항상 상수처럼 사용하기 : __country 
class Person:
    __country = "한국" #country는 클래스 변수이면서 인스턴스 변수가 될 수 있다.
    def __init__(self, name):
        self.name = name
    def myPrint(self):
        print(self.name + "은 " + self.__country+"사람이다")

p1 = Person("홍길동")    #1
p1.myPrint()             #4

p2 = Person("제임스")    #2
p2.country = "핀란드"    #6  #인스턴스가 다르기 때문에 다르게 적용된다.
p2.myPrint()            #7

Person.country = "영국" #3 #클래스 변수가 된다. 
p2.myPrint()            #5
p1.myPrint()



# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 09:47:37 2018

@author: stu
"""

[참조 : https://docs.python.org/ko/3/library/exceptions.html]

# =============================================================================
# [문제193] 양의 정수값만 입력 받아서 나누기를 수행하는 positive_divide 함수를 생성하세요.
# =============================================================================

#답1
def positive_divide():            
    try:    
        numerator = int(input("분자 숫자를 입력하세요 :"))
        denominator = int(input("분모 숫자를 입력하세요 :"))
 
        if(denominator < 0):  
            raise ValueError
        return  numerator / denominator
    except ValueError:
        print('오류  - 음수로 나눌수 없습니다.', denominator)
    except ZeroDivisionError as error:
        print('오류 -  0으로 나눌수 없습니다.',error)
            
positive_divide()

#답2 
def positive_divide(): 
    
    numerator = int(input("분자 숫자를 입력하세요 :"))
    denominator = int(input("분모 숫자를 입력하세요 :"))
    
    try:
        if denominator > 0:      
            result = numerator/denominator
            return result
        
        elif denominator < 0:
            raise Exception("오류 - 음수로 나눌 수 없습니다. -2")
        
        elif denominator == 0:
            raise Exception("오류 - 0으로 나눌 수 없습니다. division by zero")
    except Exception as error:
        print(error)

#쌤답 
def  positive_divide():
    try:
      
        x = int(input(' 분자 숫자를 입력하세요 : '))
        y = int(input(' 분모 숫자를 입력하세요 : '))
        
        if(y < 0):  
            raise ValueError
        return  x / y
    except ValueError:                          #내장되어있는 error
        print('오류  - 음수로 나눌수 없습니다.', y)
    except ZeroDivisionError as error:          #내장되어있는 error
        print('오류 -  0으로 나눌수 없습니다.',error)


# 클래스를 통해서 사용자 exception처리가 가능하다 
class NegativeDivisionError(Exception):     #Excetpion을 처리하기 위한 class를 만들어 놓음  
    def __init__(self, value):
        self.value = value
        
def  positive_divide():
    try:
        # n = NegativeDivisionError             -> 인스턴스화 해서 사용한 것을 씀; 그러나 굳이 하지 않아도 되기 때문에 #처리함 
        
        x = int(input(' 분자 숫자를 입력하세요 : '))
        y = int(input(' 분모 숫자를 입력하세요 : '))
        
        if(y < 0):  
            raise NegativeDivisionError(y)
        return  x / y
    except NegativeDivisionError as error:      #class에서 만든 error값을 만들어 error값을 그대로  
        print('오류  - 음수로 나눌수 없습니다.', error)
    except ZeroDivisionError as error:
        print('오류 -  0으로 나눌수 없습니다.',error)
        
# =============================================================================
# [문제194] 한주간동안 걸음수를 요일별로 그래프를 그리세요.
#         단 막대그래프 함수를 생성해서 인수값으로 걸음수, 요일을 입력하면 그래프가 그려지도록하세요.
# =============================================================================

# class walkPlot:
#          
#     def __init__(self, step, day):
#         self.step = step
#         self.day = day
#      
#     def walk(self):
#         walk = {self.step: self.day}
#         return walk
#     
#     def plot(self):
#         plt.bar()
#         plt.
#         
#     
#    
#     def plot(self):
#          
# 
# day1 = walkPlot(3000, "월")
# day1.walk()
# 
# day2 = walkPlot(5000, "화")
#day2.walk()


#쌤답
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

def create_bar_chart(data, labels,bar):

    num_bars = len(data)

    positions = range(1, num_bars+1)
    if bar == 1:        
        plt.bar(positions, data, align='center')
        plt.xticks(positions, labels)   #기본은 1,2,3,4..로 나오지만 요일로 나오게 만들기 위해서 
        plt.xlabel('요일')  
        plt.ylabel('걸음수')
       
    else:
         plt.barh(positions, data, align='center')
         plt.yticks(positions, labels)
         plt.xlabel('걸음수')
         plt.ylabel('요일')
    

    plt.title('한주간 동안 걸음수') 
    plt.grid()
    plt.show()
    
if __name__=='__main__':
    step = [1090,2000,3000,4000,10000,50000,2000]
    labels = ['월','화','수','목','금','토','일']
    create_bar_chart(step,labels,2)

if __name__=='__main__':
    step = [1090,2000,3000,4000,10000,50000,2000]
    labels = ['월','화','수','목','금','토','일']
    create_bar_chart(step,labels,1)



# 클래스로 만들기 
import matplotlib.pylab as plt
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

class create_bar_chart:
    def __init__(self,data, labels, bar):
        self.data = data
        self.labels = labels
        self.bar = bar
        
    def create_bar_chart(self):
    
        num_bars = len(self.data)
    
        positions = range(1, num_bars+1)
        if self.bar == 1:
            plt.bar(positions, self.data, align='center')
            plt.xticks(positions, self.labels)
            plt.xlabel('요일')
            plt.ylabel('걸음수')
           
        else:
            plt.barh(positions, self.data, align='center')
            plt.yticks(positions, self.labels)
            plt.xlabel('걸음수')
            plt.ylabel('요일')
        
    
        plt.title('한주간 동안 걸음수') 
        plt.grid()
        plt.show()
    
if __name__=='__main__':
    step = [5000,6000,7500,10000,10000,20000,2000]
    labels = ['월','화','수','목','금','토','일']
    cbc = create_bar_chart(step,labels,1)
    cbc.create_bar_chart()


# =============================================================================
# 오후 수업
# =============================================================================
import collections

#Counter: 컨테이너 ['a','b','a','c','a','b'] 안에 있는 동일한 값의 자료가 몇개인지를 파악한다. (빈도수 체크)
#컨테이너라는 것은 자료형이라고 보면 된다. 
#결과 값은 dictionary형태로 key:value값응로 제공한다. 빈도수가 높은 것부터 진열된다. 
collections.Counter(['a','b','a','c','a','b'])

collections.Counter(['우리','나라','우리','대한민국','우리','행복'])

#update: 후에 추가해서 값을 출력할 수도 있다.
container = collections.Counter()
container.update('aaaabbbbbccczzzzzzz')
print(container)

#추가기능
container.update({'c':2, 'e':5}) #'c':는 sum 'e'는 추가가 됨
print(container)

for i in 'abcdefyz':
    print('%s : %d'%(i,container[i]))

#c는 dictionary형으로 만들어진다. 따라서 key와 c.items(), c.keys(), c.values()와 같은 메소드를 사용할 수 있다.
c = collections.Counter("hellow james")
print(c)
c.keys()
c.values()
c.items()

#dict_keys를 지우기
list(c.keys())
list(c.items())

# 글자하나씩 counting함 
ct = collections.Counter()
with open("c:\data\hello.txt", "r") as f: #객체는 f로 선언함
    for i in f:
        ct.update(i.rstrip().lower()) #영어는 대소문자를 구분하기 때문에, 소문자로 만들기 + 띄어쓰기 없애기

print(ct)

#상위 5위 이상 
for i, c in ct.most_common(5):
    print("%s : %d"%(i,c))
    

# =============================================================================
# 사용자 구축 사전 만들기 pip install customized_konlpy
# =============================================================================
# anaconda prompt에서 실행
pip install customized_konlpy

#
from konlpy.tag import Twitter

twitter = Twitter()

# 
txt = "텍스트 마이닝은 텍스트 형태의 데이터를 수학적 알고리즘에 기초하여 수집, 처리, 분석, 요약하는 연구기법을 통칭하는 용어이다."

#container 로 담아서 명사수 세기
collections.Counter(twitter.nouns(txt))

#사용자 구축사전  #add_dictionary는 지속되지 않기 때문에 add_dictionary()코드를 같이 가지고 돌려야 한다. 
from ckonlpy.tag import Twitter
twitter = Twitter()
twitter.add_dictionary('마이닝','Noun') 

#단어 추가한 후 container.Counter로 명사수 세기
collections.Counter(twitter.nouns(txt))

# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 09:50:40 2018

@author: stu
"""

▣ Numpy
- 과학계산을 위한 라이브러리를 다차원배열을 처리하는데 필요한 기능을 제공한다.
- numpy 배열은 동일한 타입의 값들을 갖는다. 
- 배열의 차원을 rank라고 한다. 
- 신경망을 할 때 Numpy가 필요함 

■ 설치
pip install numpy

■ 불러들이기
import numpy as np

■ numpy 배열 생성
- 파이썬의 리스트를 사용하는 방법

z1 = np.array([1,2,3])
print(z1)
type(z1) #numpy.ndarray: 다차원 배열의 의미
z1.dtype #다차원 배열에 들어가 있는 데이터 형; 32bit운영체제에서 사용하는 integer  => 4GB정도 변수를 처리할 수 있다. 
z1.shape

z2 = np.array([[1,2,3],[4,5,6]])
print(z2)
type(z2)
z2.dtype
z2.shape

lst = [[1,2,3],[4,5,6],[7,8,9]]
z3 = np.array(lst)
z3.shape
#slicing하기
z3[0,]  #0행을 보여줌 
z3[1]   #1행을 보여줌
z3[:,0] #모든행(:)의 0열을 보여줌
z3[:,1] #모든행(:)의 1열을 보여줌
z3[:,2] #모든행(:)의 2열을 보여줌 
z3[0:2, 0] #0, 1행의 0열을 보여줌
z3[1:,1:]  #1행부터 ~다, 1열부터 다~ 보여 줌
z3[1:,:1]  #1행부터 ~다, 0열만 
z[0:2, 0:2]

■ 정수 인덱싱(integer indexing)
numpy배열 n에 대해서 n[[row1, row2], [col1, col2]]는 
n[row1, col1], n[row2, col2]
-> 두번 작성해야할 것n[row1, col1], n[row2, col2]을 한번n[[row1, row2], [col1, col2]]에 작성할 수 있다. 

lst = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
n = np.array(lst)
n[0,1] #0행 1열
n[2,3] #2행 3열
n[[0,2],[1,3]]  #[행],[열]

■ 부울린 인덱싱(boolean indexing)
lst = [[1,2,3],[4,5,6],[7,8,9]]
n = np.array(lst)
b = np.array([[False, True, False],
              [True, False, True],
              [False, True, False]])
n[b] #n이라는 array를 기준으로 b라는 부울린 값의 True값만 값을 나타냄

#조건절에 true값만 뽑아내기
b = (n % 2 == 0)
n[b]
n[n%2 == 0]

■ numpy에서 제공하는 함수를 사용해서 만드는 방법
□ zeros()함수는 배열에 모두 0을 넣는 함수 
#3x3배열이 초기값으로 0이 출력됨
np.zeros((3,3))

□ ones()함수는 배열에 모두 1을 넣는 함수
#4x4배열이 초기값으로 1이 출력됨
np.ones((4,4))

□ full()함수는 사용자가 지정한 값을 넣는 함수 
#3x3배열이 초기값으로 사용자가 지정한 값인 2로 출력됨
np.full((3,3),2)

□ eye()함수는 대각선으로 1이고 나머지는 0인 2차원배열을 생성
np.eye(3)
np.eye(4)

□ range(n)함수는 0~n-1까지의 숫자를 생성하는 함수
np.array(range(20)) #1차원 배열 

□ .reshape: 다차원을 변형하는 함수  #cf. r의 배열의 차원 바꾸기: reshape
z= np.array(range(20)).reshape(4,5)
z.reshape((20,))
z.reshape((5,4))
z.reshape(5,4)

■ numpy 연산
x = np.array([1,2,3])
y = np.array([4,5,6])
#인덱스를 가지고 연산하는 방법
x[0] + y[0]
x[1] + y[1]
x[2] + y[2]
# x와 y가 배열 형태가 같기 때문에 내부적으로 같은 방끼리 연산 된다. 
x+y
np.add(x,y)

x-y
np.subtract(x,y)

#같은 방끼리 곱해짐. 행렬의 곱이 아님
x*y
np.multiply(x,y)

x/y
np.divide(x,y)

lst1 = [[1,2],[3,4]]
lst2 = [[5,6],[7,8]]

x = np.array(lst1)
y = np.array(lst2)

#x의 0행 0열, y의 0행0열의 합
#행과 열을 표현할 때 둘다 가능
x[0,0] + y[0,0]
x[0][0]+y[0][0]

#2차원 배열에서도 np.사칙연산 가능
x+y
np.add(x,y)

x-y
np.subtract(x,y)

x*y
np.multiply(x,y)

x/y
np.divide(x,y)


#행렬의 곱 
np.dot(x,y)

x     y
1,2   5,6   (1*5 + 2*7)  (1*6 + 2*8) =(19, 22)
3,4   7,8   (3*5 + 4*7)  (3*6 + 4*8) =(43, 50)

x = np.array([[1,2],[3,4]])
np.sum(x)          #전체합
np.sum(x, axis=0)  #axis=0 열을 기준으로 해서 sum을 함
np.sum(x, axis=1)  #axis=1 행을 기준으로 해서 sum을 함

np.mean(x)          #전체평균
np.mean(x, axis=0)  #열기준의 평균
np.mean(x, axis=1)  #행기준의 평균

np.var(x)          #전체분산
np.var(x, axis=0)  #열기준의 분산
np.var(x, axis=1)  #행기준의 분산

np.std(x)          #표준편차
np.std(x, axis=0)  #열기준의 표준편차
np.std(x, axis=1)  #행기준의 표준편차

np.max(x)           #최대값
np.max(x, axis=0)   #열기준의 최대값
np.max(x, axis=1)   #행기준의 최대값

np.min(x)           #최소값
np.min(x, axis=0)   #열기준의 최소값
np.min(x, axis=1)   #행기준의 최소값 

x       색인값
1, 2    (0, 1)
3, 4    (2, 3)
#최소원소의 색인값
np.argmin(x)
np.argmin(x, axis=0)  #[0,0] 0행 1열이 아니라 1,3(0,1), 2,4(0,1)임 
np.argmin(x, axis=1)  #[0,0] 0행 1열이 아니라 1,2(0,1), 3,4(0,1)임 
#최대원소의 색인값
np.argmax(x)
np.argmax(x, axis=0)  #[0,0] 0행 1열이 아니라 1,3(0,1), 2,4(0,1)임 
np.argmax(x, axis=1)  #[0,0] 0행 1열이 아니라 1,2(0,1), 3,4(0,1)임 

#누적합
np.cumsum(x)
np.cumsum(x, axis=0) #열기준 누적합
np.cumsum(x, axis=1) #행기준 누적합
#cf. 한계확률 구할 때 열기준의합, 행기준의 합이 필요하다. 주변확률을 생각해야 하기때문에 

#누적곱
np.cumprod(x)
np.cumprod(x, axis=0)
np.cumprod(x, axis=1)

#전체곱
np.prod(x)
np.prod(x, axis=0)
np.prod(x, axis=1)

■ numpy자료형
int, float, bool, complex

□ 정수형(integer)
int8, int16, int32, int64
int8 = 2**7
int16 = 2**15
int32 = 2**31
int64 = 2**63

□ 실수형(float)
float16, float32, float64

□ 복소수(complex): 부동소숫점으로 표시하는 복소수
complex64, complex128

x = np.float32(1.0)
print(x)
print(type(x))
x.dtype

■ .arange() 함수
z1 = np.arange(5)
z1.dtype

z2 = np.arange(5, dtype="f") #dtype을 통해서 자료형을 선택할 수 있음
z2.dtype

#cf arange :0부터 그 숫자만큼 출력

#실수형로 시작점 3, 끝점 4까지 표현
np.arange(3,5, dtype="f")
#실수형으로 3,9까지 표현  (증가분은 1씩 증가)
np.arange(3,10, dtype="f")
# 시작점 2부터 3이전까지를 0,2씩 증가한 값을 출력
np.arange(2,3,0.2)

arr = np.arange(10)
arr
arr.shape #1차원배열
#5행2열로 만들기
arr.reshape(5,2)  #기본값은 행우선으로 만들어진다.
arr.reshape((5,2), order="C") #행우선(기본값)
arr.reshape((5,2), order="F") #열우선

arr = np.arange(10).reshape((5,2), order="F")
arr

■ .flatten():2차원배열을 1차원배열로 평탄화시키는 방법
arr #열우선
arr.flatten() #기본값(행우선)
arr.flatten('C') #행우선
arr.flatten('F') #열우선

arr.ravel()
arr.ravel('C')
arr.ravel('F')

arr1 = np.array([[1,2,3], [4,5,6]])
arr2 = np.array([[7,8,9],[10,11,12]])


np.concatenate([arr1, arr2], axis=0) #열기준으로 붙이겠다.
np.concatenate([arr1, arr2], axis=1) #행으로 붙이겠다.

np.hstack((arr1, arr2)) #np.concatenate([arr1, arr2], axis=1)와 같은 값 #행기준
np.vstack((arr1, arr2)) #np.concatenate([arr1, arr2], axis=0)와 같은 값 #열기준

#합쳐놓은 것을 다시 자르기 위해서는 slicing을 하면된다.

■ numpy브로드캐스트(broadcast)
np.broadcast

x=np.array([[1,2],[3,4]])
y=10 

#차원이 다르기 때문에 값이 더해지지 않는다. 그러나 y가 x모양에 맞게 만들어져 연산작업을 함 
#브로드캐스트가 없으면 loop를 통해 연산작업을 해줘야한다. 
x+y


w = np.array([10,20])
x*w

■ 난수값 표현
□ rand: 0~1 사이에 균일한 확률분포로 실수 난수를 생성하는 함수
np.random.rand(10)
np.random.rand(3,5)

□ randn: 기대값 0이고 표준편차 1인 표준 정규분포를 나타내는 난수를 생성하는 함수
np.random.randn(3,5)

□ randint: 균일한 분포의 정수 난수
np.random.randint(low, high=None, size=None)
np.random.randint(10, size=10) # 10: 0~10 사이  #size=10: 10개
np.random.randint(10,20, size=10) #10,20: 작은값:10 큰값:20 #size=10:10개
np.random.randint(10,20, size=(3,5)) #size를 3x5행렬로 표현

■ .repeat()
arr = np.arange(3)
arr.repeat(2)
arr.repeat([2,3,4]) #0은 2번, 1은 3번, 2는 4번을 반복하고 싶음

arr = np.random.randint(10,20, size=(2,5))
arr
arr.repeat(2)
arr.repeat(2, axis=0)
arr.repeat(2, axis=1)

■ np.tile  #cf. repeat과 비교하기
np.tile(arr, 2) #덩어리로 반복하기 

■ np.unique(): 유일값만 뽑아냄 
np.unique([11,11,2,3,2,12,12])

u = np.array(['a','b','a','a','b','c'])
np.unique(u)
#값과 빈도수가 동시에 출력 (값에 대한 빈도수가 return됨)
np.unique(u, return_counts=True) 

index, count = np.unique(u, return_counts=True)
print(index)
print(count)
#위의 값과 동일
#x, y = np.unique(u, return_counts=True)
#print(x)
#print(y)

#2차원 배열일 때
u = np.array([[1,0,0],[1,0,0],[2,3,4]])
np.unique(u)
np.unique(u, axis=0) #0행과 1행이 중복되어 하나로 출력됨(열기준으로 보기)
np.unique(u, axis=1) #주의하기: 없으면 값이 출력되지 않아야 하는데 순서가 바뀌어 출력됨 -> 모호성 발생. 따라서 이부분을 쓸 때는 조심하자!

u = np.array([[1,0,0],[1,0,0],[1,0,0]])
np.unique(u)
np.unique(u, axis=0)
np.unique(u, axis=1)

#u = np.array([[1,0,1],[1,2,1],[1,3,1]])
#np.unique(u)
#np.unique(u, axis=0)
#np.unique(u, axis=1)

■ np.maximum()  /np.minimum() /np.add()
#data 수가 같아야 함(현재 data1과 data2는 각각 10개임 ); 동일한 때만 가능함
data1 = np.arange(0,20,2)
data2 = np.arange(0,30,3)

#data1, data2각각의 인덱스의 값을 비교해서 최대값을 뽑아내기 
np.maximum(data1, data2)
#data1, data2각각의 인덱스의 값을 비교해서 최소값을 뽑아내기 
np.minimum(data1, data2)
#더하기
np.add(data1, data2)
#합집합
np.union1d(data1, data2)
#교집합
np.intersect1d(data1, data2)
#차집합
np.setdiff1d(data1, data2)

arr = np.array([5,4,1,3,2])
#오름차순으로 되어있는 인덱스 번호를 return해줌 
arr.argsort() #array([2, 4, 3, 1, 0], dtype=int64) 1은 2번인덱스, 2은 4번인덱스, ... 5는 0번인덱스

#오름차순정렬
ix= arr.argsort()      #ix= arr.argsort()[::]와 같은 값 출력; 오름차순 정
arr[ix]

ix= arr.argsort()[::]   #ix= arr.argsort() 과 같은 값 출력; 오름차순 정
arr[ix]

#내림차순정렬
ix= arr.argsort()[::-1] #-1: 제일 뒤에서부터를 의미함
arr[ix]


■ numpy의 배열을 pandas로 변환
lst = [[1,2,3], [4,5,6],[7,8,9]]
arr = np.array(lst)

import pandas as pd

df = pd.DataFrame(arr)

df.index
df.columns
#loc, ix: 인덱스 번호와 컬럼이름을 가지고 값을 출력할 수 있음
#1번 행의 0열과 1열을 출력함
df.loc[1,[0,1]]
df.ix[0:2,[0,1]]
#인덱스 번호만 가지고 할 수 있음
df.iloc[1,[0,1]]

