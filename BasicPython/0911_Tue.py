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
