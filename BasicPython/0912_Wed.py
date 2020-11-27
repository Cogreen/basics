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