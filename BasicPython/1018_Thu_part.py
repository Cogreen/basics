# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 13:46:32 2018

@author: stu
"""

20181018


# 워드 클라우드 추가설명(종현오빠 질문)
- 내가 추출한 빈도수를 가지고 워드클라우드를 만들고싶다

from wordcloud import WordCloud,STOPWORDS

import matplotlib.pyplot as plt

data={'국민':26,'대통령':33,'대한민국':9,'좋은나라':50}

wordcloud=WordCloud(font_path='c:\Windows\Fonts\malgunbd.ttf',stopwords=STOPWORDS,
         background_color='white',width=1000,height=800).generate_from_frequencies(data)

plt.figure(figsize=(10,10))
plt.imshow(wordcloud)
plt.axis('off')
plt.show()


# 훈이오빠의 질문
- 긍정의 반응, 부정의 반응
- https://www.lucypark.kr/docs/2015-pyconkr/#1      참고하면 좋을 자료

from nltk.tokenize import word_tokenize

import nltk

from konlpy.tag import Twitter

pos_tagger=Twitter()

train=[('홍길동은 좋아','긍정'),('강아지는 무지 좋아','긍정'),('수업이 재미없어','부정'),
   ('홍길동은 이쁜 강아지야','긍정'),('난 수업 마치고 홍길동이랑 놀거야','긍정'),
   ('오늘 하루는 너무 짜증스러운 날이야','부정'),('하루가 너무 짜증스러운 날이야','부정'),
   ('날이 맑아서 좋아','긍정'),('오늘 지하철에 사람이 너무 많아서 짜증이 난다','부정'),
   ('비가 오니 짜증난다','부정'),('친구가 짜증낸다','부정'),('하늘이 맑아서 행복하다','긍정'),
   ('공기가 맑아서 좋다','긍정'),('밝게 인사해주니 행복하다','긍정')]


allword=set(word for sentence in train
                for word in word_tokenize(sentence[0]))      단어사전의 중복성 제거를 위해 set하기

LookupError: 
**********************************************************************
  Resource punkt not found.
  Please use the NLTK Downloader to obtain the resource:

import nltk
nltk.download('punkt')
  
  Searched in:
    - 'C:\\Users\\stu/nltk_data'
    - 'C:\\nltk_data'
    - 'D:\\nltk_data'
    - 'E:\\nltk_data'
    - 'C:\\Users\\stu\\Anaconda3\\nltk_data'
    - 'C:\\Users\\stu\\Anaconda3\\share\\nltk_data'
    - 'C:\\Users\\stu\\Anaconda3\\lib\\nltk_data'
    - 'C:\\Users\\stu\\AppData\\Roaming\\nltk_data'
    - ''
**********************************************************************

nltk.download('punkt')               다운 받고 다시하기
[nltk_data] Downloading package punkt to
[nltk_data]     C:\Users\stu\AppData\Roaming\nltk_data...
[nltk_data]   Unzipping tokenizers\punkt.zip.
Out[28]: True

         allword=set(word for sentence in train
                for word in word_tokenize(sentence[0]))
                
allword            단어사전
Out[30]: 
{'강아지는',
 '강아지야',
 '공기가',
 '난',
 '난다',
 '날이',
 '날이야',
 '너무',
 '놀거야',
 '마치고',
 '많아서',
 '맑아서',
 '무지',
 '밝게',
 '비가',
 '사람이',
 '수업',
 '수업이',
 '오늘',
 '오니',
 '이쁜',
 '인사해주니',
 '재미없어',
 '좋다',
 '좋아',
 '지하철에',
 '짜증난다',
 '짜증낸다',
 '짜증스러운',
 '짜증이',
 '친구가',
 '하늘이',
 '하루가',
 '하루는',
 '행복하다',
 '홍길동은',
 '홍길동이랑'}

t=[({word : (word in word_tokenize(x[0])) for word in allword},x[1]) for x in train]

t[0]         사전의 단어가 첫번째 문장에 있는가? 있으면 True
Out[34]: 
({'오니': False,
  '좋아': True,
  '짜증스러운': False,
  '행복하다': False,
  '인사해주니': False,
  '맑아서': False,
  '짜증이': False,
  '비가': False,
  '마치고': False,
  '재미없어': False,
  '친구가': False,
  '강아지는': False,
  '난다': False,
  '하늘이': False,
  '강아지야': False,
  '너무': False,
  '무지': False,
  '수업': False,
  '날이': False,
  '날이야': False,
  '하루가': False,
  '밝게': False,
  '홍길동이랑': False,
  '이쁜': False,
  '하루는': False,
  '오늘': False,
  '놀거야': False,
  '짜증난다': False,
  '난': False,
  '많아서': False,
  '사람이': False,
  '홍길동은': True,
  '지하철에': False,
  '좋다': False,
  '공기가': False,
  '수업이': False,
  '짜증낸다': False},
 '긍정')

classifier=nltk.NaiveBayesClassifier.train(t)

classifier
Out[37]: <nltk.classify.naivebayes.NaiveBayesClassifier at 0x1c7f4278>

classifier.show_most_informative_features()
Most Informative Features
                      너무 = False              긍정 : 부정     =      1.9 : 1.0      '너무'가 없을 때 긍정과 부정의 비율 (긍정>부정)
                     맑아서 = False              부정 : 긍정     =      1.5 : 1.0
                      좋아 = False              부정 : 긍정     =      1.5 : 1.0
                      오늘 = False              긍정 : 부정     =      1.5 : 1.0
                     날이야 = False              긍정 : 부정     =      1.5 : 1.0
                   짜증스러운 = False              긍정 : 부정     =      1.5 : 1.0      '짜증스러운'이 없을 때 긍정과 부정의 비율(긍정>부정)
                    홍길동은 = False              부정 : 긍정     =      1.3 : 1.0
                    행복하다 = False              부정 : 긍정     =      1.3 : 1.0
                     많아서 = False              긍정 : 부정     =      1.2 : 1.0
                     짜증이 = False              긍정 : 부정     =      1.2 : 1.0


test='난 수업을 마치면 홍길동이랑 놀거야'

test_f={word:(word in word_tokenize(test)) for word in allword}

classifier.classify(test_f)
Out[45]: '긍정'

classifier.classify({word:(word in word_tokenize('오늘 왠일이니 짜증난다')) for word in allword})
Out[47]: '부정'

classifier.classify({word:(word in word_tokenize('하루가 너무 길다')) for word in allword})
Out[49]: '부정'

# 좋긴한데 개선이 필요함
# 조사가 붙으면 다 다른 글자로봄 명사 조사 구분이 안됨
# 형태소 분석을 먼저 해서 명사와 조사를 나눈 후에 분류하면 좋겠음


pos_tagger=Twitter()

def tokenize(doc):
    return ['/'.join(t) for t in pos_tagger.pos(doc,norm=True,stem=True)]



train_doc=[(tokenize(row[0]),row[1]) for row in train]

train_doc
[(['홍길동/Noun', '은/Josa', '좋다/Adjective'], '긍정'),
 (['강아지/Noun', '는/Josa', '무지/Noun', '좋다/Adjective'], '긍정'),
 (['수업/Noun', '이/Josa', '재미없다/Adjective'], '부정'),
 (['홍길동/Noun', '은/Josa', '이쁘다/Adjective', '강아지/Noun', '야/Josa'], '긍정'),
 (['난/Noun', '수업/Noun', '마치/Noun', '고/Josa', '홍길동/Noun', '이랑/Josa', '놀다/Verb'], '긍정'),
 (['오늘/Noun', '하루/Noun', '는/Josa', '너무/Adverb', '짜증스럽다/Adjective', '날/Noun', '이야/Josa']', '부정'),
 (['하루/Noun', '가/Josa', '너무/Adverb', '짜증스럽다/Adjective', '날/Noun', '이야/Josa']', '부정'),
 (['날/Noun', '이/Josa', '맑다/Adjective', '좋다/Adjective'], '긍정'),
 (['오늘/Noun', '지하철/Noun', '에/Josa', '사람/Noun', '이/Josa', '너무/Adverb', '많다/Adjective', '짜증/Noun', '이/Josa', '나다/Verb']', '부정'),
 (['비/Noun', '가/Josa', '오니/Noun', '짜증나다/Adjective'], '부정'),
 (['친구/Noun', '가/Josa', '짜증/Noun', '내다/Verb'], '부정'),
 (['하늘/Noun', '이/Josa', '맑다/Adjective', '행복하다/Adjective'], '긍정'),
 (['공기/Noun', '가/Josa', '맑다/Adjective', '좋다/Adjective'], '긍정'),
 (['밝다/Verb', '인사/Noun', '해주다/Verb', '행복하다/Adjective'], '긍정')]

tokens=[t for d in train_doc for t in d[0]]

tokens
Out[54]: 
['홍길동/Noun',
 '은/Josa',
 '좋다/Adjective',
 '강아지/Noun',
 '는/Josa',
 '무지/Noun',
 '좋다/Adjective',
 '수업/Noun',
 '이/Josa',
 '재미없다/Adjective',
 '홍길동/Noun',
 '은/Josa',
 '이쁘다/Adjective',
.....


def term_exists(doc):
    return{word:(word in set(doc)) for word in tokens}

train_x=[(term_exists(d),c) for d,c in train_doc]

train_x[0]
Out[58]: 
({'홍길동/Noun': True,
  '은/Josa': True,
  '좋다/Adjective': True,
  '강아지/Noun': False,
  '는/Josa': False,
  '무지/Noun': False,
  '수업/Noun': False,
  '이/Josa': False,
  '재미없다/Adjective': False,
  '이쁘다/Adjective': False,
  '야/Josa': False,
  '난/Noun': False,
  '마치/Noun': False,
  '고/Josa': False,
  '이랑/Josa': False,
  '놀다/Verb': False,
  '오늘/Noun': False,
  '하루/Noun': False,
  '너무/Adverb': False,
  '짜증스럽다/Adjective': False,
  '날/Noun': False,
  '이야/Josa': False,
  '가/Josa': False,
  '맑다/Adjective': False,
  '지하철/Noun': False,
  '에/Josa': False,
  '사람/Noun': False,
  '많다/Adjective': False,
  '짜증/Noun': False,
  '나다/Verb': False,
  '비/Noun': False,
  '오니/Noun': False,
  '짜증나다/Adjective': False,
  '친구/Noun': False,
  '내다/Verb': False,
  '하늘/Noun': False,
  '행복하다/Adjective': False,
  '공기/Noun': False,
  '밝다/Verb': False,
  '인사/Noun': False,
  '해주다/Verb': False},
 '긍정')

classifier=nltk.NaiveBayesClassifier.train(train_x)

classifier.show_most_informative_features()
Most Informative Features
                  가/Josa = True               부정 : 긍정     =      3.0 : 1.0      '가'가 있을 때 긍정과 부정의 비율(부정>긍정)
                  날/Noun = True               부정 : 긍정     =      2.1 : 1.0
               너무/Adverb = False              긍정 : 부정     =      1.9 : 1.0
            좋다/Adjective = False              부정 : 긍정     =      1.9 : 1.0
                  가/Josa = False              긍정 : 부정     =      1.7 : 1.0      '가'가 없을 때 긍정과 부정의 비율(긍정>부정)
            맑다/Adjective = False              부정 : 긍정     =      1.5 : 1.0
                홍길동/Noun = False              부정 : 긍정     =      1.5 : 1.0
                 이야/Josa = False              긍정 : 부정     =      1.5 : 1.0
                 오늘/Noun = False              긍정 : 부정     =      1.5 : 1.0
         짜증스럽다/Adjective = False              긍정 : 부정     =      1.5 : 1.0


test=[('홍길동이랑 놀거야')]

test_doc=tokenize(test[0])

test_f={word:(word in tokens) for word in test_doc}

classifier.classify(test_f)
Out[65]: '긍정'


test=[('오늘 왠일이니 짜증난다')]

test_doc=tokenize(test[0])

test_f={word:(word in tokens) for word in test_doc}

classifier.classify(test_f)
Out[66]: '부정'


# =============================================================================
# 오후수업 
# =============================================================================

■ 자료형에 따라 통계기법이 달라진다. 

#의사결정나무
#- cross table을 만들어서 chai-square 검증을 할 수 도 있고 
#- 어떤 변수를 사용하는가가 중요(cf 스무고개 생각하기)
#- if then - else 구조를 띤다. 
#- 어떤 알고리즘을 쓰느냐가 중요하다.
#- 필요한 3개 알고리즘: 카이제곱 검정, 엔트로피, 지니지수

▣ 의사결정트리
- 의사결정규칙(Decision rule)을 나무구조(Tree)로 도표화하여 분류(classification)하고 에측(prediction)을 수행하는 방법 

■ 활용분야
- 은행분야: 도산업체 분류(예측) 관거의 데이터로 부터 도산기업과 도산하지않은 기업을 찾아내는 방법 
- 카드발급대상자: 신용불량자 분류(예측)
- 통신: 이탈고객(해지자, 번호이동) 분류, 새로운 서비스 대상 고객 선정 
- 쇼핑: Direct mailing 대상 고객 선정

■ 결정트리 장점
- 지도학습(분류, 예측)의 데이터마이닝 기법
- 적용결과에 의해 if-then 표현하는 규칙이 생성 
- 규칙의 이행이 쉽고 SQL로도 할 수 있다. 
- 많은 분야에서는 결정을 내리게 된데 대한 이유를 설명하는 능력이 중요하다(해석력)

■ 분류나무(classification tree=결정트리)
- 목표변수: 범주형(긍정vs.부정, 도산vs.정상, 좋음 vs.나쁨)
- 분류 알고리즘
    CART: 지니지수(Gini index)
    C5.0: 엔트로피지수(Entropy index)
    CHAID: 카이제곱통계량(Chi-Square statistic)

#두 변수 간의 분석
#1) 분산분석
#2) 상관분석: 머신러닝이의 핵심 -> 3) 회귀분석
#4) 교차분석
    
■ 교차분석
- 교차분석은 범주형(명목척도 , 서열척도)으로 구성된 자료들간의 연관관계를 확인하기 위해 교차표를 만들어 관계를 확인하는 방법 
- 변수들의 빈도를 확인하고 그 빈도를 이용하여 상호 연관성을 판단한다.(빈도를 이용하는 이유는 명목척도이기 때문에)
- 이때 검정통계량으로 카이제곱(χ²)통계량을 이용하기 때문에 카이제곱검정이라고 한다. 
- 카이제곱(Chi-square)검정을 하기 위해서 교차표, 관측빈도, 기대빈도(행의 합과 열의 합을 가지고 주변확률을 구하여 기대빈도를 만든다.), 카이제곱통계량, 카이제곱분포의 자유도((행의 수 -1) * (열의 수-1))가 있다. 

□ 교차표 
- 2개의 조사요인에 대한 자료값을 각가 행과 열로 배열하여 교차되는 항목에 대한 빈도를 나타낸 표를 교차표라 한다. 
- 교차표의 행과 열에 범주형(명목척도)변수를 구분하여 넣으면 서로 연관성이 있는 빈도를 확인할 수 있다. 
예) 지역1과 지역2로 구분하여 최신 스마트폰의 구매 의사에 대한 각각의 행과 열에 해당하는 빈도를 표시한 교차표 

                    구 매 의 사
                있음      |       없음          |  행의 합
----------------------------------------------------------
지역 1  |       154       |        52           |    206
지역 2  |         7       |       112           |    119
----------------------------------------------------------
열의 합 |       161       |       164           |    325


□ 관측빈도(observed frequency)
  154       |        52
    7       |       112         
- 교차표를 작성할 때에는 직접 수집한 데이터를 기준으로 빈도를 입력해야 하는데 이처럼 실제로 수집된 데이터의 빈도를 관측빈도라고 한다. 

□ 기대빈도(expected frequency)
- 기대빈도는 전체빈도 n에 대하여 행과 열의 합을 기준으로 보았을 때 각 교차되는 셀에 몇 번의 빈도가 확인될 수 있을지를 예상하는 기대값이다. 
                  행의 합 * 열의 합
-  기대빈도  =  ----------------------
                    관측수

(206*161)/325= 102.05   |   (206*164)/325 = 103.95
(119*161)/325= 58.95    |   (119*164)/325 =  60.05
지역1 구매의사 있음의 기대빈도: (206*161)/325= 102.05  
지역1 구매의사 없음의 기대빈도: (206*164)/325 = 103.95

지역2 구매의사 있음의 기대빈도: (119*161)/325= 58.95
지역2 구매의사 없음의 기대빈도: (119*164)/325 = 60.05


                    구 매 의 사
                있음      |       없음          |  행의 합
----------------------------------------------------------
지역 1  |       154       |        52           |    206
기대빈도|       102       |        104          |
지역 2  |         7       |       112           |    119
기대빈도|        59       |        60           |
----------------------------------------------------------
열의 합 |       161       |       164           |    325


관측빈도 - 기대빈도의 차이값 

카이제곱 통계량(카이제곱검정)
- 카이제곱통계량이란 관측빈도와 기대빈도사이의 유의한 차이가 있는지를 확인하는 통계량을 의미한다. 
                     (관측빈도-기대빈도)²
- 카이제곱(χ²) = Σ ---------------------------
                         기대빈도
χ² = ((154-102)**2/102) + ((52-104)**2/104) + ((7-59)**2/59) + ((112-60)**2/60) 
   = 143.41

□ 카이제곱분포에서의 자유도 
- 카이제곱검정을 실시하는 경우에는 p값을 이용할수 있으며, 카이제곱분포의 유의수준과 자유도에 따라 결과를 판단한다. 
- 교차표에서 구성된 범주에 대한 자유도를 계산하는 방법은 교차표의 (행의 수 -1)*(열의 수 -1)
- df = (2-1)*(2-1) = 1


■ 독립성 검정(independence test)
1. 가설수립: 각 범주가 서로 독립적인지 아닌지에 대한 검정이므로 귀무가설은 독립적인것이다. 

Ho (Null Hypothesis): 귀무가설, 영가설
- 귀무가설은 일반적으로 믿어온 사실을 가설로 설정한다.
- 귀무가설은 당연한 사실이나 연구할 의미가 없는 가설로 설정한다.
H₁ (Anti Hypothesis): 대립가설, 연구가설
- 공공연하게 사실로 받아들여진 현상에 대립되는 가설로 연구를 통한 대립가설의 조사는 의미가 있다. 

Ho: 지역과 구매의사는 독립이다. (지역과 구매의사는 아무 의미가 없다.)
H₁: 지역과 구매의사는 독립적이지 않다. (지역과 구매의사는 아무 의미가 있다.)

2. 교차표, 교차빈도
3. 기대빈도
4. 카이제곱통계량
5. 자유도
6. 임계치: 카이제곱 분표에서 α=0.01(99%)유의수준, 자유도(df=1), 임계치는 6.63이므로 143.3보다 작다
7. 결론: 귀무가설을 기각하고 대립가설을 채택한다. 




