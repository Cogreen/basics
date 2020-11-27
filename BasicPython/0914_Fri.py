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
