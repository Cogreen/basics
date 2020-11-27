'''2018. 10. 24. Wed
지도학습: 목표변수(종속변수)가 있어서 이에 대한 labeling을 하고 이에 대해 분류함
비지도학습: 독립변수들만 있는 상태에서 cluster하고자 함 '''

''' 오늘의 학습주제: K-means '''

군집합
- 데이터 클러스터(cluster, 유사한 아이템의 그룹)로 자동 분리하는 비지도학습의 머신러닝이다. (unsupervised learning)
- 군집화는 데이터 안에서 발견되는 자연스런 그룹에 대한 통찰력을 제공
- 클러스터 안에 있는 아이템들은 서로 아주 비슷해야 하지만 클러스터 밖에 있는 아이템과 아주 달라야 한다. 
- 자율분류로 언급되는 것은 레이블이 없는 예시를 분류하기 때문이다. 

군집화 활용 범위
- 마케팅 캠페인을 위해 유사한 인구 통계나 구매 패턴을 가진 그룹으로 고객을 세분화
- 알고 있는 클러스터 밖의 사용패턴을 찾아 무단 네트워크 침입과 같은 이상 행동을 탐지 (보안분야)
- 유사한 값을 갖는 특징을 적은 개수의 동질적인 범주로 그룹핑해 초대형 데이터셋을 단순화 할 수 있다.

#cf. kNN: k-다수결의 문제를 가짐, k값을 가지고 성능을 조정함

k-means algorithm
# step1. k: 그룹으로 나누어야 할 군집의 개수 (거리계산을 통해 군집 개수에 따라 나눔)
# step2. means 각 군집들의 평균으로 위치를 위동
# step3. 다시 이동한 위치에서 거리 계산을 통해 군집을 다시 나눔 
# step4. 각 군집들의 평균으로 위치를 이동 
# --------------------------------------------
# step5. 새로운 데이터가 들어온다고 가정하기 
# step6. 새로운 데이터의 거리 계산을 통해 군집을 분류함
# step7. 새로운 데이터를 반영한 거리의 군집 평균인 위치의 중심이동을 함 
# ......
# 이를 반복하면서 각각의 그룹을 만든다. 
#cf. 거리의 값이 같을 경우 분류시 힘들다. -> 문제점을 가짐 
- n개의 예시를 k개의 클러스터 중 하나에 할당하는데 이때 k는 사전에 결정되는 수 
- 클러스터 내의 차이를 최소화하고 클러스터 간의 차이는 최대화한다. 

적당한 k값은? 
k = sqrt(n/2)
# cf. 목표하는 개수를 생각하면서 k값을 돌려보는 것도 나쁘지 않다.

c <- c(3,4,1,5,7,9,5,4,6,8,4,5,9,8,7,8,6,7,2,1)
row <- c("A", "B", "C","D","E","F","G","H","I","J")
col <- c("X", "Y")

data <- matrix(c, nrow=10, ncol=2, byrow=TRUE, dimnames = list(row,col))
data

plot(data)

#목표변수가 없는 상황에서 2개로 군집화하기
library(stats)

#2개로 
km <- kmeans(data, 2)
km
    # > km
    # K-means clustering with 2 clusters of sizes 5, 5
    # 
    # Cluster means:
    #   X   Y
    # 1 7 8.0
    # 2 3 3.8
    # 
    # Clustering vector:
    #   A B C D E F G H I J 
    #   2 2 1 2 1 2 1 1 1 2 
    # 
    # Within cluster sum of squares by cluster:
    #   [1]  8.0 20.8
    # (between_SS / total_SS =  74.5 %)
    # 
    # Available components:
    #   
    #   [1] "cluster"      "centers"      "totss"        "withinss"     "tot.withinss" "betweenss"    "size"         "iter"         "ifault"      

#평균에 대한 마지막 위치정보
km$centers
#
km$cluster
#군집화한 data 정보를 기존의 정보에 붙여넣기
cbind(data, km$cluster)

#point찍기
plot(data)
points(km$centers[,1],km$centers[,2], pch=3, cex=1.5, lwd=2)


#############################
grade <- read.csv("c:/data/academy.csv")

수학과 영어
math <- grade$수학점수
english <- grade$영어점수

c <- cbind(math, english)

#2개로 분류하기
km <- kmeans(c, 2)
km$cluster

cbind(c, km$cluster)

plot(c)
points(km$centers[,1],km$centers[,2], pch=15, cex=1.5, lwd=1)

#4개로 분류하기
km <- kmeans(c, 4)


#############################
#쌤이랑 같이하기
academy <- read.csv("c:/data/academy.csv")
academy2 <- academy[,c(3,4)]
plot(academy2)

km <- kmeans(academy2, 4)
points(km$centers[,1], km$centers[,2], pch=3, cex=1.5, lwd=2)

km$cluster

