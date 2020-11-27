# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 09:46:09 2018

@author: stu
"""
# =============================================================================
# [����199] ���赥���͸� �̿��ؼ� ����ῡ ���� ������ �ִ� ���������� �������� Ȯ���ϼ���.
# =============================================================================
import statsmodels.api as sm
import pandas as pd

df = pd.read_csv("c:/data/insurance.csv")


#���Ӻ���
charges = df.ix[:,-1]

#��������

df.head()
## 
cols = ['age','bmi','children']

##one-hot encoding: sex, smoker, region
dummy_sex = pd.get_dummies(df['sex'], prefix='sex')
dummy_smoker = pd.get_dummies(df['smoker'], prefix='smoker')
dummy_region = pd.get_dummies(df['region'], prefix='region')

#data ��ġ�� 
data = df[cols].join(dummy_sex)
data = data.join(dummy_smoker)
data = data.join(dummy_region)

#null �� Ȯ���ϱ�
data.isnull().sum()

#
data1 = data.join(charges)
data1.isnull().sum()


#�������� �÷�
train_cols = data.columns

#logisitic regression: ValueError: endog must be in the unit interval.
logit = sm.Logit(df['charges'],)

logit = sm.Logit(data1['charges'], data1.ix[:,:-1])

# =============================================================================

import math
from scipy import stats

#���� ȸ�� ���� 
#���� ���������� �ϳ��� linregression 
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



#ȸ�͸��� �����  - ����ȸ�͸���
from sklearn import linear_model

#�� �����
reg = linear_model.LinearRegression()

#fit�ϱ�  (����ȸ�ͺм�)
reg.fit(data, charges)

# �� ������ ���� ����(reg.coef_) , ����(intercept_) Ȯ���ϱ�
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

#������: ���� �������θ� Ȯ�ΰ��� (����ǥ��)
cor(insurance[c("age","bmi","children","charges")])
# > cor(insurance[c("age","bmi","children","charges")])
#               age       bmi   children    charges
# age      1.0000000 0.1092719 0.04246900 0.29900819
# bmi      0.1092719 1.0000000 0.01275890 0.19834097
# children 0.0424690 0.0127589 1.00000000 0.06799823
# charges  0.2990082 0.1983410 0.06799823 1.00000000

#�ð�ȭ
install.packages("psych")
library(psych)

pairs.panels(insurance[c("age","bmi","children","charges")])
#�ڱ��ڽ��� �κп����� �������� ������׷����� �׷��� 

#����ȸ�ͺм����� ����
ins_model = lm(charges~., data=insurance)
ins_model
#����ῡ ������ �� �� �ִ� ��Ұ� �ȴ�. smokeryes�� ���� ������ �ش�. (���� ���� �� ��ŭ ������ �ش�.)
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
# �ΰ�����  
# =============================================================================

�� �ΰ����� <- �ӽŷ��� <- �Ű��(������)

�� �ۼ�Ʈ��(perceptron)
- �ΰ�����(�ΰ������� ���� �Ű漼��)
- 1957�⿡ ���� �˰����� 
- ����ũ ��������Ʈ�� �ۼ�Ʈ�� �˰������� �����ߴ�. 
- �ۼ�Ʈ���� ������(�Ű��)�� ���
- �ټ��� ��ȣ�� �Է¹޾� �ϳ��� ��ȣ�� ����Ѵ�. 
- ��ȣ�� �帧�� ǥ���� �� �ΰ��� ���� ���´�. 
- 0: ��ȣ�� �帣�� �ʴ´�. 
- 1: ��ȣ�� �帥��. 

�� �ۼ�Ʈ�� ����
x: �Է°�(�Է½�ȣ) 
w: weight ����ġ
��: theta �Ӱ谪
y: ���

y = 0 w1 * x1 + w2 * x2 <= ��  (�Է°��� ����ġ���� ����� ��� �Ӱ谪���� �۰ų� ���� ��� ��°��� zero�� ����Ѵ�.)
y = 1 w1 * x1 + w2 * x2 > ��  

w1 * x1 + w2 * x2 ����  ��(�Ӱ谪) ������ ���� 0�� ����ϰ� �Ӱ谪 ���� Ŭ���� 1�� ����Ѵ�. 

�� ����ȸ��
��ǻ�ʹ� �ΰ��� �����а� 0,1�� �Է��ؼ� �ϳ��� ���� ����ϴ� ȸ�ΰ� �� ��������µ� �� ȸ�θ� gate(����Ʈ)��� �Ѵ�. 

�� AND����Ʈ
x1      x2      y
------------------
0       0       0
0       1       0
1       0       0
1       1       1

�� AND����Ʈ�� �ۼ�Ʈ������ ǥ��
y = 0 w1 * x1 + w2 * x2 <= �� 
y = 1 w1 * x1 + w2 * x2 > ��  

w1 = 0.5 , w2 = 0.5 , �� = 0.7

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

�� OR����Ʈ
x1      x2      y
------------------
0       0       0
0       1       1
1       0       1
1       1       1


�� OR����Ʈ�� �ۼ�Ʈ������ ǥ��
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
#�Ӱ谪�� 0.7�̶�� ������ OR����Ʈ ���� ������ �ʱ� ������ �Ӱ谪�� �����ϵ� ����ġ�� �����Ͽ��� OR����Ʈ ���� ���´�. 
#����� �Ӱ谪�� 0.4�� ������
#���࿡ �Ӱ谪�� �����̴ٰ� �ϸ� Weight���� �����ؾ��Ѵ�. 
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

�� NAND(NOT AND)����Ʈ�� �ۼ�Ʈ������ ǥ��
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

�� XOR (eXclusive OR) ��Ÿ��������
x1      x2      y
------------------
0       0       0
1       0       1
0       1       1
1       1       0

x1�� x�� ��� ������ 1�϶��� 1�� ����ϴ� ��Ÿ������ȸ���̴�.
�� �ۼ�Ʈ���� XOR  ����Ʈ�� ������ �� ����. 

�� �ۼ�Ʈ���� �Ѱ�
- ���� �ϳ��� XOR����Ʈ�� ����� ������ �� ����.
- ���Ʈ��(�����ۼ�Ʈ��)�� �����ϳ��� ���� ������ ǥ���� �� �ִ� �Ѱ谡 �ִ�. 
- �ν�Ű�� ���� �ۼ�Ʈ���� �������� �����޴µ� XOR�з��� ���Ѵٴ� �������� �����ϰ� �ΰ������� �ܿ�Ⱑ ���۵Ǿ���. 


�� �����ۼ�Ʈ��(Multi layer perceptron)
x1      x2      OR    NAND     AND
----------------------------------------
0       0       0       1       0
1       0       1       1       1
0       1       1       1       1
1       1       1       0       0

���� �ۼ�Ʈ��(OR, NAND�� �����)���� AND���� �۾��� �ϸ� XOR�� ���� �� �ִ�.
1. x1�� x2�� ���� OR���� ����
2. x1�� x2�� ���� NAND���� ����
3. �߰��� ���� OR�� NAND�� AND��� �۾��� ��

����: ������ ������ ��������
����: ��� ������ ��������

�� �����ۼ�Ʈ��(Multi layer perceptron)
- �����ۼ�Ʈ���� XOR����Ʈ�� ǥ���� �� ������.
- ��, �����ۼ�Ʈ���� ���������� �и��� �� ����. 
- ����(OR, NAND, AND)����Ʈ�� �����Ͽ� ���� ������ XOR����Ʈ�� ������ �� �ִ�. 

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

- �̺��� ���ؼ�(���� ����) �������� ���̴� �۾��� �ؾ� �Ѵ�. 
- y= ax + b�� �Ҷ�, ������ , weight(a) , bias ��(b) �� �ؼ� ���� ������ �ذ��� 

