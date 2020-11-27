'''<< �Ű��>> ''' 

'''
# ȸ�͸� ���� (�з��� �ƴ�)

<��ũ��Ʈ�� ������ ��>
���� �о߿��� �ǹ��� �������� ���� ��Ȯ�� ������ �ſ� �߿��ϴ�.
�� ������ �ǹ�, ����, ö���� �����ϴµ� ���Ǵ� ���縦 �ٷ�� ������ ��ħ�� �����ϱ� ���� �ʿ��ϴ�. 

��ũ��Ʈ�� ������ ������ �ſ� �߿��ϴ�.
��� �������忡�� ���ȴٰ� �ϴ��� ���������� ��ȣ�ۿ��ϴ� �ſ� �پ��� ������Ҷ����� ��ũ��Ʈ ������ �پ��ϴ�. 

''' 

#���� �ҷ�����
concrete <- read.csv("c:/data/concrete.csv")

#�������� 
str(concrete)

'''
cement: ��ũ��Ʈ �ѷ�, �Թ���ʹ� ų�α׷�
slag: �ø�Ʈ
ash: ��(�ø�Ʈ)
water: ��
superplasticizer: ������ ������(��ũ��Ʈ ������ ���̴� ÷����)
coarseagg(coarse aggregate): ���� �ڰ�
fineagg(fine aggregate): �� �ڰ�
aging time(age): �����ð�
strength: ���೻����

-> �ñ������δ� strength(���೻����)�� ������ Ȯ���ϱ�
-> �ٸ� �͵��� ���������� �ǰ�, strength�� ���Ӻ����� �ȴ�.
'''

#����ȭ �Լ�(����ȭ �ϱ�): max�� min�� ������ ����ȭ �Լ� �����(scale�Լ��� ����ϸ� ������ ������� ���ϱ� �� ���)
normalize <- function(x){
  return((x-min(x))/(max(x)-min(x)))
}

# ��ü ������ �����ӿ� ����ȭ ����
# ��� ���� ����ȭ �Լ� �����ϱ�: lapply���
concrete_norm <- as.data.frame(lapply(concrete, normalize))

# Ȯ��
summary(concrete)
summary(concrete_norm)

summary(concrete$strength)
summary(concrete_norm$strength)

# �Ʒ�, �׽�Ʈ ������ �����ϴ� ���
concrete_train <- concrete_norm[1:773,]
concrete_test <- concrete_norm[774:1030,]

# ���� 
length(concrete)
#[1] 9
nrow(concrete)
#[1] 1030

# �����͸��� �Ʒ� (neuralnet)
install.packages("neuralnet")
library(neuralnet)

# help������� neuralnet ��� ���캸��
?neuralnet

# �𵨸����
concrete_model <- neuralnet(formula = strength ~ cement+slag+ash+water+superplastic+coarseagg+fineagg+age, data = concrete_train)

#�ð�ȭ
plot(concrete_model) 
# �Էº����� ������ weight��, bias���� �� 
# error: 5.081158/ steps: 2507

# �𵨰��
model_results <- compute(concrete_model, concrete_test[1:8])

# ���� ����
predicted_strength <- model_results$net.result

# �������� ������ ���� �������: 
cor(predicted_strength, concrete_test$strength)
# 0.806067954

#================== upgrade! 
# ���� ���� �����(������踦 �� ���̱� ���ؼ�)
# hidden=c(5,2) ������ ������ ����: ù��°�� 5��, �ι�°�� 2��
concrete_model2 <- neuralnet(formula = strength ~ cement+slag+ash+water+superplastic+coarseagg+fineagg+age, data = concrete_train, hidden=c(5,2))

#�ð�ȭ
plot(concrete_model2)

# �𵨰��
model_results2 <- compute(concrete_model2, concrete_test[1:8])

# ��������
predicted_strength2 <- model_results2$net.result

# �������� ������ ���� �������: 
cor(predicted_strength2, concrete_test$strength)
# 0.9366598746


#================== ���������� �ٸ��� �־ ������ ������ ��� �޶������� ���캸��
# �𵨸����
concrete_model3 <- neuralnet(formula = strength~cement+slag+ash+water, data = concrete_train, hidden = c(5,2))

#�ð�ȭ
plot(concrete_model3)

#�𵨰��
model_results3 <- compute(concrete_model3, concrete_test[c('cement','slag','ash','water')])

#��������
predicted_strength3 <-model_results3$net.result

#�������� ���������� �������
cor(predicted_strength3, concrete_test$strength)
# 0.6856347574


#================== �ǻ���� Ʈ���� �غ����? (�ڽ�)

############################################################################

library(nnet)

# iris data: �з� 
# -> ���������� ���� ���Ӻ����� Ȯ�������� ������ �Ǳ� ������ activation function�� softmax function ���� ������ �ȴ�. 
# iris ���Ӻ����� name���� �Ǿ��ֱ� ������ ���ڷ� �ٲ���� �Ѵ�. -> one-hot encoding

iris <- read.csv("c:/data/iris.csv")
str(iris)

# one-hot encoding
# (���, R���� one-hot encoding�� �ʿ����. )
iris <- cbind(iris, class.ind(iris$Name))

# training dataset, test dataset ����� 
#����������  80:20Ȯ���� (replace -��������)
set.seed(12345)
idx <- sample(2, nrow(iris), prob=c(0.8, 0.2), replace=T)
iris_train <- iris[idx==1,]
iris_test <- iris[idx==2,]

# �������� ��� ��������� Ȯ���ϱ�
table(iris_train$Name)
# Ȯ�������� ���� Ȯ���ϱ�
prop.table(table(iris_train$Name))

#�� ����� nnet(���Ӻ���~��������, data = , size= )
iris_model <- nnet(Name~SepalLength+SepalWidth+PetalLength+PetalWidth, data=iris_train, size=10)

#������ 
iris_pred <- predict(iris_model, iris_test[,c(1:4)], type="class")

#�������� ������ ���� ������ ��
table(iris_pred, iris_test$Name)

#�ð�ȭ ���1
library(devtools)
source_url('https://gist.githubusercontent.com/fawda123/7471137/raw/466c1474d0a505ff044412703516c34f1a4684a5/nnet_plot_update.r')
install.packages('reshape')
library(reshape)
plot.nnet(iris_model)

#�ð�ȭ ���2
install.packages("NeuralNetTools")
library(NeuralNetTools)
plot.nnet(iris_model)

#======================
# model�� ���� �� softmax�� �ְ��� �� �� 
iris_model1 <- nnet(Name~SepalLength+SepalWidth+PetalLength+PetalWidth, data=iris_train, size=10, softmax=T)
# Error in nnet.default(x, y, w, softmax = TRUE, ...) : 
#   formal argument "softmax" matched by multiple actual arguments

# model�� ���� �� softmax�� �ְ��� �� ��, one -hot encoding �� ���� ���Ӻ����� �־�� ��
iris_model1 <- nnet(x=iris_train[,c(1:4)], y=iris_train[,c(6:8)],data=iris_train, size=10, softmax = T)

