# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 09:53:55 2018

@author: stu
"""

#KNN
#- K값을 많이 주면 overfitting이 됨
#- 거리계산(유클리드 거리계산)
#- 음수값 (멘하턴 거리)에 절대값처리함 
#https://doorbw.tistory.com/175

import math
-수학에 관련된 함수들은 math에 거의 다 들어 있음 

▣ kNN(k Nearest Neighbors)
- 거리유사도 측정
- 유클리드거리(Euclidean distance)를 사용 
-> k값을 정하는 것이 가장 어려운 문제이다. 
- 다수결의 의미는 잘못된 분류가 될 수 있음을 의미할 수 있다. 
- k값을 구할 때는 전체모집단의 수를 제곱근으로 수행하면 된다. 
- 보편적으로 k값은 5개~20개를 선택하게 된다. 짝수보다는 홀수로 하는 것이 좋다. 

토마토 단맛 6 아삭한 맛 6
목표변수는 과일, 채소, 단백질인지 분류하기 -> supervised learning 


재료   단맛   아삭한맛    음식종류          토마토와의 거리 
-------------------------------------------------------------------------
포도     8        5       과일            math.sqrt((6-8)**2 + (4-5)**2) = 2.23
콩       3        7       채소            math.sqrt((6-3)**2 + (4-7)**2) = 4.24
견과     3        6       단백질          math.sqrt((6-3)**2 + (4-6)**2) = 3.61
오렌지   7        3       과일            math.sqrt((6-7)**2 + (4-3)**2) = 1.41


k=1 : 1NN -> 가장 가까운 하나만 뽑기 (오렌지)
- 오렌지 토마토 거리는 1.4로 가까운 이웃하여 과일로 분류한다.

k=3 : 3NN -> 가장 가까운 세개 뽑기 (오렌지, 포도, 견과) -> (과일, 과일, 단백질) -> 가장 많은 음식종류로 분류됨: 과일
- 오렌지, 포도, 견과 세가지 사이에 다수결로 정한다. 
- 과일이 2/3이기 때문에 과일로 분류한다. 


# =============================================================================
# [문제196] knn 프로그램을 작성하세요.
        
#      pointlist[(1,1),(1,0),(2,0),(0,1),(2,2),(1,5),(2,3)]
#       
#
#        <수행>
#        knn([2,1],2,pointlist)
#
#        <결과>
#	[(1, 1), (2, 0)]

# =============================================================================
#목표 변수가 없음 -> 따라서 주변에서 가장 가까운 점수를 가까운 것을 뽑아낸다. 


#def knn(value, k, pointlist):
#    pointlist = [(1,1),(1,0),(2,0),(0,1),(2,2),(1,5),(2,3)]
#    neighbor = []
#    for i in pointlist:
#        distance = math.sqrt((value[0]-i[0])**2+(value[1]-i[1])**2
#        neighbor.append(distance)      
#    print(neighbor)
#          
#    print(sorted(neighbor))

import operator

pointlist = [(1,1),(1,0),(2,0),(0,1),(2,2),(1,5),(2,3)]
def knn(value, k, pointlist):
    n = {}
    for i in pointlist:
        distance = math.sqrt((value[0]-i[0])**2+(value[1]-i[1])**2)
        n[i]=distance
    
    sorted_distance = sorted(n.items(), key=operator.itemgetter(1))
    print(sorted_distance)
    res = []
    print(sorted_distance[0][0])
    print(sorted_distance[1][0])
    
    for j in sorted_distance:
        if len <
            j[0]
        
        if len(sorted_distance) < k:           
            
            res.append(j[len()][0]) 
            print (res)
    
knn([2,1],2,pointlist)



#쌤답
import numpy as np
import operator    #dictionary 정렬할 때 필요
from math import sqrt

point = [2,1]
k = 2
pointlist=[(1,1),(1,0),(2,0),(0,1),(2,2),(1,5),(2,3)] #리스트이면서 tuple


def knn(point, lists, k):       #point, lists, k: 형식매개변수
    
    dic={}
    
    for p in lists:        
        d = dist(point, p)
        dic[p]=d    # dic[p]:키값 d(거리계산값):value값 
    
  
    res = []
    sorted_dic = sorted(dic.items(), key=operator.itemgetter(1))  #dictionary정렬값 /key=operator.itemgetter(1): value값을 기준으로 정렬해줌 (import operator 필요)
    

      
    for key in sorted_dic:
        if len(res) < k:
            
            res.append(key[0])
            
    return res

 
def dist(x, y):         #list변수값으로 받고, array로 
    x = np.array(x)
    y = np.array(y)
    
    return  sqrt(sum(pow(x - y,2)))  #sum,pow: 기본으로 내장된 함수 

knn(point,pointlist,k)        

# =============================================================================
# 수업
# =============================================================================
■ kNN: 거리를 구하고, 오름차순 정렬을 하고, k개수 만큼 자르고, 다수결로 그 값을 추출한다. 

# numpy를 통해서 바꾸기 
a = [4, 3, 5, 7, 6, 8]
indices = [0, 1, 4] 

■ np.take(a, indices): a라는 list에서 0번 인덱스 값, 1번 인덱스 값, 4번 인덱스값을 뽑아내기 
np.take(a, indices)

#
lst1 = [2,1]
lst2 = [(1,1),(1,0),(2,0),(0,1),(2,2),(1,5),(2,3)] 

point1 = np.array(lst1)
point2 = np.array(lst2)
 
distances = np.sqrt(np.sum((pow(point1 - point2, 2)), axis=1))  #행을 기준으로 합 #numpy, math 모두 sqrt를 가지고 있음 

#array를 정렬 
distances.argsort() #오름차순으로 정렬한 값을 인덱스값으로 보여줌 
distances.argsort()[:3]

indices = distances.argsort()[:3]    #indices값은 지금 array임 
nn = np.take(lst2, indices, axis=0)  #축을 0으로 설정하면 뽑아내고자 하는 값을 뽑아낼 수 있음
nn

#첫번째 값이 level이라고 가정하기
    #nn = np.take(lst2, indices, axis=0)  #축을 0으로 설정하면 뽑아내고자 하는 값을 뽑아낼 수 있음
    #Out[330]: 
    #array([[1, 1],
    #       [2, 0],
    #       [2, 2]])

#빈도체크: 첫번째 열을 기준으로 빈도수 체크 1:1 2:2
#collections의 count method 사용하기  -> 인덱싱, 슬라이싱을 통해 가능

from collections import Counter
#모든 행의 1열을 뽑아냄 
nn[:,0] #array([1, 2, 2])
c = Counter(nn[:,0]) #Counter({1: 1, 2: 2})
#빈도가 높은 하나의 값 
c.most_common(1)
# key값만 뽑아내기 
freq = c.most_common(1)[0][0]
# 다수결 값을 불러내기 
nn[nn[:,0]==freq]


# =============================================================================
# [문제197] 키, 몸무게에 따른 성별을 분류해주세요.
# 
# 키, 몸무게 데이터
# [[158, 64],
# [170, 86],
# [183, 84],
# [191, 80],
# [155, 49],
# [163, 59],
# [180, 67],
# [158, 54],
# [170, 67]]
# 
# 성별 레벨
# ['male', 'male', 'male', 'male', 'female', 'female', 'female', 'female', 'female']
# 
# 
# [155, 70] 성별을 분류하세요.
# 'female'
# =============================================================================
# 성별레벨 : 목표변수가 있음

가장 가까운 거리 계산 -> 정렬작업 -> 그중 3개를 뽑아 -> 다수결의 원칙을 통해 -> 남자인지 여자인지 구분하기

def tw(tall, weight):
    
    tw1 = [tall, weight]
    tw2 = [[158, 64],
    [170, 86],
    [183, 84],
    [191, 80],
    [155, 49],
    [163, 59],
    [180, 67],
    [158, 54],
    [170, 67]]

    gender =['male', 'male', 'male', 'male', 'female', 'female', 'female', 'female', 'female']
    
    #array형식으로 바꾸기 
    eg = np.array(tw1)
    sp = np.array(tw2)
    
    #거리구하기
    distances = np.sqrt(np.sum((pow(eg - sp, 2)), axis=1))
    distances
    
    #distances정렬하고 k = 3으로 뽑기
    distances.argsort()[:3]
    indices = distances.argsort()[:3]
    indices
    
    # tw2의 k=3을 뽑아낸 값을 gender값과 합쳐 gender값 추출하기
    k3 = np.take(gender, indices, axis=0)
    k3
    
    #frequency 구하기 
    from collections import Counter
    c = Counter(k3)
    c.most_common(1)
    
    # key값만 뽑아내기 
    key = c.most_common(1)[0][0]
    print(key)

tw(155,70)

#==============================================================================
#쌤답
x_train = [[158, 64],
[170, 86],
[183, 84],
[191, 80],
[155, 49],
[163, 59],
[180, 67],
[158, 54],
[170, 67]]

label=['male', 'male', 'male', 'male', 'female', 'female', 'female', 'female', 'female']

y = np.array([[155,70]])

#거리계산
distances = np.sqrt(np.sum(pow(x_train-y,2), axis=1))    
# k=3 일때
indices = distances.argsort()[:3]
# label값 구하기
nn = np.take(label, indices)
# 다수결: collections의 counter생각하기
b =Counter(nn)
b.most_common(1)[0][0]


# =============================================================================
▣ sklearn.neighbors 모듈
from sklearn.neighbors import KNeighborsClassifier

■ 인스턴스화
clf = KNeighborsClassifier(n_neighbors =3)
□ .fit 메소드
clf.fit(x_train, label)
□ .predict 메소드: 예측메소드
clf.predict(np.array([155,70]).reshape(1,-1))[0]
    # [155,70]: 1차원
    # x_train: 2차원 
    # 비교하는 값을 2차원 모양으로 바꿔줘야함 -> 1행 2열로 만들어 줘야함 -> reshape(1,2) 을 하나 reshape(1,-1)은 같은 값을 말함; 
    #reshape(1,-1)-1은 차원을 바꿔준다. 
    #[0]을 하는 이유는 female정보만 뽑아내기
#clf.predict(np.array([155,70]).reshape(1,2))[0]    
#reshape을 사용하지 않고 2차원으로 만들어주기 [[]]로 만들기
#clf.predict(np.array([[155,70]]))[0]
    
    
