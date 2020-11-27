# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 09:56:04 2018

@author: stu
"""
CNN(Convolution Neural Network)
image ---(pixel값으로 변경)------(convolutions: 필터링작업: 가장특징이 될만한 부분은 부각시키고 의미없는 부분은 흐릿하게 만드는 작업)-----> feature maps(특징맵: 은닉층처럼 이용) --> subsampling(부각시켜지는 부분을 작게 샘플링) --> convolution --> subsampling --> fully connected 


'''
tensorflow MINIST 
https://tensorflowkorea.gitbooks.io/tensorflow-kr/content/g3doc/tutorials/mnist/beginners/

'''

image: 입력값
filter: weight값 
convolution: 합성곱 -> 필터기준으로 옮겨가며 합성곱을 만드는 작업을 함 


# =============================================================================

▣ CNN(Convolution Neural Network)
- 합성곱 신경망
- convolution 층과 pooling층을 포함하는 신경망 

■ 기존신경망과의 CNN 차이?
- 기존방법 : affine -> ReLU
- CNN : Conv -> ReLU -> Pooling  (특징이 될만한 부분은 뽑아낸다.)

■ 합성곱 계층
- feature map을 만들고 그 feature map을 선명하게 해주는 층
- 합성곱 연산: 이미지 3차원(세로, 가로, 색상) data의 형상을 유지하면서 연산하는 작업

ex)
1 2 3 0           2 0 1
0 1 2 3     Θ     0 1 2            15 16
3 0 1 2           1 0 2             6 15
2 3 0 1 

입력              필터              
(4,4)            (3,3)             (2,2)

- stride: 한칸씩 움직여 합성곱을 하는 작업
- 출력 구하기 
입력 - 필터             4 - 3 
-----------   +  1 =  --------- + 1 = 2
  stride                 1

ex) 7x7 입력, 3x3 필터, stride: 1, 5x5 출력
7-3    
----  + 1 =  5
1

ex)  7x7 입력, 3x3 필터, stride: 2,  3x3 출력
7-3    
----  + 1 =  3
2

■ tensor에서 구현해보기

import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

#cf. tensor에서 선언한 것은 session.run을 해야함-> 그러나 
#대화형 처리
sess = tf.InteractiveSession()

image = np.array([[[[1],[2],[3]], [[4],[5],[6]],[[7],[8],[9]]]], dtype=np.float32)
print(image.shape)     
#(1, 3, 3, 1) 1: 이미지 n개, 3:행(높이), 3:열(너비), 1:색(채널)

plt.imshow(image.reshape(3,3), cmap="Greys")
#plt.imshow(image.reshape(3,3), cmap="Reds")
#plt.imshow(image.reshape(3,3), cmap="Greens")
#plt.imshow(image.reshape(3,3), cmap="Blues")

weight = tf.constant([[[[1.]],[[1]]],[[[1]],[[1]]]])
print(weight.shape)
# (2,2,1,1): 행, 열, 색, 필터 
# 이미지: (1, 3, 3, 1)에서의  1:색(채널)과 weight에서의 (2,2,1,1) 1:색의 수가 같아야 한다. 

□ 합성곱을 만들어서 feature map을 만듦 
conv2d = tf.nn.conv2d(image,weight,strides=[1,1,1,1], padding='VALID')
#strides=[1,1,1,1] 하나씩 이동하겠음

#sess.run과 같은 기능 
conv2d_img = conv2d.eval()
conv2d_img
#Out[827]: 
#array([[[[12.],
#         [16.]],
#
#        [[24.],
#         [28.]]]], dtype=float32)
print(conv2d_img.shape) #(1, 2, 2, 1)

image
weight

#np.swapaxes: 전체 행렬의 축을 바꾸는 method 
conv2d_img = np.swapaxes(conv2d_img,0,3)
conv2d_img.shape
for i, one_img in enumerate(conv2d_img):
    print(one_img.reshape(2,2))
    plt.subplot(1,2,i+1),plt.imshow(one_img.reshape(2,2), cmap="Greys")

#filter를 거치다보니 합성곱에 걸쳐 나온 결과가 이미지가 축소가 됨 
# -> 입력과 동일한 크기의 이미지를 나오게 하려면 원래의 이미지의 테두리를 주면 된다. 

# 입력과 동일한 크기의 이미지를 나오게 하기  :padding='SAME' / one_img.reshape(3,3))
# padding='SAME' : 합성곱의 출력이 원본 이미지 크기와 같게하는 option 
    #단 stride가 한칸씩 이동할 경우 원본 이미지와 같은 크기의 이미지가 만들어진다.
    #만약 stride를 2로 할 경우 어쩔 수 없이 축소 될수 밖에 없다.      
conv2d = tf.nn.conv2d(image,weight,strides=[1,1,1,1], padding='SAME')
conv2d_img = conv2d.eval()
conv2d_img
#Out[827]: 
#array([[[[12.],
#         [16.]],
#
#        [[24.],
#         [28.]]]], dtype=float32)
print(conv2d_img.shape) #(1, 2, 2, 1)

image
weight

#np.swapaxes: 전체 행렬의 축을 바꾸는 method 
conv2d_img = np.swapaxes(conv2d_img,0,3)
conv2d_img.shape
for i, one_img in enumerate(conv2d_img):
    print(one_img.reshape(3,3))
    plt.subplot(1,2,i+1),plt.imshow(one_img.reshape(3,3), cmap="Greys")


□ sampling 작업 -subsampling 
- subsampling 에서는 actvation fucntion을 둘 수 있다. ReLU만 가능 (sigmoid가 안되는 경우는 원래의 이미지의 색을 반환하지 못하고 망가뜨리기 때문) 
- 이미지를 잘게 잘라 놓음 

□ 그리고 계속 반복되는 작업

image= np.array([[[[4],[3]],[[2],[1]]]],dtype=np.float32)

#max_pool: 가장 큰 수만 뽑아내는 작업  (2x2이 하나라 뽑혀 축소가 됨)
pool = tf.nn.max_pool(image, ksize=[1,2,2,1], strides=[1,1,1,1], padding="VALID")
pool.eval()  #Out[108]: array([[[[4.]]]], dtype=float32)

# =============================================================================
# MNIST 
# Check out https://www.tensorflow.org/get_started/mnist/beginners for
# =============================================================================
import tensorflow as tf
import random
import matplotlib.pyplot as plt

from tensorflow.examples.tutorials.mnist import input_data

tf.set_random_seed(777)  # reproducibility

mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
# Check out https://www.tensorflow.org/get_started/mnist/beginners for
# more information about the mnist dataset
#img = mnist.train.images[0].reshape(28,28)
#plt.imshow(img,cmap="gray")
# hyper parameters
learning_rate = 0.001
training_epochs = 15        #학습을 15번 반복 (epoch: full로 학습을 한번 하는 것)
batch_size = 100            #데이터 양이 많을 경우에는 100개씩 가져와 부분적으로 수행함 

# input place holders
X = tf.placeholder(tf.float32, [None, 784])  #784개의 열로 되어 있음 
X_img = tf.reshape(X, [-1, 28, 28, 1])   # img 28x28x1 (black/white) 세로(높이)x가로(너비)  # [-1, 28, 28, 1]: -1은 여러개이때문에 무한으로, 채널은 1로
Y = tf.placeholder(tf.float32, [None, 10]) #0~9여서 : 10개이기 때문에 나가는 값이 10개로 씀

# L1 ImgIn shape=(?, 28, 28, 1) (n개 , 28,28, 색은1)
W1 = tf.Variable(tf.random_normal([3, 3, 1, 32], stddev=0.01)) #필터크기(3,3,색, 필터수)   #[3, 3, 1, 32] 3행3열짜리 1색, 32개의 필터-> feature maps

#    Conv     -> (?, 28, 28, 32)
#    Pool     -> (?, 14, 14, 32)
L1 = tf.nn.conv2d(X_img, W1, strides=[1, 1, 1, 1], padding='SAME')
L1 = tf.nn.relu(L1)   #convolution 결과를 relu에 넣음
L1 = tf.nn.max_pool(L1, ksize=[1, 2, 2, 1],strides=[1, 2, 2, 1], padding='SAME') #maxpooling통해서 sampling 작업 #stride를 strides=[1, 2, 2, 1] 두칸씩 이동 -> 따라서 14x14로 만들어짐
'''
Tensor("Conv2D:0", shape=(?, 28, 28, 32), dtype=float32)
Tensor("Relu:0", shape=(?, 28, 28, 32), dtype=float32)
Tensor("MaxPool:0", shape=(?, 14, 14, 32), dtype=float32)
'''

# 위를 다시 한 번 돌림 Tensor("MaxPool:0", shape=(?, 14, 14, 32), dtype=float32) 에서 32개의 채널을 맞춰져야 함 
# L2 ImgIn shape=(?, 14, 14, 32)
W2 = tf.Variable(tf.random_normal([3, 3, 32, 64], stddev=0.01)) # 3,3,32,64(필터수,이미지수) #[3, 3, 32, 64] 64필터수
#    Conv      ->(?, 14, 14, 64)
#    Pool      ->(?, 7, 7, 64)
L2 = tf.nn.conv2d(L1, W2, strides=[1, 1, 1, 1], padding='SAME')
L2 = tf.nn.relu(L2)
L2 = tf.nn.max_pool(L2, ksize=[1, 2, 2, 1],strides=[1, 2, 2, 1], padding='SAME') #strides=[1, 2, 2, 1] 이기 때문에 7x7로 만들어짐 
L2_flat = tf.reshape(L2, [-1, 7 * 7 * 64])
'''
Tensor("Conv2D_1:0", shape=(?, 14, 14, 64), dtype=float32)
Tensor("Relu_1:0", shape=(?, 14, 14, 64), dtype=float32)
Tensor("MaxPool_1:0", shape=(?, 7, 7, 64), dtype=float32)
Tensor("Reshape_1:0", shape=(?, 3136), dtype=float32)
'''
# fully connected layer
# Final FC 7x7x64 inputs -> 10 outputs
W3 = tf.get_variable("W3", shape=[7 * 7 * 64, 10], initializer=tf.contrib.layers.xavier_initializer())  #get_variable: variable대신 사용 가능  #shape=[7 * 7 * 64, 10]: 크기 # initializer=tf.contrib.layers.xavier_initializer(): 변수를 초기화 하는 알고리즘 
b = tf.Variable(tf.random_normal([10])) #b= bias
logits = tf.matmul(L2_flat, W3) + b  #행렬의 곱: 펼쳐놓은 것과  

# define cost/loss & optimizer
cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(
    logits=logits, labels=Y))
optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(cost)  #AdamOptimizer(learning_rate=learning_rate) : optimizer중에 기존의 gradient descent optimizer대신 Adam optimizer를 사용  (일반적으로 Adam이 더 좋은 성능을 보이지만 그러나 dataset마다 조금씩 다를 수 있으니 optimizer도 비교를 하자)

# initialize
sess = tf.Session()
sess.run(tf.global_variables_initializer())

# train my model
print('Learning started. It takes sometime.')
for epoch in range(training_epochs):
    avg_cost = 0
    total_batch = int(mnist.train.num_examples / batch_size)

    for i in range(total_batch):
        batch_xs, batch_ys = mnist.train.next_batch(batch_size)  #데이터 양이 많을 경우에는 batch size: 100개씩 가져와 부분적으로 수행함 -> RAM이 작을 경우 batch size도 바꿔가면서 해야함  
        feed_dict = {X: batch_xs, Y: batch_ys}
        c, _ = sess.run([cost, optimizer], feed_dict=feed_dict)
        avg_cost += c / total_batch

    print('Epoch:', '%04d' % (epoch + 1), 'cost =', '{:.9f}'.format(avg_cost))

print('Learning Finished!')

# Test model and check accuracy
correct_prediction = tf.equal(tf.argmax(logits, 1), tf.argmax(Y, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
print('Accuracy:', sess.run(accuracy, feed_dict={
      X: mnist.test.images, Y: mnist.test.labels}))

# Get one and predict
r = random.randint(0, mnist.test.num_examples - 1)
print("Label: ", sess.run(tf.argmax(mnist.test.labels[r:r + 1], 1)))
print("Prediction: ", sess.run(
    tf.argmax(logits, 1), feed_dict={X: mnist.test.images[r:r + 1]}))

plt.imshow(mnist.test.images[r:r + 1].reshape(28, 28), cmap='Greys', interpolation='nearest')
plt.show()



#이미지 학습시, 각각의 폴더를 만들고, 별도의 lable을 만들어야 함 


# =============================================================================
## np.swapaxes 확인하기
#2차원행렬 
a = np.arange(15).reshape(3,5)
a
#.T: 축을 바꿈
a.T
#np.transpose(): 축을 바꿈
np.transpose(a)
#np.swapaxes: 축을 바꿈
a
np.swapaxes(a,0,1)
#np.dot()numpy에서 제공하는 행렬의 곱
np.dot(a.T,a)
np.dot(np.transpose(a),a)
np.dot(np.swapaxes(a,0,1),a)

#3차원행렬
b = np.arange(24).reshape(2,3,4)
#Out[58]: 
#array([[[ 0,  1,  2,  3],
#        [ 4,  5,  6,  7],
#        [ 8,  9, 10, 11]],
#
#       [[12, 13, 14, 15],
#        [16, 17, 18, 19],
#        [20, 21, 22, 23]]])
b.shape
#Out[59]: (2, 3, 4)
b.T
b
np.transpose(b) #면이 4개가 됨 
#Out[62]: 
#array([[[ 0, 12],
#        [ 4, 16],
#        [ 8, 20]],
#
#       [[ 1, 13],
#        [ 5, 17],
#        [ 9, 21]],
#
#       [[ 2, 14],
#        [ 6, 18],
#        [10, 22]],
#
#       [[ 3, 15],
#        [ 7, 19],
#        [11, 23]]])
np.swapaxes(b,0,2)
#Out[63]: 
#array([[[ 0, 12],
#        [ 4, 16],
#        [ 8, 20]],
#
#       [[ 1, 13],
#        [ 5, 17],
#        [ 9, 21]],
#
#       [[ 2, 14],
#        [ 6, 18],
#        [10, 22]],
#
#       [[ 3, 15],
#        [ 7, 19],
#        [11, 23]]])



# =============================================================================
# [문제] 0부터 143까지의 원소로 이루어진 12*12 행렬을 만들고 4*4필터(단위행렬)를
#    이용해 합성곱을 수행하시오. 단, 스트라이드는 1이다.
#
# *합성곱 계층
# -feature map을 만들고 그 feature map을 선명하게 해주는 층
# *합성곱 연산
# -이미지 3차원(세로,가로,색상)데이터의 형상을 유지하며 연산하는 작업
# *합성곱
# -입력 데이터에 필터를 적용한 것이 합성곱 연산이다.
# *np.eye()=numpy에서 단위행렬을 만드는 함수
# 
# =============================================================================

# 합성곱 연산 짜기 
import numpy as np
a=np.arange(144).reshape(12,12)
print(a.shape)
filter=np.eye(4,4)

result=[]
for r in range(len(a)-3):       #r: row  #몇행 몇열로 나오는지를 고민해서 돌려야 한다.
    for c in range(len(a)-3):   #c: col  
        result.append(np.sum(a[r:r+4, c:c+4]*filter))

result = np.array(result).reshape(9,9)

#중요한 부분이 테두리 쪽에 있을 겨웅 padding을 둬야한다. 
#stride의 값에 따라 합성곱의 결과물이 어떤 모양이 되는지 결과를 생각해야 한다. 

□ padding(패딩): 합성곱 연산을 수행하기 전에 입력 데이터 주변을 특정값으로 채워 늘리는 것을 말한다. 
- 이유? 패딩을 하지 않을 경우 데이터의 공간 크기는 합성곱 계층을 지날 때 마다 작아지게 되므로 가장자리 정보들이 사라지게 되는 문제가 발생하기 때문에 패딩을 사용한다. 
- np.pad() numpy에서의 padding method

a = np.arange(16).reshape(4,4)
#패딩을 모두 할 경우
a_pad = np.pad(a, pad_width=1, mode='constant', constant_values=0)

#[(top,bottom),(left,right)] #기본은 [(1,1),(1,1)]
np.pad(a, [(1,1),(1,1)], mode='constant', constant_values=0)

#패딩을 오른쪽과 아랫쪽만 할 경우 (채울 곳은:1 , 채우지 않는 곳은: 0)
np.pad(a, [(0,1),(0,1)], mode='constant', constant_values=0)

#패딩을 오른쪽 2개과 아랫쪽 2개만 할 경우 
np.pad(a, [(0,2),(0,2)], mode='constant', constant_values=0)


# =============================================================================
# [문제] 0부터 15까지 원소로 이루어진 4x4행렬을 만들고 0부터 8까지 원소로 이루어진 3x3필터를 이용해서 합성곱하는데 제로 패딩을 이용해서 출력결과를 4x4로 출력하세요.
# (단 스트라이드는 1로 수행) 
# =============================================================================

x = np.arange(16).reshape(4,4)
filter = np.arange(9).reshape(3,3)

x_pad = np.pad(x, pad_width=1, mode='constant', constant_values=0)
x_pad.shape  #Out[195]: (6, 6)
 
result=[]
for r in range(len(x_pad)-2):
    for c in range(len(x_pad)-2):   
        result.append(np.sum(x_pad[r:r+3, c:c+3]*filter))

result = np.array(result).reshape(4,4)
print(result)

# =============================================================================

입력(H,W), 필터크기(FH,FW), 출력크기(OH,OW)
스트라이드: S, 패딩: P
       H + 2P - FH
OH = ----------------  +  1
           S

#패딩구하기            
S*(OH-1) = H+2P-FH
S*(OH-1)-H+FH = 2P

    (OH-1)*S-H+FH        
P = --------------   
          2
P = ((4-1)*1-4+3)/2   #Out[286]: 1.0 그럼 패딩값이 1로 하면된다. 

# =============================================================================

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#이미지 불러들이기 (이미지 파일이 숫자일 경우는 오류가 날 수도 있음. 그러면 c:\\ 역슬래쉬를 두번쓰도록 한다.) 
img = Image.open("c:\\data\hcs.png") 
plt.imshow(img)

#RGB: 3차원 배열로 array하도록  0~255로 변환됨  #이미지 픽셀값 뽑기
img_pixel = np.array(img)
img_pixel

#특정 색상에 대한(rgb중) 가중치를 줘서 값을 return함
def rgb_gray(image):  #image는 형식매개변수
    r, g, b = image[:,:,0], image[:,:,1], image[:,:,2]
    gray = 0.2989 *r + 0.5870*g + 0.1140*b              #가중치 주기 
    return gray


plt.imshow(rgb_gray(img_pixel), cmap='gray') #cmap은 imshow의 옵션
plt.imshow(rgb_gray(img_pixel)) 

#저장하기
img_pixel_gray = rgb_gray(img_pixel)
plt.imsave("c:\\data\\gray.png", img_pixel_gray)


# =============================================================================


def convolution(image, filter, stride, bias):
    col = int((len(image[0])-len(filter[0])) / stride +1)
    row = int((len(image)-len(filter)) / stride +1)
    filter_col = len(filter[0])
    filter_row = len(filter)
    
    convolution_list = []
    for i in range(row):
        for j in range(col):
            convolution_list.append(np.sum(image[i:i+filter_row, j:j+filter_col] * filter))
    return np.array(convolution_list).reshape(row,col)
        
filter = np.array([[[255,255,255],[0,0,0],[255,255,255]],
                   [[0,0,0],[0,0,0],[0,0,0]],
                   [[255,255,255],[0,0,0],[255,255,255]]])
filter.shape

filter_gray = rgb_gray(filter)
plt.imshow(filter_gray, cmap="gray")

result = convolusion(img_pixel,filter_gray,1,0)      
result

plt.imshow(result, cmap="gray")
plt.imsave("c:/python/result.png", result, cmap="gray")




    