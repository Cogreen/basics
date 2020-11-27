의사결정트리> 

C5.0: Entropy를 가지고 의사결정트리를 만듦 

신용모델의 아이디어는 채무불이행의 고위험에 있는 고객의 특성을 찾는 일이다. 

credit <- read.csv("c:/data/credit.csv")
str(credit)

default
  yes: 대출금 상환 안함
  no : 대출금 상환 

checking_balance: 예금계좌 
saving_balance: 적금계좌

대출신청자의 예금계좌 적금계좌의 예금 정도를 확인해서 예금액이 많을수록 대출이 안전하다는 가정할 수 있다.
  
table(credit$checking_balance)
table(credit$saving_balance)

#현재 고객들의 대출기간을 확인
#대출기간은 4달에서 72달까지 기간, 중앙값은 18, 평균은 20.9개월
summary(credit$months_loan_duration)

#대출금액(단위: 마르크)
summary(credit$amount)

#상환한 고객
table(credit$default)

#상환한 고객 비율로 보기 
prop.table(table(credit$default))

#미리 정해진 순열로 임의의 수를 설정하고 분석을 반복해도 똑같은 수를 얻게하려고 하는 방법
set.seed(12345)

train_idx <-sample(2, nrow(credit), prob=c(0.9,0.1),replace=T)

#indexing하기 
credit_train <- credit[train_idx==1,]
credit_test <- credit[train_idx==2,]

#어느정도 비율로 만들어졌는지 확인하기 (0.7:0.3 정도의 비율로)
prop.table(table(credit_train$default))
prop.table(table(credit_test$default))

#의사결정트리 알고리즘 중 c5.0알고리즘을 적용해서 예측모델을 생성해보자 
install.packages("C50")
library(C50)

#str 확인하기
str(credit_train)
#column의 개수 -> 마지막 컬럼이 종속변수이고, 나머지를 독립변수로 사용하기 위해 확인함
length(credit_train)

#credit_model 만들기: C5.0메소드 사용 -> 독립변수(credit_train[,-17]), 종속변수(credit_train[,17]) 순으로 적기
credit_model1 <- C5.0(credit_train[,-17], credit_train[,17]) 
credit_model1
summary(credit_model1)

#모델의 예측하고, test의 default값을 비교하기 
credit_result1 <- predict(credit_model1, credit_test[,-17])
#crosstable로 확인하기 (모델의 예측하고, test의 default값을 비교하기)
library(gmodels)
CrossTable(credit_test[,17], credit_result1) 

# Cell Contents
# |-------------------------|
#   |                       N |
#   | Chi-square contribution |
#   |           N / Row Total |
#   |           N / Col Total |
#   |         N / Table Total |
#   |-------------------------|
#   
#   
#   Total Observations in Table:  99 
# 
# 
# | credit_result 
# credit_test[, 17] |        no |       yes | Row Total | 
#   ------------------|-----------|-----------|-----------|
#   no |        56 |        11 |        67 | 
#   |     1.085 |     2.895 |           | 
#   |     0.836 |     0.164 |     0.677 | 
#   |     0.778 |     0.407 |           | 
#   |     0.566 |     0.111 |           | 
#   ------------------|-----------|-----------|-----------|
#   yes |        16 |        16 |        32 | 
#   |     2.273 |     6.061 |           | 
#   |     0.500 |     0.500 |     0.323 | 
#   |     0.222 |     0.593 |           | 
#   |     0.162 |     0.162 |           | 
#   ------------------|-----------|-----------|-----------|
#   Column Total |        72 |        27 |        99 | 
#   |     0.727 |     0.273 |           | 
#   ------------------|-----------|-----------|-----------|
# 

#CrossTable에서 잘못된 예측값을 찾아 오류율을 줄이는 작업을 해야함  


#boosting기법을 이용: credit_model2로 
# trials = 10: 오류율을 줄이기 위해 반복 10번을 수행함
credit_model2 <- C5.0(credit_train[,-17], credit_train[,17], trials = 10) 
#boosting 기법: boost확인하기 Number of boosting iterations: 10 
credit_model2
summary(credit_model2)

#모델의 예측하고, test의 default값을 비교하기 
credit_result2 <- predict(credit_model2, credit_test[,-17])
#crosstable로 확인하기 (모델의 예측하고, test의 default값을 비교하기)
library(gmodels)
CrossTable(credit_test[,17], credit_result2) 


