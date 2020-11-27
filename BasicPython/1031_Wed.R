# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 09:46:09 2018

@author: stu
"""
# =============================================================================
# [문제199] 보험데이터를 이용해서 보험료에 가장 영향을 주는 독립변수가 무엇인지 확인하세요.
# =============================================================================
import statsmodels.api as sm
import pandas as pd

df = pd.read_csv("c:/data/insurance.csv")


#종속변수
charges = df.ix[:,-1]

#독립변수

df.head()
## 
cols = ['age','bmi','children']

##one-hot encoding: sex, smoker, region
dummy_sex = pd.get_dummies(df['sex'], prefix='sex')
dummy_smoker = pd.get_dummies(df['smoker'], prefix='smoker')
dummy_region = pd.get_dummies(df['region'], prefix='region')

#data 합치기 
data = df[cols].join(dummy_sex)
data = data.join(dummy_smoker)
data = data.join(dummy_region)

#null 값 확인하기
data.isnull().sum()

#
data1 = data.join(charges)
data1.isnull().sum()


#독립변수 컬럼
train_cols = data.columns

#logisitic regression: ValueError: endog must be in the unit interval.
logit = sm.Logit(df['charges'],)

logit = sm.Logit(data1['charges'], data1.ix[:,:-1])

# =============================================================================

import math
from scipy import stats

#단일 회귀 모형 
#각각 독립변수의 하나씩 linregression 
#age
stats.linregress(data.ix[:,0],charges)
Out[110]: LinregressResult(slope=257.7226186668955, intercept=3165.885006063025, rvalue=0.2990081933306477, pvalue=4.886693331718491e-29, stderr=22.5023892867703

#bmi
stats.linregress(data.ix[:,1],charges)
Out[111]: LinregressResult(slope=393.87303079739524, intercept=1192.9372089611497, rvalue=0.1983409688336289, pvalue=2.459085535116683e-13, stderr=53.25073835210321)

#children
stats.linregress(data.ix[:,2],charges)
Out[112]: LinregressResult(slope=683.0893824813649, intercept=12522.495549644096, rvalue=0.06799822684790487, pvalue=0.012852128520136412, stderr=274.2018326126803)

#sex_female /sex_male
stats.linregress(data.ix[:,3],charges)
Out[113]: LinregressResult(slope=-1387.1723338865486, intercept=13956.751177721895, rvalue=-0.05729206220202543, pvalue=0.036132721005929666, stderr=661.3308807850439)
stats.linregress(data.ix[:,4],charges)
Out[115]: LinregressResult(slope=1387.1723338865484, intercept=12569.578843835347, rvalue=0.05729206220202542, pvalue=0.036132721005929715, stderr=661.3308807850439)

#smoker_no/ smoker_yes
stats.linregress(data.ix[:,5],charges)
Out[116]: LinregressResult(slope=-23615.963533676637, intercept=32050.231831532845, rvalue=-0.7872514304984772, pvalue=8.271435842179102e-283, stderr=506.0752903935149)
stats.linregress(data.ix[:,6],charges)
Out[117]: LinregressResult(slope=23615.963533676633, intercept=8434.268297856206, rvalue=0.7872514304984771, pvalue=8.271435842179102e-283, stderr=506.075290393515)

#region_northeast    0
stats.linregress(data.ix[:,7],charges)
Out[119]: LinregressResult(slope=179.40581081381077, intercept=13226.978705571993, rvalue=0.00634877128015607, pvalue=0.8165263815339816, stderr=773.098520385663)
#region_northwest    0
stats.linregress(data.ix[:,8],charges)
Out[121]: LinregressResult(slope=-1126.4650941640384, intercept=13544.04046813327, rvalue=-0.039904864040438005, pvalue=0.14459698799364254, stderr=771.6895403197774)
#region_southeast    0
stats.linregress(data.ix[:,9],charges)
Out[122]: LinregressResult(slope=2012.4799925698546, intercept=12722.93144504004, rvalue=0.07398155156575988, pvalue=0.006782698910658689, stderr=742.1866482510707)
#region_southwest    0
stats.linregress(data.ix[:,10],charges)
Out[123]: LinregressResult(slope=-1219.7658242269438, intercept=13566.70320151925, rvalue=-0.043210028991684774, pvalue=0.11414659361882144, stderr=771.5833691494033)



#회귀모형 만들기  - 다중회귀모형
from sklearn import linear_model

#모델 만들기
reg = linear_model.LinearRegression()

#fit하기  (다중회귀분석)
reg.fit(data, charges)

# 각 변수에 대한 기울기(reg.coef_) , 절편(intercept_) 확인하기
reg.intercept_
Out[126]: -666.9377199366445

reg.coef_
Out[127]: 
array([   256.85635254,    339.19345361,    475.50054515,     65.6571797 ,
-65.6571797 , -11924.26727096,  11924.26727096,    587.00923503,
234.0453356 ,   -448.01281436,   -373.04175627])



# =============================================================================
#R>>>>>>>>>>>
insurance <- read.csv("c:/data/insurance.csv")

str(insurance)

#상관계수: 서로 연관여부를 확인가능 (교차표로)
cor(insurance[c("age","bmi","children","charges")])
# > cor(insurance[c("age","bmi","children","charges")])
#               age       bmi   children    charges
# age      1.0000000 0.1092719 0.04246900 0.29900819
# bmi      0.1092719 1.0000000 0.01275890 0.19834097
# children 0.0424690 0.0127589 1.00000000 0.06799823
# charges  0.2990082 0.1983410 0.06799823 1.00000000

#시각화
install.packages("psych")
library(psych)

pairs.panels(insurance[c("age","bmi","children","charges")])
#자기자신의 부분에서는 분포도로 히스토그램으로 그려줌 

#다중회귀분석으로 보기
ins_model = lm(charges~., data=insurance)
ins_model
#보험료에 영향을 줄 수 있는 요소가 된다. smokeryes가 가장 영향을 준다. (기울기 값이 그 만큼 영향을 준다.)
# Call:
#   lm(formula = charges ~ ., data = insurance)
# 
# Coefficients:
#   (Intercept)              age          sexmale              bmi         children        smokeryes
#       -11938.5            256.9           -131.3            339.2            475.5          23848.5
# regionnorthwest  regionsoutheast  regionsouthwest
#         -353.0          -1035.0           -960.1


insurance$bmi30 <- ifelse(insurance$bmi >=30, 1 ,0)
ins_model2 = lm(charges~age+children+bmi+sex+smoker+bmi30*smoker+region, data=insurance)
# Call:
#   lm(formula = charges ~ age + children + bmi + sex + smoker + 
#        bmi30 * smoker + region, data = insurance)
# 
# Coefficients:
#   (Intercept)              age         children              bmi          sexmale        smokeryes  
#       -4745.5            263.2            520.4            115.0           -491.2          13402.4  
#         bmi30  regionnorthwest  regionsoutheast  regionsouthwest  smokeryes:bmi30  
#       -865.1           -266.8           -825.0          -1224.3          19794.9  


ins_model = lm(charges~age+children+bmi+sex+smoker,data=insurance)
ins_model
# 
# Call:
#   lm(formula = charges ~ age + children + bmi + sex + smoker, data = insurance)
# 
# Coefficients:
#   (Intercept)          age     children          bmi      sexmale    smokeryes  
# -12052.5        257.7        474.4        322.4       -128.6      23823.4  


# =============================================================================
import pandas as pd

df = pd.read_csv("c:/data/insurance.csv")
df.head()

dummy_sex = pd.get_dummies(df['sex'], prefix='sex')
dummy_smoker = pd.get_dummies(df['smoker'], prefix='smoker')
cols = ['age', 'bmi', 'children', 'charges']

data = dummy_smoker.join(dummy_sex)
data = df[cols].join(data)
data

import statsmodels.formula.api as smf
lm = smf.ols(formula="charges~age+smoker_yes+sex_male+bmi+children",data=data).fit()
print(lm.params)


# =============================================================================
# 인공지능  
# =============================================================================

▣ 인공지능 <- 머신러닝 <- 신경망(딥러닝)

▣ 퍼셉트론(perceptron)
- 인공뉴런(인공적으로 만든 신경세포)
- 1957년에 만든 알고리즘 
- 프랑크 로젠블라트가 퍼셉트론 알고리즘을 고안했다. 
- 퍼셉트론은 딥러닝(신경망)의 기원
- 다수의 신호를 입력받아 하나의 신호를 출력한다. 
- 신호의 흐름을 표현할 때 두가지 값을 갖는다. 
- 0: 신호가 흐르지 않는다. 
- 1: 신호가 흐른다. 

■ 퍼셉트론 동작
x: 입력값(입력신호) 
w: weight 가중치
Θ: theta 임계값
y: 출력

y = 0 w1 * x1 + w2 * x2 <= Θ  (입력값과 가중치값을 계산한 결과 임계값보다 작거나 같을 경우 출력값은 zero로 출력한다.)
y = 1 w1 * x1 + w2 * x2 > Θ  

w1 * x1 + w2 * x2 값이  Θ(임계값) 이하일 때는 0을 출력하고 임계값 보다 클때는 1을 출력한다. 

■ 논리회로
컴퓨터는 두가지 디지털값 0,1을 입력해서 하나의 값을 출력하는 회로가 모여 만들어지는데 이 회로를 gate(게이트)라고 한다. 

■ AND게이트
x1      x2      y
------------------
0       0       0
0       1       0
1       0       0
1       1       1

■ AND게이트를 퍼셉트론으로 표현
y = 0 w1 * x1 + w2 * x2 <= Θ 
y = 1 w1 * x1 + w2 * x2 > Θ  

w1 = 0.5 , w2 = 0.5 , Θ = 0.7

AND(0,0) = 0 
AND(0,1) = 0
AND(1,0) = 0
AND(1,1) = 1 

def AND(x1,x2): 
  w1 = 0.5 
  w2 = 0.5
  theta = 0.7    
  result = w1*x1 + w2*x2
  if result <= theta:
    return 0
  elif result > theta:
    return 1

AND(0,0)  
AND(0,1) 
AND(1,0)
AND(1,1) 

#AND(0,0)  
#Out[237]: 0
#
#AND(0,1) 
#Out[238]: 0
#
#AND(1,0)
#Out[239]: 0
#
#AND(1,1) 
#Out[240]: 1

■ OR게이트
x1      x2      y
------------------
0       0       0
0       1       1
1       0       1
1       1       1


■ OR게이트를 퍼셉트론으로 표현
def OR(x1,x2): 
  w1 = 0.5
  w2 = 0.5
  theta = 0.4
  result = w1*x1 + w2*x2
  if result <= theta:
    return 0
  elif result > theta:
    return 1

OR(0,0)  
OR(0,1) 
OR(1,0)
OR(1,1) 
#임계값을 0.7이라고 했을때 OR게이트 값이 나오지 않기 때문에 임계값을 조정하든 가중치를 조정하여야 OR게이트 값이 나온다. 
#현재는 임계값을 0.4을 조정함
#만약에 임계값이 고정이다고 하면 Weight값을 조정해야한다. 
#OR(0,0)  
#Out[252]: 0
#
#OR(0,1) 
#Out[253]: 1
#
#OR(1,0)
#Out[254]: 1
#
#OR(1,1) 
#Out[255]: 1

■ NAND(NOT AND)게이트를 퍼셉트론으로 표현
x1      x2      y
------------------
0       0       1
0       1       1
1       0       1
1       1       0

def NAND(x1,x2): 
  w1 = -0.5
  w2 = -0.5
  theta = -0.7
  result = w1*x1 + w2*x2
  if result <= theta:
    return 0
  elif result > theta:
    return 1

NAND(0,0)  
NAND(0,1) 
NAND(1,0)
NAND(1,1) 

■ XOR (eXclusive OR) 배타적논리합
x1      x2      y
------------------
0       0       0
1       0       1
0       1       1
1       1       0

x1과 x중 어느 한쪽이 1일때만 1을 출력하는 배타적논리회로이다.
단 퍼셉트론은 XOR  게이트를 구현할 수 없다. 

■ 퍼셉트론의 한계
- 직선 하나로 XOR게이트의 출력을 구분할 수 없다.
- 페셉트론(단층퍼셉트론)은 직선하나로 나눈 영역만 표현할 수 있는 한계가 있다. 
- 민스키가 기존 퍼셉트론의 문제점을 지적햇는데 XOR분류를 못한다는 문제점을 지적하고 인공지능의 겨울기가 시작되었다. 


▣ 다층퍼셉트론(Multi layer perceptron)
x1      x2      OR    NAND     AND
----------------------------------------
0       0       0       1       0
1       0       1       1       1
0       1       1       1       1
1       1       1       0       0

다층 퍼셉트론(OR, NAND를 만들어)으로 AND연산 작업을 하면 XOR를 만들 수 있다.
1. x1와 x2를 통해 OR층을 만듦
2. x1와 x2를 통해 NAND층을 만듦
3. 중간에 만든 OR와 NAND를 AND계산 작업을 함

선형: 직선의 영역을 선형영역
비선형: 곡선의 영역을 비선형영역

■ 다층퍼셉트론(Multi layer perceptron)
- 단층퍼셉트론은 XOR게이트를 표현할 수 없었다.
- 즉, 단층퍼셉트론은 비선형영역을 분리할 수 없다. 
- 기존(OR, NAND, AND)게이트를 조합하여 층을 쌓으면 XOR게이트를 구현할 수 있다. 

XOR(0,0) = 0
XOR(0,1) = 1
XOR(1,0) = 1
XOR(1,1) = 0

def XOR(x1, x2):
  s1 = OR(x1,x2)
  s2 = NAND(x1, x2)
  y = AND(s1, s2)
  return y

XOR(0,0) 
XOR(0,1)
XOR(1,0)
XOR(1,1)

- 미분을 통해서(기울기 조정) 오차값을 줄이는 작업을 해야 한다. 
- y= ax + b라 할때, 은닉층 , weight(a) , bias 값(b) 를 해서 비선형 문제를 해결함 


