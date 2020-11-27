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