#boosting기법에도 불구하고 여전히 오류율이 개선되지 않을 경우 앙상블(Ensembles)기법을 사용한다.
#앙상블(Ensembles)
  - 다양한 전문가로 팀을 만드는 유사한 원칙을 사용하는 메타학습접근법을 앙상블이라고 한다. 
  - 앙상블 기법은 다수의 약한 학습기를 합해 강한 하나의 학습기로 만드는 개념을 기반으로 한다. 
                                                    -> model1
                                                    -> model2
    * 훈련데이터 -> 할당함수(allocation function)   -> model3  -> 조합함수(combination Function) -> 앙상블모델
                                                    -> model4 
  - bagging(배깅) boostrap aggregating
  :트레이닝 데이터를 반복 추출하여 표본을 여러개 만든 후에 각 표본에 맞는 분류 모델을 표본수만큼 생성한 후에 각각에 분류 모델을 앙상블하는 방법 


# credit_train, credit_test를 기반으로 bagging을 돌리기 -> bagging에 필요한 library필요: ipred
install.packages("ipred")
library(ipred)

#default는 종속변수 , training data에서 25개의 모델을 만들기 위해 data를 뽑아냄, 모델을 만든 다음 가장 좋은 모델을 return해줌; (25개의 tree를 만들어 최적화해줄 것임-; 즉 오차율이 적은 모델을 제공함)
mybag <- bagging(default~., data=credit_train, nbagg=25)
mybag

#예측하기
credit_pred <-predict(mybag, credit_test[,-17])
table(credit_pred, credit_test$default)
# table에 
    # credit_pred no yes  #Error
    #         no  59  11  #no-yes:8 
    #         yes  8  21  #yes-no:11
library(gmodels)
CrossTable(credit_test[,17], credit_pred) 

#모델 확인하기
summary(mybag)

#독립변수 몇가지만 가지고 학습시켜보기(개인적 실습)


#오후시간에는 연관분석을 합니다 :D - 유사성단어 찾기 등에 사용

#연관규칙
#연관성분석(association analysis)이란
  - 대량의 데이터에 숨겨진 항목간의 연관규칙을 찾아내는 기법으로서 장바구니분석(market basket analysis)이라고도 한다.
  - 실제 연관성 분석: 월마트, 아마존닷컴 등 여러기업에서 다양한 마케팅 활동에 활용하고 있으며 더 나아가 사회네트워크 분석에도 활용할 수 있다. 
  - 시리얼과 우유와의 관계를 알아내는 대표적인 기계학습방법
  - support(지지도): 전체거래(transaction)중 연관성 규칙을 구성하는 항목들이 포함된 거래의 비율
  (cf. sql의 트랜젝션(transaction): 데이터를 변경하는 작업)
                  x에 대한 거래개수
  - support(x) = ------------------
                    전체거래 건수
  - 신뢰도(confidence): 조건이 발생했을 때 결과가 동시에 일어날 확률(조건부확률)을 의미하며 신뢰도가 1에 가까울수록 의미있는 연관성을 가지고 있다.
                          support(x,y)         : x,y가 동시에 나올 확률
  - confidence(x->y) = -----------------
                          support(x)           : 
  - (x->y) ; x:조건 y:결과 ; x를 구매할 때 y도 구매함; x를 검색할 때 y도 검색함;
  - s(x->y) = n(x∩y)/N
  - c(x->y) = n(x∩y)/n(x)
                          
  - s(우유 -> 시리얼): 우유와 시리얼을 동시에 구매할 확률
  - c(우유 -> 시리얼): 우유를 구매할 때 시리얼도 같이 구매할 조건부 확률

  예시)  
    거래번호      구매물품
    ________      __________________________________
    1             우유, 버터, 시리얼
    2             우유, 시리얼
    3             우유, 빵
    4             버터, 맥주, 오징어
                              
    :전체 구매물품에서 우유와 시리얼을 동시에 구매할 확률은? 50%(2/4)
    :우유를 샀을 때 시리얼을 살 조건부 확률은? 66%(2/3)
    
    :시리얼을 샀을 때 우유를 살 조건부 확률은? 100%(2/2)
    
    
    :우유 -> 시리얼(50%(지지도), 66%(신뢰도))
    
    :시리얼 -> 우유(50%, 100%)

  - 향상도(lift): 지지도와 신뢰도 동시에 고려한다. 
  - lift(시리얼, 우유) = 신뢰도(시리얼->우유)/ 지지도(우유)
                        = 100% / 75% = 1.33 
                        (cf. 지지도(우유)= 3/4)
  - 지지도, 신뢰도, 향상도가 높을 때 연관이 높음을 의미한다. 

