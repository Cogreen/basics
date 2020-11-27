# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 09:40:05 2018

@author: stu
"""
###############################################################################################################
[문제134] emp.csv 파일의 데이터를 판다스를 이용해서 읽어 들인 후 급여가 10000 이상인 사원들의 이름, 급여, 입사일을 출력해주세요.

import pandas as pd

emp = pd.read_csv("c:/data/emp.csv")
emp.head()
emp.tail(10)
emp.info()

#답1
emp[['LAST_NAME','SALARY', 'HIRE_DATE']][emp['SALARY']>=10000]

#답2 
emp.ix[emp['SALARY']>=10000, ['LAST_NAME', 'SALARY', 'HIRE_DATE']] #보편적으로 없어질 method 

#답3
emp.loc[emp['SALARY']>=10000, ['LAST_NAME', 'SALARY', 'HIRE_DATE']]


[문제135] 급여 10000 이상인 사원들의 이름과 급여, 입사일를 출력하세요. 급여를 기준으로 내림차순하세요.

#답1
emp[['LAST_NAME','SALARY', 'HIRE_DATE']][emp['SALARY']>=10000].sort_values(by='SALARY', ascending=False)

#답2
emp.ix[emp['SALARY']>=10000, ['LAST_NAME', 'SALARY', 'HIRE_DATE']].sort_values(by='SALARY', ascending=False)

#답3
emp.loc[emp['SALARY']>=10000, ['LAST_NAME', 'SALARY', 'HIRE_DATE']].sort_values(by='SALARY', ascending=False)

# sort_values(by=['SALARY', 'HIRE_DATE'])와 같이 sort.vlaue에 해당하는 열은 리스트 모양으로 여러개 넣을 수 있다. 
# emp.loc[emp['SALARY']>=10000, ['LAST_NAME', 'SALARY', 'HIRE_DATE']].sort_values(by=['SALARY', 'HIRE_DATE'], ascending=False)


###############################################################################################################

obj = Series([78, 88, 92, 79, 67, 91, 70, 86, 90, 90])

#값을 기준으로 오름차순 정렬
obj.sort_values()

#값을 기준으로 내림차순 정렬
obj.sort_values(ascending=False)

#rank 구하기  (cf. sql의 분석함수 같이 공부하기)
#동일한 순위일 경우 일 경우 평균값으로 할지, 최소값으로 할지, 최대값으로 할지 결정할 수 잇다. 
# 오름차순 순위: eg. 67이 있는 위치(4)에 1로 표기됨, 78이 있는 위치(6)에 2로 표기됨
# 기본값: 동일한 순위일 경우 일 경우 평균값으로 표현
obj.rank() 

obj.rank(ascending=False)

#동일값일 때 평균으로 출력함 (기본값)
obj.rank(ascending=False, method='average')

#최소값인 동일한 순위로 나옴 (4등은 없음)
obj.rank(ascending=False, method='min')

#최대값인 동일한 순위로 나옴 (3등은 없음)
obj.rank(ascending=False, method='max')

#동일한 동률일 경우 index가 앞을 경우 먼저 순위를 줌 (e.g.90점이 8인덱스를 가진 경우 3위, 9인덱스를 가진경우 4위)
obj.rank(ascending=False, method='first')


#sql의 기존의 rank와 같음(e.g, 1,2,3,3,5 로 표현)
obj.rank(ascending=False, method='min')


#sql의 dense_rank와 같음: 연이은 정수로 표현(e.g., 1,2,3,3,4... 로 표현)
obj.rank(ascending=False, method='dense')

#series를 하나의 열로 들어가고, 순위도 하나의 열로 들어가 dataframe으로 만들기
obj1= DataFrame({'순위':obj.rank(ascending=False, method='dense'),
            '점수':obj})

#순위로 정렬하기
obj1.sort_values(by='순위')


import numpy as np
#NaN값 만들기 
obj2 = Series([70,60,80,np.nan,90])
obj2

#정렬을 하면 오름차순, 내림차순 모두 null값이 맨 뒤에 출력된다.
obj2.sort_values()
obj2.sort_values(ascending=False)
#cf. sql의 null값은 -> 오름차순: 제일 밑에/ 내림차순: 제일 위에


#NaN값을 제일 앞으로
obj2.sort_values(ascending=False, na_position='first')

#NaN값을 제일 뒤로
obj2.sort_values(ascending=False, na_position='last')


# NaN은 순위를 적용해도 무시됨 
obj2.rank()
obj2.rank(ascending=False)
#NaN값이 순위를 적용해도 무시됨: 기본값 na_option='keep'
obj2.rank(na_option='keep')
#na_option='top': NaN값이 1등으로 출력됨 
obj2.rank(na_option='top')
obj2.rank(ascending=False, na_option='top')
#na_option='bottom': NaN값이 꼴등으로 출력됨 
obj2.rank(na_option='bottom')
obj2.rank(ascending=False, na_option='bottom')



#
df = DataFrame({'영어':[60,80,70], '수학':[50,72,86]},
                index=['홍길동','박찬호','손흥민'])
df
#수학을 기준으로 정렬
df.sort_values(by='수학')
df.sort_values(by='수학', ascending=False)
#수학 데이터만 보기 
df['수학'].sort_values(ascending=False)
# rank 구하기 (과목별로 순위값이 자동으로 만들어짐)
 df.rank(ascending=False)
# 각 학생이 잘하는 과목에 대해 rank를 해줌  (axis=1 열이기 때문에 영어, 수학을 두 기준으로 순위를 구함)
df.rank(ascending=False, axis=1)
#영어에 대한 rank보기
df['영어'].rank(ascending=False)
# 홍길동에 대한 rank만 보기
df.ix['홍길동'].rank(ascending=False)


########################################################################################
[문제136] 급여를 많이 받는 순으로 10위 까지를 구하세요. 


import pandas as pd
emp.info()
emp = pd.read_csv("c:/data/emp.csv")
emp['SALARY'].rank(ascending=False, method='min').sort_values()[0:10]

DataFrame({'사원명':emp['LAST_NAME'], 
               '급여':emp['SALARY'],
               '순위':emp['SALARY'].rank(ascending=False, method='min')}).sort_values(by='순위')[0:10]

#좀 더 생각해보기 
s=DataFrame({'사원명':emp['LAST_NAME'],
           '급여':emp['SALARY'],
           '순위':emp['SALARY'].rank(ascending=False, method='dense')})
s.sort_values(by='순위')


#쌤답
emp[emp['SALARY'].rank(ascending=False, method='dense')<=10][['EMPLOYEE_ID', 'LAST_NAME', 'SALARY']]    
또는 

emp['rank'] = emp['SALARY'].rank(ascending=False, method='dense')
emp[emp['rank']<=10].sort_values('rank')
########################################################################################

□ pandas에서의 in 연산자

df = DataFrame({'영어':[60,80,70], '수학':[50,72,86]},
                index=['홍길동','박찬호','손흥민'])
df

# in 연산자: 이 조건의 값을 출력
df[df['수학'].isin([72,86])] #행을 제한하는 부분

# ~: not in 연산자의 의미로, 이 조건의 반대를 의미
df[~df['수학'].isin([72,86])]


########################################################################################
[문제137] 직업이 AD_VP, AD_PRES 인 사원들의 이름, 급여, 직업을 출력하세요.

import pandas as pd
emp.info()
emp = pd.read_csv("c:/data/emp.csv")

emp[emp['JOB_ID'].isin(['AD_VP','AD_PRES'])][['LAST_NAME','SALARY','JOB_ID']] #제한을 먼저 한 다음, 열을 가져옴 

emp[['LAST_NAME','SALARY','JOB_ID']] [emp['JOB_ID'].isin(['AD_VP','AD_PRES'])]



[문제138] 직업이 AD_VP ,AD_PRES 아닌 사원들의 이름, 급여, 직업을 출력하세요.
import pandas as pd
emp.info()
emp = pd.read_csv("c:/data/emp.csv")
emp[~emp['JOB_ID'].isin(['AD_VP','AD_PRES'])][['LAST_NAME','SALARY','JOB_ID']]

emp[['LAST_NAME','SALARY','JOB_ID']][~emp['JOB_ID'].isin(['AD_VP','AD_PRES'])]
########################################################################################

# NaN을 넣는 방법 
obj = Series([1,2,3,None,5])
obj

import numpy as np
obj = Series([1,2,3,np.nan,5])
obj

from numpy import nan as NA
obj = Series([1,2,3,NA, 5])
obj


#NaN에 0으로 채우기
obj.fillna(0) #미리보기임 (적용은 아님)

#NaN이 값을 True로 출력
obj.isnull()

#NaN이 값을 True로 출력 by Pandas
pd.isnull(obj)

#NaN 아닌 값을 True로 출력
obj.notnull()

#NaN값만 출력하기
obj[obj.isnull()]

#NaN아닌 값만 출력하기
obj[obj.notnull()]
obj.dropna()


# (from numpy import nan as NA로 만들어 놨기 때문에 NA사용 가능)
df = DataFrame([[1,2,3],[1,None,NA],[NA,NA,NA],[NA,2,3]])
df
#NaN이 하나라도 있으면 제외가 됨 
df.dropna()
df.dropna(how='all')
df.dropna(how='all', axis=0)  #0은 행을 기준
df.dropna(how='all', axis=1)  #1은 열을 기준
df.dropna(axis=0)
df.dropna(axis=1)

df[4] = NA
df.dropna(how='all', axis=1)


#NaN을 0으로 채움 
df.fillna(0)

#0번 열에만 0을 채움
df[0].fillna(0)

#1번 컬럼에는 0을, 1번 컬럼에는 1, 2번 컬럼에는 2, 4번컬럼에는 4를 채우고자 함
df.fillna({0:0, 1:1, 2:2, 4:4})

# NaN을 0으로 채우는 것이 적용됨
df.fillna(0, inplace=True)
df

#앞에 있는 내용으로 NaN를 채움
df.fillna(method='ffill')
df.fillna(method='pad')

#뒤에 있는 내용으로 NaN을 채움
df.fillna(method='bfill')
df.fillna(method='backfill')

########################################################################################
[문제139] 커미션이 null인 사원의 이름, 커미션을 출력하세요.
import pandas as pd
emp = pd.read_csv("c:/data/emp.csv")

#답1
emp[['LAST_NAME','COMMISSION_PCT']][emp['COMMISSION_PCT'].isnull()]

#답2
emp[emp['COMMISSION_PCT'].isnull()][['LAST_NAME','COMMISSION_PCT']]

#답3
emp.ix[emp['COMMISSION_PCT'].isnull(),['LAST_NAME','COMMISSION_PCT']]

#답4
emp.loc[emp['COMMISSION_PCT'].isnull(),['LAST_NAME','COMMISSION_PCT']]

[문제140] 커미션이 null아닌 사원의 이름, 커미션을 출력하세요.
import pandas as pd
emp = pd.read_csv("c:/data/emp.csv")
#답1
emp[['LAST_NAME','COMMISSION_PCT']][emp['COMMISSION_PCT'].notnull()]

#답2
emp[emp['COMMISSION_PCT'].notnull()][['LAST_NAME','COMMISSION_PCT']]

#답3
emp.ix[emp['COMMISSION_PCT'].notnull(),['LAST_NAME','COMMISSION_PCT']]

#답4
emp.loc[emp['COMMISSION_PCT'].notnull(),['LAST_NAME','COMMISSION_PCT']]
########################################################################################
▣ apply 함수
- apply함수는 행, 열값을 인수값으로 받아서 반복하여 그 함수를 적용한다. 

#series
s1 = Series([1,2,3])

def square(x):
    return x**2

#함수사용 
square(s1)
#error
s1.square()
#apply사용
s1.apply(square)
#lambda 사용
s1.apply(lambda x:x**2)


#dataframe
df = DataFrame([[1,2,3],[4,5,6]])
df
df.apply(square)
df.apply(square, axis=0)
df.apply(square, axis=1)

#행을 기준으로 열을 합함
df.apply(sum, axis=0)
#열을 기준으로 행을 합함
df.apply(sum, axis=1)
#
df.apply(lambda x:x**2)




########################################################################################
[문제141] last_name 첫글자가 S로 시작되는 사원들의 last_name을 출력하세요.

#답1
def ini(x):
    for i in range(len(x)):
        if x[i][0]=='S':
            print(x[i])

ini(emp['LAST_NAME'])

#답2
emp[emp['LAST_NAME'].apply(lambda x:x[0]=='S')]['LAST_NAME']

#답3
def start(x):
    for i in range(len(x)):
        if x[i].startswith('S'):
            print(x[i])
            
start(emp['LAST_NAME'])


#쌤답
def first_character(w):
    if w[0] == 'S':
        return True
    return False

emp['LAST_NAME'][emp['LAST_NAME'].apply(first_character)]
emp[emp['LAST_NAME'].apply(first_character)]['LAST_NAME']
emp.ix[emp['LAST_NAME'].apply(first_character),'LAST_NAME']

emp.ix[emp['LAST_NAME'].apply(lambda x:x[0]=='S'),'LAST_NAME']
emp.ix[emp['LAST_NAME'].apply(lambda x:x[0])=='S','LAST_NAME']
emp.ix[emp['LAST_NAME'].apply(lambda x:x.startswith('S')),'LAST_NAME']


[문제142] last_name g로 끝나는 사원들의 이름, 급여 출력하세요.
#답1
def last(x, y):
    for i in range(len(x)):
        if x[i][-1] == 'g':
            print(x[i],y[i])
            
last(emp['LAST_NAME'],emp['SALARY'])     
       
#답2
def last_character(w):
    if w[-1] == 'g':
        return True
    return False

emp[['LAST_NAME','SALARY']][emp['LAST_NAME'].apply(last_character)]

#답3
emp.ix[emp['LAST_NAME'].apply(lambda x:x[-1]=='g'),['LAST_NAME','SALARY']]
#답4
emp.ix[emp['LAST_NAME'].apply(lambda x:x.endswith('g')),['LAST_NAME','SALARY']]


[문제143] 110번 사원의 급여보다 많이 받는 사원들의 이름, 급여를 출력하세요.
#일반적인 data인 scalar형식에서 가져왔다면 문제가 되지 않지만, dataframe은 series형식으로 가져오기 때문에 이 부분을 고려해야하는 문제이다. 
import pandas as pd
emp = pd.read_csv("c:/data/emp.csv")
emp.info()

#답1
emp101 = emp['SALARY'][emp['EMPLOYEE_ID']==110]
emp[['LAST_NAME','SALARY']][emp['SALARY']> int(emp101)]

#답2
emp[['LAST_NAME','SALARY']][emp['SALARY']>int(emp['SALARY'][emp['EMPLOYEE_ID']==110])]

#쌤답 
-int를 함수를 이용하면 scalar 값으로 return함
-v_110.values[0]을 사용하면 값을 추출함 

v_110 = emp[emp['EMPLOYEE_ID']==110]['SALARY']
type(v_110)
emp[emp['SALARY'] > int(v_110)][['LAST_NAME','SALARY']]
emp[emp['SALARY'] > v_110.values[0]][['LAST_NAME','SALARY']]


[문제144] 관리자 사원의 이름, 입사일, 급여를 출력하세요.
#답1
emp[['LAST_NAME','HIRE_DATE','SALARY']][emp['EMPLOYEE_ID'].isin(emp['MANAGER_ID'])]

#답2
file = open("c:/data/emp.csv",'r')
emp_csv = csv.reader(file)
next(emp_csv)
manager_id=[]
for emp_list in emp_csv: 
    manager_id.append(emp_list[-2])
print(set(manager_id))
file.close()  

file = open("c:/data/emp.csv",'r')
emp_csv = csv.reader(file)
next(emp_csv)
for emp_list in emp_csv:
    if emp_list[0] in manager_id:
        print(emp_list[2], emp_list[5], emp_list[7])
file.close()  

#답3 #유일값만 넣기 위해 
file = open("c:/data/emp.csv",'r')
emp_csv = csv.reader(file)
next(emp_csv)
v_mgr = []
for emp_list in emp_csv:
    if (not emp_list[9] in v_mgr) & (emp_list[9] != ''):
        v_mgr.append(emp_list[9])
print(len(v_mgr))
file.close()

file = open("c:/data/emp.csv",'r')
emp_csv = csv.reader(file)
next(emp_csv)
for emp_list in emp_csv:
    for mgr in v_mgr:
        if emp_list[0]==mgr:
            print(emp_list[2], emp_list[5], emp_list[7])
file.close()


 
 