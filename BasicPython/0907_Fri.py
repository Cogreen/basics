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


