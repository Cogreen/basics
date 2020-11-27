# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 09:50:40 2018

@author: stu
"""

▣ Numpy
- 과학계산을 위한 라이브러리를 다차원배열을 처리하는데 필요한 기능을 제공한다.
- numpy 배열은 동일한 타입의 값들을 갖는다. 
- 배열의 차원을 rank라고 한다. 
- 신경망을 할 때 Numpy가 필요함 

■ 설치
pip install numpy

■ 불러들이기
import numpy as np

■ numpy 배열 생성
- 파이썬의 리스트를 사용하는 방법

z1 = np.array([1,2,3])
print(z1)
type(z1) #numpy.ndarray: 다차원 배열의 의미
z1.dtype #다차원 배열에 들어가 있는 데이터 형; 32bit운영체제에서 사용하는 integer  => 4GB정도 변수를 처리할 수 있다. 
z1.shape

z2 = np.array([[1,2,3],[4,5,6]])
print(z2)
type(z2)
z2.dtype
z2.shape

lst = [[1,2,3],[4,5,6],[7,8,9]]
z3 = np.array(lst)
z3.shape
#slicing하기
z3[0,]  #0행을 보여줌 
z3[1]   #1행을 보여줌
z3[:,0] #모든행(:)의 0열을 보여줌
z3[:,1] #모든행(:)의 1열을 보여줌
z3[:,2] #모든행(:)의 2열을 보여줌 
z3[0:2, 0] #0, 1행의 0열을 보여줌
z3[1:,1:]  #1행부터 ~다, 1열부터 다~ 보여 줌
z3[1:,:1]  #1행부터 ~다, 0열만 
z[0:2, 0:2]

■ 정수 인덱싱(integer indexing)
numpy배열 n에 대해서 n[[row1, row2], [col1, col2]]는 
n[row1, col1], n[row2, col2]
-> 두번 작성해야할 것n[row1, col1], n[row2, col2]을 한번n[[row1, row2], [col1, col2]]에 작성할 수 있다. 

lst = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
n = np.array(lst)
n[0,1] #0행 1열
n[2,3] #2행 3열
n[[0,2],[1,3]]  #[행],[열]

■ 부울린 인덱싱(boolean indexing)
lst = [[1,2,3],[4,5,6],[7,8,9]]
n = np.array(lst)
b = np.array([[False, True, False],
              [True, False, True],
              [False, True, False]])
n[b] #n이라는 array를 기준으로 b라는 부울린 값의 True값만 값을 나타냄

#조건절에 true값만 뽑아내기
b = (n % 2 == 0)
n[b]
n[n%2 == 0]

■ numpy에서 제공하는 함수를 사용해서 만드는 방법
□ zeros()함수는 배열에 모두 0을 넣는 함수 
#3x3배열이 초기값으로 0이 출력됨
np.zeros((3,3))

□ ones()함수는 배열에 모두 1을 넣는 함수
#4x4배열이 초기값으로 1이 출력됨
np.ones((4,4))

□ full()함수는 사용자가 지정한 값을 넣는 함수 
#3x3배열이 초기값으로 사용자가 지정한 값인 2로 출력됨
np.full((3,3),2)

□ eye()함수는 대각선으로 1이고 나머지는 0인 2차원배열을 생성
np.eye(3)
np.eye(4)

□ range(n)함수는 0~n-1까지의 숫자를 생성하는 함수
np.array(range(20)) #1차원 배열 

□ .reshape: 다차원을 변형하는 함수  #cf. r의 배열의 차원 바꾸기: reshape
z= np.array(range(20)).reshape(4,5)
z.reshape((20,))
z.reshape((5,4))
z.reshape(5,4)

■ numpy 연산
x = np.array([1,2,3])
y = np.array([4,5,6])
#인덱스를 가지고 연산하는 방법
x[0] + y[0]
x[1] + y[1]
x[2] + y[2]
# x와 y가 배열 형태가 같기 때문에 내부적으로 같은 방끼리 연산 된다. 
x+y
np.add(x,y)

x-y
np.subtract(x,y)

#같은 방끼리 곱해짐. 행렬의 곱이 아님
x*y
np.multiply(x,y)

x/y
np.divide(x,y)

lst1 = [[1,2],[3,4]]
lst2 = [[5,6],[7,8]]

x = np.array(lst1)
y = np.array(lst2)

#x의 0행 0열, y의 0행0열의 합
#행과 열을 표현할 때 둘다 가능
x[0,0] + y[0,0]
x[0][0]+y[0][0]

#2차원 배열에서도 np.사칙연산 가능
x+y
np.add(x,y)

x-y
np.subtract(x,y)

x*y
np.multiply(x,y)

x/y
np.divide(x,y)


#행렬의 곱 
np.dot(x,y)

x     y
1,2   5,6   (1*5 + 2*7)  (1*6 + 2*8) =(19, 22)
3,4   7,8   (3*5 + 4*7)  (3*6 + 4*8) =(43, 50)

x = np.array([[1,2],[3,4]])
np.sum(x)          #전체합
np.sum(x, axis=0)  #axis=0 열을 기준으로 해서 sum을 함
np.sum(x, axis=1)  #axis=1 행을 기준으로 해서 sum을 함

np.mean(x)          #전체평균
np.mean(x, axis=0)  #열기준의 평균
np.mean(x, axis=1)  #행기준의 평균

np.var(x)          #전체분산
np.var(x, axis=0)  #열기준의 분산
np.var(x, axis=1)  #행기준의 분산

np.std(x)          #표준편차
np.std(x, axis=0)  #열기준의 표준편차
np.std(x, axis=1)  #행기준의 표준편차

np.max(x)           #최대값
np.max(x, axis=0)   #열기준의 최대값
np.max(x, axis=1)   #행기준의 최대값

np.min(x)           #최소값
np.min(x, axis=0)   #열기준의 최소값
np.min(x, axis=1)   #행기준의 최소값 

x       색인값
1, 2    (0, 1)
3, 4    (2, 3)
#최소원소의 색인값
np.argmin(x)
np.argmin(x, axis=0)  #[0,0] 0행 1열이 아니라 1,3(0,1), 2,4(0,1)임 
np.argmin(x, axis=1)  #[0,0] 0행 1열이 아니라 1,2(0,1), 3,4(0,1)임 
#최대원소의 색인값
np.argmax(x)
np.argmax(x, axis=0)  #[0,0] 0행 1열이 아니라 1,3(0,1), 2,4(0,1)임 
np.argmax(x, axis=1)  #[0,0] 0행 1열이 아니라 1,2(0,1), 3,4(0,1)임 

#누적합
np.cumsum(x)
np.cumsum(x, axis=0) #열기준 누적합
np.cumsum(x, axis=1) #행기준 누적합
#cf. 한계확률 구할 때 열기준의합, 행기준의 합이 필요하다. 주변확률을 생각해야 하기때문에 

#누적곱
np.cumprod(x)
np.cumprod(x, axis=0)
np.cumprod(x, axis=1)

#전체곱
np.prod(x)
np.prod(x, axis=0)
np.prod(x, axis=1)

■ numpy자료형
int, float, bool, complex

□ 정수형(integer)
int8, int16, int32, int64
int8 = 2**7
int16 = 2**15
int32 = 2**31
int64 = 2**63

□ 실수형(float)
float16, float32, float64

□ 복소수(complex): 부동소숫점으로 표시하는 복소수
complex64, complex128

x = np.float32(1.0)
print(x)
print(type(x))
x.dtype

■ .arange() 함수
z1 = np.arange(5)
z1.dtype

z2 = np.arange(5, dtype="f") #dtype을 통해서 자료형을 선택할 수 있음
z2.dtype

#cf arange :0부터 그 숫자만큼 출력

#실수형로 시작점 3, 끝점 4까지 표현
np.arange(3,5, dtype="f")
#실수형으로 3,9까지 표현  (증가분은 1씩 증가)
np.arange(3,10, dtype="f")
# 시작점 2부터 3이전까지를 0,2씩 증가한 값을 출력
np.arange(2,3,0.2)

arr = np.arange(10)
arr
arr.shape #1차원배열
#5행2열로 만들기
arr.reshape(5,2)  #기본값은 행우선으로 만들어진다.
arr.reshape((5,2), order="C") #행우선(기본값)
arr.reshape((5,2), order="F") #열우선

arr = np.arange(10).reshape((5,2), order="F")
arr

■ .flatten():2차원배열을 1차원배열로 평탄화시키는 방법
arr #열우선
arr.flatten() #기본값(행우선)
arr.flatten('C') #행우선
arr.flatten('F') #열우선

arr.ravel()
arr.ravel('C')
arr.ravel('F')

arr1 = np.array([[1,2,3], [4,5,6]])
arr2 = np.array([[7,8,9],[10,11,12]])


np.concatenate([arr1, arr2], axis=0) #열기준으로 붙이겠다.
np.concatenate([arr1, arr2], axis=1) #행으로 붙이겠다.

np.hstack((arr1, arr2)) #np.concatenate([arr1, arr2], axis=1)와 같은 값 #행기준
np.vstack((arr1, arr2)) #np.concatenate([arr1, arr2], axis=0)와 같은 값 #열기준

#합쳐놓은 것을 다시 자르기 위해서는 slicing을 하면된다.

■ numpy브로드캐스트(broadcast)
np.broadcast

x=np.array([[1,2],[3,4]])
y=10 

#차원이 다르기 때문에 값이 더해지지 않는다. 그러나 y가 x모양에 맞게 만들어져 연산작업을 함 
#브로드캐스트가 없으면 loop를 통해 연산작업을 해줘야한다. 
x+y


w = np.array([10,20])
x*w

■ 난수값 표현
□ rand: 0~1 사이에 균일한 확률분포로 실수 난수를 생성하는 함수
np.random.rand(10)
np.random.rand(3,5)

□ randn: 기대값 0이고 표준편차 1인 표준 정규분포를 나타내는 난수를 생성하는 함수
np.random.randn(3,5)

□ randint: 균일한 분포의 정수 난수
np.random.randint(low, high=None, size=None)
np.random.randint(10, size=10) # 10: 0~10 사이  #size=10: 10개
np.random.randint(10,20, size=10) #10,20: 작은값:10 큰값:20 #size=10:10개
np.random.randint(10,20, size=(3,5)) #size를 3x5행렬로 표현

■ .repeat()
arr = np.arange(3)
arr.repeat(2)
arr.repeat([2,3,4]) #0은 2번, 1은 3번, 2는 4번을 반복하고 싶음

arr = np.random.randint(10,20, size=(2,5))
arr
arr.repeat(2)
arr.repeat(2, axis=0)
arr.repeat(2, axis=1)

■ np.tile  #cf. repeat과 비교하기
np.tile(arr, 2) #덩어리로 반복하기 

■ np.unique(): 유일값만 뽑아냄 
np.unique([11,11,2,3,2,12,12])

u = np.array(['a','b','a','a','b','c'])
np.unique(u)
#값과 빈도수가 동시에 출력 (값에 대한 빈도수가 return됨)
np.unique(u, return_counts=True) 

index, count = np.unique(u, return_counts=True)
print(index)
print(count)
#위의 값과 동일
#x, y = np.unique(u, return_counts=True)
#print(x)
#print(y)

#2차원 배열일 때
u = np.array([[1,0,0],[1,0,0],[2,3,4]])
np.unique(u)
np.unique(u, axis=0) #0행과 1행이 중복되어 하나로 출력됨(열기준으로 보기)
np.unique(u, axis=1) #주의하기: 없으면 값이 출력되지 않아야 하는데 순서가 바뀌어 출력됨 -> 모호성 발생. 따라서 이부분을 쓸 때는 조심하자!

u = np.array([[1,0,0],[1,0,0],[1,0,0]])
np.unique(u)
np.unique(u, axis=0)
np.unique(u, axis=1)

#u = np.array([[1,0,1],[1,2,1],[1,3,1]])
#np.unique(u)
#np.unique(u, axis=0)
#np.unique(u, axis=1)

■ np.maximum()  /np.minimum() /np.add()
#data 수가 같아야 함(현재 data1과 data2는 각각 10개임 ); 동일한 때만 가능함
data1 = np.arange(0,20,2)
data2 = np.arange(0,30,3)

#data1, data2각각의 인덱스의 값을 비교해서 최대값을 뽑아내기 
np.maximum(data1, data2)
#data1, data2각각의 인덱스의 값을 비교해서 최소값을 뽑아내기 
np.minimum(data1, data2)
#더하기
np.add(data1, data2)
#합집합
np.union1d(data1, data2)
#교집합
np.intersect1d(data1, data2)
#차집합
np.setdiff1d(data1, data2)

arr = np.array([5,4,1,3,2])
#오름차순으로 되어있는 인덱스 번호를 return해줌 
arr.argsort() #array([2, 4, 3, 1, 0], dtype=int64) 1은 2번인덱스, 2은 4번인덱스, ... 5는 0번인덱스

#오름차순정렬
ix= arr.argsort()      #ix= arr.argsort()[::]와 같은 값 출력; 오름차순 정
arr[ix]

ix= arr.argsort()[::]   #ix= arr.argsort() 과 같은 값 출력; 오름차순 정
arr[ix]

#내림차순정렬
ix= arr.argsort()[::-1] #-1: 제일 뒤에서부터를 의미함
arr[ix]


■ numpy의 배열을 pandas로 변환
lst = [[1,2,3], [4,5,6],[7,8,9]]
arr = np.array(lst)

import pandas as pd

df = pd.DataFrame(arr)

df.index
df.columns
#loc, ix: 인덱스 번호와 컬럼이름을 가지고 값을 출력할 수 있음
#1번 행의 0열과 1열을 출력함
df.loc[1,[0,1]]
df.ix[0:2,[0,1]]
#인덱스 번호만 가지고 할 수 있음
df.iloc[1,[0,1]]

