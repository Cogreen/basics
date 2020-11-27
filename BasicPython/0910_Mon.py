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

