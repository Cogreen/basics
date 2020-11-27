# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 09:50:48 2018

@author: stu
"""

▣ 연관성 분석
두개의 변수가 서로 독립적인가 아니면 이들간에 어떠한 연관성이 존재하는가를 파악하는 분석방법

명목, 서열(질적자료): 교차분석(카이스퀘어검정)
등간, 비율(양적자료): 상관분석(피어슨상관분석)

■ 공분산(covariance)
- 두 변수가 얼마나 함께 변하는지를 측정
- cov(x, y) > 0 : x와 y의 변화가 같은 방향으로 변화가 된다.
즉, 한 변수가 커질 때 다른 변수가 함께 커지거나 한 변수가 작아질 때 다른 변수가 함께 작아지는 경우는 변화의 방향이 같다. 
- cov(x, y) < 0 : x와 y의 변화가 다른 방향으로 변화가 된다. 
한 변수가 커질 때 다른 변수가 작아지거나 한 변수가 작아질 때 다른 변수가 커지는 경우는 변화의 방향이 다르다는 의미가 된다.
- cov(x, y) = 0: 두 변수의 값이 서로 상관없이 움직일 경우 공분산은 0이다. 

- 모집단의 공분산: N
                [(개별 x측정치 - x의 평균) * (개별 y측정치 - y의 평균)]합
공분산(x, y) = ----------------------------------------------------------
                                    N    
    
- 표본의 공분산 : n-1
                [(개별 x측정치 - x의 평균) * (개별 y측정치 - y의 평균)]합
공분산(x, y) = ----------------------------------------------------------
                                    n - 1   
             Σ((x-x평균) *(y-y평균))
cov(x,y) = ---------------------------- 
                    n - 1
                    
                    
## R>>>>>>>>>>>>>>
x <- c(184, 170, 180)
y <- c(85, 70, 82)

> (((184-178)*(85-79))+((170-178)*(70-79))+((180-178)*(82-79)))/2
[1] 57

> cov(x,y)
[1] 57

## python >>>>>>>>>> 
x = [184, 170, 180]
y = [85, 70, 82]

import numpy as np
np.mean(x)
np.mean(y)

# numpy를 이용하기 때문에 행렬을 통해 값이 뽑아지기 때문에 필요한 행렬의 값을 같이 적어야 한다.
np.cov(x,y)[0][1]


import pandas as pd
df= pd.concat([pd.DataFrame(x), pd.DataFrame(y)], axis=1)
df
df.columns = ['x','y']
df['x'].cov(df['y'])

■ 상관계수: 각각의 데이터에 따른 단위가 다르기 때문에 공분산을 표준화 시키는 작업이 필요하다. 따라서 상관계수를 구해야한다. 

▣ 상관분석(correlation analysis)
- 변수들 간의 연관성을 파악하기 위해 사용하는 분석기법중의 하나로 변수간의 선형관계 정도로를 분석하는 통계기법이다. 
- 두 변수 사이의 관련성을 파악하는 방법

■ 상관계수
- 두 변수간의 관련성의 정도를 의미 
- 계산방법: 피어슨 상관계수, 스피어만 상관계수(서열척도의 상관분석을 해야할 때), 겐달 순위상관계수
- 상관계수값이 크면 데이터간의 관계가 존재한다는 의미
- 한쪽 값이 커질 때 다른 쪽 값이 커지는 정도 
- 상관 -1 <= r <= 1
        공분산(x,y)    
- r = -------------------------- 
        루트(x분산 * y분산) 
        
cf. 루트(x분산 * y분산)-> 표준편차
                Σ(x-x의 평균)*(y-y의 평균)
                --------------------------
                            n-1
  = -------------------------------------------------
      루트((Σ(x-x의 평균)제곱)  * (Σ(y-y의 평균)제곱))

  
### python
import math
(((184-178)*(85-79))+((170-178)*(70-79))+((180-178)*(82-79)))/math.sqrt(((184-178)**2+(170-178)**2+(180-178)**2)*((85-79)**2+(70-79)**2+(82-79)**2))

df['x'].corr(df['y'])


# =============================================================================
#  [문제] 학생 10명의 키와 몸무게를 측정한 자료이다. 자료를 분석하여 키와 몸무게의 선형관계를 나타내는 상관관계를 구하고, 그 유의성을 유의수준(α) 0.05에서 검정하세요. 
# height <- c(176, 172, 182, 160, 163, 165, 168, 163, 182, 182)
# weight <- c(72, 72, 70, 43, 48, 54, 51, 52, 73, 88)
# =============================================================================
# R>>>>
height <- c(176, 172, 182, 160, 163, 165, 168, 163, 182, 182)
weight <- c(72, 72, 70, 43, 48, 54, 51, 52, 73, 88)

mean(height)
mean(weight)

plot(height, weight)
cov(height, weight)
cor(height, weight)

▣ 가설검정
- Ho (귀무가설): 키와 몸무게 간에 선형관계가 없다(키와 몸무게의 상관계수는 0이다)
- H₁ (대립가설, 연구가설): 키와 몸무게 간에 선형관계가 있다.(키와 몸무게의 상관계수는 0이 아니다)


- 유의수준(α) 0.05
- t분포의 자유도 n-2
- df = 10-2 =8
                      /           \
                     /             \
                    /               \
                   /                 \
                  /                   \  
                 /                     \
                /                       \
               /                         \
              /                           \
             /                             \
            /                               \
           /                                 \
          /                                   \
-------------|-----------------------------|-------------
        t(α/2,n-2)                    t(α/2,n-2)        cf. α/2: 양쪽 두개 중 한 부분이기 때문에 2로 나눈다.
        t(0.0258, 8)                  t(0.0258, 8)
        2.306                         2.306

t = r * sqrt((n-2)/1-r²) 
  = 0.91*sqrt(8/(1-((0.91)^2)))
  = 6.207
  
■ 결과해석
- 유의수준(α) 0.05로 하여 검정한 결과 검정통계량 t값(6.207)이 우측 임계치(2.306)보다 크므로 귀무가설을 기각하고 대립가설을 채택한다. 
- 즉, 키와 몸무게의 상관계수 0.91은 5% 유의수준에서 검정한 결과 통계적으로 유의하다. 

■ R에서 제공하는 t검정 
cor.test(height, weight, method ="pearson", alternative = "two.sided") 
#기본값이 양측검정임(alternative = "two.sided")
help(cor.test)

# Pearson's product-moment correlation
# 
# data:  height and weight
# t = 6.193, df = 8, p-value = 0.0002614
# alternative hypothesis: true correlation is not equal to 0
# 95 percent confidence interval:
# 0.6553010 0.9787161
# sample estimates:
# cor 
# 0.909622 

#
cor.test(height, weight, method ="pearson", alternative = "two.sided") 
cor.test(height, weight, method ="pearson", alternative="greater")
cor.test(height, weight, method ="pearson", alternative="less")

#alternative
two.sided : x,y집단이 서로 같은지 비교
less : x집단이 y집단보다 작은지 비교(x less than y)
greater: x집단이 y집단보다 큰지 비교(x greater than y)

#method
method = pearson, kendall, spearman

□ 양측검정을 하더라도 r에서 p-value는 단측검정의 p-value값으로 출력한다. 

■ Python에서 제공하는 t검정 (pearsonr)
height = [176, 172, 182, 160, 163, 165, 168, 163, 182, 182]
weight= [72, 72, 70, 43, 48, 54, 51, 52, 73, 88]

from scipy.stats import pearsonr

#
pearsonr(height, weight)
Out[44]: (0.9096220430530334, 0.00026141557536073885) -> 상관계수, p-value

□ 양측검증은 양측에 p-value가 있기 때문에 p-value값을 유의수준 값과 비교한다.
-> 이 경우 p-value값이 유의수준 값보다 작기 때문에 귀무가설을 기각하고 대립가설을 채택한다. 
-> pvalue = 0.0002614이기 때문에 유의수준 0.05라고 하고
0.0002614 < 0.05 가 되어 귀무가설을 기각하고 대립가설을 채택한다.

□ 단측검증 p-value를 유의수준 값과 바로 비교하면 된다.  


▣ 회귀분석(Regression )
인과관계를 분석하는 방법

□ 인과관계
- 어떤 변수가 어떤 변수에게 어떤 영향을 주는지를 판단 
□ 상관관계
- 변수와 변수가 어떤 연관이 있는지, 방향성을 나타낸다. 

■ 인과관계 조건
1. x가 변할 때 y도 변한다.
    교육연수(독립변수) - 생활만족도(종속변수)
2. 시간적으로 선행되어야 한다.(독립변수가 종속변수보다 선행되어야 한다.)
    교육연수가 먼저 선행되어야 한다.
3. 외생변수를 통제(다른 요인들을 통제하고 인과관계를 분석)
    교육연수 -> 생활만족도 
        다른요인(성별, 직업, 거주지, 근무연수 등)

■ 회귀분석(regression)
독립변수 -> 종속변수 
광고비 -> 매출액
매출액 -> 광고비
담배량 -> 폐암
배기량 -> 연료소비량 
온도 -> 아이스크림 판매량

■ 독립변수의 수
1개 일때: 단순회귀분석
2개 이상일 때: 다중회귀분석 

■ 독립변수의 척도 
등간, 비율: 일반회귀분석
명목, 서열: 가변수회귀분석(dummy변수회귀분석: on-hot encoding)

■ 독립변수와 종속변수관계
- 선형
- 비선형

1. 회귀분석을 할때 산점도를 그려보는 것도 좋다. 
x가 커지면서 y도 커진다.(선형)
x가 커지면서 y도 작아진다.(선형)
x가 커지면서 y도 커지다가 작아진다. (비선형) 

2. 모델 선을 그려본다.
최소제곱법을 이용해서 선을 그린다. 
y = ax+b (일차원방정식)
y = 종속변수
x = 독립변수
a = 회귀계수(기울기)  *가장 중요한 값임 
b = 절편(y의 시작점)

직선의 방정식의 기울기를 구하려면 
y = ax      a = y/x

편차제곱의 합 
    Σ(y-y평균)^2
= -----------------
    Σ(x-x평균)^2

            Σ((x-x평균)*(y-y평균))          x와 y 공분산 
기울기 = ---------------------------- = ------------------
                Σ(x-x평균)^2                   x분산      
            cov(x,y)
       = -----------------
            var(x)

b = y의평균 - 기울기*x의 평균 

height <- c(176, 172, 182, 160, 163, 165, 168, 163, 182, 182)
weight <- c(72, 72, 70, 43, 48, 54, 51, 52, 73, 88)

키 185일 때 몸무게는?
  
y = ax + b

a: 기울기
cov(height, weight)/ var(height) = 1.51
      cov(height, weight)
a = -----------------------
        var(heihgt)

y = mean(weihgt)  
y <-mean(weight)
x = mean(height)
x <-mean(height)
b = y - a * x  
#b <- y-1.51*x
b= mean(weight) - ((cov(height,weight)/var(height))) *mean(height)
> b
[1] -197.9022

기울기를 줄이기 위해 미분을 해야함 -> 편미분 필요 

■ 예측모형 만들기(linear model)
□ 단일회귀분석 
lm(weight~height) #linear model lm(종속변수~독립변수)

# Call:
#   lm(formula = weight ~ height)
# 
# Coefficients:
#   (Intercept)       height  
# -197.902        1.519  

기울기: 1.519  
y = 1.519*185 + (-197.902)
> y
[1] 83.113

□ 다중회귀분석 
lm(weihgt~height+독립변수2+독립변수3+....)

# =============================================================================

##R >>>>>>>>>
#score파일: txt파일 이기때문에 read.table을 사용하고, 나머지 옵션을 사용함
score <- read.table("c:/data/score.txt",header=T, sep=",")
score

#앞에 score$를 계속 사용하지 않기 위해 attach를 사용할 수 있다. 
attach(score)

□ 단일회귀분석 
#공분산 [1] 70.6
cov(IQ,성적)

#상관계수 [1] 0.9102242
cov(IQ, 성적)/ (sd(IQ)*sd(성적))
cor(IQ,성적)

#회귀분석
l <- lm(성적~IQ)
# Call:
#   lm(formula = 성적 ~ IQ)
# 
# Coefficients:
#   (Intercept)           IQ  
# -5.2918       0.6714  

IQ가 130일때 시험성적 예측?
# -5.2918: 절편 / 0.6714: 기울기
성적 = 130*0.6714+(-5.2918)
     = 81.9902 

#산점도와 회귀라인 그리기  
plot(IQ, 성적, pch=20, col="red")
abline(l, col="blue")
#cf. 신경망에서 abline을 산점도에 맞게 fitting되도록 오차범위를 줄이는 것이 중요하다. -> 경사하강법 

#간단하게 절편과 기울기보기 
coef(l)

#성적과 다니는 학원의수의 상관관계
lm(성적~다니는학원수)

plot(다니는학원수, 성적, pch=20, col="red")
abline(lm(성적~다니는학원수), col="blue")

□ 다중회귀분석 
lm(성적~IQ+다니는학원수+게임하는시간+TV시청시간)
# Call:
#   lm(formula = 성적 ~ IQ + 다니는학원수 + 게임하는시간 + TV시청시간)
# 
# Coefficients:
#   (Intercept)            IQ  다니는학원수  게임하는시간    TV시청시간  
# 23.2992        0.4684        0.7179       -0.8390       -1.3854  

y = ax1 + bx2 + cx3+ dx4 + z
= (135*0.4684)+(5*0.7919)+(1*-0.8390)+(1*-1.3854)+23.2992
= 88.2683

 
# =============================================================================
#python >>>>>>>>>
전기 생산금액과 전기사용량의 상관관계 
from scipy import stats

#월별 전기 생산금액(억원)
x = [3.52,2.58,3.31,4.07,4.62,3.98,4.29,4.83,3.71,4.61,3.90,3.20]
#월별 전기사용량(백만kwh)
y = [2.48,2.27,2.47,2.77,2.98,3.05,3.18,3.46,3.03,3.25,2.67,2.53]

#단순(선형)회귀분석 (x:독립변수, y종속변수)
stats.linregress(독립변수,종속변수)
stats.linregress(x,y)
# Out[54]: LinregressResult(slope=0.4956032360182905, intercept=0.9195814280689418, rvalue=0.8929235125385305, pvalue=9.238421943157891e-05, stderr=0.07901935226531728)

#새로운 변수들로 뽑아내기 
slope, intercept, r_value, p_value, stderr = stats.linregress(x,y)
- slope: 기울기
- intercept: 절편
- r_value: 상관계수
- p_value: p값
- stderr: error에 대한 표준편차(관측값과 abline의 오차률에 대한 표준편차)

# 생산금액: 4억원이라 할 때 사용량은?
y = 4*slope + intercept
y  
Out[61]: 2.901994372142104

# 가설검정
Ho(귀무가설): 전기생산금액과 전기사용량은 상관관계가 없다.
H₁(대립가설): 전기생상금액과 전기사용량은 상관관계가 있다. 

유의수준(α) 
p-value(9.238421943157891e-05)가 유의수준 값보다 (0.05)보다 작으므로 귀무가설을 기각하고 대립가설을 채택한다. 
#cf. p-value: 양측검정값  

#plot그리기
import matplotlib.pyplot as plt 

#월별 전기 생산금액(억원)
x = [3.52,2.58,3.31,4.07,4.62,3.98,4.29,4.83,3.71,4.61,3.90,3.20]
#월별 전기사용량(백만kwh)
y = [2.48,2.27,2.47,2.77,2.98,3.05,3.18,3.46,3.03,3.25,2.67,2.53]

#산점도와 회귀선 그리기 
plt.scatter(x,y)
#x변수를 array값으로 만들기
x1 = np.array(x)
plt.plot(x1, slope*x1 + intercept, c="red", linewidth="0.5")

# =============================================================================
#ozone <- read.csv("c:/data/ozone.csv")
#
#ozone.nafill 
#
#
#ozone과 temp관계
#attach(Ozone)
#
##Ozone의 na값 평균으로 대체 
#Ozone1 <- replace(Ozone, is.na(Ozone), mean(Ozone, na.rm=T))
#
##Temp의 na값 평균으로 대체
#Temp1 <- replace(Temp, is.na(Temp), mean(Temp, na.rm=T))
#
#
## na 값을 평균값으로 치환했을 때 
#l1<-lm(Ozone1~Temp1)
#
#plot(Ozone1,Temp1, pch=20, col="red")
#abline(l1, col="blue")
#
#
##
#l <-lm(Ozone~Temp)
#
#plot(Ozone1,Temp1, pch=20, col="red")
#abline(l1, col="blue")

# =============================================================================
# python >>>>>>>
□ 단일회귀분석
import pandas as pd

df = pd.read_csv("c:/data/ozone.csv")
df.head()

df.count()

#df에 열단위의 na의 건수 세기(컬럼별 결측값 개수)
df.isnull().sum()

#행단위로 na의 건수 보기(행단위로 결측값 개수)
df.isnull().sum(1)

#결측값을 제거한 데이터 만들기
df2 = df.dropna(axis=0)
df2.isnull().sum()

x = df2["Temp"].values
y = df2["Ozone"].values

stats.linregress(x,y)

#
귀무가설: 오존과 온도는 상관관계가 없다. (온도가 오존에 영향을 주지 않는다.)
대립가설: 오존과 온도는 상관관계가 있다. (온도가 오존에 영향을 준다.)

#유의수준을 0.05라고 가정할때 
p-value(1.552677229392932e-17)는 0.05보다 작기 때문에 귀무가설을 기각하고 대립가설을 채택한다. 

#cf-na를 0로 했을 때 
df['Ozone'].fillna(0, inplace=True)
df['Temp'].fillna(0, inplace = True)

slope, intercept, rvalue, pvalue, stderr = stats.linregress(x,y)

#온도가 화씨 80도 일때 오존량 예측?
y = slope*x + intercept 
  = slope*80 + intercept 
  = 47.48272006175401


# =============================================================================
# python >>>>>>>
□ 다중회귀분석
#score파일을 encoding을 utf-8로 바꿔 저장하기

score = pd.read_csv("c:/data/score.txt")

stats.linregress(score.ix[:,2], score['성적'])

slope, intercept, rvalue, pvalue, stderr = stats.linregress(score.ix[:,2], score['성적'])

#회귀모형 만들기  - 다중회귀모형
from sklearn import linear_model

#모델 만들기
reg = linear_model.LinearRegression()

#fit하기  (다중회귀분석)
reg.fit(score.ix[:,2:6], score['성적'])

# 각 변수에 대한 기울기(reg.coef_) , 절편(intercept_) 확인하기
print("절편: \n", reg.intercept_)
print("기울기: \n", reg.coef_)
