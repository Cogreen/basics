# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 09:52:59 2018

@author: stu
"""


# =============================================================================
# 복습
# =============================================================================


■ output layer 
활성화 함수 

- 회귀(regression): 항등함수(indentify function); 그대로 값을 return해줄 때 사용
- 분류(classification): softmax function
(만약에 개/고양이 분류라면 2개의 출력값이 필요, 0~9까지의 숫자 분류라면 10개의 출력값이 필요)
- 분류 문제에서 출력층의 node수는 분류하고 싶은 클래스 수로 설정하면 된다. 

■  softmax function
- 출력값으로 확률 벡터로 나온다. 
- 

#softmax function 수정: 지수의 문제를 해결하기 위해 가장 큰 값으로 빼주면 된다. 
def softmax_function(x):
    m = np.max(x)
    exp_x = np.exp(x-m)
    sum_exp_x = np.sum(exp_x)
    return exp_x / sum_exp_x


# =============================================================================
# 오늘 수업 (11.02) 
# =============================================================================

▣ TensorFlow
- 구글이 오픈소스로 공개한 머신러닝(machine learning)라이브러리
- 다차원행렬계산(tensor), 대규모 숫자계산 작업을 수행한다.
- 딥러닝을 비롯한 여러 머신러닝에 사용되는 라이브러리 제공
- C++로 만들어진 라이브러리 (cf. C계열 언어는 하드웨어를 제어할 수 있기 때문에 프로그램 개발자로서는 유용한 언어다. 나중에라도 공부해라 애들아!)
- PYTHON 지원한다. 

> Anaconda Prompt
pip install --upgrade tensorflow 
pip install --upgrade tensorflow-gpu

>spyder 
import tensorflow as tf
tf.__version__

#tensorflow의 상수값 지정(변할 수 없음)
tensor = tf.constant("tensorflow")  #tensorflow에서 사용하는 상수/ 변수
tensor #Out[6]: <tf.Tensor 'Const_1:0' shape=() dtype=string>  -> 객체모양으로 출력 
print(tensor) #Tensor("Const_1:0", shape=(), dtype=string) #Const_1: 상수의 약자 

cf.python의 변수와 tensorflow의 변수와는 다름
#tensor = "tnesorflow" #python의 변수임  /#주의 파이썬의 변수로 동작

#print(tensor) 를 해도 값이 나오지 않고 flow를 만들어야 함, #즉 변수를 조작하기 위해서는 세션을 시작해야한다. 
■ 세션시작 
- 클라이언트 프로그램이 텐서플로 런터임 시스템과 통신하기 위해서는 세션이 생성되어야 한다. 

#세션 시작
sess = tf.Session() #plsql에서 처럼 cursor를 열었던 것처럼 조작하기 위해 session을 열어야 한다.
sess.run(tensor)    #변수 안에 있는 내용을 실행시킴 -> 이때 화면에 출력함 
#세션 끝
sess.close()

#============================
#상수 선언
a = tf.constant(1234)
b = tf.constant(5678)

add_op = a+b
add_op      #Out[18]: <tf.Tensor 'add:0' shape=() dtype=int32> #tensor 객체정보

sess = tf.Session()
sess.run(add_op)        #Out[20]: 6912
sess.run([a,b,add_op])  #Out[21]: [1234, 5678, 6912]
sess.close()

#==============================
a = tf.constant(1)
b = tf.constant(2)
c = tf.constant(3)
x1 = a+b*c
x2 = (a+b)*c
sess = tf.Session()
z1 = sess.run(x1)
z2 = sess.run(x2)
z1
z2
sess.close()

#==============================
#assign을 사용해 v를 x1으로 치환하기 
a = tf.constant(120, name="a") #name="a" # bias값인지 weight값인지 알기 우해 name에 이름을 만들 수 있는 옵션이다.
b = tf.constant(130, name="b")
c = tf.constant(140, name="c")
#변수: Variable
v = tf.Variable(0, name="v")
x1 = a+b+c
assign_op = tf.assign(v,x1) #x1식을 v에 변수 복제함 
sess = tf.Session()
sess.run(assign_op)     #Out[47]: 390
#v변수에 들어가 있는 값 확인하기 
sess.run(v)             #Out[48]: 390
sess.run(x1)            #Out[49]: 390
sess.close()

#==============================
#assign을 사용하지 않고 치환해보기 
a = tf.constant(120, name="a") #name="a" # bias값인지 weight값인지 알기 우해 name에 이름을 만들 수 있는 옵션이다.
b = tf.constant(130, name="b")
c = tf.constant(140, name="c")
#변수: Variable
v = tf.Variable(0, name="v")
x1 = a+b+c
v = x1
#assign_op = tf.assign(v,x1) #x1식을 v에 변수 복제함 
sess = tf.Session()
#sess.run(assign_op)     #Out[47]: 390
#v변수에 들어가 있는 값 확인하기 
sess.run(v)             #Out[48]: 390
sess.run(x1)            #Out[49]: 390
sess.close()

#==============================
x = tf.Variable([[1,2,3],[4,5,6]])  #2x3
y = tf.Variable([[1,2],[3,4],[5,6]])    #3x2
z = tf.Variable(0)
z = tf.matmul(x,y)      #2x2
sess = tf.Session()
sess.run(z)  #에러 -> 상수가 아니라 변수이기 때문에 오류가 남
#상수와 변수의 차이 / 상수는 변하지 않은 값이니 메모리를 할당하지 않고 값을 바로 값을 넣음 
#그러나 변수는 초기화를 시켜야 값을 할당할 수 있다. 
sess.run(tf.global_variables_initializer()) #변수는 꼭 초기화 시켜야한다. (이때 메모리에 할당되는 듯 하다)
sess.run(z) 
#Out[89]: 
#array([[22, 28],
#       [49, 64]])
sess.close()

#==============================
p1 = tf.placeholder("int32")    #tf.placeholder: runtime시점에 값을 넣어 실행하겠다는 의미임 #값이 존재하지 않음 #초기화 시키지 않고 값이 나옴
p2 = tf.placeholder("int32")
y = tf.add(p1,p2)   #더하기 메소드
sess = tf.Session()
sess.run(y, feed_dict={p1:10, p2:20}) #runtime 시점에 값을 넣어 사용함 
#constant, variable, placeholder모두가 섞여 있을 수 있기 때문에 그럴 경우에는 sess.run(tf.global_variables_initializer()) 를 사용하여 초기화시켜놓고 run을 실행한다. 
sess.close()

■ 함수            설명
------------------------------- 
tf.add            덧셈
tf.subtract       뺄셈
tf.multiply       곱셈
tf.div            나눗셈의 몫
tf.truediv        나누셈의 몫, 소수점
tf.mod            나눗셈의 나머지
tf.abs            절대값
tf.negative       음수
tf.sign           부호(음수-1, 양수 1, 0)
tf.reciprocal     역수(3은 1/3)
tf.square         제곱
tf.round          반올림
tf.sqrt           제곱근
tf.pow            거듭제곱
tf.exp            지수값
tf.log            로그값
tf.maximum        최대값
tf.minimum        최소값
tf.cos            코사인
tf.sin            사인
tf.matmul         행렬의 곱


#====실습===============================
p1 = tf.placeholder("int32")    #tf.placeholder: runtime시점에 값을 넣어 실행하겠다는 의미임 #값이 존재하지 않음 #초기화 시키지 않고 값이 나옴
p2 = tf.placeholder("int32")
y = tf.div(p1,p2)   #더하기 메소드
sess = tf.Session()
y = tf.truediv(p1,p2)

sess.run(y, feed_dict={p1:9, p2:4}) 

y = tf.mod(p1,p2)
y = tf.abs(p1,p2)
y = tf.negative(p1,p2)
y = tf.sign(p1,p2)
y = tf.reciprocal(p1,p2)
y = tf.square(p1,p2)
y = tf.round(p1,p2)
y = tf.sqrt(p1,p2)
y = tf.pow(p1,p2)
y = tf.exp(p1,p2)
y = tf.log(p1,p2)
y = tf.maximum(p1,p2)
y = tf.minimum(p1,p2)
y = tf.cos(p1,p2)
y = tf.sin(p1,p2)

#==============================
■ 세션 열고 닫기를 함께 하기
x = tf.Variable(0)
y = tf.assign(x,1)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())  #변수는 꼭 초기화 시켜주기
    print(sess.run(x)) #0
    print(sess.run(y)) #1
    print(sess.run(x)) #1


# =============================================================================
# [문제200] tensorflow 상수를 이용해서 아래와 같이 결과를 출력하는 프로그램을 만드세요.
# a + b = 6
# a * b = 8
# =============================================================================
a = tf.constant(2)
b = tf.constant(4)
c = a + b
d = a * b
sess = tf.Session()
print("a + b = {}".format(sess.run(c)))
print("a * b = {}".format(sess.run(d)))
sess.close()

with tf.Session() as sess:
    print("a + b = {}".format(sess.run(a+b)))
    print("a * b = {}".format(sess.run(a*b)))
    
# =============================================================================
# [문제201] tensorflow 상수를 이용해서 아래와 같이 결과를 출력하는 프로그램을 만드세요.
# 단 두 변수의 입력값을 실행시 넣도록하는 변수를 이용하세요.  
# Add = 6
# Multiply = 8
# =============================================================================

a = tf.placeholder(tf.int32)
b = tf.placeholder(tf.int32)
add = tf.add(a,b)
mul = tf.multiply(a,b)
sess = tf.Session()
print("Add: %d"%sess.run(add,feed_dict={a:2, b:4}))
print("Multiply: %d"%sess.run(mul,feed_dict={a:2, b:4}))
sess.close()


#a = tf.placeholder(tf.int32) 
#b = tf.placeholder(tf.int32)
a = tf.placeholder("int32")
b = tf.placeholder("int32")
y = tf.add(a, b)
z = tf.multiply(a,b)
with tf.Session () as sess:
    print("Add = {}".format(sess.run(y, feed_dict={a:2, b:4})))
    print("Multiply = {}".format(sess.run(z, feed_dict={a:2, b:4})))


# =============================================================================
■ 텐서 자료 구조
- 텐서는 텐서플로의 기본 자료 구조
- 텐서는 다차원배열, 리스트로 구성
- 텐서는 학습데이터가 저장되는 다차원 배열

□ 1차원 tensor
#tensor에서는 바로 값을 출력할 수 없지만 numpy의 값은 바로 출력할 수 있다. 
import numpy as np
arr_1 = np.array([1.5, 1.5, 0, 10])
arr_1
arr_1[0]      #Out[237]: 1.5
arr_1.ndim    #Out[238]: 1
arr_1.shape   #Out[239]: (4,)
arr_1.dtype   #Out[240]: dtype('float64')

#numpy에서 만든 자료를 tensor자료로 converting 해주기
arr_tf = tf.convert_to_tensor(arr_1, dtype=tf.float64)
#세션을 열어 tensor값 확인하기
with tf.Session() as sess:
    print(sess.run(arr_tf))
    print(sess.run(arr_tf[0]))

arr_tf.shape    #Out[244]: TensorShape([Dimension(4)])
arr_tf.dtype    #Out[246]: tf.float64
arr_tf.ndim     #AttributeError: 'Tensor' object has no attribute 'ndim'


□ 2차원 tensor
arr_1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
arr_2 = np.array([[1,1,1],[2,2,2],[3,3,3]])
type(arr_1)    #Out[254]: numpy.ndarray
type(arr_2)    #Out[255]: numpy.ndarray

#numpy의 array를 상수값으로 그대로 넣으면 conversion없이 사용할 수 있음 
tm1 = tf.constant(arr_1)
tm2 = tf.constant(arr_2)

tm_product = tf.matmul(tm1, tm2)
tm_add = tf.add(tm1, tm2)
with tf.Session() as sess:
    print(sess.run(tm_product))
    print(sess.run(tm_add))
#[[14 14 14]
# [32 32 32]
# [50 50 50]]
#[[ 2  3  4]
# [ 6  7  8]
# [10 11 12]]


□ 3차원 tensor
arr_3 = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
arr_3.ndim     #Out[266]: 3
arr_3.shape    #Out[267]: (2, 2, 2) (plane면, row행, column렬) 면이 2개인 3차원이 만들어짐
tm_3 = tf.constant(arr_3)
with tf.Session() as sess:
    print(sess.run(tm_3))
#[[[1 2]
#  [3 4]]
#
# [[5 6]
#  [7 8]]]

# =========================================
x = tf.placeholder(tf.float32)
y = tf.placeholder(tf.float32)
z = tf.matmul(x,y)  #행렬의 곱 
with tf.Session() as sess:
    print(sess.run(z, feed_dict={x:[[3.,3.],[3.,3.]],y:[[5.,5.],[5.,5.]]}))
    
    
x = tf.placeholder(tf.float32, shape=(2,2))  #shape을 지정해줄 수도 있다. 
y = tf.placeholder(tf.float32, shape=(2,2))
z = tf.multiply(x,y)
with tf.Session() as sess:
    print(sess.run(z, feed_dict={x:[[3.,3.],[3.,3.]],y:[[5.,5.],[5.,5.]]}))
    
# =============================================================================
# [문제202] x변수는 1행3열 모양의 1,2,3
# w변수는 3행 1열 모양의 2,2,2
# y변수는 x와 w를 행렬의 곱을 이용한 결과를 수행하는 프로그램을 작성하세요. 
# =============================================================================
x = tf.placeholder(tf.float32)
w = tf.placeholder(tf.float32)
y = tf.matmul(x,w)
with tf.Session() as sess:
    print(sess.run(y, feed_dict={x:[[1,2,3]], w:[[2],[2],[2]]}))


x = np.array([[1,2,3]])
w = np.array([[2],[2],[2]])
tm1 = tf.constant(x)
tm2 = tf.constant(w)
tm_product = tf.matmul(tm1, tm2)
with tf.Session() as sess:
    print(sess.run(tm_product))

#get_shape: 행과 열을 같이 보이게 하도록 하기
x = tf.constant([[1.0,2.0,3.0]])
print(x.get_shape())
w = tf.constant([[2.0],[2.0],[2.0]])
print(w.get_shape())
y = tf.matmul(x,w)
sess = tf.Session()
print(sess.run(x))
print(sess.run(w))
print(sess.run(y))

#변수를 사용할 때는 꼭 초기화를 시켜줘야 한다.  init_op = tf.global_variables_initializer()
x = tf.Variable([[1.0,2.0,3.0]])
w = tf.Variable([[2.0],[2.0],[2.0]])
y = tf.matmul(x,w)
init_op = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init_op)
    print(sess.run(y))
