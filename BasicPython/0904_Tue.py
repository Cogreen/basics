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