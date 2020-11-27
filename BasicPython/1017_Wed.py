# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 09:51:01 2018

@author: stu
"""

# =============================================================================
# [문제198] 상품구매여부를 knn으로 분류해주세요.
#
# =============================================================================
import csv

file = open("c:/data/buy.csv","r")
buy_csv = csv.reader(file)
next(buy_csv)

buy_list=[]
for i in buy_csv:
    buy_list.append(i)
print(buy_list)
buy_list

#train_set만들기
train_set=[]
for i in range(len(buy_list)):
    
    train_set.append(buy_list[i][:2])
    train_set[0]

#int(train_set[0][1])
#
#train_integer=[]
#for i in range(len(train_set)):
#    train_integer.append(int(train_set[i][0]))
#
#    #int(train_set[i][1]))
#print(train_integer)
#    


train_set=[]
for i in range(len(buy_list)):
    train_set.append(int(buy_list[i][:2]))
print(train_set)


#label만들기
label=[]
for i in range(len(buy_list)):
    label.append(buy_list[i][2])
print(label)

#예측하기    
from sklearn.neighbors import KNeighborsClassifier
import numpy as np

clf = KNeighborsClassifier(n_neighbors =3)

clf.fit(train_set, label)

clf.predict(np.array([25,120]).reshape(1,-1))[0]
clf.predict(np.array([25,280]).reshape(1,-1))[0]

# =============================================================================
#pandas사용: utf-8로 바꾸기
#쌤답 

from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import scale
import pandas  as  pd
import numpy as np

df = pd.read_csv("c:/data/buy.csv")

#scale: 표준정규화 작업의 method                
x_train = np.array([scale(df['나이']),scale(df['월수입'])]).T #.T:전치행렬
label = list(df['상품구매여부'])
age_mean = np.mean(df['나이'])
age_std = np.std(df['나이'])

pay_mean = np.mean(df['월수입'])
pay_std = np.std(df['월수입'])

K = 3
clf = KNeighborsClassifier(n_neighbors=K)
clf.fit(x_train,label)
#입력 값도 표준화된 값으로 넣어준다. scale작업=(입력값-평균)/표준편차
prediction_label = clf.predict(np.array([[(40-age_mean)/age_std, (500-pay_mean)/pay_std]]))[0]
prediction_label

