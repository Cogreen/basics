# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 10:09:14 2018

@author: stu
"""

▣ 회귀분석(Regression)
- 독립변수(X)와 종속변수(Y)의 관계식을 구하는 기법 
- 독립변수(영향을 주는 변수)가 한 단위 증가할 때 종속변수(영향을 받는 변수)가 얼마나 영향을 받는지 분석하는 방법
- 회귀식(y=ax+b), 회귀계수(a)

■ 단순회귀분석: 독립변수가 1개인 회귀모형 
예) 기업의 광고집행액(X)을 이용하여 그 기업의 매출액(Y)을 예측하는 모형

■ 다중회귀분석: 독립변수가 2개 이상인 회귀모형
예) 학생의 학원 수(X1)과 하루 평균학습시간(X2)을 이용하여 그 학생의 성적(Y)을 예측하는 모형

- 회귀분석은 대상 변수들은 양적자료(등간, 비율)

Y값의 증가량
기울기 = ---------------
  X값의 증가량

X: 독립변수
Y: 종속변수

X값에 따라 Y값이 달라진다. 

회귀식 
Y = aX + b
a = 회귀계수, 기울기
b = Y의 절편 

(X-X평균)(Y-Y평균)의 합          (x,y)의 공분산
a =  ---------------------------  =   ------------------
  (X-X평균)제곱의 합                (x)의 분산

b = y의평균 - (기울기*x의평균)

x =2, 4, 6, 8
y = 71, 83, 91, 97

#python >>>>
x =[2, 4, 6, 8]
y = [71, 83, 91, 97]

import numpy as np
import pandas as pd
np.mean(x)
Out[6]: 5.0

np.mean(y)
Out[7]: 85.5

a = ((2-5)*(71-85.5) + (4-5)*(83-85.5) + (6-5)*(91-85.5) + (8-5)*(97-85.5))/((2-5)**2+(4-5)**2+(6-5)**2+(8-5)**2)
a 
Out[23]: 4.3

b = 85.5 -(4.3*5)
b 
Out[25]: 64.0

3시간 공부했을 때 성적을 예측?
  y = 43.3*3-64
y
Out[27]: 65.899

# =============================================================================
#>> method를 이용해서 구해보기
import math

df = pd.concat([pd.DataFrame(x), pd.DataFrame(y)], axis=1)
df.columns = ['x','y']

df['x'].corr(df['y'])

from scipy import stats

stats.linregress(x,y)

slope, intercept, rvalue, pvalue, stderr = stats.linregress(x,y)

y = slope*x + intercept

# =============================================================================
# 프로그램으로 짜기 

import numpy as np
x = np.array([2,4,6,8])
y = np.array([71,83,91,97])

x_mean = np.mean(x)
y_mean = np.mean(y)

#리스트 내장객체로 프로그램만들기
denominator = sum([(i- x_mean)**2 for i in x])
#함수로 만들어보기 
def func(x, x_m, y, y_m):   #x, x_m, y, y_m: 형식매개변수이므로 밖의 변수의 이름과 다르다.
  s = 0
for i in range(len(x)):
  s += (x[i]-x_m) * (y[i]-y_m)        #누적합만들기
return s

numerator = func(x, x_mean, y, y_mean)
numerator 
Out[49]: 86.0

a = numerator/denominator
b = y_mean -(a*x_mean)

print("기울기: ",a)
print("절편: ",b)

#최소제곱법으로 plot과 회귀선 그리기 
import matplotlib.pyplot as plt
%matplotlib.inline

plt.scatter(x,y)
plt.plot(x, a*x+b, c="red")

#오차 출력하기
print("실제값 :", y)          # 실제값 : [71 83 91 97]
print("예측값: ", a*x+b)      # 예측값:  [72.6 81.2 89.8 98.4]
print("오차: ", y-(a*x+b))    # 오차:  [-1.6  1.8  1.2 -1.4]

# 
■ 평균제곱근오차(root mean square error) rmse
주어진 선의 오차를 평가하는 오차평가 알고리즘
오차 = 실제값 - 예측값
                      Σ(실제값-예측값)²        (편차제곱의 합)
평균제곱오차(mse) = -----------------------  = ----------------- 
                            n                        n

평균제곱오차를 하게 되면 숫자가 커지기 때문에 root를 사용하여 값을 줄이는 방법으로서 평균제곱근오차가 나옴
                              Σ(실제값-예측값)²        
평균제곱근오차(rmse) = sqrt -----------------------  
                                     n   

평균제곱근오차를 줄이는 것이 중요하다.

np.sqrt(sum((y-a*x-b)**2)/len(y))

np.sqrt(np.mean((y-a*x-b)**2))

# =============================================================================
▣ logistic regression
- 분류를 하는데 있어서 가장 흔한 경우는 이분법을 기준으로 분류하는 경우
예) 특정 고객이 물건을 구매할지(1), 안 할것인지(0)
어떤 기업이 부도가 날것인지(1), 안 날것인지(0)
내일 비가 올 것인지(1), 안 올것인지(0)
- 적용분야
기업의 부도예측, 주가, 환율, 금리 등의 UP/DOWN예측 모형    

import pandas as pd
from sklearn.linear_model import LogisticRegression

iris = pd.read_csv("c:/data/iris.csv")

x = iris.ix[:,:-1]
y = iris['Name']

#
logreg = LogisticRegression()
logreg.fit(x,y) #x:독립변수, y:종속변수

new_observation = [[5.1,3.5,1.4,0.2]]
logreg.predict(new_observation)
#Out[95]: array(['Iris-setosa'], dtype=object)

new_observation = [[6.9,3.2,5.7,2.3]]
logreg.predict(new_observation)
#Out[97]: array(['Iris-virginica'], dtype=object)

new_observation = [[7.0,3.2,4.7,1.4]]
logreg.predict(new_observation)
#Out[109]: array(['Iris-versicolor'], dtype=object)


# =============================================================================
# 자율학습
# =============================================================================


titanic = pd.read_csv("c:/data/titanic.csv")
titanic.head()
t

#동물
zoo = pd.read_csv("c:/data/zoo.csv")
zoo.head()

x = zoo.ix[:,2:17]
y = zoo.ix[:,-1]

logreg = LogisticRegression()
logreg.fit(x,y)

new_observation = [[0,0,1,0,0,0,1,1,1,0,0,4,1,0,1,1]]
logreg.predict(new_observation)

lark=[[1,1,0,1,0,0,0,1,1,0,0,2,1,0]]
logreg.predict(lark)

housefly=[[0,1,0,1,0,0,0,0,1,0,0,6,0,0]]
logreg.predict(housefly)

# =============================================================================
# statsmodels
# =============================================================================

statsmodels
검정 및 추정(test and estimation)
회귀분석(regressio analysis)
시계열분석(time-series analysis)

import statsmodels.api as sm
import pandas as pd

df = pd.read_csv("c:/data/titanic.csv")
df.head()
성별(gender), 나이(age), 객실등급(pclass), 요금(fare)이 생존에 어느 정도의 영향을 미치는가? 
  
  회귀분석에는 연속형 자료/
  성별(gender) - one-hot encoding으로/ dummy table로 
gender.replace


cols = ['survived', 'age', 'fare']

#
분류할 수 있는 컬럼들은 더미 컬럼으로 만든다. 
pclass 1,2,3의 들어 갈 경우 => pclass_1(0/1), pclass_2(0/1), paclass3(0/1)
dummy_pclass = pd.get_dummies(df['pclass'], prefix='pclass')
#Out[221]: 
#     pclass_1  pclass_2  pclass_3
#0           0         0         1
#1           1         0         0
#2           0         0         1
#3           1         0         0
#4           0         0         1
#5           0         0         1
#6           1         0         0
#7           0         0         1
#8           0         0         1

dummy_gender = pd.get_dummies(df['gender'], prefix='gender')
#Out[223]: 
#     gender_female  gender_male
#0                0            1
#1                1            0
#2                1            0
#3                1            0
#4                0            1

#data 합치기  (concat, join 등 이용 가능)
data = df[cols].join(dummy_pclass)
data = data.join(dummy_gender)

#NaN이 있으면 회귀분석이 안되고 -> 결과값이 NaN으로 나온다. 
#따라서 NaN값을 처리해줘야한다. -> NaN값을 어떻게 처리할 것인가? 1. 버릴것인가? drop.nan 2.나이값을 대체함 -> 최저? 최고? 평균?! 
#NaN값 개수 구하기
data.isnull().sum()

1. median으로 구한 경우
data1 = data.copy()

#데이터가 같은 메모리를 참조하고 있으므로, deep copy를 하애함 
id(data)    #Out[233]: 205596712
id(data1)   #Out[234]: 222309736

# 중심경향을 파악하기 위해서는 중앙값이 더 나으므로 
data1['age'].fillna(data1['age'].median(skipna=True), inplace=True) #inplace=True: 값을 적용하기
data1.isnull().sum()

#독립변수 컬럼 
train_cols = data1.columns[1:]

#logistic regression
logit = sm.Logit(data1['survived'],data1.ix[:,1:])
result = logit.fit()

# 분석된 결과 출력
result.summary2()
#Coef.: 회귀계수  - 큰값이 가장 영향을 많이 줌 
Out[246]: 
  <class 'statsmodels.iolib.summary2.Summary'>
  """
