# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 09:51:50 2018

@author: stu
"""
#Graphviz2.38
http://www.graphviz.org

물리적 주소
C:\Program Files (x86)\Graphviz2.38\bin

#시스템 환경변수에 path를 설정해야함 
내컴퓨터> 속성> 고급시스템설정> 환경변수 > path > 편집 > 시스템 변수값path: 맨끝 ;C:\Program Files (x86)\Graphviz2.38\bin

#Anaconda Prompt
pip install pydotplus

pip install graphviz


#spyder
import pydotplus
import graphviz
from sklearn.tree import export_graphviz 
from IPython.display import Image 

import pandas as pd

# =============================================================================
# # 10/22/Fri
# #붓꽃 품종 분류
# 붓꽃의 꽃잎(petal), 꽃받침(sepal)의 폭, 길이를 측정하여 품종을 예측
# 붓꽃의 품종은 150종류 이상있고 크게 3가지로 분류된다.
# setosa, versicolor, virginica
# 
# dataset = pd.read_csv("c:/data/iris.csv")
# dataset.head()
# x = dataset.drop('Name', axis=1)
# y = dataset['Name']
# x
# y   #y: label값 
# 
# from sklearn.model_selection import train_test_split
# x_train, x_test, y_train, y_test = train_test_split(x,y,test_size =0.20)
# x_train
# x_test
# y_train
# y_test 
# 
# from sklearn.tree import DecisionTreeClassifier
# classifier = DecisionTreeClassifier()
# classifier.fit(x_train, y_train)
# y_pred = classifier.predict(x_test)
# y_pred #품종정보 출력
# 
# from sklearn.metrics import classification_report
# print(classification_report(y_test, y_pred))
# =============================================================================

#위의모형에 대해 graph를 그리기
dot_data = export_graphviz(classifier, out_file=None, feature_names=['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth'], class_names=['Iris-setosa', 'Iris-virginica', 'Iris-virsicolor'], filled=True, rounded =True, special_characters=True)
#feature_names에 대해서는 list 변수로 넣는다. (넣지않으면 x로 y나옴 )
#class_name에 (넣지 않으면 0,1,2.로 나옴)
#filled =True
#rounded= True, 그래프 모양 
#special_characters=True

graph = pydotplus.graph_from_dot_data(dot_data)
Image(graph.create_png())
Image(graph.create_jpg())

# PetalLength
# 의사결정트리에서 gini값이 기본임 
# 의사결정트리에서 criterion을 "entropy"로 , max_depth는 가지치기의 개수라고 생각하면 됨
classifier = DecisionTreeClassifier(criterion="entropy", max_depth=2) 
classifier.fit(x_train, y_train)

# =============================================================================

import pandas as pd
titanic = pd.read_csv("c:/data/titanic.csv")
titanic
titanic.head()

#survived: 목표변수 -> 생존여부 (0:사망, 1:생존) , 종속변수
#나머지 변수들: 독립변수 
#sklearn에 들어갈 독립변수들은 문자변수가 사용될 수 없고, 숫자변수만 사용가능
    #gender -> 0과 1로 변경작업 필요(on-hot-encoding)

#여성은 0, 남성은 1로 encoding (조건제어문 if를 사용하지 않고도 .map과 dictionary형을 통해 값을 바꿀 수 있다.)
titanic['gender'] = titanic.gender.map({'female':0, 'male':1})

#Null값 체크하기 - 모든 컬럼의
titanic.isnull()

#모든 NaN이 하나라도 있으면 True로 return함
titanic.isnull().any()

#NaN의 갯수 정보 보기 -> True에 해당하는 개수 정보 세기
titanic.isnull().sum()

# age의 NaN의 개수 
titanic.isnull().sum()['age']
titanic['age'].isnull().sum()

#전체 NaN의 sum
titanic.isnull().sum().sum()

#age의 NaN값만 뽑아내기 
titanic[titanic['age'].isnull()]

#NaN은 보통 중앙값으로 대체한다. (평균으로 대체하기도 함)

#fillna : Nan 채우기 fillna(값, inplace=True) #inplace=True는 바로 적용시키기 / 옵션을 선택하지 않으면 미리보기
titanic.age.fillna(titanic.age.median())
titanic.age.fillna(titanic.age.median(), inplace =True)

titanic['age'].isnull

#
titanic.head()

#embarked 탑승항구
C(Cherbourg), Q(Queenstown), S(Southampton)

#embarked 탑승항구의 변수를 dummy변수를 만들고자 할 때  - (on-hot-encoding사용: 0과 1로)
    #(on-hot-encoding: 독립변수가 종속변수에 영향을 주는지에 대해 체크할 때 하는 encoding) 
    #C(Cherbourg)이 들어간 것은 1, 아닌 것은 0
    #Q(Queenstown)이 들어간 것은 1, 아닌 것은 0
    #S(Southampton)이 들어간 것은 1, 아닌 것은 0
#pandas의 기능 ->위의 탑승학구가 세개의 독립변수로 만들어짐
embarked_dummies = pd.get_dummies(titanic.embarked, prefix="embarked")
embarked_dummies 
   #embarked_dummies의 세개의 변수가 생김 (dataframe으로 만들어짐)

embarked_dummies.drop(embarked_dummies.columns[0], axis=1, inplace=True)
embarked_dummies 

#기존의 emarked와 새 독립변수를 같은 dataframe에 합치기 #axis=0는 위아래로 합침
titanic = pd.concat([titanic, embarked_dummies], axis=1)

titanic 

#컬럼정보확인
titanic.columns

#영향을 주는 독립변수를 따로 모아서 데이터프레임을 별도로 지정하기 
feature_cols = ['pclass','gender','age','embarked_Q', 'embarked_S']
titanic[feature_cols]

x = titanic[feature_cols]
x.head()

#종속변수
y = titanic.survived

from sklearn.tree import DecisionTreeClassifier
 
model = DecisionTreeClassifier(criterion='gini', max_depth=3) #criterion='gini'는 default값 
model = DecisionTreeClassifier(criterion='entropy', max_depth=3) 
model.fit(x,y)

# 중요성이 높은 속성들 -> gender, plcass, age, embarked_S ( embarked_Q는 전혀 영향을 주지 않음) -> 다음의 순수로 의사결정트리 
pd.DataFrame({'feature': feature_cols, 'importance': model.feature_importances_})

classifier = DecisionTreeClassifier()
classifier.fit(x,y)

dot_data = export_graphviz(classifier, out_file=None, feature_names=['pclass','gender','age','embarked_Q', 'embarked_S'], class_names=[], filled=True, rounded =True, special_characters=True)


graph = pydotplus.graph_from_dot_data(dot_data)
Image(graph.create_png())


'''
#######R##############

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

expect <- predict(partymodel, test[1:4]) #종속변수를 넣지 말아야하므로 test[1:]
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