# cf #항목을 만들 때 가장 거래건수가 많은 물품을 하나씩 교차시켜 
# 조합가능한 것을 모두 교차시켜보기

거래도    아이템
1         A C D
2         B C E
3         A B C E
4         B E

아이템    지지도 (지금은 분모를 생략하고 나타내기)
A         2
B         3
C         3
D         1
E         3
#cf. D는 전체구매건 중에 하나밖에 없으므로 제외시킬 수 있다. 제외시켜 조합할 수 있다.

#지지도가 2이상인 것만 추출한다고 가정하면 지지도가 2이상인 것만 추출하여 다시 정리
아이템    지지도 (지금은 분모를 생략하고 나타내기)
A         2
B         3
C         3
E         3

#아이템목록 (조합하기) | 지지도
A B                       1
A C                       2
A E                       1
B C                       2
B E                       3
C E                       2

#지지도가 1인것은 제외시키자!

#아이템목록 | 지지도
A C           2
B C           2
B E           3
C E           2
#B C를 추천한 고객들에게는 E도 추천할 수 있음

#B C E를 한꺼번에 추천해주기
#아이템목록 | 지지도
B C E         2

#연관분석 알고리즘
#apriori(아프리오리) algorithm
- 집합의 크기가 1인 경우부터 차례로 늘려가면서 처리한다. 
- k개인 빈도 높은 항목을 구했다면 그 다음에는 k+1인 항목의 집합을 계산한다. 그래서 총 최대 개수를 가진 빈도항목까지 반복한다. (조합가능한 것을 다 만들어 보는 개념)
- library(arules)

install.packages("arules")
library(arules) #matrix모양으로 data를 넣어줘야 함 (일반적으로 transactions 형으로 넣어주면 더 좋다)

#리스트로 넣어주기
buylist <- list(c("우유", "버터","시리얼"),
                c("우유","시리얼"),
                c("우유","빵"), 
                c("버터", "맥주", "오징어"))

#transactions으로 형변환 하기(python의 dictionary형과 유사);
buylist <- as(buylist, "transactions") 
buylist
  # transactions in sparse format with
  # 4 transactions (rows) and -> 건수
  # 6 items (columns)     -> unique한 아이템
  # 데이터가 보이지 않기 때문에 -> inspect 메소드 사용하기
inspect(buylist)  #matrix에서는 inspect를 사용하지 못함
  # items             
  # [1] {버터,시리얼,우유}
  # [2] {시리얼,우유}     
  # [3] {빵,우유}         
  # [4] {맥주,버터,오징어}

# #cf.buylist <- as(buylist, "matrix") matrix형으로 변환함
#buylist <- as(buylist, "matrix") 

buyresult <- apriori(buylist)
inspect(buyresult)
  # lhs              rhs      support confidence lift     count
  # [1]  {빵}          => {우유}   0.25    1          1.333333 1    
  # [2]  {맥주}        => {오징어} 0.25    1          4.000000 1    
  # [3]  {오징어}      => {맥주}   0.25    1          4.000000 1    
  # [4]  {맥주}        => {버터}   0.25    1          2.000000 1    
  # [5]  {오징어}      => {버터}   0.25    1          2.000000 1    
  # [6]  {시리얼}      => {우유}   0.50    1          1.333333 2    
  # [7]  {맥주,오징어} => {버터}   0.25    1          2.000000 1    
  # [8]  {맥주,버터}   => {오징어} 0.25    1          4.000000 1    
  # [9]  {버터,오징어} => {맥주}   0.25    1          4.000000 1    
  # [10] {버터,시리얼} => {우유}   0.25    1          1.333333 1    
  # [11] {버터,우유}   => {시리얼} 0.25    1          2.000000 1

#supprot값: 0.5 {시리얼}      => {우유}
#confidence값: 다 1
#lift: 4.0이 높음
#count값으로 보면 lift의 4.0이 너무 작은 것일 수 있기 때문에 고려하기
#이를 토대로 의사결정을 해야함 

