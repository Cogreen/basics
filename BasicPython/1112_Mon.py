# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 09:43:34 2018

@author: stu
"""

from PIL import Image
import os, glob
import numpy as np
from sklearn.model_selection import train_test_split
caltech_dir = "c:/data/101_ObjectCategories"
categories = ["chair","camera","butterfly","elephant","flamingo"]
nb_class = len(categories)
image_w = 64
image_h = 64
pixels = image_w * image_h * 3
X = []
Y = []
for idx , cat in enumerate(categories):
    label = [0 for i in range(nb_class)]
    label[idx] = 1 
    image_dir =caltech_dir + "/"+cat
    files = glob.glob(image_dir+"/*.jpg") # 물리적 경로 형태 만들어 놓기
    for i ,f in enumerate(files):
        img =Image.open(f)
        img = img.convert("RGB")
        img = img.resize((image_w,image_h))
        data = np.asarray(img)
        X.append(data)
        Y.append(label)
        if i % 10 == 0:
            print(i,"\n",data)
X=np.array(X)            
Y=np.array(Y)
    

X_train ,X_test,y_train,y_test =train_test_split(X,Y)
xy = (X_train ,X_test,y_train,y_test)
# numpy 배열 저장하기 ,확장자는 npy 
np.save("c:/data/101_ObjectCategories/5obj.npy",xy)
print(len(Y))

from keras.models import Sequential
from keras.layers import Convolution2D , MaxPooling2D
from keras.layers import Activation ,Dropout , Flatten ,Dense
import numpy as np
categories = ["chair","camera","butterfly","elephant","flamingo"]
nb_class = len(categories)
image_w = 64 
image_h = 64
# 데이터 정규화
X_train ,X_test,y_train,y_test = np.load("c:/data/101_ObjectCategories/5obj.npy")
X_train =X_train.astype("float")/255
X_test =X_test.astype("float") / 255
X_train.shape
model = Sequential()
# input_shape : 입력값  입력값과 동일하게 same ,첫번째 은닉 층
model.add(Convolution2D(32,3,3,border_mode = "same",input_shape = X_train.shape[1:]))
# 32는 특징 그림조각 (레이어 틀)
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
# 성능 옵션: 가지치기 n% 만큼 
model.add(Dropout(0.25))


# 두번째 은닉층
model.add(Convolution2D(64,3,3,border_mode ="same"))
model.add(Activation('relu'))
model.add(Convolution2D(64,3,3))
model.add(MaxPooling2D(pool_size = (2,2)))
model.add(Dropout(0.25))
model.add(Flatten()) 
model.add(Dense(512)) # OUPUT 갯수로 생각하면 쉬움
model.add(Activation('relu'))
model.add(Dropout(0.5)) 
# 선 갯수
model.add(Dense(nb_class)) # 최종 OUTPUT
# 출력층  soft max
model.add(Activation('softmax'))
model.compile(loss='binary_crossentropy',optimizer= 'rmsprop',metrics = ['accuracy'])
# 모델 학습시키기
model.fit(X_train,y_train,batch_size = 32,nb_epoch = 50)
# 모델 평가
score =model.evaluate(X_test,y_test)
print('loss : ',score[0])
# 결과
print('accuracy : ' ,score[1])
# 이미지 각도를 바꿔가면서 데이터양을 많이 훈련하자
# 검증을 함 해볼까요>ㅋ<

import sys ,os
from PIL import Image
import numpy as np
image_size = 64
categories = ["chair","camera","butterfly","elephant","flamingo"]
nb_class = len(categories)
X = []
files = glob.glob("c:/data/101_ObjectCategories/sample.jpg")
for i ,f in enumerate(files):
    img=Image.open(f)
    img= img.convert("RGB")
    img= img.resize((image_size ,image_size))
    data= np.asarray(img)
    X.append(data)
X = np.array(X)    

# 모델 적합

np.argmax(model.predict(X))


# error!!
import sys ,os
from PIL import Image
import numpy as np
image_size = 64
categories = ["chair","camera","butterfly","elephant","flamingo"]
nb_class = len(categories)
X = []
files = glob.glob("c:/data/sample_4.jpg")
for i ,f in enumerate(files):
    img=Image.open(f)
    img= img.convert("RGB")
    img= img.resize((image_size ,image_size))
    data= np.asarray(img)
    X.append(data)
X = np.array(X)    

np.argmax(model.predict(X))

html = ""
pre = model.predict(X)
for i, p in enumerate(pre):
    y = p.argmax()
    print("입력:", files[i])
    print("분류 이름:", categories[y])
    html += """
        <h3>입력:{0}</h3>
        <div>
          <p><img src="{1}" width=300></p>
          <p>분류 이름:{2}</p>
         </div>
    """.format(os.path.basename(files[i]),
               files[i], categories[y])
# 리포트 저장하기 --- (※5)
html = "<html><body style='text-align:center;'>" + \
    "<style> p { margin:0; padding:0; } </style>" + \
    html + "</body></html>"
with open("c:/data/101_ObjectCategories/result.html", "w") as f:
    f.write(html)

# 이미지에 여백이 많으면 분리가 어려움 
pre = model.predict(X_test)
for i,v in enumerate(pre):
    pre_ans = v.argmax()
    ans = y_test[i].argmax()
    dat = X_test[i]
    if ans == pre_ans: continue
    print("[NG]", categories[pre_ans], "!=", categories[ans])
    print(v)
    fname = "c:/data/101_ObjectCategories/error/" + str(i) + "-" + categories[pre_ans] + \
        "-ne-" + categories[ans] + ".png"
    dat *= 256
    img = Image.fromarray(np.uint8(dat))
    img.save(fname)
score = model.evaluate(X_test, y_test)
print('loss=', score[0])
print('accuracy=', score[1])

# 학습된 모델 저장하기
from keras.models import load_model
model.save("c:/data/101_ObjectCategories/5obj-model.h5")

# 내보낸 모델 불러오기

model_1 = load_model("c:/data/101_ObjectCategories/5obj-model.h5")

# 새로운 이미지 테스트하기
import sys ,os
from PIL import Image
import numpy as np
image_size = 64
categories = ["chair","camera","butterfly","elephant","flamingo"]
nb_class = len(categories)
X = []
files = glob.glob("c:/data/sample_4.jpg")
for i ,f in enumerate(files):
    img=Image.open(f)
    img= img.convert("RGB")
    img= img.resize((image_size ,image_size))
    data= np.asarray(img)
    X.append(data)
X = np.array(X)    

np.argmax(model_1.predict(X))