# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 09:55:45 2018

@author: stu
"""

▣ SVM (Support Vector Machine)
- 기계학습 분야 중 하나로 패턴 인식, 자료분석을 위한 지도학습모델이다. 
- 지도학습은 미리 답을 주고 학습을 시킨다. (종속변수의 여부: 유)
- 비지도학습은 답을 미리주지 않고 학습을 시킨다. (종속변수의 여부: 무)
- 분류와 회귀분석을 위해 사용된다.
- 두 카테고리 중 어느 하나에 속한 데이터의 집합이 주어졌을 때 새로운 데이터는 어느 카테고리에 속할지 판단하는 기준으로 가장 큰 폭을 가진 경계를 찾는 알고리즘 
- 선형분류 뿐 아니라 비선형 분류도 가능하다 (kernel: svm의 장점: linear뿐만 아니라 non-linear도 가능)
- 모델을 만들 때 고려해야할 파라미터가 많지 않다. 
- 적은양의 데이터로 모델을 만들 수 있다. 
- 딥러닝이 이전에는 분류 모형중에서 기술적으로 가장 진보된 모형으로 평가되었다. 


cf. 추가 그림 설명> wx+b 가 default로 사용된다. 
맨하튼 거리, 유클리드 거리를 통해 거리 계산 (일반적으로 맨하튼 거리 계산 사용)
a집합의 마지막 카테고리된 a'와 b집합의 마지막 카테고리리 된 b' 사이의 선을 긋고, 
a집합의 마지막 카테고리 a'를 support vector라 하고 이를 기준으로 선을 긋고, 이쪽을 (+)로
b집합의 마지막 카테고리 b'를 support vector라 하고 이를 기준으로 선을 긋는다, 이쪽을 (-)로 한다. 
a'와 b'사이를 margin이라고 한다. margin을 크게 잡으면 모호성이 떨어짐으로 margin이 클 수록 좋다.
집합사이의 세개를 잡아서 삼각형을 만들어 삼각함수를 사용해 거리계산을 한다. 

# =============================================================================

■ 실습

□ iris data 가지고 svm  
#Version 1 
import pandas as pd 
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split

iris = pd.read_csv("c:/data/iris.csv")

#꼭 컬럼이름 아니어도 loc, ix를 사용해서 index를 사용할 수도 있다.
iris_data = iris[["SepalLength", "SepalWidth", "PetalLength","PetalWidth"]]
iris_label = iris["Name"]

#sklearn에서 제공하는 method이용하기 
train_data, test_data, train_label, test_label = train_test_split(iris_data, iris_label, test_size=0.2)

# 모델만들기
iris_model = svm.SVC(kernel='linear')

# 모델에 train data를 fit하기
iris_model.fit(train_data, train_label)

# 예측하기
iris_pred = iris_model.predict(test_data)

# 정답률 확인하기
ac_score = metrics.accuracy_score(test_label, iris_pred)
print("정답률 :",ac_score)

#직접 data넣어 predict해보기 
iris_model.predict([[6.0,2.9,4.5,1.5]]) #Out[30]: array(['Iris-versicolor'], dtype=object)
iris_model.predict([[3.0,1.9,2.5,0.5]])[0]  #Out[31]: 'Iris-setosa'


#Version 2
#from sklearn.svm import LinearSVC 로 모델 만들기
import pandas as pd
from sklearn.svm import LinearSVC

iris_model = LinearSVC()
iris_model.fit(train_data, train_label)
iris_pred = iris_model.predict(test_data)
ac_score = metrics.accuracy_score(test_label, iris_pred)
print("정답률 :",ac_score)
iris_model.predict([[6.0,2.9,4.5,1.5]]) 
iris_model.predict([[3.0,1.9,2.5,0.5]])[0]

# =============================================================================
□ bmi data 가지고 svm 돌리기

#= 본데이터만 사용해서 svm 
bmi = pd.read_csv("c:/data/bmi.csv")

bmi_data = bmi.ix[:,0:2]
bmi_label = bmi.ix[:,2]

train_data, test_data, train_label, test_label = train_test_split(bmi_data, bmi_label, test_size=0.2)

bmi_model = LinearSVC()
bmi_model.fit(train_data, train_label)
bmi_pred = bmi_model.predict(test_data)
ac_score = metrics.accuracy_score(test_label, bmi_pred)
print("정답률 :",ac_score)

#= 정규화 작업 후 svm :0~1사이의 데이터를 가지고 
키 최대값 : 200, 몸무게 최대값: 100이라고 가정하고
df = pd.read_csv("c:/data/bmi.csv")
label = df['label']
w = df["weight"]/100
h = df["height"]/200

wh = pd.concat([w,h],axis=1)

train_data, test_data, train_label, test_label = train_test_split(wh, label, test_size=0.2)

#kernel을 쓰지 않으면 kernel="linear"가 기본값임
bmi_model = svm.SVC()
bmi_model.fit(train_data,train_label)
bmi_pred = bmi_model.predict(test_data)

ac_score = metrics.accuracy_score(test_label, bmi_pred)
print("정답률 :", ac_score)

#첫번째 열: weight, 두번째 열:heihgt
bmi_pred = bmi_model.predict([[71/100, 178/200]])


# ============
import matplotlib.pyplot as plt
import pandas as pd
#특정 컬럼을 label로 한번에 만들기: 어떤 컬럼을 label로 만들건지에 따라 index_col=2처럼, index_col에 해당 col 번호를 넣어 주면 된다. 
df = pd.read_csv("c:/data/bmi.csv", index_col=2)

# 처음 데이터 볼때 도통 이해가 되지 않으면 다음과 같이 그림을 그려 전체 분포도를 살펴보는 것도 좋은 방법이다. 
# fig~ ax.legned(loc=1)까지 한번에 실행하기

#==========
# 그림객체 선언
fig = plt.figure()
ax = fig.add_subplot(1,1,1)

# sub객체 선언  /(lbl, color)는 형식매개변수
def scatter(lbl, color):
    b = df.loc[lbl]
    ax.scatter(b['weight'], b['height'], c=color, label=lbl)

scatter('fat', 'red')
scatter('normal', 'yellow')
scatter('thin', 'purple')
ax.legend(loc=1)

#============
# fig 저장하기
plt.savefig("c:/data/bmi.jpg")



# =============================================================================
iris_svm_kernels.txt 파일
- 바로 load를 사용해서 파일을 불러들일 수 없다. 
- pandas로 불러들이되 np.array로 array로 사용해서 바꿔야한다. (왜냐하면 이름에 문자타입으로 되어있어서)


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import svm
from sklearn.model_selection import train_test_split
#%matplotlib inline
csv = pd.read_csv('c:/data/iris.csv')
X =  csv[["SepalLength","SepalWidth"]]
y = csv["Name"]
X = np.array(X)
# 종류가 적을 때는 dictionary를 사용하여 다음과 같이 바꿀 수 있다.
bclass = {"Iris-setosa": 0, "Iris-virginica": 1, "Iris-versicolor":2}
# 문자를 숫자로, 숫자를 문자로 바꿀 수 있다. 
y = y.apply(lambda x : bclass[x])
y = np.array(y)


def plotSVC(title):
    x_min, x_max = X[:, 0].min()- 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min()- 1, X[:, 1].max() + 1
    h = (x_max / x_min)/100
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
    np.arange(y_min, y_max, h))
    plt.subplot(1, 1, 1)
    Z = svc.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    plt.contourf(xx, yy, Z, cmap=plt.cm.Paired, alpha=0.8)
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Paired)
    plt.xlabel('Sepal length')
    plt.ylabel('Sepal width')
    plt.xlim(xx.min(), xx.max())
    plt.title(title)
    plt.show()
 
# linear 분류시 이상치도 같이 분류 되는 경우가 있다. 그럴경우 rbf커널(비선형기법)을 사용해서 linear를 굴곡지도록 하여 분류되도록한다. (svm의 장점)
kernels = ['linear', 'rbf']
for kernel in kernels:
    svc = svm.SVC(kernel=kernel).fit(X, y)
    plotSVC('kernel=' + str(kernel))


# gamma는 가중치를 조정 -> gamma 를 통해 직선 구간이 굴곡이 생길 수 있다. -> 비선형으로 분류시에는 gamma를 사용하여 가중치를 줘야한다. gamma를 주지 않으면 kernel값을 줄지라도 잘 분류가 되지 않을 수 있다. 
# 데이터 포인트 사이의 거리는 가우시안 커널에 의해 계산된다 (유클리드 거리 계산법에 감마값에 따라 가중치를 두어 넓게, 좁게 조절이 된다.)
# gamma는 가우시안 커널의 폭을 제어하는 매개변수 
gammas = [0.1, 1, 10, 100]
for gamma in gammas:
   svc = svm.SVC(kernel='rbf', gamma=gamma).fit(X, y)
   plotSVC('gamma=' + str(gamma))


# cf. 
# kmeans - 비지도 학습
# svm - 지도학습 (knn)
   