Results: Logit
=================================================================
Model:              Logit            Pseudo R-squared: 0.321     
Dependent Variable: survived         AIC:              817.3956  
Date:               2018-10-30 15:36 BIC:              846.1497  
No. Observations:   891              Log-Likelihood:   -402.70   
Df Model:           5                LL-Null:          -593.33   
Df Residuals:       885              LLR p-value:      3.2405e-80
Converged:          1.0000           Scale:            1.0000    
No. Iterations:     6.0000                                       
-----------------------------------------------------------------
Coef.  Std.Err.    z    P>|z|   [0.025  0.975]
-----------------------------------------------------------------
age               -0.0329   0.0074 -4.4271 0.0000 -0.0475 -0.0183
fare               0.0008   0.0021  0.3611 0.7180 -0.0034  0.0049
pclass_1           1.5328      nan     nan    nan     nan     nan
pclass_2           0.4622      nan     nan    nan     nan     nan
pclass_3          -0.7497      nan     nan    nan     nan     nan
gender_female      1.9249      nan     nan    nan     nan     nan
gender_male       -0.6798      nan     nan    nan     nan     nan
=================================================================
"""
#의사결정트리를 쓰지 않아도 회귀분석을 통해 Coef를 통해 가장 영향을 많이 주는 독립변수를 확인할 수 있다. 

#계산이 잘 나오질 않을 경우 동일하게 가중치를 주기도 한다. 
#가중치 설정 
data1['intercept'] = 1.0 

#독립변수 컬럼 
train_cols = data1.columns[1:]

#logistic regression
logit = sm.Logit(data1['survived'],data1.ix[:,1:])
result = logit.fit()

# 분석된 결과 출력
result.summary2()
Out[255]: 
  <class 'statsmodels.iolib.summary2.Summary'>
  """
