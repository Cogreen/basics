# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 09:54:24 2018

@author: stu
"""

▣ linear regression - 예측 

# =============================================================================


▣ binary classfication (0아니면 1로 분류)

#입력값: 데이터가 문자가 아닌 숫자여야 한다. 
#출력값(목표값): 데이터가 문자가 아닌 숫자여야 한다.   -> One-hot encoding 필요 

import tensorflow as tf
x_data = [[1,2],[2,3],[3,1],[4,3],[5,3],[6,2]]  #[1,2] 공부시간 1시간, 게임시간 2시간 
y_data = [[0],[0],[0],[1],[1],[1]]  #[0] 불합격 [1]합격 

#tensor 모양으로 바꾸기
x = tf.placeholder(tf.float32, shape=[None, 2])
y = tf.placeholder(tf.float32, shape=[None, 1])

w = tf.Variable(tf.random_normal([2,1]), name='weight')
b = tf.Variable(tf.random_normal([1]), name='bias')

#기존 hypothesis
#hypothesis = tf.matmul(x,w) + b 

#affine sum을 하면 숫자가 크게 된다. 그러나 숫자는 0과 1사이에서 나와야 하기 때문에 activation function(sigmoid, step function)을 통해서 출력값을 출력하도록 한다. 
hypothesis = tf.sigmoid(tf.matmul(x,w) + b)
#0과 1사이, 실수이기 때문에 sigmoid 값도 미분을 해야한다. (즉, w, b를 조정하여 미분해야 하는데, sigmoid도 미분해야하기 때문에, 골격 생긴 그래프가 만들어진다.)
#sigmoid를 gradient descent를 쓰면서 골격이 생기기 때문에 수평을 바로 마주하기 때문에 바로 에러율이 없다고 나올 경우가 많다. 사실 최소 에러율이 도달하지 않았는데도 에러율이 없다고 출력하게 되는 문제가 생긴다.  -> 잘못된 예측 
#sigmoid를 하는 순간 오차함수가 문제가 될 수 있다. 
#log0 = 1 / log1 = ∞  (무한이면 우리가 원하는 예측이 아님) -> 따라서 log를 사용하면 에러율을 잘못 예측한 것을 막을 수 있다. 

■ cost function: 1과 0으로 return 하게 됨 
#cf. 기존의 cost function: 편차제곱의 합의 평균 
logisctic cost function은 두가지를 만들어서 사용하도록 한다.  -> 두가지를 만들어서 사용하기 때문에 조건제어문이 필요하다. 

y = 1      -y*log(h(x))
y = 0      (1-y)*log(1-h(x))
 
위의 두 식을 붙여서 만들면 (로그값을 통해 계산함) 

cost = -tf.reduce_mean(y*tf.log(hypothesis)+(1-y)*tf.log(1-hypothesis))
#y=1이면 (1-y)*tf.log(1-hypothesis)가 없어지고 y*tf.log(hypothesis만 계산
#y=0이면 y*tf.log(hypothesis)가 없어지고 (1-y)*tf.log(1-hypothesis)만 계산

train = tf.train.GradientDescentOptimizer(learning_rate=0.01).minimize(cost)

predict = tf.cast(hypothesis > 0.5, dtype=tf.float32)
## tf.cast(hypothesis > 0.5 : 이부분이 조건제어문과 같다. 0.5보다 크면 True, 0.5와 같거나 작으면 False
# 밑의 조건제어문 처럼 작용한다. ##
if hypothesis > 0.5 then 
    True(1.0)
else: 
    False(0.0)
##################################

accuracy = tf.reduce_mean(tf.cast(tf.equal(predict, y), dtype=tf.float32))
#(tf.cast(tf.equal(predict, y), dtype=tf.float32))에 대한 평균을 내어 정확도를 예측 

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for step in range(10001):
        cost_val, _ = sess.run([cost, train], feed_dict={x:x_data, y:y_data})
        if step %200 == 0:
            print(step, cost_val)
    h, c, a  = sess.run([hypothesis, predict, accuracy], feed_dict={x: x_data, y:y_data})
    print ("hypothesis : ",h)
    print ("predict : ",c)
    print ("accuracy: ",a)

#hypothesis :  [[0.03072654]
# [0.15882765]
# [0.3048026 ]
# [0.7814115 ]
# [0.9395937 ]
# [0.9801752 ]]
#predict :  [[0.]
# [0.]
# [0.]
# [1.]
# [1.]
# [1.]]
#accuracy:  1.0


# =============================================================================
# 다층퍼셉트론(and+nand -> xor) 으로 구분한 XOR 분류의 문제를 신경망을 통해 해결해보기 
# 단층퍼셉트론에서 되지 않았던 것처럼, 신경망에서도 층에 대해서 생각해봐야한다.
# logistic regression classifier : 0아니면 1의 값
# 
# [문제] XOR 를 logistic regression classifier를 이용해서 프로그램을 생성하세요.
# 
# 입력값  출력값 
# ------------
# 0 0    0
# 0 1    1
# 1 0    1 
# 1 1    0
# =============================================================================
#은닉층을 만들어야 한다. 
    
x_data = [[0,0],[0,1],[1,0],[1,1]]
y_data = [[0],[1],[1],[0]]

x = tf.placeholder(tf.float32, shape=[None, 2])
y = tf.placeholder(tf.float32, shape=[None, 1])

w1 = tf.Variable(tf.random_normal([2,2], seed=0),  name='weight1')
b1 = tf.Variable(tf.random_normal([2], seed=0), name='bias1')
layer1 = tf.sigmoid(tf.matmul(x,w1) + b1)

w2 = tf.Variable(tf.random_normal([2,1], seed=0),  name='weight2')
b2 = tf.Variable(tf.random_normal([1], seed=0), name='bias2')
hypothesis = tf.sigmoid(tf.matmul(layer1,w2) + b2)

cost = -tf.reduce_mean(y*tf.log(hypothesis)+(1-y)*tf.log(1-hypothesis))

train = tf.train.GradientDescentOptimizer(learning_rate=0.01).minimize(cost)

predict = tf.cast(hypothesis > 0.5, dtype=tf.float32)

accuracy = tf.reduce_mean(tf.cast(tf.equal(predict, y), dtype=tf.float32))


with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for step in range(10001):
        cost_val, _ = sess.run([cost, train], feed_dict={x:x_data, y:y_data})
        if step %200 == 0:
            print(step, cost_val)
    h, c, a  = sess.run([hypothesis, predict, accuracy], feed_dict={x: x_data, y:y_data})
    print ("hypothesis : ",h)
    print ("predict : ",c)
    print ("accuracy: ",a)
    


########################
#쌤답안 
import tensorflow as tf
import numpy as np

x_data = [[0,0],[0,1],[1,0],[1,1]]
y_data = [[0],[1],[1],[0]]
x_data = np.array(x_data, dtype=np.float32)
y_data = np.array(y_data, dtype=np.float32)

x = tf.placeholder(tf.float32, [None, 2])
y = tf.placeholder(tf.float32, [None, 1])

#input layer층 
w1 = tf.Variable(tf.random_normal([2,5], seed=0),  name='weight1')  #두개가 나가니 b1에 2개의 bias가 생긴다. 
b1 = tf.Variable(tf.random_normal([5], seed=0), name='bias1')  
layer1 = tf.sigmoid(tf.matmul(x,w1) + b1)

#hidden layer2 층 
w2 = tf.Variable(tf.random_normal([5,4], seed=0),  name='weight2')  
b2 = tf.Variable(tf.random_normal([4], seed=0), name='bias2')  
layer2 = tf.sigmoid(tf.matmul(layer1,w2) + b2)

#hidden layer3 만들기
w3 = tf.Variable(tf.random_normal([4,4], seed=0),  name='weight3')  
b3 = tf.Variable(tf.random_normal([4], seed=0), name='bias3')  
layer3 = tf.sigmoid(tf.matmul(layer2,w3) + b3)

#output layer
w4 = tf.Variable(tf.random_normal([4,1], seed=0),  name='weight4')  
b4 = tf.Variable(tf.random_normal([1], seed=0), name='bias4')  
hypothesis = tf.sigmoid(tf.matmul(layer3,w4) + b4)

#cross entropy cost function 
cost = -tf.reduce_mean(y*tf.log(hypothesis)+(1-y)*tf.log(1-hypothesis))

#학습률 조절하기 0.1 -> 0.5 ->
train = tf.train.GradientDescentOptimizer(learning_rate=0.5).minimize(cost)


predict = tf.cast(hypothesis > 0.5, dtype=tf.float32)

accuracy = tf.reduce_mean(tf.cast(tf.equal(predict, y), dtype=tf.float32))


sess = tf.Session()
sess.run(tf.global_variables_initializer())
for step in range(10001):
    sess.run(train, feed_dict={x:x_data, y:y_data})
    if step%1000 == 0:
        print(step, sess.run(cost, feed_dict={x:x_data, y:y_data}))
        h = sess.run(hypothesis, feed_dict={x:x_data, y:y_data})
        print(h)

a = sess.run(hypothesis, feed_dict = {x:[[0,0],[0,1],[1,0],[1,1]]})
print(sess.run(tf.cast(a>0.5, dtype=tf.int32))) #0.5보다 크면 1, 0.5같거나 작으면 0으로 출력 [0],[0],[0],[1]으로 출력해야 함 

#코스트가 작았어도 값이 잘 안나왔을 경우, 은닉층을 더 둬야한다. 
#학습율 조절 

▣ multi classification (softmax classifier)
# 종속변수를 one-hot encoding  -> y값이 3개로 분류 된다면, y1, y2, y3로 만들어 one-hot encoding이 되도록 하자. 
# softmax 이용 -> 확률을 기반으로 큰쪽으로 분류하자  
# 기존의 cost function을 cross_entroy function 이라고 하는데, 이를 기반으로 하여 softmax를 사용할 수 있도록 tensor에서 제공한다. 
# -> cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=logits, labels=y_one_hot))
# argmax를 통해서 보여주는 값은 고객들에게 [0],[1],[2]라고 나타날 때, 해석해줄 줄 알아야 한다. 예를 들어, [0] 인덱스를 a로 , [1]인덱스를 b로, [2]인덱스를 c로  

''' 
train.txt 파일로 저장 

#x0,x1,x2,y
1,2,1,0
1,3,2,0
1,3,4,0
1,5,5,1
1,7,5,1
1,2,5,1
1,6,6,2
1,7,7,2

'''

import numpy as np

xy = np.loadtxt("c:/data/train.txt", delimiter=",", dtype=np.float32)

x_data = xy[:,0:-1]
y_data = xy[:,[-1]]

x = tf.placeholder(tf.float32, [None,3])
y = tf.placeholder(tf.int32, [None,1]) #one-hot encoding은 0아니면 1이기 때문에 integer형으로 해야함 
# y를 tf.float32로 할 경우 밑의 error가 뜬다.
# TypeError: Value passed to parameter 'indices' has DataType float32 not in list of allowed values: uint8, int32, int64


#None을 한 이유는 y 데이터는 0,1,2인데 logistic regression처럼 0과 1로 표현이 되어있어야한다. -> one-hot encoding을 해야한다. 
#tensor에서 제공하는 one-hot encoding: y:목표값 ,3: 범주는 3개
y_one_hot = tf.one_hot(y,3)    #Out[360]: <tf.Tensor 'one_hot_3:0' shape=(?, 1, 3) dtype=float32>

#3차원 배열로 만들지 않을 것이기 때문에 reshape을 해준다.
#[-1,3] : -1은 None이라고 생각하면 된다.
y_one_hot = tf.reshape(y_one_hot, [-1,3])   #Out[363]: <tf.Tensor 'Reshape:0' shape=(?, 3) dtype=float32>

w = tf.Variable(tf.random_normal([3,3]), name='weight')
b = tf.Variable(tf.random_normal([3]), name='bias')


logits = tf.matmul(x,w)+b
#나온 값을 확률로 만들기 위해 softmax를 사용한다. 
hypothesis = tf.nn.softmax(logits)

#cross entropy / logits = (logits = tf.matmul(x,w)+b)
#1안 : 짧게 끊어서 코딩하기
cost_i = tf.nn.softmax_cross_entropy_with_logits(logits=logits, labels=y_one_hot)
cost = tf.reduce_mean(cost_i)

#2안: 한번에 길게 코딩하기
cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=logits, labels=y_one_hot))

#traininig 
train = tf.train.GradientDescentOptimizer(learning_rate = 0.1).minimize(cost)

#(hypothesis, 1) :1은 1차원을 의미함 (기본값은 1차원, 2일땐 2차원, 3일땐 3차원을 의미한다.)
#argmax를 이용하는 이유: 인덱스가 가장 큰 값을 return해주기 때문에 
prediction = tf.argmax(hypothesis, 1)

''' argmax를 test해보기
a1 = tf.Variable([0.1,0.3,0.5])
sess = tf.Session()
sess.run(tf.global_variables_initializer())
print(sess.run(tf.argmax(a1)))  #a1의 argmax, 즉 인덱스가 가장 큰 값을 return해줌 
print(sess.run(tf.argmin(a1)))  #a1의 argmin, 즉 인덱스가 가장 작은 값을 return해줌 
sess.close()
'''

correct_prediction = tf.equal(prediction, tf.argmax(y_one_hot, 1))

#corredction_prediction을 tf.float32로 dtype 설정하여 reduce_mean을 해줌 
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

sess = tf.Session()
sess.run(tf.global_variables_initializer())
for step in range(2001):
    sess.run(train, feed_dict={x:x_data, y:y_data})
    if step % 100 ==0:
        loss, acc = sess.run([cost, accuracy], feed_dict={x:x_data, y:y_data})
        print("Step: ", step, " Loss: ", loss," Accuracy : ",acc)

#Step:  200  Loss:  0.61006963  Accuracy :  0.625
#Step:  300  Loss:  0.5493963  Accuracy :  0.75
#Step:  400  Loss:  0.50647  Accuracy :  1.0
#Step:  500  Loss:  0.4729592  Accuracy :  1.0
#Step:  600  Loss:  0.445494  Accuracy :  1.0
#Step:  700  Loss:  0.4223158  Accuracy :  1.0
#Step:  800  Loss:  0.40235963  Accuracy :  1.0

#test1
a = sess.run(hypothesis, feed_dict={x:[[1,2,1]]})
#Out[403]: array([[9.9798632e-01, 2.0132938e-03, 3.5136199e-07]], dtype=float32)
print(a,sess.run(tf.argmax(a,1))) # [0]번 인덱스가 가장 큼   # argmax(a,1) -> argmax에서 반환되는 값은 index이다. 여기서 1은 1차원을 의미한다. 
#[[9.9798632e-01 2.0132938e-03 3.5136199e-07]] [0] 

#test2
b = sess.run(hypothesis, feed_dict={x:[[1,7,7]]})
print(b,sess.run(tf.argmax(b,1))) #[2]번 인덱스가 가장 큼 
#[[1.7023287e-04 8.4930271e-02 9.1489947e-01]] [2]

#test3
c = sess.run(hypothesis, feed_dict={x:[[1,4,5]]})
print(c,sess.run(tf.argmax(c,1))) #[1]번 인덱스가 가장 큼   
#[[0.12192319 0.7085265  0.16955036]] [1]

#train data(train.txt)에서 test1, test2는 있음 -> 알맞게 분류 / test3는 없는 데이터를 넣어 분류를 받음


# =============================================================================
