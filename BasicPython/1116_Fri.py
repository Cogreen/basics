""" -*- coding: utf-8 -*-

Created on Fri Nov 16 09:53:59 2018

@author: stu
"""

▣ TF-IDF(Term Frequency - Inverse Document Frequency)

■ TF
- TF(단어 빈도)는 특정한 단어가 문서내에 얼마나 자주 등장하는지를 나타내는 값이다.
- 이 값이 높을 수록 문서에서 중요하다고 생각할 수 있다.
- 하지만 하나의 문서에 많이 나오지 않고 다른 문서에서 자주 등장하면 단어의 중요도는 낮아진다. 

문제 
- 한 문장에 여러개가 존재하면 TF값은 높아진다. 
- 문장마다 하나씩 존재하면 TF값은 작게된다.
- 그렇다면 이 문제를 해결하기 위해 ->idf 

■ IDF
DF(문서 빈도): 이 값을 역수를 IDF(역문서 빈도)
TF-IDF는 TF와 IDF를 곱한 값으로 점수가 높은 단어일수록 다른 문서에는 많지 않고 해당 문서에 자주 등장하는 단어의 의미이다. 

■ TF-IDF 계산 단계
1. 각 문서에 대한 각 단어의 빈도를 계산(TF)
2. IDF 계산
3. TF*IDF 

예시)
문서1 : if you think you can
문서2 : or you think you can not you are right


문서 1
단어       단어수 
------------------
if           1
you          2
think        1
can          1


문서 2
단어       단어수 
------------------
or           1
you          3
think        1
can          1
not          1         
are          1
right        1

문서1 단어수: 5
문서2 단어수: 9


think일 때>
단계1) 
          어떤 문서에서 단어 t가 나오는 횟수 
TF(t) = ----------------------------------------
              그 문서에 있는 단어의 총 수 

TF('think', 문서1) =  1 / 5 = 0.2
TF('think', 문서1) = 1 / 9 ≒ 0.11

단계2) 
IDF(t) = log10(문서의 총수)/ 단어 t가 들어간 문서의 수 
import numpy as np
IDF('think', D)  = np.log10(2/2)  = 0   #D:Document; 특정문서가 아님
IDF('right', D) = np.log10(2/1)  = 0.301029


단계3)
TF * IDF 계산
TFIDF('think', 문서1) = 0.2 * 0 = 0
TFIDF('think', 문서2) = 0.11 * 0 = 0
-> think 값이 유익하려면 값이 올라가야 한다.
-> 그러나 think 값이 0이기 때문에 유익하지 않은 값이다. 
-> 어떤 단어가 중요한지는 빈도수 뿐만 아니라 얼마나 포진되어있는지 확인해야 한다. 

 
right일 때>
단계1)
TF('right', 문서1) = 0/5 = 0
TF('right', 문서2) = 1/9 = 0.11

단계2)
IDF(t) = np.log10(2/1) = 0.301

단계3) 
TF * IDF 계산 
TFIDF('right', 문서1) = 0 * 0.301 = 0
TFIDF('right', 문서2) = 0.11 * 0.301 = 0.03311


# =============================================================================

▣ word2vec(word to vector)
- 구글의 토마스미콜로프(Tomas Mikolov) 이끄는 팀이 개발 
- 2계층 신경망(two layer neural network)을 사용해 개발
- 텍스트에서 벡터 집합을 생성한다. 

from konlpy.tag import Komoran 
tagger = Komoran()

from urllib.parse import quote_plus
from bs4 import BeautifulSoup
import requests
import lxml.html
import codecs

fp = codecs.open("c:/data/미술관옆동물원.txt", "r") #cursor 열어는 것처럼 이렇게 파일을 열어도 된다.
soup = BeautifulSoup(fp, "html.parser")
body = soup.select_one("body")
text = body.getText()
articles = []
articles = text.split("\n")
len(articles)
fp.close()

# ■ tfidf 를 제공해주는 library 
from sklearn.feature_extraction.text import TfidfVectorizer

#■ TfidfVectorizer
#- TF-IDF방식으로 단어의 가중치를 조정한 BOW 벡터를 만든다. 
#
#□ BOW(Bag of Words)
#- 문서를 숫자 벡터로 변환하는 가장 기본적인 방법 

