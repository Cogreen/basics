# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 09:45:39 2018

@author: stu
"""

###############################################################################

#sort_value는 같은 값이 없을 때 순위를 구하는 것이 가능하지만 같은 값이 있게 되면 누락되는 상황이 발생되기 때문에 순위를 구할때는 rank를 사용해야 한다. 
#rank안의 option의 dense를 사용해서 
#sql에는 inline view를 통해서 바깥쪽에서 제한을 함,(select 문장에서 rank구하기 확인하기-> 순위를 구하되 10위까지 구한 것을 dataframe을 하나 만들어 넣어놔야한다. 그런다음 제한하면 됨)
[문제173] emp1.csv 데이터를 이용해서 급여를 많이 받는 순으로 10위까지 구하세요.

import pandas as pd
from pandas import Series, DataFrame


emp = pd.read_csv('c:/data/emp1.csv', names=['empid','name','hire_date', 'sal', 'deptno']) 

emprank = DataFrame({ 'rank':emp['sal'].rank(ascending=False, method='desne')})

emprank = DataFrame({'empid':emp['empid'], 'name':emp['name'], 'hire_date':emp['hire_date'], 'sal':emp['sal'], 'rank':emp['sal'].rank(ascending=False, method='dense'), 'deptno':emp['deptno']})
rank=emprank[['empid','name','hire_date','sal','rank','deptno']][emprank['rank']<=10].sort_values('rank')
rank

#쌤답
emp['rank'] = emp['sal'].rank(ascending=False, method='dense')
emp[emp['rank']<=10] .sort_values('rank')


[문제174] emp1.csv 데이터를 이용해서 부서별로 급여를 많이 받는 순으로 5위까지 구하세요.
#답1
import pandas as pd
from pandas import Series, DataFrame

emp = pd.read_csv('c:/data/emp1.csv', names=['empid','name','hire_date', 'sal', 'deptno']) 
emp['dept_rank'] = emp['sal'].groupby(emp['deptno']).rank(ascending=False, method='dense')

for i in emp[emp['dept_rank'] <= 5].sort_values(['dept_rank']).groupby('deptno'):
    print(i)


#답2
import pandas as pd
from pandas import Series, DataFrame

emp = pd.read_csv('c:/data/emp1.csv', names=['empid','name','hire_date', 'sal', 'deptno']) 

emp['dept_rank'] = emp['sal'].groupby(emp['deptno']).rank(ascending=False, method='dense')
emp[emp['dept_rank']<=5].sort_values(['deptno','dept_rank'])


###############################################################################


[문제175] yob2016.txt 데이터를 이용해서 아기 이름 순위 10위까지 구하세요.

import pandas as pd
data = pd.read_csv('c:/data/yob2016.txt', names = ['name','gender','num'])

data['rank'] = data['num'].rank(ascending=False, method='dense')
data[['name','gender','num','rank']][data['rank']<=10].sort_values('rank')



[문제176] yob2016.txt 데이터를 이용해서 성별 아기 이름 순위 5위까지 구하세요.

import pandas as pd
data = pd.read_csv('c:/data/yob2016.txt', names = ['name','gender','num'])
data['gender_rank'] = data['num'].groupby(data['gender']).rank(ascending=False, method='dense')
data[data['gender_rank']<=5].sort_values(['gender','gender_rank'])

import pandas as pd
data = pd.read_csv('c:/data/yob2016.txt', names = ['name','gender','num'])
data['gender_rank'] = data['num'].groupby(data['gender']).rank(ascending=False, method='dense')

for i in data[data['gender_rank']<=5].sort_values(['gender_rank']).groupby('gender'):
    print(i)
    
    
[문제177] 2000 ~ 2016년도 년도별 출생수

https://catalog.data.gov/dataset/baby-names-from-social-security-card-applications-national-level-data

def countName():
    counting = []
    for i in range(2000,2017):
        count = 0
        filename = 'c:\python_data\yob\yob%d.txt'%i
        with open(filename,'r') as f:
            data=f.readlines()
            for j in data:
                birth = j.split(',')[2]
                count += int(birth)
            counting.append((j,count))
    return counting

result = countName()            
for year, cn in result:
    print(year, cn)
    
#쌤답1
def countBirths():
    ret=[]
    for y in range(2000,2017):
        count=0
        filename='c:python_data\yob\yob%d.txt'%y
        with open(filename,'r') as f:
            data=f.readlines()
            for d in data:
                birth = d.split(',')[2]
                count += int(birth)
            ret.append((y,count))
    return ret



result = countBirths()
for year, cn in result:
    print(year,cn)

##오답: 누적합이 되어버림 
import os
from pandas import Series, DataFrame
import pandas as pd
import numpy as np

year_cn=[]
all_data = pd.DataFrame()
for y in range(2000,2017):
    filename='c:\python_data\yob\yob%d.txt'%y
    name = os.path.basename(filename)
    name = name.split('.')[0]
    df = pd.read_csv(filename, names=['name','gender','birth'])
    #all_data = all_data.append(df)    -> 필요없는 부분 
    year_cn.append((name[3:],all_data['birth'].sum()))
    print(name[3:],all_data['birth'].sum())

#답
import os
from pandas import Series, DataFrame
import pandas as pd
import numpy as np

year_cn=[]
all_data = pd.DataFrame()
for y in range(2000,2017):
    filename='c:\python_data\yob\yob%d.txt'%y
    name = os.path.basename(filename)
    name = name.split('.')[0]
    df = pd.read_csv(filename, names=['name','gender','birth'])
    year_cn.append((name[3:], df['birth'].sum()))
    print(name[3:], df['birth'].sum())


#답
        
import pandas as pd

for i in range(2000,2017):
    temp = pd.read_csv('c:/python_data/yob/yob{}.txt'.format(i), names = ['name', 'gender', 'cnt'])
    print(i,temp['cnt'].sum())
    
[문제178]  2000 ~ 2016년도 년도별 출생수 결과를 year.txt 파일에 저장하세요.

import os
import glob
from pandas import Series, DataFrame
import pandas as pd
import numpy as np

#답1
#write 대상을 만들기 
year_cn=[]                                          #append 하여 만드는 작업
all_data = pd.DataFrame()
for f in glob.glob("c:\python_data\yob\yob*.txt"):   #물리적 확장자 주소
    name = os.path.basename(f)      # (물리적 확장자 주소가 아닌) file이름만 뽑아내기 -> 나중에 년도만 뽑아내기 위해서 
    name = name.split('.')[0]       # 파일 이름의 년도 정보 뽑아내기 
    df = pd.read_csv(f, names=['name','gender','birth'])   
    year_cn.append((name[3:],df['birth'].sum()))  #name[3:] :yob을 제거하고 연도만 넣기: 200x, 출생수 저장
    print(name[3:],df['birth'].sum())             #출력


# 이제부터 파일로 떨어뜨리기 ; 
#기존 데이터를 저장할때는 하나씩 저장하여 ,를 써주면서 형식을 저장해야함 (밑의 writer= csv.writer(f, delimiter=','와 다름))
with open('c:\python_data\yob\year.txt','w') as f:      #'w' :write정보 , f별칭 
    for year, birth in year_cn:                     #year_cn에서 year와 birth를 가져옴
        data = '%s,%s\n'%(year,birth)               #%s를 통해 year, birth를 넣음, \n 줄바꿈
        print(data)         
        f.write(data)                               #data 차곡차곡 정리



#답2 - append 하지 않고 한번에 작업하기 

import os
from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import csv

with open('c:/python_data/yob/year_total.csv','w') as f:
    writer = csv.writer(f, delimiter=',')   #csv.writer : csv로 저장, / 구분자: delimiter=',' 
    for y in range(2000,2017):
        filename='c:/python_data/yob/yob%d.txt'%y   #for문을 사용하여 data읽어들이기 
        name = os.path.basename(filename)
        name = name.split('.')[0]
        df = pd.read_csv(filename, names=['name','gender','birth'])
        writer.writerow([name[3:],df['birth'].sum()])   #writerow(): 결과물 ()부분을 행단위로 저장하겠다. :writerow([name[3:],df['birth'].sum()]) 


#답3

import pandas as pd

f = open("c:/python_data/yob/year2.txt", "w")

for i in range(2000,2017):
    temp = pd.read_csv('c:/python_data/yob/yob{}.txt'.format(i), names = ['name', 'gender', 'cnt'])
    txt = "{},{}\n".format(i,temp['cnt'].sum())
    f.write(txt)

f.close()





[문제179] 2010 ~ 2016  년도까지 성별 출생 현황을
year_gender_total.csv 파일로 생성해주세요.

# 덥
import pandas as pd

f = open("c:/data/year_gender_total.csv", "w")

f.write('year,M,F\n')

for i in range(2000,2017):
    temp = pd.read_csv('c:/python_data/yob/yob{}.txt'.format(i), names = ['name', 'gender', 'cnt'])
    M = temp[temp['gender']=='M']['cnt'].sum()
    F = temp[temp['gender']=='F']['cnt'].sum()
    txt = "{},{},{}\n".format(i,M,F)
    f.write(txt)

f.close()



#이상한 답

import pandas as pd

f = open("c:/python_data/yob/year_gender_total2.csv", "w")

for i in range(2000,2017):
    temp = pd.read_csv('c:/python_data/yob/yob{}.txt'.format(i), names = ['name', 'gender', 'cnt'])
    temp1 = temp.groupby(temp['gender']).sum()
    f_cnt = temp1.loc['F']
    m_cnt = temp1.loc['M']
    txt = "{},{},{}\n".format(i,f_cnt, m_cnt)
    f.write(txt)

f.close()


#답

import os
from pandas import Series, DataFrame
import pandas as pd
import numpy as np

with open('c:/python_data/year_gender_total.csv','w') as f:
    writer = csv.writer(f, delimiter=',')
    writer.writerow(['년도','여자','남자'])
    for y in range(2000,2017):
        filename='c:\python_data\yob%d.txt'%y
        name = os.path.basename(filename)
        name = name.split('.')[0]
        df = pd.read_csv(filename, names=['name','gender','birth'])
        gender_cn = df['birth'].groupby(df['gender']).sum()
        f_cn = gender_cn.loc['F']
        m_cn = gender_cn.loc['M']
        writer.writerow([name[3:],f_cn, m_cn])
        


#writing시 영어 외의 문자열은 utf-8로 encoding 을 해야 문자가 깨지지 않는다. option으로 encoding='utf-8'을 사용하기! 
with open('c:/python_data/year-gender_total.csv','w',encoding='utf-8') as f:
    
    
###############################################################################

▣ matplotlib: 시각화 패키지

import matplotlib as mpl
import matplotlib.pylab as plt

plt.plot([1,5,10,15,20])
#graph격자
plt.grid(True)  
#plot을 show 해줘
plt.show

#x축: [100,200,300,400,500], y축: [1,5,10,15,20]
plt.plot([100,200,300,400,500],[1,5,10,15,20])
#web에서는 show를 하지 않으면 출력하지 않기 때문에 plt.show를 하면 출력된다. (spider에서는 plt.show를 쓰지 않아도 plot이 제공되지만 그래프 정보만 나오는 경우는 plt.show를 해줘야 그래프를 볼 수 있다.)
plt.show


plt.plot([100,200,300,400,500],[1,5,10,15,20], color='blue')
plt.plot([100,200,300,400,500],[1,5,10,15,20], color='c')  #rgbcmyk
plt.plot([100,200,300,400,500],[1,5,10,15,20], color='r')
plt.plot([100,200,300,400,500],[1,5,10,15,20], color='b')
plt.plot([100,200,300,400,500],[1,5,10,15,20], color='g')
plt.plot([100,200,300,400,500],[1,5,10,15,20], color='m')
plt.plot([100,200,300,400,500],[1,5,10,15,20], color='y')
plt.plot([100,200,300,400,500],[1,5,10,15,20], color='k')
plt.show

#회색조
plt.plot([100,200,300,400,500],[1,5,10,15,20], color='0.75') #0~1 회색조
plt.show

#linestyle -solid, dashed, dashdot
plt.plot([100,200,300,400,500],[1,5,10,15,20], color='blue', linestyle='dotted')
plt.show

plt.plot([100,200,300,400,500],[1,5,10,15,20], color='blue', linestyle='solid')
plt.show

plt.plot([100,200,300,400,500],[1,5,10,15,20], color='blue', linestyle='dashed')
plt.show

plt.plot([100,200,300,400,500],[1,5,10,15,20], color='blue', linestyle='dashdot')
plt.show

#
plt.plot([100,200,300,400,500],[1,5,10,15,20], '--r') #dashed red
plt.show

plt.plot([100,200,300,400,500],[1,5,10,15,20], '.r')
plt.show

plt.plot([100,200,300,400,500],[1,5,10,15,20], '-g') #solid green
plt show

plt.plot([100,200,300,400,500],[1,5,10,15,20], '--c') #dashed cyan
plt.show 

plt.plot([100,200,300,400,500],[1,5,10,15,20], '-.k') #dashdot black
plt.show

plt.plot([100,200,300,400,500],[1,5,10,15,20], ':r') #dotted red 
plt.show


# anaconda propmt에서 jupyter notebook 실행

clrl +enter: 실행
alt + enter: command line 생성 


# 
data = {'홍길동':[15,13,11],
        '윤건' : [13,14,15],
        '나얼': [10,9,12]}
data

df = DataFrame(data, index=['2015','2016','2017'])
df.rank()

x = df.rank()
x

plt.plot(x)
plt.show()


#한글은 깨짐 -> font를 불러와야 함 
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/windows/fonts/malgun.ttf").get_name()
rc('font', family=font_name)


#범례만들기: label 
plt.plot(x.ix[:,0], label='나얼')
plt.plot(x.ix[:,1], label='윤건', linestyle='--')
plt.plot(x.ix[:,2], label='홍길동', linestyle=':')
plt.title('기록 순위 비교 그래프', fontsize=15)
plt.xlabel('년도', fontsize=10)
plt.ylabel('순위',fontsize=10)
plt.legend() 
#yticks: 기존의 레벨을 다른 형식으로 변환해 주는 method
plt.yticks([1,2,3],['1등','2등','3등'])
#xticks:
plt.xticks(['2015','2016','2017'],['2015년', '2016년', '2017년'])

plt.xlim([2015.9,2017.9])


#y축의 범위: ylim
plt.ylim([1,2,3])
#x축의 범위: xlim
plt.xlim([2015.9,2017.9])


#범례출력하기 

#수평막대그래프
df.plot(kind='barh')
df.plot(kind='barh', stacked=True)

#수직막대그래프
df.plot(kind='bar')
df.plot(kind='bar', stacked=True)



##############################################################################
[문제180] 2010 ~ 2016  년도까지 성별 출생 현황을 그래프를 그리세요.

#module import 
import csv
from pandas import Series,DataFrame
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)
%matplotlib inline

with open('c:/python_data/year_gender_total.csv','w',encoding="utf-8") as f:
    writer = csv.writer(f, delimiter=',')
    writer.writerow(['년도','여자','남자'])
    for y in range(2000,2017):
        filename='c:\python_data\yob\yob%d.txt'%y
        name = os.path.basename(filename)
        name = name.split('.')[0]
        df = pd.read_csv(filename, names=['name','gender','birth'])
        gender_cn = df['birth'].groupby(df['gender']).sum()
        writer.writerow([name[3:],gender_cn.loc['F'],gender_cn.loc['M']])
      


df = pd.read_csv('c:/python_data/year_gender_total.csv')
df
#여자만 뽑아내어 그래프를 그리고 싶다면 df['여자']로 해서 Data를 뽑아낸 다음 
df['여자']

#set_index : '년도'를 index로 표현하고 싶을 때 사용 
df = df.set_index("년도")
df
df.plot()
df.plot(kind="bar")
df.plot(kind="barh")

plt.plot(df.ix[:,0], label="여자", color="r", linestyle="--")
plt.plot(df.ix[:,1], label="남자", color="b", linestyle=":")
plt.title("성별 출생 현황", fontsize=15)
plt.xlabel("년도",fontsize=10)
plt.ylabel("출생수",fontsize=10)
plt.legend()
plt.grid()



