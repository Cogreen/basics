# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 09:55:38 2018

@author: stu
"""

# =============================================================================
# [문제] zoo data set을 이용해서 분류프로그램을 만드세요.
# =============================================================================

import tensorflow as tf
import numpy as np
import pandas as pd

#zoo = np.loadtxt("c:/data/zoo_data.txt", delimiter=",", dtype=np.float32)
#zoo = np.array(")

zoo = pd.read_csv("c:/data/zoo_data.csv")

zoo = pd.read_csv("c:/data/zoo_data.csv")



#zoo = tf.data.Dataset("c:data/zoo_data.txt")

#x_data = zoo[:,1:16]

x_data = zoo.ix[:,1:-1]

y_data = zoo.ix[:,[-1]]

x = tf.placeholder(tf.float32, [None,16])
y = tf.placeholder(tf.int32, [None,1])

#one-hot encoding : 7개 범주
y_one_hot = tf.one_hot(y,7) 

#3차원 배열로 만들지 않을 것이기 때문에 reshape을 해준다.
#[-1,3] : -1은 None이라고 생각하면 된다.
y_one_hot = tf.reshape(y_one_hot, [-1,7])

w = tf.Variable(tf.random_normal([16,7]), name='weight')
b = tf.Variable(tf.random_normal([7]), name='bias')

logits = tf.matmul(x,w)+b

#나온 값을 확률로 만들기 위해 softmax를 사용한다. 
hypothesis = tf.nn.softmax(logits)

#cross entropy / logits = (logits = tf.matmul(x,w)+b)
cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=logits, labels=y_one_hot))

#training시키기
train = tf.train.GradientDescentOptimizer(learning_rate = 0.1).minimize(cost)

#prediction하기 ->(hypothesis, 1) :1은 1차원을 의미함 
prediction = tf.argmax(hypothesis, 1)

correct_prediction = tf.equal(prediction, tf.argmax(y_one_hot, 1))

accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

sess = tf.Session()
sess.run(tf.global_variables_initializer())
for step in range(2001):
    sess.run(train, feed_dict={x:x_data, y:y_data})
    if step % 100 ==0:
        loss, acc = sess.run([cost, accuracy], feed_dict={x:x_data, y:y_data})
        print("Step: ", step, " Loss: ", loss," Accuracy : ",acc)


#0 : 포유류, 1 : 조류, 2 : 파충류, 3 : 어류, 4 : 양서류, 5 : 곤충/거미류, 6 : 무척추동물
#test: aardvark : 0
a = sess.run(hypothesis, feed_dict={x:[[1,0,0,1,0,0,1,1,1,1,0,0,4,0,0,1]]})
print(a,sess.run(tf.argmax(a,1)))

# test: dove : 1
b = sess.run(hypothesis, feed_dict={x:[[0,1,1,0,1,0,0,0,1,1,0,0,2,1,1,0]]})
print(c,sess.run(tf.argmax(b,1)))

# test: dove : 6
c = sess.run(hypothesis, feed_dict={x:[[0,0,1,0,0,1,1,0,0,0,0,0,6,0,0,0]]})
print(c,sess.run(tf.argmax(c,1)))

# =============================================================================
# 쌤답안; 코드 확인 필요 ㅠㅠㅠㅠㅠㅠ
# 신경망안에는 숫자만 들어가야함 

import tensorflow as tf
import numpy as np

#usecols: 특정한 열만 사용할 경우 컬럼 인덱스를 표시하면 된다.
xy = np.loadtxt("c:/data/zoo_data.txt", delimiter=",", usecols = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17), dtype=np.float32)
x_data = xy[:,0:-1]
y_data = xy[:,[-1]]

# 1 : 포유류, 2 : 조류, 3 : 파충류, 4 : 어류, 5 : 양서류, 6 : 곤충/거미류, 7 : 무척추동물 
# 위의 분류의 값을 0~6번으로 바꾸기 (왜냐하면 python은 0번부터 시작하기때문에 나중에 분류할 때 헷갈리지 않게 y_data에서 1을 빼줌 )
# 결과 0 : 포유류, 1 : 조류, 2 : 파충류, 3 : 어류, 4 : 양서류, 5 : 곤충/거미류, 6 : 무척추동물 
y_data = y_data -1 

#데이터 모형 확인하기 
print(x_data.shape, y_data.shape)

# 7개로 분류함 ;미리 선언하기
nb_classes = 7

x = tf.placeholder(tf.float32, [None,16])
y = tf.placeholder(tf.int32, [None, 1])

# one-hot encoding
y_one_hot = tf.one_hot(y, nb_classes)

#reshape -> 별도의 7개 열을 생성함 
y_one_hot = tf.reshape(y_one_hot, [-1, nb_classes])

# weight, bias
w = tf.Variable(tf.random_normal([16, nb_classes], seed=0), name="weight")
b = tf.Variable(tf.random_normal([nb_classes], seed=0), name="bias") 

# 분류를 이용하기 위해 softmax를 사용해야 함
# tf.matmul: tensor에서 제공하는 행렬의 곱 - affine sum
logits = tf.matmul(x,w)+b

# activation function을 softmax로 이용
hypothesis = tf.nn.softmax(logits)

#
cost = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(logits=logits, labels=y_one_hot))

optimizer = tf.train.GradientDescentOptimizer(learning_rate = 0.1).minimize(cost)

predicton = tf.argmax(hypothesis,1)
correct_prediction  = tf.equal(prediction, tf.arg_max(y_one_hot,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

sess = tf.Session()
sess.run(tf.global_variables_initializer())
for step in range(2001):
    sess.run(optimizer, feed_dict={x:x_data, y:y_data})
    if step%100 == 0:
        loss, acc = sess.run([cost, accuracy], feed_dict = {x: x_data, y: y_data})
        print("Step: {:5}\tLoss:{:.3f} )\tAcc:{:.2%}".format(step, loss, acc))
    
     #{:5}: 다섯칸을 만들어서 오른쪽을 기준으로 하여 왼쪽에 공백이 나오도록 하기 / 이 모양으로 
     # {:.3f} :  소수점 3자리까지만 표현하겠음 
     # {:.2%} : 소수점 2자리까지 쓰고 %를 사용 
     #\t : tab키가 들어가서 가지런한 정렬을 함 



#비교하기
pred = sess.run(prediction, feed_dict = {x:x_data})
for p, y in zip(pred, y_data.flatten()):
    print("[{}] Prediction: {} True Y:{}".format(p==int(y),p,int(y)))

# =============================================================================
# 쌤답안; 서옥이 
import tensorflow as tf
import numpy as np

xy = np.loadtxt("c:/data/zoo_data.txt",delimiter=",",usecols=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17),dtype=np.float32)

x_data = xy[:,0:-1]
y_data = xy[:,[-1]]
y_data=y_data-1 # 인덱스를 0번 부터 시작하는걸로 맞추려고  지금은 1번부터 7번까지 

print(x_data.shape,y_data.shape)

x= tf.placeholder(tf.float32,[None,16])
y= tf.placeholder(tf.int32,[None,1])

y_one_hot = tf.one_hot(y,7)
y_one_hot = tf.reshape(y_one_hot,[-1,7])  ## -1 = None

w=tf.Variable(tf.random_normal([16,7],seed =0), name ="weight")
b=tf.Variable(tf.random_normal([7],seed =0), name ="bias")

logits = tf.matmul(x,w)+b
hypothesis = tf.nn.softmax(logits)

cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=logits,labels=y_one_hot))

optimizer= tf.train.GradientDescentOptimizer(learning_rate=0.9).minimize(cost)

prediction = tf.argmax(hypothesis,1)
correct_prediction = tf.equal(prediction,tf.argmax(y_one_hot,1))

accuracy = tf.reduce_mean(tf.cast(correct_prediction,tf.float32))

sess=tf.Session()
sess.run(tf.global_variables_initializer())
for step in range(2001):
    sess.run(optimizer,feed_dict={x:x_data,y:y_data})
    if step % 100 == 0:
        loss,acc =sess.run([cost,accuracy],feed_dict={x:x_data,y:y_data})
        print("Step:{:5}\tLoss:{:3f}\tACC:{:.2%}".format(step,loss,acc))
        

#비교하기 ;  y_data.flatte(): 데이터를 펼처 보기
pred = sess.run(prediction, feed_dict = {x:x_data})
for p, y in zip(pred, y_data.flatten()):
    print("[{}] Prediction: {} True Y:{}".format(p==int(y),p,int(y)))


#worm,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,7
zoo_hypothesis = sess.run(hypothesis, feed_dict={x:[[0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0]]})
#출력된 확률중 가장 큰 확률을 뽑아주기 arg_max 
print(zoo_hypothesis, sess.run(tf.arg_max(zoo_hypothesis,1)))

#wren,0,1,1,0,1,0,0,0,1,1,0,0,2,1,0,0,2
zoo_hypothesis = sess.run(hypothesis, feed_dict={x:[[0,1,1,0,1,0,0,0,1,1,0,0,2,1,0,0]]})
print(zoo_hypothesis, sess.run(tf.arg_max(zoo_hypothesis,1)))


# =============================================================================

#만약 문자로 제공되었다면  numpy의 one-hot encoding을 사용해야한다. 

#cf. 
a = np.arange(12)
a
#3x4로 만들기
b = a.reshape(3,4)
#한쪽이 상수값이 들어 갔을 경우 숫자가 고정되기 때문에, -1로 하면 4열이 자동으로 들어가나.
b = a.reshape(3,-1)
a.reshape(2,2,-1)
a.reshape(2,-1,2)
#.flatten(): array를 풀어버리는 기능(array를 펼치는 기능)
a.flatten()
 
# =============================================================================

# =============================================================================
# [문제] bmi.csv 내용을 신경망을 이용해서 분류해 보세요.
#
#BMI
# BMI = 몸무게 / (키(m)*키(m))
# 18.5 이상 25미만이면 표준
#label : thin(저체중), normal(정상), fat(비만)
#
# =============================================================================

#학습을 했을 때 잘 나오지 않으면 -> 1. data작업에서 scale작업을 하거나(max, 표준편차 등을 이용) 2. activation function을 다르게 사용하거나 해야한다. 
import pandas as pd

xy = pd.read_csv("c:/data/bmi.csv")

cols = ['height', 'weight']

# label data 이름 -> 숫자로 변경
xy['label']= xy['label'].replace('thin', 0)
xy['label'] = xy['label'].replace('normal', 1)
xy['label'] = xy['label'].replace('fat', 2)

# pandas를 이용한 one-hot encoding 
dummy_label = pd.get_dummies(xy['label'], prefix='label')

# x, y data만들기
    #x_data = xy[:,0:-1]
    #y_data = xy[:,[-1]]

x_data = xy[cols]
y_data = xy['label']

#x_data, y_data array형식으로 만들기
x_data = np.array(x_data)

y_data2 = []
for i in y_data:
    y_data2.append([i])

y_data = y_data2    

y_one_hot = dummy_label

# 3안 성능향상시키기 scale해주기 (3안 적용후 1안 또는 2안해보기 )
    from sklearn.preprocessing import StandardScaler
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(x_data)


x = tf.placeholder(tf.float32, [None,2])
y = tf.placeholder(tf.int32, [None, 1])

#1안 
    w = tf.Variable(tf.random_normal([2,3], seed=0), name = 'weight')
    b1 = tf.Variable(tf.random_normal([3], seed=0), name= 'bias')
    
    logits = tf.matmul(x,w)+b
    
    #softmax 이용
    hypothesis = tf.nn.softmax(logits)

    #relu 이용
    #hypothesis = tf.nn.(logits)


#2안
    w1 = tf.Variable(tf.random_normal([2,5], seed=0), name = 'weight')
    b1 = tf.Variable(tf.random_normal([5], seed=0), name= 'bias')
    
    layer1 = tf.sigmoid(tf.matmul(x,w1))+b1
        
    w2 = tf.Variable(tf.random_normal([5,3], seed=0),  name='weight2')
    b2 = tf.Variable(tf.random_normal([3], seed=0), name='bias2')
    
    logits = tf.matmul(layer1,w2) + b2
    
    hypothesis = tf.nn.softmax(logits)

cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=logits,labels=y_one_hot))

optimizer= tf.train.GradientDescentOptimizer(learning_rate=0.01).minimize(cost)

prediction = tf.argmax(hypothesis,1)
correct_prediction = tf.equal(prediction,tf.argmax(y_data,1))

accuracy = tf.reduce_mean(tf.cast(correct_prediction,tf.float32))

sess=tf.Session()
sess.run(tf.global_variables_initializer())
for step in range(10001):
    ss.run(train,feed_dict = {x:x_data,y:y_data})
    if step % 1000 == 0:
        loss ,acc =ss.run([cost,accuracy],feed_dict  = {x:x_data,y:y_data})
        print("setp{:5}\tLoss:{:.3f}\tAcc:{:.1%}".format(step,loss,acc))
        
pred = ss.run(prediction,feed_dict ={x:X_scaled})
for p ,y in zip(pred,yda['label']):
    print("[{}] prediction : {} True Y : {}" .format(p==int(y),p,int(y)))     
    
        

# =============================================================================
#영은이
        # [문제] bmi.csv 내용을 신경망을 이용해서 분류해 보세요.

#BMI
# BMI = 몸무게 / (키(m)*키(m))
# 18.5 이상 25미만이면 표준
#label : thin(저체중), normal(정상), fat(비만)

bmi = pd.read_csv("c:/data/bmi.csv")
xda = bmi.ix[:,0:2]
yda = bmi.ix[:,[2]]
set(yda['label'])
yda[yda == 'thin' ] = 0
yda[yda == 'normal' ] = 1
yda[yda == 'fat' ] = 2
np.array(xda)
np.array(yda)

# pd.get_dummies(yda)

import tensorflow as f
x = f.placeholder( f.float32,[None,2])
y = f.placeholder( f.int32 ,[None,1])

y_one_hot = f.one_hot(y,3)
y_one_hot = f.reshape(y_one_hot,[-1,3])
w = f.Variable(f.random_normal([2,3],seed=0),name ='weight')
b = f.Variable(f.random_normal([3],seed=0),name ='bias')

logits = f.matmul(x,w)+b

hypothesis = f.nn.softmax(logits)

cost = f.reduce_mean(f.nn.softmax_cross_entropy_with_logits(logits = logits,labels =y_one_hot))
train = f.train.GradientDescentOptimizer(learning_rate = 0.01 ).minimize(cost)

prediction =f.argmax(hypothesis,1)
correct_prediction = f.equal(prediction,f.argmax(y_one_hot,1))
accuracy = f.reduce_mean(f.cast(correct_prediction,f.float32))


scaler = StandardScaler()
X_scaled = scaler.fit_transform(xda)


ss = f.Session()
ss.run(f.global_variables_initializer())


for step in range(10001):
    ss.run(train,feed_dict = {x:X_scaled,y:yda})
    if step % 1000 == 0:
        loss ,acc =ss.run([cost,accuracy],feed_dict  = {x:X_scaled,y:yda})
        print("setp{:5}\tLoss:{:.3f}\tAcc:{:.1%}".format(step,loss,acc))
        
pred = ss.run(prediction,feed_dict ={x:X_scaled})
for p ,y in zip(pred,yda['label']):
    print("[{}] prediction : {} True Y : {}" .format(p==int(y),p,int(y)))     
    
    
    
    