corpus = ['This is the first document', 
          'This document is the second document', 
          'And this is the third one', 
          'Is this the first document']

# 이 클래스를 instance화 함 
v = TfidfVectorizer()
x = v.fit_transform(corpus) #term-document matrix 생성 

#matrix에서 특징이 될 만한 단어들의 목록을 보여줨; 단어들을 index만들어 놓음 
#단어들을 a-z으로 오름차순으로 만들어 놓음 
print(v.get_feature_names()) 

#['and', 'document', 'first', 'is', 'one', 'second', 'the', 'third', 'this']
x.shape #Out[52]: (4, 9)  #(4, 9)의 의미 -> 4: 문장의 수, 9: 분석해야 할 단어의 수
print(x)
# 총 문서는 4개 (0~3), 단어의 인덱스(0~8)
#  (0, 8)        0.38408524091481483    #(0,8) 첫번째 문장에서 this가 8번 인덱스에 있음 /  0.38408524(수치값): tf * idf 결과 
#  (0, 3)        0.38408524091481483    #(0,3) 첫번째 문장에서 is가 3번 인덱스에 있음 
#  (0, 6)        0.38408524091481483
#  (0, 2)        0.5802858236844359
#  (0, 1)        0.46979138557992045
#  (1, 8)        0.281088674033753
#  (1, 3)        0.281088674033753
#  (1, 6)        0.281088674033753
#  (1, 1)        0.6876235979836938     #제일 큰 tf*idf값(자주 나오면서 문장에 흩어져 많이 나오는 단어) : document라는 단어(두번째 문장의 2번 인덱스 값)
#  (1, 5)        0.5386476208856763
#  (2, 8)        0.267103787642168
#  (2, 3)        0.267103787642168
#  (2, 6)        0.267103787642168
#  (2, 0)        0.511848512707169
#  (2, 7)        0.511848512707169
#  (2, 4)        0.511848512707169
#  (3, 8)        0.38408524091481483
#  (3, 3)        0.38408524091481483
#  (3, 6)        0.38408524091481483
#  (3, 2)        0.5802858236844359
#  (3, 1)        0.46979138557992045

#index번호 확인하기
print(v.vocabulary_.get('first')) 
print(v.vocabulary_.get('document')) 

#■  문서를 토큰 리스트로 변화한다. 
from sklearn.feature_extraction.text import CountVectorizer
#- 문서를 토큰 리스트로 변화한다. 
#- 각 문서에서 토큰의 출현빈도를 센다. 
#- 각 문서를 BOW 인코딩 벡터로 변환한다. 

c = CountVectorizer()
c.fit(corpus)

# 단어를 딕션너리형으로 인덱스 추출 
c.vocabulary_
#Out[60]: 
#{'this': 8,
# 'is': 3,
# 'the': 6,
# 'first': 2,
# 'document': 1,
# 'second': 5,
# 'and': 0,
# 'third': 7,
# 'one': 4}

c.transform(['This is the second document']).toarray()
#Out[63]: array([[0, 1, 0, 1, 0, 1, 1, 0, 1]], dtype=int64)
# c.vocabulary_의 단어의 개수를 'this is the second document'를 확인함 ['and', 'document', 'first' ...] -> [0,1,0....]
# 즉 단어에서 문장을 바라보는 것 (9개 단어가 문장을 filter함)

c.transform(corpus).toarray()
#Out[65]: 
#array([[0, 1, 1, 1, 0, 0, 1, 0, 1],
#       [0, 2, 0, 1, 0, 1, 1, 0, 1], 
#       [1, 0, 0, 1, 1, 0, 1, 1, 1],
#       [0, 1, 1, 1, 0, 0, 1, 0, 1]], dtype=int64)


# 2글자 이상인 명사만 추출 
def get_noun(text):
    nouns = tagger.nouns(text)
    return [n for n in nouns if len(n) > 1]