##############
군집화 시각화
install.packages("factoextra")
library(factoextra)
#k-menas를 가지고 군집화 그림을 그림 
fviz_cluster(km, data=academy2, stand=F, ellipse.type = "t", geom="point")
help(fviz_cluster)
fviz_cluster(km, data=academy2, stand=F, ellipse.type = "convex", geom="point")


#--------------------------------------------------------------
Python에서 하기 


Python> 
  
  
  from sklearn.cluster import KMeans
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

iris = pd.read_csv("c:\data\iris.csv")

#산점도를 통해서 흩어져 있는 정도 보기
#분류하고자 할 때 무엇을 가지고 분류해야할 지 선택할 때 산점도를 이용하도록 한다. 
plt.scatter(iris.SepalLength, iris.SepalWidth, s=40)
plt.title("Sepal")

plt.scatter(iris.PetalLength, iris.PetalWidth, s=40)
plt.title("Petal")

# 3가지 분류로 분류하기
model = KMeans(n_clusters=3)
#데이터를 가지고 학습시키기(이름빼고)
model.fit(iris.ix[:,0:4])
#레벨확인하기-> 3개 레벨로 만들어져 있음 
model.labels_
#Out[17]: 
#array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
#       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
#       1, 1, 1, 1, 1, 1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
#       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
#       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 2, 2, 2, 0, 2, 2, 2,
#       2, 2, 2, 0, 0, 2, 2, 2, 2, 0, 2, 0, 2, 0, 2, 2, 0, 0, 2, 2, 2, 2,
#       2, 0, 2, 2, 2, 2, 0, 2, 2, 2, 0, 2, 2, 2, 0, 2, 2, 0])

colormap = np.array(['red','blue','black'])
plt.scatter(iris.PetalLength, iris.PetalWidth, c=colormap[model.labels_], s=40) #color: 3가지색으로 분류되어있기 때문에 c=colormap[model.labels_]
plt.title("K Means Classification")



model.labels_

# kMeans에 init='k-means++': k값을 3개라 하면 어디에 표시자를 달것인가? 가장 첫번째에 데이터에 달고, 다음 두번째 데이터에 달고... 등
model.labels_



# =============================================================================
academy 데이터가지고 KMeans

academy = pd.read_csv("c:/data/academy.csv")

from pandas import Series, DataFrame
grade = DataFrame([academy["수학점수"], academy["영어점수"]])
grade = grade.T


#plt.scatter(academy.수학점수, academy.영어점수)
plt.scatter(grade.수학점수, grade.영어점수)

# k=4
#모델만들기
model = KMeans(n_clusters=4)
model.fit(grade.ix[:,0:1])
model.labels_

#scatter plot 그리기
colormap = np.array(['red','blue','green','black'])
plt.scatter(grade.수학점수, grade.영어점수, c=colormap[model.labels_], s=10) 
plt.title("K Means Classification")


# k=2
model = KMeans(n_clusters=2)
model.fit(grade.ix[:,0:1])

colormap = np.array(['red','blue'])
plt.scatter(grade.수학점수, grade.영어점수, c=colormap[model.labels_], s=10) 
plt.title("K Means Classification")


# =============================================================================
academy = pd.read_csv("c:/data/academy.csv")

academy.columns

model = KMeans(n_clusters=4)
model.fit(academy.ix[:,2:4])
model.labels_
#모델의 중심좌표 -> array형식으로 출력됨 
model.cluster_centers_

#
colormap = np.array(['red','blue','black','yellow'])
plt.scatter(academy.ix[:,2], academy.ix[:,3], c=colormap[model.labels_], s=30) 
centers = pd.DataFrame(model.cluster_centers_)
plt.scatter(centers.ix[:,0], centers.ix[:,1], s=50, marker='D', c='g')
plt.title("K Means Classification")
plt.show()

#k값을 변화주어 시뮬레이션 돌리기
ks = range(1,10)
inertia = []
for k in ks:
  model = KMeans(n_clusters=k)
model.fit(academy.ix[:,2:4])
inertia.append(model.inertia_)

inertia 
#k=1 일때 값은 커져 있음 그러다가 점점점 더디게 줄어듦
#Out[68]: 
#[24978.596153846152,
# 11716.462519936204,
# 8097.708683473389,
# 5145.44890077243,
# 3659.014880952381,
# 2445.419047619048,
# 1892.002380952381,
# 1493.169047619048,
# 1266.2690476190478]
# inertia가 작은 것이 응집도가 좋은 것이라 할 수 있다. 

plt.plot(ks, inertia, '-o')
plt.xlabel("number of cluster K")
plt.ylabel("inertia")
plt.xticks(ks)
plt.show()

#k값(그룹의 개수를)을 결정할 때 graph가 확 꺾여지는 지점으로 잡으면 좋다. (위의 데이터에서는 3-4으로 k값을 넣어서 비교해 본다.)

inertia value 
- 각 중심점에서 군집의 데이터간의 거리를 합산한 것으로 군집의 응집도를 나타내는 값이다. 
- 이 값이 작을수록 응집도가 높게 군집화가 잘 되었다고 평가한다. 



