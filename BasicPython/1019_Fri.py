# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 10:01:31 2018

@author: stu
"""
정보이론(information theory)

information 
degree of suprise (놀람의 정도)

■ 엔트로피(entropy)
- 무질서
- 열역학의 제 2법칙
- entropy는 정보량의 평균 

- -Σp * log2p
    (- 테니스 유무에 대한 예/아니요의 확률을 기준으로)
        - "예" 확룔 9/14
        - 9/14 * log2(9/14)
        - "아니요" 확률 5/14
        - 5/14 * log2(5/14)
        - log 값을 구하기 위해 import numpy as np
        -9/14 * np.log2(9/14) - 5/14 * np.log2(5/14)
        Out[3]: 0.9402859586706311
    (- 습도 유무에 대한 예/아니요의 확률을 기준으로)

        테니스 유무
습도    아니요   예
높음     4       3     7
보통     1       6     7
         5       9     14
      
import numpy as np
엔트로피(전체)        
-9/14 * np.log2(9/14) - 5/14 * np.log2(5/14)
Out[6]: 0.9402859586706311
엔트로피(높음)
-3/7*np.log2(3/7)-4/7*np.log2(4/7)
Out[7]: 0.9852281360342515
엔트로피(보통)
-6/7*np.log2(6/7)-1/7*np.log2(1/7)
Out[8]: 0.5916727785823275       

정보이득 = 전체엔트로피 - 7/14*엔트로피(높음) - 7/14*엔트로피(보통) 
         = 0.94 - (7/14)*0.98 - (7/14)*0.59
         = 0.154    Out[9]: 0.15499999999999997



모든 변수에 관한 정보 이득값을 계산하고 가장 높은 정보이득값을 가진 변수를 선택한다. 

(테니스 유무는 고정이며 각각의 컬럼과 정보이득값을 구한다) -> 정보이득이 큰 값을 기준으로 의사결정 트리에 먼저 사용된다. 
 
import padnas as pd
df = pd.read_csv("c:/data/tree.csv")
#바람
        테니스 유무
바람    아니요   예
강함     3       3     6
약함     2       6     8
         5       9     14
정보이득(바람) = 전체엔트로피 - 6/14*엔트로피(강함)-8/14*엔트로피(약함)
#              = 0.94 - (6/14)*0.98 - (8/14)*0.59
#              = 0.18  Out[20]: 0.18285714285714288

엔트로피(강함)
-3/6*np.log2(3/6)-3/6*np.log2(3/6)
Out[26]: 1.0
엔트로피(보통)
-2/8*np.log2(2/8)-6/8*np.log2(6/8)
Out[27]: 0.8112781244591328     

cf. 브라질vs중국 축구 브라질 vs.프랑스 축구에 대한 의사결정트리 순위 구하기
브라질이 이길 확률의 놀라움 정도
-np.log(0.99) = 0.01        Out[22]: 0.01005033585350145
중국이 이길 확률의 놀라움 정도
-np.log(0.01) = 4.6         Out[24]: 4.605170185988091
0.99*-np.log(0.99) + 0.01*-np.log(0.01) = 0.05 Out[31]: 0.056001534354847345

-브라질이 이길 확률의 놀라움의 정도
-np.log(0.5) = 0.69     Out[36]: 0.6931471805599453
-프랑스가 이길 확률의 놀라움의 정도 
-np.log(0.5) = 0.69     Out[36]: 0.6931471805599453
0.5*-np.log(0.5) + 0.5*-np.log(0.5) = 0.69  Out[35]: 0.6931471805599453

-정보의 이득값에 따라 무엇을 먼저 의사결정트리에 넣을 지 순위를 정한다. 
0.05 < 0.69


■ 지니지수
1 - Σp²


#습도 
         테니스 유무
습도    아니요   예
높음     4       3     7
보통     1       6     7
         5       9     14

습도(높음)의 지니지수 
1 - pow(3/7, 2) - pow(4/7, 2) = 0.49    Out[37]: 0.489795918367347
습도(낮음)의 지니지수 
1 - pow(6/7, 2) - pow(1/7, 2) = 0.24    Out[38]: 0.24489795918367355

습도 지니 기대값
= (7/14) * 0.49 + (7/14) * 0.24 = 0.365   Out[39]: 0.365


#바람
        테니스 유무
바람    아니요   예
강함     3       3     6
약함     2       6     8
         5       9     14
바람(강함)의 지니지수 
1 - pow(3/6, 2) - pow(3/6, 2) = 0.5    Out[40]: 0.5
바람(약함)의 지니지수 
1 - pow(6/8, 2) - pow(2/8, 2) = 0.375   Out[41]: 0.375   

바람 지니 기대값
= (6/14)*0.5 + (8/14)*0.38 = 0.43     Out[42]: 0.4314285714285714

■ 지니기대값과 최적 변수: 모든 변수에 관해 지니 기대값을 계산하고 최소 기대값을 가진 변수를 최적 변수로 선택한다. 
  습도  바람
0.365 < 0.43  
-> 습도를 최적 변수로 선택한다. 

■ 
cf. 카이제곱, 자유도 1 
습도 카이제곱: 2.8      (p값 0.09정도)
바람 카이제곱: 0.94     (p값 0.4~5정도)

카이제곱과 자유도를 통해 p값을 찾아 p값이 최소값인 값을 찾아 최적변수로 선택한다. 
습도     바람
0.09 < 0.4~0.5


# cf. python에서는 카이제곱에 대한 method는 있으나 s
# cf. R은 table을 통해 교차테이블을 만들고, summary를 하면 자유도, p값, 분포도를 모두 출력해준다. 

# =============================================================================
#
# =============================================================================

import pandas as pd

#붓꽃 품종 분류
붓꽃의 꽃잎(petal), 꽃받침(sepal)의 폭, 길이를 측정하여 품종을 예측
붓꽃의 품종은 150종류 이상있고 크게 3가지로 분류된다.
setosa, versicolor, virginica

dataset = pd.read_csv("c:/data/iris.csv")
dataset.head()
x = dataset.drop('Name', axis=1)
y = dataset['Name']
x
y   #y: label값 

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size =0.20)
x_train
x_test
y_train
y_test 

from sklearn.tree import DecisionTreeClassifier
classifier = DecisionTreeClassifier()
classifier.fit(x_train, y_train)
y_pred = classifier.predict(x_test)
y_pred #품종정보 출력

from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))

#5.1, 3.5, 1.4, 0.2, Iris-setosa
classifier.predict([[5.1, 3.5, 1.4, 0.2,]])
Out[78]: array(['Iris-setosa'], dtype=object)
classifier.predict([[5.1, 3.5, 1.4, 0.2,]])[0]
Out[79]: 'Iris-setosa'

#5.9, 3.0, 5.1, 1.8
classifier.predict([[5.9,3.0,5.1,1.8]])
Out[80]: array(['Iris-virginica'], dtype=object)
classifier.predict([[5.9,3.0,5.1,1.8]])[0]
Out[81]: 'Iris-virginica'

#6.7, 3.1, 4.7, 1.5
classifier.predict([[6.7, 3.1, 4.7, 1.5]])[0]
Out[82]: array(['Iris-versicolor'], dtype=object)
classifier.predict([[6.7, 3.1, 4.7, 1.5]])[0]
Out[83]: 'Iris-versicolor'

#
classifier.predict([[6.7, 3.1, 4.7, 1.5]])[0]

classifier.score(x_train, y_train)  #학습 데이터셋 정확도
classifier.score(x_test, y_test)    #검증용 데이터셋 정확도

#dataset의 중요성 

#dataset 안에 있는 name열만 빼놓고 예측해야 함 
label = classifier.predict(dataset.ix[:,:4])
dataset.ix[:,:4] == pd.Series(label) #데이터형을 일치시키기 Series 
#label은 현재 numpy의 array형식 

#잘못된 예측된 값
dataset[dataset.ix[:,4] != pd.Series(label)]

#
label[dataset.ix[:,4] != pd.Series(label)]

##트레이닝 셋만 가지고 학습이 잘 되어있는지 확인하기    
#dataset[dataset.ix[:,4] != pd.Series(label)]
#
##데이터 셋을 트레이닝 데이터만 가지고 해보기 


#
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size =0.10)

from sklearn.tree import DecisionTreeClassifier
classifier = DecisionTreeClassifier()
classifier.fit(x_train, y_train)
y_pred = classifier.predict(x_test)

from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))


''' R 
iris = read.csv("c:/data/iris.csv")

#iris structure
str(iris)

#r에서는 주의해야할 사항
-문자로 불러들여 목표변수를 설정하면 에러가 난다. 

summary(iris)

#정규화 함수
normalize <- function(x){return((x-min(x))/(max(x)-min(x)))}
#정규화 함수를 통해서 범주화는 0~1에서 사이의 값으로 보여준다. - 단위를 맞추기 위해
#cf.학습이 잘 안되면 정규화 작업을 했는지 한번 확인해 본다.
normalize(c(1,2,3,4,5))
normalize(c(10,20,30,40,50))

normalize(c(12,24,35,47,59))

#컬럼에 대한 slicing, normalize함수를 이용해서 
iris_n <- as.data.frame(lapply(iris[1:4], normalize))

summary(iris_n)

#빈도값 확인: 각각의 건수를 확인하기 
table(iris$Name)

# training set:70 , test set:30으로 표본추출할 때 인덱싱이 필요하다. -> sample method 사용하기

#2: indexing 번호 1,2로 구성#replace=True -> 복원추출 #prob(0.7,0.3)
#cf. sample(3, nrow(iris), replace=True, prob=c(0.6, 0.3, 0.1))
set.seed(1234) #할 때마다 random값이 변화되는 것을 방지하기 위해 사용
iris_sample <- sample(2,nrow(iris), replace=TRUE,prob = c(0.7,0.3))
iris_training <-iris[iris_sample==1, 1:5]
iris_test <- iris[iris_sample==2, 1:5]

#붓꽃이 균일하게 잘 분리되어 있는지 확인하기
nrow(iris_training)
table(iris_training$Name)
table(iris_test$Name)



#의사결정트리 패키지 설치
install.packages("tree")
library(tree)
help(tree)

#step1 :tree형성(Growing tree)
#tree(종속변수~독립변수1+독립변수2+..., data=변수)
#tree(종속변수~.,data=변수) .은 독립변수를 다 이용하겠음
treemodel <- tree(Name~., data=iris_training)
treemodel 
#treemodel 출력값 -> 지니계수에 따르면 petal length가 가장 영향을 많이 끼치는 독립변수임 
    node), split, n, deviance, yval, (yprob)
    * denotes terminal node
    
    1) root 99 217.500 Iris-virginica ( 0.33333 0.32323 0.34343 )  
    2) PetalLength < 2.6 33   0.000 Iris-setosa ( 1.00000 0.00000 0.00000 ) *
      3) PetalLength > 2.6 66  91.430 Iris-virginica ( 0.00000 0.48485 0.51515 )  
    6) PetalWidth < 1.75 35  24.880 Iris-versicolor ( 0.00000 0.88571 0.11429 )  
    12) PetalLength < 4.9 30   8.769 Iris-versicolor ( 0.00000 0.96667 0.03333 )  
    24) SepalLength < 5.3 5   5.004 Iris-versicolor ( 0.00000 0.80000 0.20000 ) *
      25) SepalLength > 5.3 25   0.000 Iris-versicolor ( 0.00000 1.00000 0.00000 ) *
      13) PetalLength > 4.9 5   6.730 Iris-virginica ( 0.00000 0.40000 0.60000 ) *
      7) PetalWidth > 1.75 31   8.835 Iris-virginica ( 0.00000 0.03226 0.96774 )  
    14) SepalLength < 6.15 5   5.004 Iris-virginica ( 0.00000 0.20000 0.80000 ) *
      15) SepalLength > 6.15 26   0.000 Iris-virginica ( 0.00000 0.00000 1.00000 ) *

#의사결정트리 그림그리기
plot(treemodel)
text(treemodel)

#의사결정트리 스텝
step1 :tree형성(Growing tree) - 독립변수들로 키워나가는 작업을 한다. 너무 많이 키워나가면 과적합(overfitting)이 발생한다.
step2 :tree 가지치기(pruning tree) - 과적합(overfitting)을 해결하기위해서 가지치기를 한다. 
step3 :최종모형 


#>step2 :tree 가지치기(pruning tree) - 과적합(overfitting)을 해결하기위해서 가지치기를 한다.
#tree가지치기  #FUN=prune 제공해주는 함수
cv <- cv.tree(treemodel, FUN=prune.misclass)
cv

#가지치기한 cv에서  #$k 의 값을 $size값에 대응시켜본다. inf는 = 6/  0 = 4 / 1= 3/ 2=27 / 1=33
cv값 = $k값 / 노드수 = $size값 
cv(cost complexity parameter) 복답도계수의 값이 최소가 되는 노드수를 선택
plot(cv)
# size=3 인 이상이후로 부터는 node 수를 더 많이 만들어도 값이 같기 때문에 그 이상이 되는 노드수는 과적합이라고 할 수 있다.


#step3: 최종모형
p <- prune.misclass(treemodel, best=3) #best=3  -> 3개노드
plot(p)
text(p)

#예측값
tree_pred <- predict(p, iris_test, type="class")
expect <- tree_pred

#test값
actual <- iris_test$Name

#test값과 예측값과 비교하기
data.frame(actual, expect)

#library(caret): 오분류하기 위한 교차표를 쉽게 만들어 주는 라이브러리
install.packages("caret")
library(caret)

#교차표가 만들어짐 
confusionMatrix(expect, actual)
  #reference: 실제범주 / prediction: 예측범주 
  #Confusion Matrix and Statistics

                      Reference
    Prediction        Iris-setosa Iris-versicolor Iris-virginica
    Iris-setosa              17               0              0
    Iris-versicolor           0              18              1  #오분류값
    Iris-virginica            0               0             15

    
str(iris)
#factor값의 값 확인하기 
levels(iris$Name)
table(iris$Name)

# createDataPartition: 목표변수를 균일하게 training값, test값을 나누기 (단순히 의사결정트리에서만 사용되는 것이 아니라 kNN에서도 사용될 수 있음)
iris_idx <- createDataPartition(iris$Name, p=0.8, list=FALSE) #list=FALSE: factor형으로 뽑기 -> 이렇게 지정하지 않으면 list로 값을 출력한다.
train <- iris[iris_idx,]
str(train)
nrow(train)
table(train$Name)

#test set만들기
test <- iris[-iris_idx,]
str(test)
nrow(test)
table(test$Name)

#다시 의사결정트리 만들기
treemodel <- tree(Name~., data=test)
treemodel
  #node), split, n, deviance, yval, (yprob)
  * denotes terminal node
  
  1) root 30 65.920 Iris-setosa ( 0.33333 0.33333 0.33333 )  
  2) PetalLength < 2.95 10  0.000 Iris-setosa ( 1.00000 0.00000 0.00000 ) *
    3) PetalLength > 2.95 20 27.730 Iris-versicolor ( 0.00000 0.50000 0.50000 )  
  6) PetalLength < 4.8 9  0.000 Iris-versicolor ( 0.00000 1.00000 0.00000 ) *
    7) PetalLength > 4.8 11  6.702 Iris-virginica ( 0.00000 0.09091 0.90909 )  
  14) SepalLength < 6.35 5  5.004 Iris-virginica ( 0.00000 0.20000 0.80000 ) *
    15) SepalLength > 6.35 6  0.000 Iris-virginica ( 0.00000 0.00000 1.00000 ) *  

plot(treemodel)
text(treemodel)


#rpart
install.packages(rpart)
library(rpart)
iris_rpart <- rpart(Name~., data=train, control=rpart.control(minsplit = 2))  #minsplit = 2 최소 split은 2개로 
iris_rpart  

  n= 120 #120개
  
  node), split, n, loss, yval, (yprob)
  * denotes terminal node
  
  1) root 120 80 Iris-setosa (0.33333333 0.33333333 0.33333333)  
  2) PetalLength< 2.45 40  0 Iris-setosa (1.00000000 0.00000000 0.00000000) *
    3) PetalLength>=2.45 80 40 Iris-versicolor (0.00000000 0.50000000 0.50000000)  
  6) PetalWidth< 1.65 39  1 Iris-versicolor (0.00000000 0.97435897 0.02564103)  
  12) PetalLength< 5.35 38  0 Iris-versicolor (0.00000000 1.00000000 0.00000000) *
    13) PetalLength>=5.35 1  0 Iris-virginica (0.00000000 0.00000000 1.00000000) *
    7) PetalWidth>=1.65 41  2 Iris-virginica (0.00000000 0.04878049 0.95121951) *

install.packages("rpart.plot")
library(rpart.plot)

#의사결정트리 그리기  
#step1
rpart.plot(iris_rpart)


#step2: cv값을 구하는 것처럼 cptable을 통해서 cp값을 sp
iris_rpart$cptable

오분류가 최소값이 되는 살펴보면서 결정하도록 한다. 그러나 이때 split이 너무 과하지 않게 되도록 결정한다. 이때 cptable을  참고한다. 
cp가 가장 작은 것: 0.01 ->  nsplit=3  -> error:0.0375  #error값에 큰 차이가 나지 않음
cp가 0.0125 -> nsplit=2  -> error -> error: 0.0250 

iris_prune <- prune(iris_rpart, cp=0.0125) #cp값 0.125를 기준으로 가지치기 
rpart.plot(iris_prune)

expect <- predict(iris_prune, test, type="class")
actual <- test$Name

confusionMatrix(expect, actual)
  Confusion Matrix and Statistics
  
  Reference
  Prediction        Iris-setosa Iris-versicolor Iris-virginica
  Iris-setosa              10               0              0
  Iris-versicolor           0              10              3 #오분류
  Iris-virginica            0               0              7
  
install.packages("rattle")
library(rattle)
rpart <- rpart(Name~., data=iris, method="class")
#rpart
  n= 150 
  
  node), split, n, loss, yval, (yprob)
  * denotes terminal node
  
  1) root 150 100 Iris-setosa (0.33333333 0.33333333 0.33333333)  
  2) PetalLength< 2.45 50   0 Iris-setosa (1.00000000 0.00000000 0.00000000) *
    3) PetalLength>=2.45 100  50 Iris-versicolor (0.00000000 0.50000000 0.50000000)  
  6) PetalWidth< 1.75 54   5 Iris-versicolor (0.00000000 0.90740741 0.09259259) *
    7) PetalWidth>=1.75 46   1 Iris-virginica (0.00000000 0.02173913 0.97826087) *

fancyRpartPlot(rpart, main= "iris")

##Rpart는 "카트"라는 알고리즘을 사용한다.  -> 카트라는 의사결정의 분류가 있는데, cart와 rpart가 있다. 
#Rpart는 ANOVA(분산분석)를 사용한다. 
#tree로 학습을 시킬 때 느리거나 오류율이 높다면 Rpart를 사용하는 것이 좋다. Rpart가 처리속도가 더 빠르고 설명변수는 Rpart가 더 잘 짜져있음

#party의 장점 : 가지치기를 하지 않아도 됨(tree와 Rpart는 가지치기를 step2에서 꼭 해줘야 함)
#p값을 이용함(p-test을 이용해서 수행)
#제약:독립변수가 31개 이상은 되지 않음 
install.packages("party")
library(party)

partymodel = ctree(Name~., data=train)
plot(partymodel)

expect <- predict(partymodel, test)
actual <- test$Name
confusionMatrix(expect, actual)

#의사결정트리를 고를 때는 tree, Rpart, party모두 한번씩 고려해서 잘나온 값을 사용한다. 
#tree, Rpart: 지니계수를 이용
#party: p-value를 사용 
#CART는 지니계수를 사용해서 회귀를 함
#C.ZERO : 

#cf. Tree algorithms: ID3, C4.5, C5.0 and CART 
http://scikit-learn.org/stable/modules/tree.html


'''