#신뢰도를 0.5이상인 결과만 보고 싶을 때; subset method이용 
inspect(subset(buyresult, subset=support >= 0.5))
#향상도의 값의 결과만 보고 싶을 때 
inspect(subset(buyresult, subset=lift >= 3))

lhs: left hand side
rhs: right hand side

#%in%  : left hand side에 (버터 or 시리얼)이 있는 것만 다 출력하기
inspect(subset(buyresult, subset=lhs %in% c("버터","시리얼")))
#%ain% : all in의 의미로 left hand side에 (버터 and 시리얼)이 있는 것만 다 출력하기
inspect(subset(buyresult, subset=lhs %ain% c("버터","시리얼")))
  # lhs              rhs    support confidence lift     count
  # [1] {버터,시리얼} => {우유} 0.25    1          1.333333 1    
#%oin% : left hand side에 버터가 혼자 있는거, 시리얼이 혼자있는것, 둘다 있는 것을 출력하기
inspect(subset(buyresult, subset=lhs %oin% c("버터","시리얼")))
  # lhs              rhs    support confidence lift     count
  # [1] {시리얼}      => {우유} 0.50    1          1.333333 2    
  # [2] {버터,시리얼} => {우유} 0.25    1          1.333333 1    
#%pin%: like연산자처럼 "우"자가 있는 데이터는 다 출력하기
inspect(subset(buyresult, subset=lhs %pin% c("우")))
  # lhs            rhs      support confidence lift count
  # [1] {버터,우유} => {시리얼} 0.25    1          2    1  

#buylist로 빈도 값 구하기   (1을 기준으로 비율로 빈도값이 나타내짐)
itemFrequencyPlot(buylist)

#buylist에서 support가 0.2이상인 값 그래프그리기
itemFrequencyPlot(buylist, support=0.2)


######################################################################################

#상가들의 연관분석 (부동산 상권과 관련하여); 파일에서 건물에서 있는 상가종류는 상가의 여부를 의미하지 수량을 의미하지 않는다. 
#파일 불러들이기
building <- read.csv("c:/data/building.csv")

#건물이름(건물정보)은 지우기
building <- building[2:13]
#또는 building <- building[-1]

# building에서 na값을 0으로 바꾸기
building[is.na(building)] <- 0 
building

# dataframe을 matrix로 만들기(as.matrix를 이용해서)
trans <- as.matrix(building) 
#trans <- as.matrix(building, "transactions"): 이렇게 해도 matrix로 전환되기 때문에 transaction을 쓰지 않아도 된다. matrix때문에 inspect를 사용할 수 없음 
trans

#
apriori(trans)
#너무 과도하게 지정될 경우 parameter를 제한해서 만들수 있음
rules <- apriori(trans, parameter = list(supp=0.2, conf=0.6))
rules

#
inspect(rules)
inspect(subset(rules, subset=lhs %in% c("약국","병원")))
inspect(subset(rules, subset=lhs %in% c("보습학원","은행")))

#이러한 결과를 바탕으로 insight를 가지고 report를 만들어 준다.!

#apriori 의 시각화를 더 잘하기 위해서는 R의 3.4 version이상이 되어야 한다.
#https://cran.r-project.org/web/packages/arulesViz/vignettes/arulesViz.pdf
install.packages("arulesViz")
library(arulesViz)
#연관있는 부분들을 network(네트워크)모양으로 그래프를 그려준다.
plot(rules, method="graph")
#plot(rules, method="??")
#Available methods: ‘matrix’, ‘mosaic’, ‘doubledecker’, ‘graph’, ‘paracoord’, ‘scatterplot’, ‘grouped matrix’, ‘two-key plot’, ‘matrix3D’, ‘iplots’
plot(rules, method="paracoord")
plot(rules, method="matrix")
plot(rules, method="grouped matrix") #plot(rules, method="group")
plot(rules, method="scatterplot")
plot(rules, method="two-key plot")
plot(rules, method="matrix3D")
# install.packages("iplots")
# library("iplots")
plot(rules, method="iplots")

istitue <- subset(rules, subset=rhs %in% "보습학원")

a <- subset(rules, subset=rhs %in% "편의점"&confidence > 0.7)
inspect(a)
plot(a, method="graph")
plot(a, method="group")


