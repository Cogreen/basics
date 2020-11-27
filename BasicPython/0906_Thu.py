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

