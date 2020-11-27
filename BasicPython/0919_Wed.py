# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 09:47:35 2018

@author: stu
"""
###############################################################################

[문제156]부서별로 급여 총액을 출력하세요.

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
nan 7000.0

# pandas에서 제공하는 isnull() 생각해서 풀기!

import pandas as pd
import numpy as np
from pandas import Series,DataFrame

emp = pd.read_csv("c:/data/emp.csv")
deptno = Series(emp['DEPARTMENT_ID'].unique())
deptno=deptno.sort_values()
deptno
for i in deptno:
    if pd.isnull(i):
        print(i, emp.loc[emp['DEPARTMENT_ID'].isnull(), 'SALARY'].sum())
    else:
        print (int(i), emp.loc[emp['DEPARTMENT_ID']==i, 'SALARY'].sum())



###############################################################################
   
▣ pandas      
■ groupby: pandas에서 grouping을 통한 집계값 구하기 

import pandas as pd
import numpy as np
from pandas import Series,DataFrame
import pandas as pd 
emp =pd.read_csv('c:/data/emp_new.csv',names=['empid','name','job','mgr','hire_date','sal','comm','deptno'])

# sql select 문
select deptno,sum(al)
from emp
group by deptno

# groupby 를 통한 함수
emp['sal'].groupby(emp['deptno']).sum()
emp['sal'].groupby(emp['deptno']).mean()
emp['sal'].groupby(emp['deptno']).var()
emp['sal'].groupby(emp['deptno']).std()
emp['sal'].groupby(emp['deptno']).count()
emp['sal'].groupby(emp['deptno']).max()
emp['sal'].groupby(emp['deptno']).min()

#grouping만 적용
deptno_group = emp['sal'].groupby(emp['deptno'])
#객체정보만 보여줌 
deptno_group
#
deptno_group.sum()
deptno_group.mean()

# 동일한 부서 안에서도 job이 다른 사원들의 결과값을 정리해줌 
#sql select문장
select deptno, job, sum(sal)
from emp
group by deptno, job
#pandas의 groupby사용 
emp['sal'].groupby([emp['deptno'], emp['job']]).sum()

dept_group = emp['sal'].groupby([emp['deptno'], emp['job']])
dept_group.sum()
dept_mean = dept_group.mean()
dept_mean

#unstack(): corsstable 모양으로 결과값이 출력됨
dept_mean.unstack()

#
emp.groupby(['deptno','job'])['sal'].sum()
#unstack(): corsstable 모양으로 결과값이 출력됨
emp.groupby(['deptno','job'])['sal'].sum().unstack()

#부서별로 data를 분리하여 바라보기  -> for문을 통해 출력 
#object 정보만 보임
emp.groupby('deptno')
# for 문을 통해 출력
for name, group in emp.groupby('deptno'):
    print(name)
    print(group)

★★★★★ # name1, name2.. 
for (name1, name2), gorup in emp.groupby(['deptno','job']):
    print(name1, name2)
    print(group)
    
        
#groupby는 NaN은 누락됨 -> 따라서 fillna와 같은 method를 사용하여 데이터를 정제한다음 적용하는 것이 좋다.
emp['sal'].groupby(emp['deptno'].fillna(0)).sum()


###############################################################################
[문제157] 년도별로 입사한 인원수 결과를 출력해주세요.
import pandas as pd
import numpy as np
from pandas import Series,DataFrame
import pandas as pd 
emp =pd.read_csv('c:/data/emp_new.csv',names=['empid','name','job','mgr','hire_date','sal','comm','deptno'])

import datetime


emp['hire_date']>='2005'
for name, group in emp.groupby(['hire_date']).count():
    print(name)
    print(group)


emp['hire_date'].dstrftime('%Y')
emp['hire_date']

emp.groupby(['hire_date']).count()

for i in emp['hire_date']:
   y = datetime.datetime.strptime(i, '%Y-%m-%d')  #char -> date
   print((y.strftime('%Y')))
   
   for j in year:
       if emp['hire_date'] == j: 
         
#답 
emp['empid'].groupby([i[0:4] for i in emp['hire_date']]).count()


[문제157] emp.csv 파일에 데이터 중에 년도별로 입사한 인원수 결과를 출력해주세요.

from pandas import Series, DataFrame
import pandas as pd
import numpy as np

#쌤답: 기존의 datatime을 사용할 수 없음 
# str.slice(,): 문자의 slicing 
emp = pd.read_csv("c:\data\emp_new.csv", names = ['empid','name','job','mgr','hire_date','sal','comm','deptno'])
emp.dtypes
#답1: str.slice 이용
print(emp.groupby(emp['hire_date'].str.slice(0,4))['empid'].count()) #문자이기 때문에 slicingㅇ르 할 수 있음 
#답2: .dt: pandas에서 제공하는 날짜 형을 바꿔주는 함수 (object만 보임)
# .dt.year: 년도를 뽑아냄
# .dt.month: 달을 뽑아냄

print(emp.groupby(pd.to_datetime(emp['hire_date']).dt.year)['empid'].count())
pd.to_datetime(emp['hire_date']).dt
pd.to_datetime(emp['hire_date']).dt.year
pd.to_datetime(emp['hire_date']).dt.month
pd.to_datetime(emp['hire_date']).dt.day
pd.to_datetime(emp['hire_date']).apply(lambda x: x.year)
pd.to_datetime(emp['hire_date']).apply(lambda x: x.month)

#format의 기본값: '2018-09-19 11:01:30', '20180919 11:01:30'
pd.to_datetime(Series('2018-09-19 11:01:30')).dt.year
pd.to_datetime(Series('2018-09-19 11:01:30')).dt.month
pd.to_datetime(Series('2018-09-19 11:01:30')).dt.day
pd.to_datetime(Series('2018-09-19 11:01:30')).dt.hour
pd.to_datetime(Series('2018-09-19 11:01:30')).dt.minute
pd.to_datetime(Series('2018-09-19 11:01:30')).dt.second
pd.to_datetime(Series('2018-09-19 11:01:30')).dt.quarter #분기
pd.to_datetime(Series('2018-09-19 11:01:30')).dt.dayofweek #(월요일=0, 일요일=6)
pd.to_datetime(Series('2018-09-19 11:01:30')).dt.dayofyear
pd.to_datetime(Series('2018-09-19 11:01:30')).dt.date
pd.to_datetime(Series('2018-09-19 11:01:30')).dt.time
pd.to_datetime(Series('2018-09-19 11:01:30')).dt.week
pd.to_datetime(Series('2018-09-19 11:01:30')).dt.days_in_month

# format을 사용하여 날짜의 형식을 새로 제공할 수 있음 
pd.to_datetime(Series('09192018 11:01:30'),format='%m%d%Y %H:%M:%S').dt.year



[문제158] emp_new.csv 를 emp리스트 변수안에 아래 모양과 같은 딕셔너리 데이터 유형에 데이트를 입력한 후 출력하세요.
# -> 앞으로 join과 관련된 문제를 풀기위해 필요한 부분임 
# list 변수안에 dictionary 형을 만들기 ;key -value 값
{'empno': 100, 'ename': King, 'job': AD_PRES, 'mgr': '', 'hiredate': 2003-06-17, 'sal': 24000, 'comm': '', 'deptno': 90}


100 King AD_PRES  2003-06-17 24000  90
101 Kochhar AD_VP 100 2005-09-21 17000  90
102 De Haan AD_VP 100 2001-01-13 17000  90
103 Hunold IT_PROG 102 2006-01-03 9000  60
104 Ernst IT_PROG 103 2007-05-21 6000  60

import csv
file = open("c:/data/emp_new.csv", 'r')
emp_csv =csv.reader(file) 
emp = []
for emp_list in emp_csv:
    emp.append({'empno':emp_list[0], 
    'ename':emp_list[1], 
    'job':emp_list[2], 
    'mgr':emp_list[3],
    'hiredate':emp_list[4],
    'sal':emp_list[5], 
    'comm':emp_list[6], 
    'deptno':emp_list[7]})
    
for e in emp:
    print(e['empno'], e['ename'], e['job'], e['mgr'],e['hiredate'], e['sal'], e['comm'], e['deptno'])
file.close()

# 잘못된 내답 ㅠ
import csv
file = open("c:/data/emp_new.csv", 'r')
emp_csv =csv.reader(file) 
emp={}
for emp_list in emp_csv:
    emp['empno']=emp_list[0], 
    emp['ename']=emp_list[1], 
    emp['job']=emp_list[2], 
    emp['mgr']=emp_list[3],
    emp['hiredate']=emp_list[4],
    emp['sal']=emp_list[5], 
    emp['comm']=emp_list[6], 
    emp['deptno']=emp_list[7]
    print(emp)



[문제159] emp_new.csv, dept_new.csv 파일을 읽어서 사원의 이름, 부서 이름을 출력하세요.
import csv
file1 = open("c:/data/emp_new.csv", 'r')
emp_csv =csv.reader(file1) 
emp = []
for emp_list in emp_csv:
    emp.append({'empno':emp_list[0], 
    'ename':emp_list[1], 
    'job':emp_list[2], 
    'mgr':emp_list[3],
    'hiredate':emp_list[4],
    'sal':emp_list[5], 
    'comm':emp_list[6], 
    'deptno':emp_list[7]})
file2 = open("c:/data/dept_new.csv", 'r')   
dept_csv = csv.reader(file2)
dept = []
for dept_list in dept_csv:
    dept.append({'deptno':dept_list[0],
                 'dname':dept_list[1],
                 'mgrid':dept_list[2],
                 'locid':dept_list[3]})      

for i in dept:
    for j in emp:
        if dept[i]['deptno']==emp[j]['deptno']:
            print(emp[j]['ename'], dept[i]['dname'])


import csv
file1 = open("c:/data/emp_new.csv", 'r')
emp_csv =csv.reader(file1) 
file2 = open("c:/data/dept_new.csv", 'r')   
dept_csv = csv.reader(file2)
for i in emp_csv:
    print(i)
    
    
    for j in dept_csv:
        if emp_list[][7]==dept_list[0]:
            print(emp_list[1], dept_list[1])
    

#쌤답
import csv
file1 = open("c:/data/emp_new.csv", 'r')
file2 = open("c:/data/dept_new.csv", 'r')   
emp_csv =csv.reader(file1)        
dept_csv = csv.reader(file2)
 
emp = []
dept = []

for i in dept_csv:
    dept.append({'deptno':i[0], 'dname':i[1], 'mgrid':i[2], 'locid':i[3]})

for j in emp_csv:
    emp.append({'empno':j[0], 
    'ename':j[1], 
    'job':j[2], 
    'mgr':j[3],
    'hiredate':j[4],
    'sal':j[5], 
    'comm':j[6], 
    'deptno':j[7]})
    
for d in dept:
    for e in emp:
        if e['deptno']==d['deptno']:
            print(e['ename'], d['dname'])
            
empfile.close()
deptfile.close()



[문제160] 사원들의 이름, 부서 이름을 출력하면서 소속부서가 없는 사원도 출력해주세요. 마지막에는 총건수도 출력하세요. 
import  csv
empfile = open("c:\data\emp_new.csv",'r')
deptfile = open("c:\data\dept_new.csv",'r')
emp_csv = csv.reader(empfile)
dept_csv = csv.reader(deptfile)

emp = []  
dept =[]

for i in  dept_csv:
    dept.append({'deptno':i[0],'dname':i[1],'mgr':i[2],'loc':i[3]})

for j in emp_csv:
    emp.append({'empno':j[0],'ename':j[1],'job':j[2],'mgr':j[3], 'hiredate':j[4],'sal':j[5],'comm':j[6],'deptno':j[7]})

cn = 0   # outer 조인 (driving 고정 +반대쪽이 driving 고정  cf. right outer join => left가 드라이빙 / left otuer join= > right이 드라이빙 )
for e in emp:
    if e['deptno'] == '':
        print(e['ename'])
        cn += 1
    else:
        for d in dept:
            if e['deptno'] == d['deptno']:
               print ( e['ename'], d['dname'])
               cn += 1

print(cn)

empfile.close()
deptfile.close()


#sql의 select 문장
select e.ename, d.dname
from emp e, dept d
where e.deptno = d.deptno:
    
select e.ename, d.dname
from emp e, dept d
where e.deptno = d.deptno(+):
    
select e.ename, d.dname
from emp e left otuer join dept d
where e.deptno =  d.deptno(+):
###############################################################################

from pandas import Series, DataFrame
import pandas as pd
import numpy as np

emp = pd.read_csv("c:/data/emp_new.csv", names=['empid','name','job','mgr','hire_date', 'sal','comm','deptno'])
dept = pd.read_csv("c:/data/dept_new.csv", names=['deptno','dname', 'mgr','loc'])

#몇개의 row와 몇개의 coulmn이 있는지 확인 
emp.shape
#columns 확인
emp.columns
#data type
emp.dtypes

■ pd.merge: pandas의 merge 
(#sql: merge는 dml 문장을 한꺼번에 실행할 수 있는 것)

#동일한 column이름(key값)이 존재하기 때문에 원하는 join결과가 나오지 않을 수 있음 -> deptno, mgr
#-> 이럴경우 먼저 나열 되어 있는 mgr을 기준으로 joind을 함
pd.merge(emp, dept)

#on 절을 통함 merge on에 쓴 것이 컬럼의 기준이 됨
pd.merge(emp, dept, on='deptno')

# on='deptno'을 기준으로 name, deptno, dname을 출력  (on절에 이름이 같을 경우 이렇게 실행하면 된다.)
pd.merge(emp[['name', 'deptno']],dept[['deptno','dname']], on='deptno')

# merge하고자 하는 컬럼의 이름이 다른 경우 left_on과 right_on을 사용하면 된다.  
# e.g., selfjoin시에 키 컬럼 이름이 달라지므로 selfjoin시 사용할 수 있다. 
pd.merge(emp[['name', 'deptno']],dept[['deptno','dname']],
         left_on='deptno', right_on='deptno')

# inner join(equijoin)  -> data 1개가 출력되지 않음 : 106건 
pd.merge(emp[['name','deptno']],dept[['deptno','dname']], on='deptno', how='inner')
# 왼쪽 데이터 프레임은 다 출력
pd.merge(emp[['name','deptno']],dept[['deptno','dname']], on='deptno', how='left')
# 오른쪽 데이터 프레임은 다 출력 
pd.merge(emp[['name','deptno']],dept[['deptno','dname']], on='deptno', how='right')
# full outer join: 모든 양쪽의 내용을 다 출력 
pd.merge(emp[['name','deptno']],dept[['deptno','dname']], on='deptno', how='outer')


###############################################################################
[문제161] emp_new.csv, dept_new.csv 파일 데이터에서 50번 부서 사원의 중에 급여가 5000 이상인 사원의 이름, 부서 이름을 출력하세요.

from pandas import Series, DataFrame
import pandas as pd
import numpy as np

#답1
emp = pd.read_csv("c:/data/emp_new.csv", names=['empid','name','job','mgr','hire_date', 'sal','comm','deptno'])
dept = pd.read_csv("c:/data/dept_new.csv", names=['deptno','dname', 'mgr','loc'])

pd.merge(emp[['name','sal','deptno']],dept[['deptno','dname']], on='deptno')
new=pd.merge(emp[['name','sal','deptno']],dept[['deptno','dname']], on='deptno')
  
new= new[['name','dname','sal']][new['deptno']==50]
new[['name','dname','sal']][new['sal']>=5000]

#답2
emp = pd.read_csv("c:/data/emp_new.csv", names=['empid','name','job','mgr','hire_date', 'sal','comm','deptno'])
dept = pd.read_csv("c:/data/dept_new.csv", names=['deptno','dname', 'mgr','loc'])

(pd.merge(emp[['name','sal','deptno']],dept[['deptno','dname']], on='deptno')[emp['deptno']==50])[['name','dname','sal']][emp['sal']>=5000]

#쌤답
emp = pd.read_csv("c:/data/emp_new.csv", names=['empid','name','job','mgr','hire_date', 'sal','comm','deptno'])
dept = pd.read_csv("c:/data/dept_new.csv", names=['deptno','dname', 'mgr','loc'])

pd.merge(emp[(emp['deptno']==50)&(emp['sal']>=5000)][['name','sal','deptno']],dept[['deptno','dname']], on='deptno')

[문제162] 2002년도에 근무한 사원들의 이름, 급여, 입사일, 부서코드,부서이름을 출력하세요.

from pandas import Series, DataFrame
import pandas as pd
import numpy as np

#답1
pd.merge(emp[['name','sal', 'hire_date','deptno']],dept[['deptno','dname']], on='deptno', how='left')[['name','sal','hire_date','deptno','dname']][emp['hire_date'].str.slice(0,4)=='2002']

#답2
new2=pd.merge(emp[['name','sal', 'hire_date','deptno']],dept[['deptno','dname']], on='deptno')
new2[['name','sal','hire_date','deptno','dname']][new2['hire_date'].str.slice(0,4)=='2002']

#쌤답1
pd.merge(emp[emp['hire_date'].str.slice(0,4)=='2002'][['name','sal','hire_date','deptno']], dept[['deptno','dname']], on='deptno')

#쌤답2
from datetime import datetime
pd.merge(emp[pd.to_datetime(emp['hire_date']).dt.year==datetime.strptime('2002','%Y').year][['name','sal','hire_date','deptno']],dept[['deptno','dname']],on='deptno')


[문제163] 직업이 AD_VP, AD_PRES 인 사원들의 이름, 급여, 직업, 부서코드, 부서이름 을 출력하세요.
emp = pd.read_csv("c:/data/emp_new.csv", names=['empid','name','job','mgr','hire_date', 'sal','comm','deptno'])
dept = pd.read_csv("c:/data/dept_new.csv", names=['deptno','dname', 'mgr','loc'])

#답1
import pandas as pd 
pd.merge(emp[(emp['job']=='AD_VP')|(emp['job']== 'AD_PRES')][['name','sal','job','deptno']],dept[['deptno','dname']], on='deptno')

#답2
import pandas as pd 
pd.merge(emp[emp['job'].isin(['AD_VP','AD_PRES'])][['name','sal','job','deptno']],dept[['deptno','dname']], on='deptno')



###############################################################################\
dept = DataFrame({'dname':['관리팀', '마케팅팀','구매팀','인사팀','경영지원팀','기술지원팀','홍보팀','영업팀','기획팀','재무팀','회계팀']},
                  index=[10,20,30,40,50,60,70,80,90,100,110])
dept

# right index/ left index: index를 이용할 때
pd.merge(emp[['name','sal','deptno']], dept, left_on='deptno', right_index=True)


###############################################################################
[문제164] 부서이름별 총액 급여를 출력하세요.  

#답1 
import pandas as pd 
emp = pd.read_csv("c:/data/emp_new.csv", names=['empid','name','job','mgr','hire_date', 'sal','comm','deptno'])
dept = DataFrame({'dname':['관리팀', '마케팅팀','구매팀','인사팀','경영지원팀','기술지원팀','홍보팀','영업팀','기획팀','재무팀','회계팀']},
                  index=[10,20,30,40,50,60,70,80,90,100,110])

m=pd.merge(emp[['name','sal','deptno']], dept, left_on='deptno', right_index=True)
dname_unique = Series(m['dname'].unique())
m

for i in dname_unique.sort_values():
    print(i, m.loc[m['dname']==i, 'sal'].sum())

#답2
    import pandas as pd 
emp = pd.read_csv("c:/data/emp_new.csv", names=['empid','name','job','mgr','hire_date', 'sal','comm','deptno'])
dept = DataFrame({'dname':['관리팀', '마케팅팀','구매팀','인사팀','경영지원팀','기술지원팀','홍보팀','영업팀','기획팀','재무팀','회계팀']},
                  index=[10,20,30,40,50,60,70,80,90,100,110])

# dataframe만 join이 가능하다, 따라서 처리를 한뒤 join을 해야함 
m=pd.merge(emp[['name','sal','deptno']], dept, left_on='deptno', right_index=True)
dname_unique = Series(m['dname'].unique())

m['sal'].groupby(m['dname']).sum()

# 쌤답1
from pandas import Series, DataFrame
import pandas as pd
emp = pd.read_csv("c:\data\emp_new.csv", names = ['empid','name','job','mgr','hire_date','sal','comm','deptno'])
dept = pd.read_csv("c:\data\dept_new.csv", names = ['deptno','dname','mgr','loc'])

#먼저 grouping 한 뒤에 -> join 함
dept_sal = emp['sal'].groupby(emp['deptno']).sum() #series형이어서 merge할수 없음 
dept_sal = DataFrame(dept_sal) #따라서 dataframe형을 바꿈 
dept_sal.reindex([10,20,30,40,50,60,70,80,90,100,110]) #다시 reindex가 필요함 
pd.merge(dept[['deptno','dname']], dept_sal, left_on = 'deptno', right_index=True)


# 쌤답2 
# 먼저 join 한 뒤 -> grouping의 집계값 구함
from pandas import Series, DataFrame
import pandas as pd
emp = pd.read_csv("c:\data\emp_new.csv", names = ['empid','name','job','mgr','hire_date','sal','comm','deptno'])
dept = pd.read_csv("c:\data\dept_new.csv", names = ['deptno','dname','mgr','loc'])
m = pd.merge(emp[['deptno','sal']], dept[['deptno','dname']])
m
m['sal'].groupby(m['dname']).sum()


#쌤답3 
dept= DataFrame({'dname':['관리팀','마케팅팀','구매팀','인사팀','경영지원팀','기술지원팀','홍보팀',
'영업팀','기획팀','재무팀','회계팀']},
index=[10,20,30,40,50,60,70,80,90,100,110])
pd.merge(dept, dept_sal, left_index = True, right_index=True)
