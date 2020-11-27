# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 09:45:20 2018

@author: stu
"""
###############################################################################

[문제165] emp_new.csv 파일  데이터에 커미션 정보를 분석하려 합니다.
커미션에 null값들의 수, null이 아닌값들의 수를 구하세요.

1. 일반적으로 csv file을 읽어서 해결
import csv
file = open("c:/data/emp_new.csv",'r')
emp_csv = csv.reader(file)
comm = 0
for emp_list in emp_csv:
    if emp_list[-2] == '':
        comm +=1
print(comm)
        
import csv
file = open("c:/data/emp_new.csv",'r')
emp_csv = csv.reader(file)
comm = 0
for emp_list in emp_csv:
    if emp_list[-2] != '':
        comm +=1 
print(comm)
                
                
#쌤답
import csv

file = open("c:/data/emp_new.csv",'r')
emp_csv = csv.reader(file)
cn1 = 0
cn2 = 0
for emp_list in emp_csv:
    if emp_list[6] == '':
        cn1 += 1
    else:
        cn2 += 1
print('null의 수:' , cn1)
print('null이 아닌 수:' , cn2)
file.close()
        
                
                
2. pandas를 이용해서 해결
#답1 - null
import pandas as pd
emp = pd.read_csv("c:\data\emp_new.csv", names = ['empid','name','job','mgr','hire_date','sal','comm','deptno'])
emp[emp['comm'].isnull()]['empid'].count()
#답2
emp[(emp['comm']).isnull()]['comm'].fillna(0).count()

    
#답1 - notnull
import pandas as pd
emp = pd.read_csv("c:\data\emp_new.csv", names = ['empid','name','job','mgr','hire_date','sal','comm','deptno'])
emp[emp['comm'].notnull()]['comm'].count()


#쌤답 
#
import pandas as pd
emp = pd.read_csv("c:\data\emp_new.csv", names = ['empid','name','job','mgr','hire_date','sal','comm','deptno'])
print('null 수: ', emp[emp['comm'].isnull()]['empid'].count())
print('null 아닌 수: ', emp[emp['comm'].notnull()]['empid'].count())

[문제166] emp_new.csv, dept_new.csv 파일 데이터를 이용해서  조인된 결과를 보려고 합니다.
조인 함수를 생성하세요.

join(emp,'deptno','ename', dept,'deptno','dname')

join(emp,'mgr','ename', emp,'empno','ename') 

#답xxxxxx 잘못된 답! 근데 merge되는 순서 다시 확인하기 위해서 남겨둠 
from pandas import Series, DataFrame
import pandas as pd
emp = pd.read_csv("c:\data\emp_new.csv", names = ['empno','ename','job','mgr','hire_date','sal','comm','deptno'])
dept = pd.read_csv("c:\data\dept_new.csv", names = ['deptno','dname','mgr','loc'])
def join(x, x1, x2, y, y1, y2):
    print(pd.merge(x[[x1,x2]],y[[y1,y2]]))
    
#동일한 column이름(key값)이 존재하기 때문에 원하는 join결과가 나오지 않을 수 있음 -> deptno, mgr
#-> 이럴경우 먼저 나열 되어 있는 mgr을 기준으로 joind을 함

#답 1
from pandas import Series, DataFrame
import pandas as pd
emp = pd.read_csv("c:\data\emp_new.csv", names = ['empno','ename','job','mgr','hire_date','sal','comm','deptno'])
dept = pd.read_csv("c:\data\dept_new.csv", names = ['deptno','dname','mgr','loc'])
def join(x, x1, x2, y, y1, y2):
    print(pd.merge(x[[x1,x2]],y[[y1,y2]], left_on = x1, right_on = y1))


#쌤답2
import csv
empfile = open("c:/data/emp_new.csv",'r')    
deptfile = open("c:/data/dept_new.csv",'r')
emp_csv = csv.reader(empfile)
detp_csv = csv.reader(deptfile)
emp = []
dept = []

for j  in emp_csv:
    emp.append({'empno':j[0], 'enanme':j[1], 'job': j[2], 'mgr':j[3], 'hiredate':j[4], 'sal':j[5], 'comm':j[6], 'deptno':j[7]})

def join (outer_table, outer_column1, outer_column2, inner_table, inner_coulmn1, inner_coulmn2):
    for o in outer_table:
        for i in inner_table:
            if o[outer_column1] == i[inner==column1]:
                print(o[outer_column2], i[inner_coulmn2])

#쌤답2
import  pandas  as  pd

emp = pd.read_csv("c:\data\emp_new.csv", names = ['empid','ename','job','mgr','hire_date','sal','comm','deptno'])
dept = pd.read_csv("c:\data\dept_new.csv",names = ['deptno','dname','mgr','loc'])

def join(outer_table,outer_column1,outer_column2,inner_table,inner_column1,inner_column2):
    print(pd.merge(outer_table[[outer_column1,outer_column2]],inner_table[[inner_column1,inner_column2]],left_on=outer_column1,right_on=inner_column1))

join(emp,'deptno','ename', dept,'deptno','dname')

join(emp,'mgr','ename', emp,'empid','ename')    



###############################################################################
#하나씩 인덱싱을 함수에 넣음 
def f(arg):
    result=[]
    for i in arg:
        result.append(i*2)
    return result

f([1,2,3,4,5])
id(f)

#한통으로 [1,2,3,4,5]를 넣음
def f1(arg)  :
    return arg*2

f1([1,2,3,4,5])

■ map 함수는 입력받는 자료형의 각 요소가 함수에 수행된 결과를 묶어서 리턴하는 함수
#map 정보만 추출
map(f1,[1,2,3,4,5])
#list로 만들어줌 
list(map(f1,([1,2,3,4,5])))

#람다함수 이용
list(map(lambda x: x*2,[1,2,3,4,5]))


###############################################################################
[문제167] x변수에는 1,2,3,4,5  y변수에는 6,7,8,9,10 들어 있다. f(x,y) = x2 + y 를 구하세요.(lambda, map 함수를 이용하세요)

#답1
f = lambda x, y : x*2 +y
x = [1,2,3,4,5]
y = [6,7,8,9,10]
result = map(f,x,y)
print(list(result))

#답2
x = [1,2,3,4,5]
y = [6,7,8,9,10]
print(list(map(lambda x,y: x*2+y, x,y)))

###############################################################################
□ 한쪽의 value값과 한쪽의 index값을 붙이는 작업
from pandas import Series, DataFrame
import pandas as pd
import numpy as np

x = Series([1,2,3],index=['one','two','three']) #값, 인덱스 
y = Series(['하나','둘','셋'], index=[1,2,3]) #값, 인덱스 

#series에서는 pd.merge가 안됨 -> dataframe형으로 만들어야 함  
x1=DataFrame(x)
y1=DataFrame(y)

# merge: merge는 작업후 필요없 열을 버려줘야함
pd.merge(x1,y1, left_on = 0, right_index=True)

# map을 통해 pandas에서도 한쪽의 값과 한쪽의 index를 붙이는 작엄을 함 
#꼭 항상 value, index순서로 쓰지 않아도 됨 
x.map(y)

###############################################################################
[문제168] emp_new.csv는 pandas로 읽고  dept_new.csv는 일반 csv로 읽어 들인 후 조인을 수행하세요.

#답1
#한쪽은 DataFrame
import  pandas  as  pd
emp = pd.read_csv("c:\data\emp_new.csv", names = ['empid','ename','job','mgr','hire_date','sal','comm','deptno'])

import csv
file = open("c:\data\dept_new.csv",'r')


#dictionary형으로 만들기
import csv
file = open("c:\data\dept_new.csv",'r')
dept = csv.reader(file)
d = {}
for dept_list in dept:
    if dept_list[0] != d:
        d[int(dept_list[0])] = dept_list[1]
d

emp['dname']=emp['deptno'].map(d) 
print(emp[['empid','deptno','dname']])


#
import csv
file = open("c:\data\dept_new.csv",'r')
dept = csv.reader(file)
d = {}
for dept_list in dept:
    d[int(dept_list[0])] = dept_list[1]

d
emp['dname']=emp['deptno'].map(d)
print(emp[['empid','deptno','dname']])

#쌤답

#한쪽은 DataFrame
import  pandas  as  pd
emp = pd.read_csv("c:\data\emp_new.csv", names = ['empid','ename','job','mgr','hire_date','sal','comm','deptno'])

import csv
deptfile = open("c:\data\dept_new.csv",'r')
dept_csv = csv.reader(deptfile)
dept = {}

for i in dept_csv:
    if i[0] != dept:
        dept[int(i[0])] = i[1]
dept  

for k,v in dept.items():
    print(k,v)

# merge하지 않아도 join된 결과를 얻을 수 있다. 
emp['dname']=emp['deptno'].map(dept) 
print(emp[['empid','deptno','dname']])



[문제169] happiness 변수에 문장이 있습니다. 행복이란 단어가 몇개 나오는지 분석하시고, 위치정보도 출력해주세요.



happiness = '우리나라 「헌법」 제10조는 “모든 국민은 인간으로서의 존엄과 가치를 가지며, 행복을 추구할 권리를 가진다”라고 규정하고 있다.행복추구권은 근대 입헌민주주의의 핵심인 개인주의·자유주의를 그 사상적 기반으로 하고 있다. 행복추구권에 있어서 행복은 다의적인 개념으로, 각자의 생활조건이나 가치관에 따라 다르게 이해될 수 있으나, 최소한 인간적인 고통이 없는 상태 내지 만족감을 느낄 수 있는 행복한 상태를 의미한다.'

#답: 행복 단어 개수
cn=0
i=0
for i in range(len(happiness)):
    i += 1
    if happiness[i:i+2]=='행복':
        cn += 1
print(cn)    

#답2
cn = happiness.count('행복')
print('단어의 수:', cn)


#단어의 위치찾기- 다시 시도 해보기 
cn=0
i=0
loc=[]
for i in range(len(happiness)):
    i += 1
    if happiness[i:i+2]=='행복':
        cn += 1
        loc.append(happiness.find('행복'))       
print(loc)
print(cn)    

#답1
print('단어의 위치:', happiness.find('행복',44))
print('단어의 위치:', happiness.find('행복',71))
print('단어의 위치:', happiness.find('행복',122))
print('단어의 위치:', happiness.find('행복',133))
print('단어의 위치:', happiness.find('행복',217))

#답2: find: 있으면 인덱스 번호를 return해주고, 없으면 -index1의 값으로 return한다. 
a =1 
while happiness.find('행복',a) != -1:
    a = happiness.find('행복', a)
    print('단어의 위치: ', a)
    a += 1
    
happiness.find('행복') != -1





[문제170] emp1.csv, emp2.csv파일을 읽어서 부서별 총액급여를 구하세요.

import pandas as pd 

#답1
import pandas as pd 
emp1 = pd.read_csv("c:\data\emp1.csv", names = ['empid','name','hire_date','sal','deptno'])
emp = emp1
for i in range(2,3):
    emp = emp.append(pd.read_csv("c:\data\emp{}.csv".format(i), names = ['empid','name','hire_date','sal','deptno']))
emp['sal'].groupby(emp['deptno']).sum()



#답2
import pandas as pd 
emp=emp1.append(emp2)
    
emp1 = pd.read_csv("c:\data\emp1.csv", names = ['empid','ename','hire_date','sal','deptno'])
emp2 = pd.read_csv("c:\data\emp2.csv", names = ['empid','ename','hire_date','sal','deptno'])

emp['sal'].groupby(emp['deptno']).sum()
emp1['sal'].groupby(emp1['deptno']).sum()
emp2['sal'].groupby(emp2['deptno']).sum()

#답3
emp = pd.DataFrame(index = ['empid','name','hire_date','sal','deptno'])
for i in range(1,3):
    emp = emp.append(pd.read_csv("c:\data\emp{}.csv".format(i), names = ['empid','name','hire_date','sal','deptno']))
emp['sal'].groupby(emp['deptno']).sum()


#쌤답1
import pandas as pd
emp = pd.DataFrame()
for i in range(1,3):
    file = 'c:/data/emp{}.csv'.format(i)
    temp = pd.read_csv(file, names = ['empid','name','hire_date','sal','deptno'])
    emp = emp.append(temp)
    
print(emp['sal'].groupby(emp['deptno']).sum())


#쌤답2
■ import glob
glob.glob(): 동일이름이지만 번호만 달라지는 파일명을 불러들일때 사용하는 method, *가 키워드임

import glob
import pandas as pd

file = 'C:/python_data/emp*.csv'
file_list = glob.glob(file)
print(file_list)
emp = pd.DataFrame()

for i in file_list:
    temp = pd.read_csv(i, names =  ['empid','name','hire_date','sal','deptno'])
    emp = emp.append(temp)

print(emp['sal'].groupby(emp['deptno']).sum())



[문제171] 2016년도에 태어난 아이들의 정보가 들어 있는 year2016파일을 분석해야 합니다. 총 출생수를 출력해주세요.

#txt파일에서 ,로 구분자가 되어있기 때문에 csv로 읽어들일 수 있다. 
#총 출생수 
import pandas as pd
data = pd.read_csv('c:/data/yob2016.txt', names = ['name','gender','num'])

data['num'].sum()

# pandas를 사용하지 않을 때
readlines


#쌤답1: csv객체로 읽어들임 
import csv
import os 

count=0
file = 'c:\data\yob2016.txt'
name = os.path.basename('c:\data\yob2016.txt')  #물리적인 절대적경로를 빼고, 파일이름.확장자
name = name.split('.')[0]   #.을 기준으로 split [0]인덱스의 값만 뽑아내면 파일 이름만 뽑아내게 됨 
with open(file,'r') as f: #with를 사용하면 file.close()를 안해도 됨 
    data=csv.reader(f)
    for d in data:
        count += int(d[2]) #2번 index값을 intger형으로 바꾼후 count 변수에 누적 
print(name,count) #파일이름과 총출생수 출력 

#쌤답2 : readlines로 읽어들일 때 ★★★★★★★ 주의하기 
import csv
import os

count=0
file = 'c:\data\yob2016.txt'
name = os.path.basename('c:\data\yob2016.txt')
name = name.split('.')[0]
with open(file,'r') as f:
    data=f.readlines()
    for d in data:
        birth = d.split(',')[2] #split 을 해야함 
        count += int(birth)
print(name,count)



import pandas as pd 
import os

file = 'c:/data/yob2016.txt'
name = os.path.basename(file)
name = name.split('.')[0]

#쌤답3
yob = pd.read_csv('c:\data\yob2016.txt', names=['name','gender','birth'])
print(name,yob['birth'].sum())




[문제172] 2016년도에 태어난 아이 이름 상위 10까지 보여주세요. 성별 상위 5까지 보여주세요.
import pandas as pd
data = pd.read_csv('c:/data/yob2016.txt', names = ['name','gender','num'])


data[data['gender']=='F']
data[data['gender']=='M']

#답: 아이 이름 상위 10까지
total = DataFrame({'순위':data['num'].rank(ascending=False, method='dense'), '이름':data['name'], '성별':data['gender'], '인원수':data['num']})
total[['순위','이름','성별','인원수']][total['순위']<= 10]


#답: 성별 상위 5까지 
f= data[data['gender']=='F']
total_f= DataFrame({'순위':f['num'].rank(ascending=False, method='dense'), '이름':f['name'], '성별':f['gender'], '인원수':f['num']})
total_f[['순위','이름','성별','인원수']][total_f['순위']<= 5]

m= data[data['gender']=='M']
total_m= DataFrame({'순위':m['num'].rank(ascending=False, method='dense'), '이름':m['name'], '성별':m['gender'], '인원수':m['num']})
total_m[['순위','이름','성별','인원수']][total_m['순위']<= 5]



# 답22
import pandas as pd
name=pd.read_csv("c:/data/yob2016.txt", names = ['name','gender','count'])
a=name.sort_values(by='count',ascending=False)[0:10]
a

female=name[name['gender']=='F']
male=name[name['gender']=='M']

f=female.sort_values(by='count', ascending=False)[0:10]
f
m=male.sort_values(by='count', ascending=False)[0:10]
m


#쌤답
import pandas as pd 

yob2016 = pd.read_csv('c:\data\yob2016.txt', names=['name','gender','birth'])

def top(df, n=5, column='birth'):   # 넣지 않으면 n=5, column='birth' -> default값으로 설정할 수 있음 
    return df.sort_values(by=column, ascending=False)[:n]  #[:n]은 slicing ; 기억하기!! sort.values로 상위 몇 개만 뽑아내기! 

print(top(yob2016 , n=10))

print(yob2016.groupby('gender').apply(top))


#rank를 이용해서 출생수가 동일하게 counting된 아이들의 이름을 누락시키지 않게 하기 위해 