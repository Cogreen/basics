# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 09:45:39 2018

@author: stu
"""


'''
참고자료: 구글검색  -> keyword: bric 실제 이미지 데이터를 활용한 cnn 
http://www.birc.co.kr/2018/02/26/%EC%8B%A4%EC%A0%9C-%EC%9D%B4%EB%AF%B8%EC%A7%80-%EB%8D%B0%EC%9D%B4%ED%84%B0%EB%A5%BC-%ED%99%9C%EC%9A%A9%ED%95%9C-cnn-%EB%AA%A8%EB%8D%B8-%EA%B5%AC%ED%98%84%ED%95%98%EA%B8%B0/

'''


■ 기존신경망과의 CNN 차이?
- 기존방법 : affine -> ReLU
- CNN : Conv -> ReLU -> Pooling  (특징이 될만한 부분은 뽑아낸다.)
    (CNN은 sigmoid를 사용하면 안된다. -> 이미지 분류에서 )
- 기존의 'weight' = cnn의 'filter'


■ pooling 계층
[ conv -> pooling ]이것이 은닉층 하나가 된다. -> fully connected

■ convolution
- 이미지의 특징을 추출하는 계층(하나의 이미지로 여러개의 다른 feature map을 생성; 즉 filter에 따라 feature map의 여러개 생성할 수 있다. )
- 이미지 학습을 잘 하려면? 
    v 관련된 이미지가 많으면 많을 수록 좋다. 
    v 본 이미지를 각도를 돌려가며 학습을 시킨다. 

■ pooling 계층
- 출력값에서 일부분만 취하는 기능(왜 일부분만 취하는가?)    
- 합성곱을 하다보면 이렇게 저렇게 망쳐놓은 그림들을(원래의 이미지가 왜곡될 수 있음) 각각 부분에서 대표들을 뽑아 사이즈가 작은 이미지를 만드는 것이다. 마치 사진을 축소하면 해상도가 좋아지는 듯한 효과와 비슷하다. 
- 따라서 사이즉 작아지지만, 합성곱에서 특징이 되는 것을 뽑아낸다. 

□ pooling(풀링)의 종류 3가지
- 최대 풀링(max pooling): 합성곱 데이터에서 가장 큰값을 대표값으로 선정 (-> 가장 많이 사용하는 방법)
          :(나의 언어로 정의: 합성곱의 특징이 되는 부분을 뽑아내는 것은 합성곱의 결과에서 가장 큰 수가 되는 부분을 뽑아내는 기법이 있다. )
- 평균 풀링: 합성곱 데이터에서 모든 값의 평균을 대표값으로 선정
- 확률적 풀링: 합성곱 데이터에서 임의 확률로 한개를 선정  (-> 이 방법은 좀 문제가 될 수 있다.)
(pooling은 )


예시)
-3x3 maxpooling filter를 가지면서, stride 1일 때
:21 19 / (밑으로 내려가서) 19  19

21  8  8 12     
12 19  9  7       
 8 10  4  3      
18 12  9 10 

-2x2 maxpooling filter를 가지면서, stride 2일 때
:21 12 /(밑으로 내려가서)  18 10

21  8  8 12     
12 19  9  7         
 8 10  4  3      
18 12  9 10 

# =============================================================================
# a = np.array([[21,8,8,12],
#               [12,19,9,7],
#               [8,10,4,3],
#               [18,12,9,10]])
# 
# print(max_pooling(a))
# [[21,12],[18,10]으로 나오도록 함수를 만드세요.
# 
# stride = 2, fitler = 2x2 
# =============================================================================

import numpy as np

 a = np.array([[21,8,8,12],
               [12,19,9,7],
               [8,10,4,3],
               [18,12,9,10]])

def max_pooling(array):
    res = []
    a = array.flatten()  #flatten함 a = 21,8,8,12,12,19,9,7, 8, 10, 4, 3, 18, 12, 9, 10
    for i in range(0,12,2):   #i = 0,2,4,6,8,10,12
        if i==4 or i==6:
            continue          # i =4 ->밑에 수행하지 않고 없어짐 / i = 6 ->밑에 수행하지 않고 없너짐  
        temp = np.array([a[i:i+2],a[i+4:i+6]])  #a[0,2] = [21,8],a[4,6] =[12,19] / a[2:4]=[], a[6,8]
        res.append(np.max(temp))
    res = np.array(res).reshape(2,2)
    return res

print(max_pooling(a))


#filter = np.array([[1,1],[1,1]])
#np.max(a[0:2,0:2]*filter)
#np.max(a[0:2,2:4]*filter)
#
#
#np.max(a[2:4,0:2]*filter)
#np.max(a[2:4,2:4]*filter)



