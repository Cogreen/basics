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
    