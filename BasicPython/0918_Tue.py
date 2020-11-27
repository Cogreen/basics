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