# =============================================================================
# java.lang.NullPointerExceptionPyRaisable: java.lang.NullPointerException 
# -> 빈칸이 있거나 띄어쓰기가 있을 경우 nullpointerexception이 발생 따라서 용선이나 훈오빠 버전으로 돌리기 
#    
# cv = TfidfVectorizer(tokenizer=get_noun, max_features=100) #java.lang.NullPointerExceptionPyRaisable: java.lang.NullPointerException; 오류 남 뽑아내야할 method #feature값 maximum 100개로 
# 
# cv = TfidfVectorizer()
# tdm = cv.fit_transform(articles)
# 
# cv = TfidfVectorizer(max_features=100)
# tdm = cv.fit_transform(articles)
# 
# cv = TfidfVectorizer(tokenizer=get_noun)
# tdm = cv.fit_transform(articles)
# 
# 
# =============================================================================
# 용선이 버전 articles_1에 다시 넣기
count=0
articles_1=[]
for i in articles:
    if len(i)==0:
        print(count)
        continue
    articles_1.append(i)

cv = TfidfVectorizer(tokenizer=get_noun, max_features=100)
tdm = cv.fit_transform(articles_1)

print(cv.get_feature_names())
print(tdm.toarray())
print(tdm)


#훈오빠 버전 
articles = [article for article in articles if len(article)>0]

def get_noun(text):
    nouns=tagger.nouns(text)
    return [n for n in nouns if len(n)>1]

cv = TfidfVectorizer(tokenizer=get_noun, max_features=100)
tdm = cv.fit_transform(articles)

print(cv.get_feature_names())
print(tdm.toarray())
print(tdm) #각각의 tf*idf 값 


# =============================================================================
import numpy as np
import operator # dictionary에 대한 정렬을 위해 필요한 moduel 

# 100개 단어에 대한 tdm값을 옆에 붙이는 작업
# 단어를 하나씩 key에 넣고 
words = cv.get_feature_names()
# 같은 값을 sum 해줌  (tdm을 value로 넣기위해)
count_map = tdm.sum(axis=0)
count_map.shape  #Out[133]: (1, 100): 2차원임 

#squeeze: 차원을 없앰 (1차원을 줄임) -> 1차원으로 만듦 
count = np.squeeze(np.array(count_map))
count.shape #Out[132]: (100,): 1차원으로 만듦 

# word와 tdm 값을 붙이기 
word_count = list(zip(words, count))
#Out[135]: 
#[('가방', 4.434913496798847),
# ('강아지', 5.080785037138985),
# ('거리', 4.900322014383277),
# ('거지', 5.043354781541623),

# value절을 중심으로 내림차순 정리  # key=operator.itemgetter(0): 이름을 기준으로 #key=operator.itemgetter(1): tdm값을 기준으로
word_count = sorted(word_count, key=operator.itemgetter(1), reverse=True)
#Out[138]: 
#[('춘희', 337.43858525826454),
# ('철수', 293.91056879594333),
# ('다혜', 95.45631516029485),
# ('소리', 71.14455790664736),
# ('인공', 58.087670600711924),
# ('사람', 34.16288367723765),

# 상위 50개만 보기
hot_key = list(dict(word_count[:50]).keys())

# wordclouda만들기
from matplotlib import pyplot
from wordcloud import WordCloud

wc = WordCloud(font_path='c:\\Windows\Fonts\malgunbd.ttf',background_color="white", width=400, height=300)
cloud = wc.fit_words(dict(word_count))
pyplot.figure(figsize=(12,9))
pyplot.imshow(cloud)
pyplot.axis("off")
pyplot.show()

wc = WordCloud(font_path='c:\\Windows\Fonts\gulim.ttc',background_color="white", width=400, height=300)
cloud = wc.fit_words(dict(word_count))
pyplot.figure(figsize=(12,9))
pyplot.imshow(cloud)
pyplot.axis("off")
pyplot.show()


# =============================================================================
# 이 작업을 하는 이유: 의외성을 볼 수 있음 
# -> 즉, 쇼핑이라는 단어를 검색할 때 예상치 못한 단어를 볼 때, 여기서 왜 그 단어가 나왔는지 분석하고 insight를 제공할 수 있다. 

from konlpy.tag import Komoran
tagger = Komoran()  # 형태소 분석기
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
import requests
import lxml.html
import codecs