Results: Logit
============================================================================
Model:                   Logit               Pseudo R-squared:    0.321     
Dependent Variable:      survived            AIC:                 817.3956  
Date:                    2018-10-30 15:44    BIC:                 846.1497  
No. Observations:        891                 Log-Likelihood:      -402.70   
Df Model:                5                   LL-Null:             -593.33   
Df Residuals:            885                 LLR p-value:         3.2405e-80
Converged:               1.0000              Scale:               1.0000    
No. Iterations:          10.0000                                            
----------------------------------------------------------------------------
Coef.    Std.Err.      z    P>|z|      [0.025       0.975]   
----------------------------------------------------------------------------
age           -0.0329       0.0074 -4.4271 0.0000       -0.0475      -0.0183
fare           0.0008       0.0021  0.3611 0.7180       -0.0034       0.0049
pclass_1       1.3064          nan     nan    nan           nan          nan
pclass_2       0.2358          nan     nan    nan           nan          nan
pclass_3      -0.9761          nan     nan    nan           nan          nan
gender_female  1.5854 2952743.2140  0.0000 1.0000 -5787268.7698 5787271.9405
gender_male   -1.0194 2952743.2140 -0.0000 1.0000 -5787271.3745 5787269.3358
intercept      0.5660          nan     nan    nan           nan          nan
============================================================================

"""

#data1[train_cols]: 설명변수 (독립변수) / data1['survived']목적변수 
data1['predict'] = result.predict(data1[train_cols])

data1[data1['predict']>=0.9]
data1[data1['predict']>=0.7]    

# =============================================================================
# R>>>>>>>>>>>

help(cars)
str(cars)

speed: 차속도(단위 mi/h)
dist: 제동거리(단위 feet)
#dist: 종속변수, speed: 독립변수
lmresult <- lm(dist~speed, data=cars)
lmresult
summary(lmresult)
# > summary(lmresult)
# 
# Call:
#   lm(formula = dist ~ speed, data = cars)
# 
# Residuals:
#   Min      1Q  Median      3Q     Max 
# -29.069  -9.525  -2.272   9.215  43.201 
# 
# Coefficients:
#   Estimate Std. Error t value Pr(>|t|)    
# (Intercept) -17.5791     6.7584  -2.601   0.0123 *  
#   speed         3.9324     0.4155   9.464 1.49e-12 ***
#   ---
#   Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
# 
# Residual standard error: 15.38 on 48 degrees of freedom
# Multiple R-squared:  0.6511,	Adjusted R-squared:  0.6438 
# F-statistic: 89.57 on 1 and 48 DF,  p-value: 1.49e-12

#####
# 절편: (Intercept) -17.5791 
# 회귀계수: 3.9324 
# p-value: 1.49e-12 -> 유의수준 0.05를 기준으로 봤을 때 귀무가설을 기각하고 대립가설을 채택한다. 따라서 속력과 제동거리의 상관관계가 있다. 

coef(lmresult)

plot(cars$speed, cars$dist)
abline(lmresult, col='red')

speed <- c(50,60,70,80,90,100)
df <- data.frame(speed)

■점추정 (speed에 따른 예측된 거리 계산)
point_estimation <- predict(lmresult, df)
cbind(df, point_estimation)

■구간추정 (speed에 따른 예측된 구간추정)
interval_estimation <- predict(lmresult,df,interval="confidence", level=0.95)
cbind(df, interval_estimation)
fit:점추정, lwr:구간최소값, upr:구간 최대값 
# > cbind(df, interval_estimation)
# speed      fit      lwr      upr
# 1    50 179.0413 149.8060 208.2766
# 2    60 218.3654 180.8489 255.8820
# 3    70 257.6895 211.8651 303.5139
# 4    80 297.0136 242.8670 351.1602
# 5    90 336.3377 273.8603 398.8151
# 6   100 375.6618 304.8480 446.4755

#60mi/h 속도인 경우 제동거리를 예측하면
점추정: 218.3654 feet
구간추정: 180.8489 feet~255.8820 feet사이일 확률이 95%이다. 


