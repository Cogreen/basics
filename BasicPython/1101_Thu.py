# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 10:01:09 2018

@author: stu
"""


# =============================================================================

■ 은닉층(Hidden layers)
x1      x2      or(s1)      nand(s2)        and  y
----------------------     ------------   -----------
0       0       0              1              0
0       1       1              1              1
1       0       1              1              1
1       1       1              0              0


y = ax + b

■ bias(편향)
가중치와 편향을 도입한 퍼셉트론식 
Θ를 -b로 치환하면 
y = a1x1 + a2x2 + b 

y = 0  w1*x1 + w2*x2  <= Θ
y = 1  w1*x1 + w2*x2  >  Θ

y = 0  w1*x1 + w2*x2  <= -b
y = 1  w1*x1 + w2*x2  >  -b

#퍼셉트론식, 신경망의 식 
y = 0  w1*x1 + w2*x2 + b  <= 0
y = 1  w1*x1 + w2*x2 + b  >  0

import numpy as np

x = np.array([0,1])
w = np.array([0.5,0.5])
b = -0.7

x[0]*w[0]+x[1]*w[1]+b
np.sum(x*w)+b

def OR(x1,x2): 
    x = np.array([x1,x2])
    w = np.array([0.5,0.5])
    b = -0.2
    tmp = np.sum(w*x)+b
    if tmp <= 0:
        return 0
    else:
        return 1
    
OR(0,0)
OR(0,1)
OR(1,0)
OR(1,1)

#bias값이 달라지면 값이 달라진다.
def AND(x1,x2): 
    x = np.array([x1,x2])
    w = np.array([0.5,0.5])
    b = -0.7
    tmp = np.sum(w*x)+b
    if tmp <= 0:
        return 0
    else:
        return 1
    
AND(0,0)
AND(0,1)
AND(1,0)
AND(1,1)

#bias값의 조정을 어떻게 하느냐, weight값을 어떻게 조정하느냐에 따라 함수가 달라질 수 있다.

def NAND(x1,x2): 
    x = np.array([x1,x2])
    w = np.array([-0.5,-0.5])
    b = 0.7
    tmp = np.sum(w*x)+b
    if tmp <= 0:
        return 0
    else:
        return 1
    
NAND(0,0)
NAND(0,1)
NAND(1,0)
NAND(1,1)

def XOR(x1, x2):
  s1 = OR(x1,x2)
  s2 = NAND(x1, x2)
  y = AND(s1, s2)
  return y

XOR(0,0) 
XOR(0,1)
XOR(1,0)
XOR(1,1)


▣ 인공신경망(ANN, Artificial Neural Network)
인간의 뇌구조를 모방하여 모델링한 수학적 모델이다. 

■ 신경세포(Neuron 뉴런)
- 뉴런의 입력은 다수이고 출력은 하나이며, 여러 신경세포로 부터 전달되어 온 신호들은 합산되어 출력된다.
- 합산된 값이 설정값(threshold) 이상이면 출력신호가 생기고 이하이면 출력신호가 없다.
- 세포체(cell body) - 노드(node)
- 수상돌기(dendrites) - 입력(input)
- 축삭(axon) - 출력(output)
- Synapse weight (가중치)


 affine sum: 최종적 output을 내기 위해 모든 값을 sum 값 (밑의 sum)
 
            weight w
- input x ----------------> sum(σ) ------------> output y
                
                             ^
                             |
                            bias
                
σ = w*x + b = 0.6*3 + 1 = 2.8
x = 0.6
w= 3
b =1

affine sum이 너무 작으면 신호를 보내지 못하기 때문에, activate function을 적용해 신호의 크기를 크게 해줘야 한다. 


▣ 활성화 함수(actvatio function)
- synapse는 전달된 전기신호가 최소한의 작은 자극값을 초과하여 활성화되어 다음 뉴런으로 전기신호를 전달한다.
- 활성화 함수는 이것을 모방하여 값이 작을 때는 출력값을 작은값으로 막고 일정한 값을 초과하면 출력값이 급격하게 커지는 함수를 이용한다.
- 신경망에서는 전달받은 데이터를 가중치를 고려해서 합산하고 그값을 활성화함수f(σ)를 적용해 다음층에 전달한다. 
            weight w
- input x ----------------> σ|f(σ) ------------> output y
                
                             ^
                             |
                            bias
σ = w*x + b
f(σ) = f(w*x + b) #활성화 함수안에는 affine sum의 값이 들어가 있어야 한다. 

■ 은닉층 함수
□ 계단함수(Binary step function)
- 임계값을 경계로 출력이 바뀌는 함수
- 입력이 0을 넘으면 1을 출력하고 그외에는 0을 출력하는 함수 
- (activaiton function을 통해서 다음 출력값을 0, 1으로 출력하게 한다)

#그냥 집어넣을 때는 문제가 되지 않지만, array형식으로 x값을 넣을 경우 문제가 된다. 오류가 생긴다.! 
def step_function(x):
    if x > 0:
        return 1
    else:
        return 0
    
import numpy as np
step_function(1)
#Out[66]: 1
step_function(-1)
#Out[67]: 0

#array형식에 x입력값을 넣었을 때 -> 오류 발생 
step_function(np.array([1,2]))
x = np.array([-1.0,1.0,2.0])
y = x > 0
#Out[73]: array([False,  True,  True])

★ astype: 자료형변화 (bool -> int)
                    #True: 1, False: 0
y.astype(np.int)
#Out[74]: array([0, 1, 1])

#방법1) array형식으로 x입력값을 넣었을 때 -> 함수가 올바르게 수행하기 위해 astype을 사용한다. 
def step_function(x):
    y = x > 0
    return y.astype(np.int)

step_function(np.array([-1.0,1.0,2.0]))
#Out[78]: array([0, 1, 1])

#방법2) array형식으로 x입력값을 넣었을 때 -> 함수가 올바르게 수행하기 위해 
def step_function(x):
    return np.array(x> 0, dtype=np.int) #boolean 형식을 integer값으로 바꿔 array로 전달해줌
step_function(np.array([-1.0,1.0,2.0]))
#Out[80]: array([0, 1, 1])

#step_function을 plot으로 보기
import matplotlib.pylab as plt
x = np.arange(-5.0,5.0,0.1)
y = step_function(x)
plt.plot(x,y)
plt.ylim(-0.1,1.1)
plt.show

□ Sigmoid(시그모이드)
신경망에서는 활성화 함수로 시그모이드 함수를 이용하여 함수를 변환하고 그 변환된 신호를 다음 뉴런에 전달하는 함수이다. 
e-x (x승): e는 자연상수 2.7182.....
np.exp(-x)

def sigmoid(x):
    return 1/(1+np.exp(-x))

-> affine sum 값을 x에 넣는다. 
sigmoid함수는 0에 근사한 값을/ 1에 근사한 값을 출력한다. 

sigmoid(1)  #Out[87]: 0.7310585786300049
sigmoid(-1) 
sigmoid(100)  #Out[89]: 1.0
sigmoid(-100) #Out[91]: 3.7200759760208356e-44 
sigmoid(1000) #Out[98]: 1.0
sigmoid(-10000) #Out[95]: 0.0

x = np.arange(-5.0, 5.0, 0.1)  #-5.0, 5.0, 0.1: affine sum의 결과
y= sigmoid(x)
plt.plot(x,y)
plt.ylim(-0.1,1.1)
plt.grid()
plt.show()

□ 계단함수와 시그모이드 함수의 비교
- 계단함수는 0과 1중 하나의 값만 전달 
- 시그모이드는 함수는 0과 1사이의 실수값을 전달 
- 시그모이드 함수는 곡선
- 계단 함수는 계단처럼 구부러진 직선 
- (신경망에서는 계단함수보다는 시그모이드함수가 좋다. 왜냐하면 비선형구조를 만들 수 있기 때문에)
- 선형함수는 직선 하나만 표현
- 신경망에서는 활성함수로 비선형함수를 사용해야한다.
- 비선형함수를 사용해야 은닉층을 표현할 수 있다. 


□ ReLU(Rectified Linear Unit)
- 입력이 0을 넘으면 그 입력값으로 그대로 출력하고 0이하면 0을 출력한다. 

x: x > 0  (x값이 0보다 크면 x를 return해 주고)
0: x <= 0 (x값이 0하고 같거나 작으면 0으로 return해 준다.)

def ReLU(x):
    if x > 0:
        return x
    else:
        return 0

ReLU(3.2)
ReLU(-2)
ReLU(np.array([3.2,2.5,-0.2])) #오류발생 

★ np.maximum() :두 입력중에 큰값을 선택해 변환하는 함수
np.maximum(0,1) :두 입력중에 큰값을 선택해 변환하는 함수
np.maximum(0,-1)

def ReLU(x):
    return np.maximum(0,x)

ReLU(3.2) #Out[128]: 3.2
ReLU(-2)  #Out[129]: 0
ReLU(np.array([3.2,2.5,-0.2]))  #Out[130]: array([3.2, 2.5, 0. ])

x = np.arange(-5.0,5.0,0.1)
y = ReLU(x)
plt.plot(x,y)
plt.ylim(-0.1,6)
plt.show()

# =============================================================================

import numpy as np
a = np.array([1,2,3,4])
a
#배열의 차수 
np.ndim(a)
#배열의 모양
a.shape 

#3행 2열
x = np.array([[1,2],[3,4],[5,6]])
np.ndim(x)
x.shape

# =============================================================================

x     y      z(행렬의 내적 계산)
1 2   5 6   1*5+2*6  1*6+2*8   5+14  6+16     19  22
3 4   7 8   3*5+4*7  3*6+4*8   15+28 18+32    43  50

x = np.array([[1,2],[3,4]])
y = np.array([[5,6],[7,8]])
x.shape  #Out[156]: (2, 2) 
y.shape  #Out[157]: (2, 2)

# 행렬의 내적계산이 가능한 행렬모형 고려하기 : x의 열 벡터 = y의 행 벡터
# shape = 행 벡터 x 열 벡터

#행렬의 내적계산
np.dot(x,y)


#x       y
1 2 3   1 2
4 5 6   3 4
        5 6 

x = np.array([[1,2,3],[4,5,6]])
y = np.array([[1,2],[3,4],[5,6]])
x.shape #Out[163]: (2, 3): 2행 x 3열 
y.shape #Out[164]: (3, 2): 3행 x 2열 
#2행 x 3열 - 3행 x 2열 -> 2행 2열 
np.dot(x,y)
#Out[165]: 
#array([[22, 28],
#       [49, 64]])

#x   y
1 2  7 8 
3 4
5 6 
#cf 입력값은 x처럼, wieght값은 y처럼 주기 때문에 [7,8] 

# =============================================================================

x = np.array([[1,2],[3,4],[5,6]]) 
y = np.array([7,8])  #1차원이기 때문에 (행렬을 반영하지 않고) 그대로 차수만 반영한다. 
x.shape  #Out[169]: (3, 2)
y.shape  #Out[170]: (2,) 
np.dot(x,y) #Out[171]: array([23, 53, 83])

#입력값을 1,2로  하고 weight을 [1,3,5],[2,4,6]으로 뒀을 때 
x = np.array([1,2])
w = np.array([[1,3,5],[2,4,6]])
x.shape
w.shape
y = np.dot(x,w) #Out[194]: array([ 5, 11, 17])

# =============================================================================

x = np.array([1.0,0.5]) #입력층
w1 = np.array([[0.1,0.3,0.5],[0.2,0.4,0.6]]) #wieght
b1 = np.array([0.1,0.2,0.3]) #bias
a1 = np.dot(x,w1) + b1 #affine sum

z1 = sigmoid(a1) #activation function

w2 = np.array([[0.1,0.4],[0.2,0.5],[0.3,0.6]])
b2 = np.array([0.1,0.2])
a2 = np.dot(z1, w2) +b2 #Out[226]: array([0.58597175, 1.37965826])
z2 = sigmoid(a2) #Out[220]: array([0.64244035, 0.79893611])

w3 = np.array([[0.1,0.3],[0.2,0.4]])
b3 = np.array([0.1,0.2])
a3 = np.dot(z2,w3) +b3

■ 출력층 함수
□ 항등함수: 입력을 그대로 출력한다. 입력 = 출력
def indentify_function(x):
    return x

y = indentify_function(a3) #Out[239]: array([0.32403126, 0.71230655])

□ softmax function: 지수값으로 출력한다. 
a = np.array([0.3, 2.9, 4.0])  #마지막 최종결과라고 a라고 가정할 때
exp_a = np.exp(a) #지수함수
sum_exp_a = np.sum(exp_a)
exp_a / sum_exp_a #비율값으로 계산하면 좋다. #Out[244]: array([0.01821127, 0.24519181, 0.73659691])
#cf. 분류를 할 때는 항등함수보다 softmax function을 사용하는 것이 좋다. 
#cf. 예측할 때는 항등함수를 사용하는 것이 좋다. 그대로 값을 사용하면 되면 된다. 

def softmax_function(x):
    exp_x = np.exp(x)
    sum_exp_x = np.sum(exp_x)
    return exp_x / sum_exp_x

#지금 softmax_function의 한계와 주의점: 지수로 값이 들어갈 경우의 문제 -> 숫자가 너무 커져 overhead(overflow)가 되어 1000,10000숫자까지는 계산이 안되어 infinite가 된다. / 지수계산을 하다보니 컴퓨터의 부하를 준다. 
a = np.array([100,1000,10000])
softmax_function(a)
#C:/Users/stu/Desktop/cogreen/note/1101_Thu.py:4: RuntimeWarning: invalid value encountered in true_divide
#  
#Out[248]: array([ 0., nan, nan])


#softmax function 수정: 지수의 문제를 해결하기 위해 가장 큰 값으로 빼주면 된다. 
def softmax_function(x):
    m = np.max(x)
    exp_x = np.exp(x-m)
    sum_exp_x = np.sum(exp_x)
    return exp_x / sum_exp_x

a = np.array([100,1000,10000])
softmax_function(a)

▣ 은닉층에서 사용하는 함수와 출력층에서 사용하는 함수는 다르다. 
■ 은닉층: step function/ sigmoid function/ ReLU function 
■ 출력층: 항등함수/ softmax function     