articles = []
fp = codecs.open("c:/data/미술관옆동물원.txt", "r")
soup = BeautifulSoup(fp, "html.parser")
body = soup.select_one("body")
text = body.getText()
articles = text.split("\n")
len(articles)
fp.close()



from sklearn.feature_extraction.text import TfidfVectorizer

def get_noun(text):
    nouns = tagger.nouns(text)
    return [n for n in nouns if len(n) > 1] 


cv = TfidfVectorizer(tokenizer=get_noun, max_features=100)
tdm = cv.fit_transform(articles)
print(cv.get_feature_names())
print(tdm.toarray())
print(tdm) 


import numpy as np
import operator
words = cv.get_feature_names()

count_mat = tdm.sum(axis=0)
count_mat.shape
count = np.squeeze(np.asarray(count_mat))
count.shape
word_count = list(zip(words, count))
word_count = sorted(word_count, key=operator.itemgetter(1), reverse=True)
word_count

hot_key = list(dict(word_count[:50]).keys())
hot_key


%matplotlib inline
from matplotlib import pyplot
from wordcloud import WordCloud
wc = WordCloud(font_path='C:\\Windows\\Fonts\\NGULIM.ttf', background_color='white', width=400, height=300)
cloud = wc.fit_words(dict(word_count))
pyplot.figure(figsize=(12, 9))
pyplot.imshow(cloud)
pyplot.axis("off")
pyplot.show()

#=== 위에는 지금까지 한 부분
import codecs
from konlpy.tag import Twitter
from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.preprocessing import StandardScaler

def sigmoid(x):
    return 1 / (1 + math.e ** -x)


twitter = Twitter()
results = []
lines = articles
words_all = []

for line in lines:
    # 형태소 분석하기
    malist = twitter.pos(line, norm=True, stem=True)
    r = []
    for word in malist:
        # 명사/동사/부사만 걸러내기 
        if word[1] in ['Noun','Verb','Adjective']:
            r.append(word[0])
            words_all.append(word[0])
    rl = (" ".join(r)).strip()
    results.append(rl)
    #print(rl)


#reults 된 부분을 file로 떨어뜨림 
from gensim.models import word2vec

yang_file = 'c:/data/yang.model'
with open(yang_file, 'w', encoding='utf-8') as fp2:
    fp2.write("\n".join(results))    
fp2.close() 

# word2vec으로 돌리기
data = word2vec.LineSentence(yang_file) 
model = word2vec.Word2Vec(data,size=200, window=10, hs=1, min_count=2, sg=1) 
# word2vec.Word2Vec(data,size=200, window=10, hs=1, min_count=2, sg=1) 
# size : 200차원 벡터
# window : 주변단어는 앞뒤로 10개씩 
# min_count : 출현빈도가 2개 미만은 제외
# hs : 1이면 softmax를 트레이닝할때 사용/ 0이면 0이 아닌 음수로 샘플링(sampling)된다. (보편적으로 1로 한다.)
# sg : 분석방법론은 CBOW와 Skip-Gram
    # CBOW(Continuous Bag Of Word) : 주변 단어들을 가지고 중심에 있는 단어를 맞추는 방식
    # Skip-Gram : 중심에 있는 단어로 주변 단어를 예측하는 방법 
    
# 학습된 모델을 save
model.save("c:/data/yang_w2v.model")

# most_similar: 유사단어
# 춘희와 positive하게 유사한 단어 찾기 (춘의와 가까운 단어 찾기)
model.most_similar(positive=["춘희"])
# 춘희와 positive하게 유사한 단어 찾기 
model.most_similar(positive=["철수"])
model["결혼"]
model["사람"]
# 유사한 단어를 찾되 여자는 빼고 찾기
# 미술관, 여자의 유사단어를 찾되 여자는 빼고 유사도를 찾음
model.most_similar(positive=["미술관","여자"] , negative=["여자"])
# 비교 테스트 
model.most_similar(positive=["미술관","여자"])
model.most_similar(positive=["미술관"])
model.most_similar(positive=["여자"])

# 두개의 관계의 밀접도 보기 (캐릭터 끼리 관련하여 관련성 알아보기)
model.similarity('춘희','철수')
model.similarity('춘희','인공')





