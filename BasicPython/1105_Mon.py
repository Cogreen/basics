# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 09:49:23 2018

@author: stu
"""


■ feed forward

- 입력   ->   출력
         |
        bias

y = w * x + b      
w = 2
b = 1

x   y
---------- 
0   1
1   3
2   5


- 목표 
( 입력: 1 -> 목표: 4 ) 가정하자. (입력은 고정이고, weight, bias를 조정하여 4가 나오도록 해보자)
즉, y = w * 1 + b = 4          

#cf. 기존에는 입력값, weight, bias값을 주었으나, 이제는 하나씩 값을 돌리면서 목표값이 나오도록 맞춰나가는 작업을 할 것임

#1. 다음과 같이 가정해 보자. 입력값과 bias가 고정되어 있다고 가정해보자. => weight를 수정하면서 목표를 찾는다. 
입력 = 1
bias = 1

w     출력 (목표)  
----------------- 
1     2
2     3
2.5   3.5
3     4

즉, y = w * 1 + b = 4 가 되기 위해서는 
    y = 3 *1 + 1 = 4가 되었다. 
=> weight 수정하면서 목표를 찾는다. 

#2. 다음과 같이 가정해 보자. 입력값과 weight가 고정되어 있다고 가정해보자. => bias를 수정하면서 목표를 찾는다. 
입력 = 1
weight = 2
목표 4

bias     출력(목표)
----------------------
1        2*1 + 1 = 3
1.5      2*1 + 1.5 = 3.4
2        2*1 + 2 = 4
=> bias를 수정하면서 목표를 찾는다. 


#1.#2를 위해서 => 미분(순간변화율)을 생각해보면서 오차율을 줄일 수 있도록 함 
#즉, 오차를 줄이기 위해서는 weight(기울기)를 줄여줘야함 -> 미분을 통해서 가능함 "경사하강법"
f = wx + b 
g = wx    (#g값에 영향을 주는 것은 w와 x)
f = g + b

# g = wx 
# w를 기준으로 해서 미분하면 x가 남음 (미분의 값과 x는 같다)
∂ g
----   = x 
∂ w 

# x를 기준으로 해서 미분하면 x가 남음 (미분의 값과 w는 같다)
∂ g
----   = w
∂ x 

# f = g + b
# f를 기준으로 해서 미분하면 1이 남음 (어짜피 상수는 미분하면 1; 버리는 것이기 때문에 1이 남음 )
∂ f   
----  =  1
∂ w
# g를 기준으로 해서 미분하면 1이 남음 
∂ g  
----  =  1
∂ b


#∂ F  
#----  =  1
#∂ g


■ chain rule

∂ f       ∂ f      ∂ g
----  =  -----   ------
∂ w       ∂ g      ∂ w

      =    1         x
      
∂ f       ∂ f      ∂ g
----  =  -----   ------
∂ x       ∂ g      ∂ x    (g는 f에 영향을 주고)(g는 x에 영향을 줌)
      =     1      w


■ backpropagation 역전파  (역으로 가기 위해서는 weight, bias를 조정해야 한다. -> 무엇으로? 미분으로 조정한다. ; 이를 통해 오차를 줄일 수 있다.)

- cost function
신경망 학습에서 학습데이터에 대한 오차를 측정하는 척도 

    - 평균제곱오차(mean squared error, MSE): 1/m Σ(ytarget- y)²  #tensorflow의 method: tf.reduce_mean
        :일반적으로 많이 사용한다. 
        
    - 오차 = 1/2 Σ(ytarget- y)²
        - ytarget: 목표값 
        - y: 예측값
        - minus를 하면 음수가 나올 수 있기 때문에 제곱이 필요하다. 
        - 오차를 만드는 원인: weight, bias 

import numpy as np

t = np.array([0,0,0,0,1,0,0,0,0,0])
y = np.array([0.1,0.03,0.05,0.2,0.9,0.0,0.1,0.2,0.12,0.03])

sum((t-y)**2)/2

def mse(t,y):
    return 0.5*np.sum((t-y)**2)
print("오차는",mse(t,y))

    
    
■ gradient descendent method(경사하강법); 어떻게 하면 오차를 줄일 수 있을까? (tf.train.GradientDescentOptimizer는 편미분을 자동적으로 해준다.)
 ∂E  (Error rate)
---- 
 ∂w  
 
w(weight)수정 = w - ∂E/ ∂w
    - E: Error rate
=> 기존의 weight - weight값의 미분한 값을 계속 빼면서 기울기를 내려가게 하는 방법

=> 기울기 조정은 : learning rate(α)을 주면서 weight 값을 조정해야 한다. 
w(weight)수정 = w - α *∂E/ ∂w (α: learning rate)
    - α: 미세하게 움직일지, 큼직하게 움직일지(다른쪽으로 넘어가버릴 수도 있다.) 
    

■ linear regression
입력(x)     출력(y)
------     -------
1           2
2           4
3           6
4           8
5           10
6           12

7를 입력하면 출력값은? 

y = w*x + b

2 = w + b
4 = 2w + b

import tensorflow as tf

x_data = [1,2,3,4,5,6]      #입력값
y_data = [2,4,6,8,10,12]    #실제 target 
y = w*x + b                 #여기서 y는 예측값 

x = tf.placeholder(tf.float32)
y = tf.placeholder(tf.float32)
w = tf.Variable(tf.random_normal([1], seed=0), name="weihgt")  #tf.random_normal: 한자리 난수를 가져옴, #seed=0 난수값을 고정시킴
b = tf.Variable(tf.random_normal([1], seed=0), name="bias")

hypothesis = w*x + b

cost = tf.reduce_mean(tf.square(hypothesis-y)) 
#tf.square :tensor에서 제공하는 제곱 
#tf.reduce_mean: 평균의 합 

# cost값을 조정하기 위해서는 weight, bias를 조정해야 한다. => 미분이 들어가야 한다. (미분을 통해 로직 구현을 하면 된다.)
# 경사하강법을 사용: cost를 줄이기 위해서, cost값을 조정함 
optimizer = tf.train.GradientDescentOptimizer(learning_rate = 0.001) #learning_rate는 조정해줘야 함  #GradientDescentOptimizer: 이 method를 통해 미분을 사용한다. (일반적으로 편미분을 말한다.)
#cost를 최소화 시켜줘야한다.  
train = optimizer.minimize(cost)

#즉, 위의 과정이 연쇄화처럼 돌아가게 된다. 

#session을 열어 시작 
sess = tf.Session()
sess.run(tf.global_variables_initializer())  #variable은 초기화 시켜아한다.
#for 문을 사용하여 
for step in range(2001):
    cost_v, w_v, b_v, _ = sess.run([cost, w, b, train], feed_dict={x:x_data, y:y_data}) # _:underscope는 위치자임; train에 대해 들어 갈 것이 없기 때문에  
    if step % 20 == 0:
        print(step, cost_v, w_v, b_v)

#(step, cost_v, w_v, b_v)
#0 94.1615 [-0.32358906] [-0.38156518]
#20 25.674927 [0.76995075] [-0.12730911]
#40 7.0030427 [1.3410589] [0.00492619]
#60 1.9123893 [1.639381] [0.07345283]
#80 0.5244544 [1.7952688] [0.10871811]
#.................................
#1920 0.001107541 [1.9822853] [0.0758381]
#1940 0.001091486 [1.982414] [0.07528657]
#1960 0.0010756744 [1.9825425] [0.074739]
#1980 0.0010600793 [1.9826689] [0.07419543]
#2000 0.0010447168 [1.9827952] [0.07365584]

#예측하기
print(sess.run(hypothesis, feed_dict = {x:7}))
print(sess.run(hypothesis, feed_dict = {x:10}))


# =============================================================================
# 자율학습

#learhing 숫자바꿔보기 
x_data = [1,2,3,4,5,6]      #입력값
y_data = [2,4,6,8,10,12]    #실제 target 
              #여기서 y는 예측값 
x = tf.placeholder(tf.float32)
y = tf.placeholder(tf.float32)
w = tf.Variable(tf.random_normal([1], seed=0), name="weihgt")  #tf.random_normal: 한자리 난수를 가져옴, #seed=0 난수값을 고정시킴
b = tf.Variable(tf.random_normal([1], seed=0), name="bias")

hypothesis = w*x + b

cost = tf.reduce_mean(tf.square(hypothesis-y)) 

optimizer = tf.train.GradientDescentOptimizer(learning_rate = 0.05)  #
train = optimizer.minimize(cost)
sess = tf.Session()
sess.run(tf.global_variables_initializer()) 
for step in range(2001):
    cost_v, w_v, b_v, _ = sess.run([cost, w, b, train], feed_dict={x:x_data, y:y_data}) # _:underscope는 위치자임; train에 대해 들어 갈 것이 없기 때문에  
    if step % 20 == 0:
        print(step, cost_v, w_v, b_v)
print(sess.run(hypothesis, feed_dict = {x:150}))
print(sess.run(hypothesis, feed_dict = {x:58}))
sess.close()

#dataset 바꿔보기, step 수도 바꿔보기, 등등등
x_data = [1,3,4,7,15,58]      #입력값
y_data = [2,14,26,58,89,190]  


x = tf.placeholder(tf.float32)
y = tf.placeholder(tf.float32)
w = tf.Variable(tf.random_normal([1], seed=0), name="weihgt")  #tf.random_normal: 한자리 난수를 가져옴, #seed=0 난수값을 고정시킴
b = tf.Variable(tf.random_normal([1], seed=0), name="bias")

hypothesis = w*x + b

cost = tf.reduce_mean(tf.square(hypothesis-y)) 

optimizer = tf.train.GradientDescentOptimizer(learning_rate = 0.0015)  #
train = optimizer.minimize(cost)
sess = tf.Session()
sess.run(tf.global_variables_initializer()) 
for step in range(10000):
    cost_v, w_v, b_v, _ = sess.run([cost, w, b, train], feed_dict={x:x_data, y:y_data}) # _:underscope는 위치자임; train에 대해 들어 갈 것이 없기 때문에  
    if step % 20 == 0:
        print(step, cost_v, w_v, b_v)
print(sess.run(hypothesis, feed_dict = {x:150}))
print(sess.run(hypothesis, feed_dict = {x:58}))


# =============================================================================

기울기 = 4.3
절편 = 64

공부시간     점수
-----------------
2           71
4           83
6           91
8           97

ab = [4.3, 64]      #미리 기울기와 절편값을 알고 있음 -> 따라서 predict를 할 수 있음 
data = [[2,71],[4,83],[6,91],[8,97]]

#리스트 내장객체 사용
x = [i[0] for i in data]
y = [i[1] for i in data]

#예측된 값 ab를 return값에 넣어 주기: 기울기와 절편값
def predict(x):
    return ab[0]*x + ab[1]

predict(2)  #Out[222]: 72.6

#오차 함수 만들기
RMSE(Root Mean Squared Error) 평균제곱근오차
def rmse(p,a):
    return np.sqrt(((p-a)**2).mean())

def rmse_val(predict_result, y):
    return rmse(np.array(predict_result), np.array(y))

predict_result = []
for i in range(len(x)):
    predict_result.append(predict(x[i]))
    print("공부시간 : %.f, 실제점수 : %.f, 예측점수 : %.f"%(x[i],y[i],predict(x[i])))
    
#공부시간 : 2, 실제점수 : 71, 예측점수 : 73
#공부시간 : 4, 실제점수 : 83, 예측점수 : 81
#공부시간 : 6, 실제점수 : 91, 예측점수 : 90
#공부시간 : 8, 실제점수 : 97, 예측점수 : 98    
    
print("오차 : ",rmse_val(predict_result, y))
#오차 :  1.5165750888103096


▣ 선형회귀
- 임의의 직선을 그어 이에 대한 평균제곱근오차를 구하고 이값을 가장 작게 만들어 주는 기울기와 절편을 찾아가는 작업 
- 기울기와 절편이 이미 만들어져 있을 때 
- 기울기와 절편이 없을 때 (Gradient Descent): 임의의 선을 어디에 그어야 최적인지(오차를 최소로 줄일 수 있는지)의 작업 -> 이에 알맞는 기울기와 절편을 구하기

# =============================================================================
# 기울기와 절편이 없을 때 wieght, bias 구하기: 평균제곱오차 적용시(편차제곱 합의 평균) 
# 스스로 해 보기 
data = [[2,71],[4,83],[6,91],[8,97]]
x_data = [i[0] for i in data]
y_data = [i[1] for i in data]

x = tf.placeholder(tf.float32)
y = tf.placeholder(tf.float32)
w = tf.Variable(tf.random_normal([1], seed=0), name="weihgt")  #tf.random_normal: 한자리 난수를 가져옴, #seed=0 난수값을 고정시킴
b = tf.Variable(tf.random_normal([1], seed=0), name="bias")

hypothesis = w*x + b

cost = tf.reduce_mean(tf.square(hypothesis-y)) 

optimizer = tf.train.GradientDescentOptimizer(learning_rate = 0.001)  #
train = optimizer.minimize(cost)
sess = tf.Session()
sess.run(tf.global_variables_initializer()) 
for step in range(20001):
    cost_v, w_v, b_v, _ = sess.run([cost, w, b, train], feed_dict={x:x_data, y:y_data}) # _:underscope는 위치자임; train에 대해 들어 갈 것이 없기 때문에  
    if step % 20 == 0:
        print("Step: %.f, Cost = %.f, 기울기 w = %.f, 절편 b = %.f"%(step, cost_v, w_v, b_v))

#Step: 20000, Cost = 2, 기울기 w = 4, 절편 b = 64

print(sess.run(w))  #[4.3158374]
print(sess.run(b))  #[63.905476]
print(sess.run(hypothesis, feed_dict = {x:2}))  #[81.16882]
print(sess.run(hypothesis, feed_dict = {x:4}))  #[81.16882]
print(sess.run(hypothesis, feed_dict = {x:6}))  #[89.8005]
print(sess.run(hypothesis, feed_dict = {x:8}))  #[98.432175]

sess.close()

# =============================================================================
# 기울기와 절편이 없을 때 wieght, bias 구하기: 평균제곱근오차를 사용하여 
# 스스로 해 보기 
data = [[2,71],[4,83],[6,91],[8,97]]
x_data = [i[0] for i in data]
y_data = [i[1] for i in data]

#x = tf.placeholder(tf.float32)
#y = tf.placeholder(tf.float32)
w = tf.Variable(tf.random_normal([1], seed=0), name="weihgt")  #tf.random_normal: 한자리 난수를 가져옴, #seed=0 난수값을 고정시킴
b = tf.Variable(tf.random_normal([1], seed=0), name="bias")

predict = w*x_data + b

#오차 함수 만들기
#RMSE(Root Mean Squared Error) 평균제곱근오차
rmse = tf.sqrt(tf.reduce_mean(tf.square(predict-y_data)))


optimizer = tf.train.GradientDescentOptimizer(learning_rate = 0.01)
train = optimizer.minimize(rmse)  #rmse = cost 


# learning_rate = 0.1
#gradeint_decent = tf.train.GradientDescentOptimizer(learning_rate).minimize(rmse)

with tf.Session() as Sess:
    sess.run(tf.global_variables_initializer())
    for step in range(20001):
        sess.run(train)
        if step%20 ==0:
            print("Step: %f, RSME = %.f, 기울기 w = %.f, 절편 b = %.f"%(step, sess.run(rmse), sess.run(w), sess.run(b)))
 
#learning_rate = 0.001일때            
#Step: 20000.000000, RSME = 22, 기울기 w = 13, 절편 b = 10

#learning_rate = 0.01일때   
#Step: 20000.000000, RSME = 2, 기울기 w = 4, 절편 b = 64



# =============================================================================
# 기울기와 절편이 없을 때 wieght, bias 구하기: 평균제곱오차 적용시(편차제곱 합의 평균) 
            
# 선생님 버전 : learning_rate -> 0.1 / learning_rate -> 0.001 등 learning_rate의 튜닝과  (제곱근이 안되어있기 때문에 값이 크기 때문에 작은 값으로 곱해야한다. learning_rate를 작게 해보자!)
#            range(10001)로 수정해 보자
data = [[2,71],[4,83],[6,91],[8,97]]
x_data = [i[0] for i in data]
y_data = [i[1] for i in data]

x = tf.placeholder(tf.float32)
y = tf.placeholder(tf.float32)
w = tf.Variable(tf.random_normal([1], seed=0), name="weihgt")  #tf.random_normal: 한자리 난수를 가져옴, #seed=0 난수값을 고정시킴
b = tf.Variable(tf.random_normal([1], seed=0), name="bias")

hypothesis = w*x + b

cost = tf.reduce_mean(tf.square(hypothesis-y)) 

# learning_rate =0.1 , range(2001) 로 했을 때 
optimizer = tf.train.GradientDescentOptimizer(learning_rate = 0.1)  #
train = optimizer.minimize(cost)
sess = tf.Session()
sess.run(tf.global_variables_initializer()) 
for step in range(2001):
    cost_val, w_val, b_val, _ = sess.run([cost, w, b, train], feed_dict={x:x_data, y:y_data}) # _:underscope는 위치자임; train에 대해 들어 갈 것이 없기 때문에  
    if step % 20 == 0:
        print("Step: %.f, Cost = %.f, 기울기 w = %.f, 절편 b = %.f"%(step, cost_val, w_val, b_val))
#Step: 2000, Cost = nan, 기울기 w = nan, 절편 b = nan
    

# learning_rate =0.001 , range(10001) 로 했을 때 
optimizer = tf.train.GradientDescentOptimizer(learning_rate = 0.001)  #
train = optimizer.minimize(cost)
sess = tf.Session()
sess.run(tf.global_variables_initializer()) 
for step in range(10001):
    cost_val, w_val, b_val, _ = sess.run([cost, w, b, train], feed_dict={x:x_data, y:y_data}) # _:underscope는 위치자임; train에 대해 들어 갈 것이 없기 때문에  
    if step % 1000 == 0:
        print(step, cost_val, w_val, b_val)
#10000 3.272409 [4.7046027] [61.585506]

print(sess.run(hypothesis, feed_dict= {x:7}))
#[94.51773]

# =============================================================================
# 기울기와 절편이 없을 때 wieght, bias 구하기: 평균제곱근오차를 사용하여 
#선생님 버전: learning_rate -> 0.1
data = [[2,71],[4,83],[6,91],[8,97]]
x_data = [i[0] for i in data]
y_data = [i[1] for i in data]

x = tf.placeholder(tf.float32)
y = tf.placeholder(tf.float32)
w = tf.Variable(tf.random_normal([1], seed=0), name="weihgt")  #tf.random_normal: 한자리 난수를 가져옴, #seed=0 난수값을 고정시킴
b = tf.Variable(tf.random_normal([1], seed=0), name="bias")

hypothesis = w*x_data + b
rmse = tf.sqrt(tf.reduce_mean(tf.square(hypothesis-y)))

optimizer = tf.train.GradientDescentOptimizer(learning_rate = 0.1)
train = optimizer.minimize(rmse)

sess = tf.Session()
sess.run(tf.global_variables_initializer())
for step in range(2001):
    rmse_val, w_val, b_val, _ = sess.run([rmse, w, b, train], feed_dict={x:x_data, y:y_data})
    if step%100 == 0:
        print(step, rmse_val, w_val, b_val)
# 2000 1.517429 [4.2952394] [63.972393]
        
print(sess.run(hypothesis, feed_dict= {x:7}))
#[72.562874 81.15335  89.74383  98.334305]

#learning_rate  -> 0.001로 넣을 때 (제곱근을 해버리니깐 값이 엄청 작아져, learning_rate을 작은값으로 곱할 경우 값이 나오지 않게 된다.)
optimizer = tf.train.GradientDescentOptimizer(learning_rate = 0.0001)
train = optimizer.minimize(rmse)

sess = tf.Session()
sess.run(tf.global_variables_initializer())
for step in range(2001):
    rmse_val, w_val, b_val, _ = sess.run([rmse, w, b, train], feed_dict={x:x_data, y:y_data})
    if step%100 == 0:
        print(step, rmse_val, w_val, b_val)
# 2000 38.879887 [9.352289] [1.5858985]
        
print(sess.run(hypothesis, feed_dict= {x:7}))
#[20.290478 38.995056 57.699635 76.40421 ]


# =============================================================================
# 문제 linear regression 학습을 통해서 입력값에 대한 예측값을 출력하세요. 
# 
# x1 x2 x3   y
# --------------
# 73 80 75  152
# 93 88 93  185
# 89 92 90  180
# 96 98 100 196
# 73 66 70  142
#
#print("당신의 점수는 ", sess.run(hypothesis, feed_dict = {x1: 100, x2: 70, x3: 60}))
#
#힌트: y = w1 * x1 + w2 * x2 + w3 * x3 + b 
# x1,x2,x3는 확정된 값
# w1, w2, w3, b는 정해야 하는 값 
# =============================================================================

x1_data = [73, 93, 89, 96, 73]
x2_data = [80, 88, 92, 98, 66]
x3_data = [75, 93, 90, 100 , 70]
y_data = [152, 185, 180, 196, 142]


x1 = tf.placeholder(tf.float32)     # data를 run 시점에 넣을 것임
x2 = tf.placeholder(tf.float32)
x3 = tf.placeholder(tf.float32)

y = tf.placeholder(tf.float32)

w1 = tf.Variable(tf.random_normal([1], seed=0), name="weihgt1")  #tf.random_normal: 한자리 난수를 가져옴, #seed=0 난수값을 고정시킴
w2 = tf.Variable(tf.random_normal([1], seed=0), name="weihgt2") 
w3 = tf.Variable(tf.random_normal([1], seed=0), name="weihgt3") 
b = tf.Variable(tf.random_normal([1], seed=0), name="bias")
    

hypothesis = w1 * x1 + w2 * x2 + w3 * x3 + b 

cost = tf.reduce_mean(tf.square(hypothesis-y))
#rmse = tf.sqrt(tf.reduce_mean(tf.square(hypothesis-y)))

# ====================learning_rate = 0.00001
optimizer = tf.train.GradientDescentOptimizer(learning_rate = 0.00001)
train = optimizer.minimize(cost)

sess = tf.Session()
sess.run(tf.global_variables_initializer())
for step in range(100001):
    cost_val, hy_val, _ = sess.run([cost, hypothesis, train], feed_dict={x1:x1_data, x2:x2_data, x3:x3_data, y:y_data})
    if step%10000 == 0:
        print(step, cost_val, hy_val)    
#값이 nan 나오면 큼직하게 내려가다가 그래프 선상에서 바깥으로 나오기 때문에 학습률을 줄이는 작업을 해야한다.

#0 75768.92 [ -91.40709  -109.76834  -108.57087  -117.751495  -83.8231  ]
#10000 0.44027776 [151.09657 184.69226 180.8661  196.54204 141.50345]
#20000 0.40287417 [151.0501  184.73642 180.86674 196.42232 141.66388]
#30000 0.38355592 [151.08208 184.72041 180.89647 196.3423  141.72395]
#40000 0.37186092 [151.11092 184.70503 180.92105 196.2812  141.76672]
#50000 0.36473194 [151.13353 184.69293 180.94005 196.23404 141.79967]
#60000 0.3603143 [151.15121 184.68349 180.95462 196.19768 141.82513]
#70000 0.3575406 [151.16498 184.67606 180.96576 196.16953 141.84485]
#80000 0.3557214 [151.17549 184.67049 180.97414 196.14772 141.86053]
#90000 0.35449666 [151.18388 184.666   180.98055 196.13098 141.8725 ]
#100000 0.35361928 [151.19038 184.66255 180.98532 196.11807 141.8819 ]    

print("당신의 점수는 ", sess.run(hypothesis, feed_dict = {x1: 100, x2: 70, x3: 60}))
#당신의 점수는  [166.4719]


# ====================learning_rate = 0.000001
optimizer = tf.train.GradientDescentOptimizer(learning_rate = 0.000001)
train = optimizer.minimize(cost)

sess = tf.Session()
sess.run(tf.global_variables_initializer())
for step in range(100001):
    cost_val, hy_val, _ = sess.run([cost, hypothesis, train], feed_dict={x1:x1_data, x2:x2_data, x3:x3_data, y:y_data})
    if step%10000 == 0:
        print(step, cost_val, hy_val)    
        
print("당신의 점수는 ", sess.run(hypothesis, feed_dict = {x1: 100, x2: 70, x3: 60}))
#당신의 점수는  [160.70312]


# =============================================================================

#확인하기: weight 값을 출력하면 왜 이렇게 나오나요?
#for step in range(100001):
#    cost_val, hy_val, w1_val, w2_val, w3_val, _ = sess.run([cost, hypothesis, w1, w2, w3, train], feed_dict={x1:x1_data, x2:x2_data, x3:x3_data, y:y_data})
#    if step%10000 == 0:
#        print(step, cost_val, hy_val, w1_val, w2_val, w3_val)    
#60000 0.41393796 [151.04512 184.73627 180.85684 196.46237 141.62534] [0.92375475] [0.44092336] [0.64937156]
#70000 0.41083837 [151.04492 184.73756 180.85886 196.4515  141.63716] [0.92733103] [0.44155437] [0.64519924]
#80000 0.40793252 [151.04628 184.73743 180.86139 196.44104 141.64697] [0.93061006] [0.4424184] [0.6410882]
#90000 0.40531117 [151.04822 184.73692 180.86409 196.43153 141.65564] [0.9335903] [0.44331247] [0.6372439]
#100000 0.40274936 [151.05019 184.73643 180.86679 196.42203 141.66429] [0.9365705] [0.44420654] [0.63340026]

# =============================================================================
#hypothesis = w1 * x1 + w2 * x2 + w3 * x3 + b 를 행렬의 곱으로 개선시키려고 함
# x의 열과[None, 3], w[3, 1]의 행의 값을 맞추도록 한다.  -> 따라서 y는 [None, 1] 이 됨

x_data = [[73,80,75],[93,88,93],[89,91,90],[96,98,100],[73,66,70]]
y_data = [[152],[185],[180],[196],[142]]

x = tf.placeholder(tf.float32, shape=[None,3]) #shape의 None이 되어있을 경우는, 몇행이 들어올지 모르는 상황일 때/ 열은 3열로 고정됨  #모든 행의 3열
y = tf.placeholder(tf.float32, shape=[None,1]) #모든 행의 1열

#[3,1] 3:x의(열값) 들어오는 값 / 1: y로 나가는 값 
w = tf.Variable(tf.random_normal([3,1], seed=0), name='weight') #weight값은 난수값, x의 shape의 열에 맞춰 weight값을 맞춘다. [3,1] 
#[1] 1: y로 나가는값 
b = tf.Variable(tf.random_normal([1], seed=0), name= 'bias')

hypothesis = tf.matmul(x,w)+b

cost = tf.reduce_mean(tf.square(hypothesis-y))
optimizer = tf.train.GradientDescentOptimizer(learning_rate = 0.000001)
train = optimizer.minimize(cost)

sess = tf.Session()
sess.run(tf.global_variables_initializer())
for step in range(100001):
    cost_val, hy_val, _ = sess.run([cost, hypothesis, train], feed_dict={x:x_data, y:y_data})
    if step%10000 == 0:
        print(step, cost_val, hy_val)    
        
print("당신의 점수는 ", sess.run(hypothesis, feed_dict = {x: [[100,70,60]]}))

# =============================================================================
data는 file자체로 있기 때문에 파일에 있는 데이터를 불러들이도록 해야한다. 

#파일유형 = 모든 텍스트 / 파일명 = 1105ex.csv 로 저장한 다음
73,80,75, 152
93,88,93, 185
89,91,90, 180
96,98,100, 196
73,66,70, 142

import tensorflow as tf
import numpy as np

#numpy로 data불러들이기: np.loadtxt()
xy = np.loadtxt("c:/data/1105ex.csv", delimiter=",", dtype=np.float32) #delimiter="," 구분자/ dtype=np.float32 불러들일 데이터 형식
xy
#array([[ 73.,  80.,  75., 152.],
#       [ 93.,  88.,  93., 185.],
#       [ 89.,  91.,  90., 180.],
#       [ 96.,  98., 100., 196.],
#       [ 73.,  66.,  70., 142.]], dtype=float32)

#slicing하기  (슬라이싱 할 때 주의할 점) -> 목표변수 만들기
x_data = xy[:,0:-1]
#Out[473]: 
#array([[ 73.,  80.,  75.],
#       [ 93.,  88.,  93.],
#       [ 89.,  91.,  90.],
#       [ 96.,  98., 100.],
#       [ 73.,  66.,  70.]], dtype=float32)
y_data = xy[:,[-1]]
#Out[477]: 
#array([[152.],
#       [185.],
#       [180.],
#       [196.],
#       [142.]], dtype=float32)
x_data.shape     #Out[478]: (5, 3)
y_data.shape     #Out[479]: (5, 1)

# *** 슬라이싱 주의사항 *****  ######
#y_data = xy[:,-1] 로 하게 되면 1행의 5열로 만들어짐  (1행 5열)  Out[475]: array([152., 185., 180., 196., 142.], dtype=float32)
#y_data = xy[:,[-1]] 로 하게 되면 5행 1열로 만들어짐 (5행 1열)

# run time 시점에 x, y 데이터를 넣기 위해 placeholder를 만듦 
x = tf.placeholder(tf.float32, shape=[None,3])
y = tf.placeholder(tf.float32, shape=[None,1])

#weight값, bias값 
w = tf.Variable(tf.random_normal([3,1], seed=0), name='weight')
b = tf.Variable(tf.random_normal([1], seed=0), name='bias')

hypothesis = tf.matmul(x,w)+b

cost = tf.reduce_mean(tf.square(hypothesis-y))
optimizer = tf.train.GradientDescentOptimizer(learning_rate = 0.000001)
train = optimizer.minimize(cost)

sess = tf.Session()
sess.run(tf.global_variables_initializer())
for step in range(100001):
    cost_val, hy_val, _ = sess.run([cost, hypothesis, train], feed_dict={x:x_data, y:y_data})
    if step%10000 == 0:
        print(step, cost_val, hy_val)    
#90000 0.18888655 [[151.4298 ]
# [184.67465]
# [180.66763]
# [196.22499]
# [141.86926]]
#100000 0.18839629 [[151.43077]
# [184.67445]
# [180.66846]
# [196.22124]
# [141.87273]]        

print("당신의 점수는", sess.run(hypothesis, feed_dict ={x:[[100,70,60]]}))
#여러 명의 값을 구하고자 할 때 
print("당신의 점수는", sess.run(hypothesis, feed_dict ={x:[[100,70,60], [90,100,80]]}))

