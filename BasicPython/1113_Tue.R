'''<< 신경망>> ''' 

'''
# 회귀를 통해 (분류가 아님)

<콘크리트의 내구력 모델>
공학 분야에서 건물의 내구성에 대한 정확한 추정이 매우 중요하다.
이 추정은 건물, 교량, 철도를 건축하는데 사용되는 자재를 다루는 안전한 지침을 제정하기 위해 필요하다. 

콘크리트의 내구력 추정은 매우 중요하다.
모든 건축현장에서 사용된다고 하더라도 복합적으로 상호작용하는 매우 다양한 구성요소때문에 콘크리트 성능은 다양하다. 

''' 

#파일 불러오기
concrete <- read.csv("c:/data/concrete.csv")

#구조보기 
str(concrete)

'''
cement: 콘크리트 총량, 입방미터당 킬로그램
slag: 시멘트
ash: 분(시멘트)
water: 물
superplasticizer: 고성능 감수재(콘크리트 강도를 높이는 첨가제)
coarseagg(coarse aggregate): 굵은 자갈
fineagg(fine aggregate): 잔 자갈
aging time(age): 숙성시간
strength: 압축내구력

-> 궁극적으로는 strength(압축내구력)가 좋은지 확인하기
-> 다른 것들은 독립변수가 되고, strength가 종속변수가 된다.
'''

#정규화 함수(정규화 하기): max와 min를 가지고 정규화 함수 만들기(scale함수를 사용하면 쉽지만 사용하지 못하기 할 경우)
normalize <- function(x){
  return((x-min(x))/(max(x)-min(x)))
}

# 전체 데이터 프레임에 정규화 적용
# 모든 열에 정규화 함수 적용하기: lapply사용
concrete_norm <- as.data.frame(lapply(concrete, normalize))

# 확인
summary(concrete)
summary(concrete_norm)

summary(concrete$strength)
summary(concrete_norm$strength)

# 훈련, 테스트 데이터 생성하는 방법
concrete_train <- concrete_norm[1:773,]
concrete_test <- concrete_norm[774:1030,]

# 참고 
length(concrete)
#[1] 9
nrow(concrete)
#[1] 1030

# 데이터모델을 훈련 (neuralnet)
install.packages("neuralnet")
library(neuralnet)

# help기능으로 neuralnet 기능 살펴보기
?neuralnet

# 모델만들기
concrete_model <- neuralnet(formula = strength ~ cement+slag+ash+water+superplastic+coarseagg+fineagg+age, data = concrete_train)

#시각화
plot(concrete_model) 
# 입력변수의 각각의 weight값, bias값이 들어감 
# error: 5.081158/ steps: 2507

# 모델결과
model_results <- compute(concrete_model, concrete_test[1:8])

# 강도 예측
predicted_strength <- model_results$net.result

# 예측값과 실제값 간의 상관관계: 
cor(predicted_strength, concrete_test$strength)
# 0.806067954

#================== upgrade! 
# 은닉 뉴런 만들기(상관관계를 더 높이기 위해서)
# hidden=c(5,2) 은닉층 뉴런의 개수: 첫번째는 5개, 두번째는 2개
concrete_model2 <- neuralnet(formula = strength ~ cement+slag+ash+water+superplastic+coarseagg+fineagg+age, data = concrete_train, hidden=c(5,2))

#시각화
plot(concrete_model2)

# 모델결과
model_results2 <- compute(concrete_model2, concrete_test[1:8])

# 강도예측
predicted_strength2 <- model_results2$net.result

# 예측값과 실제값 간의 상관관계: 
cor(predicted_strength2, concrete_test$strength)
# 0.9366598746


#================== 독립변수를 다르게 넣어서 내구성 강도가 어떻게 달라지는지 살펴보기
# 모델만들기
concrete_model3 <- neuralnet(formula = strength~cement+slag+ash+water, data = concrete_train, hidden = c(5,2))

#시각화
plot(concrete_model3)

#모델결과
model_results3 <- compute(concrete_model3, concrete_test[c('cement','slag','ash','water')])

#강도예측
predicted_strength3 <-model_results3$net.result

#예측값과 실제값간의 상관관계
cor(predicted_strength3, concrete_test$strength)
# 0.6856347574


#================== 의사결정 트리로 해볼까요? (자습)

############################################################################

library(nnet)

# iris data: 분류 
# -> 독립변수를 통해 종속변수가 확률값으로 나오면 되기 때문에 activation function을 softmax function 으로 뽑으면 된다. 
# iris 종속변수는 name으로 되어있기 때문에 숫자로 바꿔줘야 한다. -> one-hot encoding

iris <- read.csv("c:/data/iris.csv")
str(iris)

# one-hot encoding
# (사실, R에서 one-hot encoding은 필요없다. )
iris <- cbind(iris, class.ind(iris$Name))

# training dataset, test dataset 만들기 
#난수값으로  80:20확률로 (replace -복원추출)
set.seed(12345)
idx <- sample(2, nrow(iris), prob=c(0.8, 0.2), replace=T)
iris_train <- iris[idx==1,]
iris_test <- iris[idx==2,]

# 종류별로 몇개씩 만들었는지 확인하기
table(iris_train$Name)
# 확률값으로 종류 확인하기
prop.table(table(iris_train$Name))

#모델 만들기 nnet(종속변수~독립변수, data = , size= )
iris_model <- nnet(Name~SepalLength+SepalWidth+PetalLength+PetalWidth, data=iris_train, size=10)

#예측값 
iris_pred <- predict(iris_model, iris_test[,c(1:4)], type="class")

#예측값과 실제값 간의 데이터 비교
table(iris_pred, iris_test$Name)

#시각화 방법1
library(devtools)
source_url('https://gist.githubusercontent.com/fawda123/7471137/raw/466c1474d0a505ff044412703516c34f1a4684a5/nnet_plot_update.r')
install.packages('reshape')
library(reshape)
plot.nnet(iris_model)

#시각화 방법2
install.packages("NeuralNetTools")
library(NeuralNetTools)
plot.nnet(iris_model)

#======================
# model을 만들 때 softmax를 넣고자 할 때 
iris_model1 <- nnet(Name~SepalLength+SepalWidth+PetalLength+PetalWidth, data=iris_train, size=10, softmax=T)
# Error in nnet.default(x, y, w, softmax = TRUE, ...) : 
#   formal argument "softmax" matched by multiple actual arguments

# model을 만들 때 softmax를 넣고자 할 때, one -hot encoding 된 것을 종속변수로 넣어야 함
iris_model1 <- nnet(x=iris_train[,c(1:4)], y=iris_train[,c(6:8)],data=iris_train, size=10, softmax = T)


