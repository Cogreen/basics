# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 09:45:42 2018

@author: stu
"""

# =============================================================================
# KoNLPY(코엔엘파이) : 한국어 정보처리를 위한 파이썬 패키지
# =============================================================================

▣ KoNLPY(코엔엘파이) : 한국어 정보처리를 위한 파이썬 패키지

■ 형태소(morpheme)
- 언어학에서 일정한 의미가 있는 가장 작은 말의 단위를 뜻함 
- 자연어 처리에서 토큰으로 형태소를 이용한다. 

■ 형태소 분석(morphological analysis)
- 단어로 부터 어근, 접두사, 접미사, 품사 등 다양한 언어적 속성을 파악하고 이를 이용하여 형태소를 찾아내거나 처리하는 작업

■ KoNLPy
- 형태소 분석을 하기위해서 필요한 라이브러리를 모아 놓은 패키지이다.

■ 형태소 분석기 종류
    □ Twitter
    - 트위터 코리아에서 개발 
    - https://github.com/twitter/twitter-korean-text
    
    □ Kkma(꼬꼬마)
    - 서울대학교 개발
    - http://kkma.snu.ac.kr
    
    □ Hannaum(한나눔)
    - KAIST
    - http://semanticweb.kaist.ac.kr/hannanum
    
    □ Mecav(매카브)
    - 일어용 형태소 분석기를 한국어를 사용할 수 있도록 수정
    - http://bitbucket.org/eunjeon/mecab-ko
    
    □ Komoran(코모란)
    - shineware에서 개발 
    - http://github.com/shin285/KOMORAN

■ 설치 
pip install konlpy
pip install jpype1

■ 꼬꼬마 실행
from konlpy.tag import Kkma
kkma = Kkma() 

txt = '통찰력은 사물이나 현상의 원인과 결과를 이해하고 간파하는 능력이다. 통찰력을 얻는 좋은 방법은 독서이다'
txt1 = '통찰력은 사물이나 현상의 원인과 결과를 이해하고 간파하는 능력이고 통찰력을 얻는 좋은 방법은 독서이다'

#문장을 분석 
kkma.sentences(txt)
kkma.sentences(txt1)

#형태소 분석
kkma.pos(txt)

#명사 분석
kkma.nouns(txt)

■ Twitter 실행
from konlpy.tag import Twitter
twitter = Twitter()

#형태소 분석
twitter.pos(txt)

#명사 분석
twitter.nouns(txt)

#트위터에서 추가적으로 제공하는 부분: 맞춤법, 원형
txt = '그래욬ㅋㅋㅋㅋ'
twitter.pos(txt, norm=True, stem=True)
norm: '그래욬ㅋㅋㅋ -> 그래요'
stem: 그렇다 원형으로 찾아준다.

#꼬꼬마와 트위터 비교하기
txt = '텍스트 마이닝은 텍스트 형태의 데이터를 수학적 알고리즘에 기초하여 수집, 처리, 분석, 요약하는 연구기법을 통칭하는 용어이다.'

kkma.pos(txt)
twitter.pos(txt)

#konlpy의 corpus위치 정보
C:\Users\stu\Anaconda3\Lib\site-packages\konlpy\data\corpus

■ nltk 설치/실행: 
pip install nltk

import nltk

from konlpy.corpus import kolaw
#kolaw 디렉토리에 있는 내용을 보여줌 
kolaw.fileids()
#파일 읽어 들이기 
doc_ko = kolaw.open('constitution.txt').read()
#twitter로 명사를 뽑아내고 별도의 변수에 저장
tokens_ko = twitter.nouns(doc_ko)
tokens_ko
# 단어의 수를 세기 -> dictonary형으로 자료형으로 만들어 없으면 새로운 방을 만들어 counting, 있으면 누적해서 counting
# 단어의 수를 세기: nltk method 이용하기
ko = nltk.Text(tokens_ko)
# token이 만들어짐
ko.tokens
#단어개수를 뽑아줌
len(ko.tokens) 
#단어의 중복제거
len(set(ko.tokens))
#단어의 빈도수 
ko.vocab()

■ plot 만들기 -> 한국어를 깨지지 않게 하기 위해 폰트를 불러와야 함 
import matplotlib.pyplot as plt
from matplotlib import font_manager ,rc
font_name = font_manager.FontProperties(fname="c:\windows\Fonts\malgun.ttf").get_name()
rc('font',family=font_name)

# plot 만들기 
plt.figure(figsize=(12,6))
ko.plot(50) #상위 50개만 보여주기
plt.show()

#빈도 상위 10개 단어 보여주기 
ko.vocab().most_common(10)


■ 분석해야할 문서는 임의로 절대적 경로를 불러들일 수 없고, corpus위치 정보에 넣어야 함
- 문재인 대통령 취임사를 바탕으로 다시 분석하기
kolaw.fileids()

doc_ko = kolaw.open('moon_speech.txt').read()
#twitter로 명사를 뽑아내고 별도의 변수에 저장
tokens_ko = twitter.nouns(doc_ko)
tokens_ko
# 단어의 수를 세기 -> dictonary형으로 자료형으로 만들어 없으면 새로운 방을 만들어 counting, 있으면 누적해서 counting
# 단어의 수를 세기: nltk method 이용하기
ko = nltk.Text(tokens_ko)
# token이 만들어짐
ko.tokens
#단어개수를 뽑아줌
len(ko.tokens) 
#단어의 중복제거
len(set(ko.tokens))
#단어의 빈도수 
ko.vocab()


import matplotlib.pyplot as plt
from matplotlib import font_manager ,rc
font_name = font_manager.FontProperties(fname="c:\windows\Fonts\malgun.ttf").get_name()
rc('font',family=font_name)

# plot 만들기 
plt.figure(figsize=(12,6))
ko.plot(20) #상위 20개만 보여주기
plt.show()

#빈도 상위 10개 단어 보여주기 
ko.vocab().most_common(10)

■ 불용어(필요없는글자;stopword) 제거하기 
#리스트 변수에 불용어 만들기 
stopword=['.',',','(',')','의','지','에','간','것','곳','달','저','이','과','향']
#리스트 내장객체 생각해보기  (eachword가 stopword에만 없어야 ko안에서 eachwod를 리스트로 만들기)
ko = [eachword for eachword in ko if eachword not in stopword]
#토큰작업
ko = nltk.Text(ko)
# token이 만들어짐
ko.tokens
#단어개수를 뽑아줌
len(ko.tokens) 
#단어의 중복제거
len(set(ko.tokens))
#단어의 빈도수 
ko.vocab()
ko.vocab().most_common(10)

■ 다양한 method 
#특정단어 개수 세기
ko.count('국민')
#특정단어와 연관있는 단어(특정단어 side에 있는 단어)
ko.concordance('약속')
ko.concordance('문재인')

■ wordcloud install하기/ 실행하기
#Anaconda Prompt에 설치하기
pip install wordcloud
# 실행하기 (spyder에서 )
from wordcloud import WordCloud
#data 변수에 상위 30개 단어 담기
data = ko.vocab().most_common(30)
#wordcloud 만들기
wordcloud = WordCloud(font_path="c:\Windows\Fonts\malgunbd.ttf", background_color='white', width=1000, height=800).generate_from_frequencies(dict(data))
plt.figure(figsize=(10,10))
plt.imshow(wordcloud)
plt.axis("off")
plt.show()

# =============================================================================
# 꼬꼬마로 문재인 취임사 분석하기 (twitter로 분석한 부분 kkma로만 바꾸고 다시 실행)
# =============================================================================
■ 꼬꼬마로 분석하기 
doc_ko = kolaw.open('moon_speech.txt').read()
#kkoma로 명사를 뽑아내고 별도의 변수에 저장
tokens_ko = kkma.nouns(doc_ko)
tokens_ko
# 단어의 수를 세기 -> dictonary형으로 자료형으로 만들어 없으면 새로운 방을 만들어 counting, 있으면 누적해서 counting
# 단어의 수를 세기: nltk method 이용하기
ko = nltk.Text(tokens_ko)
# token이 만들어짐
ko.tokens
#단어개수를 뽑아줌
len(ko.tokens) 
#단어의 중복제거
len(set(ko.tokens))
#단어의 빈도수 
ko.vocab()


import matplotlib.pyplot as plt
from matplotlib import font_manager ,rc
font_name = font_manager.FontProperties(fname="c:\windows\Fonts\malgun.ttf").get_name()
rc('font',family=font_name)

# plot 만들기 
plt.figure(figsize=(12,6))
ko.plot(20) #상위 20개만 보여주기
plt.show()

#빈도 상위 10개 단어 보여주기 
ko.vocab().most_common(10)

■ 불용어(필요없는글자;stopword) 제거하기 
#리스트 변수에 불용어 만들기 
stopword=['.',',','(',')','의','지','에','간','것','곳','달','저','이','과','향']
#리스트 내장객체 생각해보기  (eachword가 stopword에만 없어야 ko안에서 eachwod를 리스트로 만들기)
ko = [eachword for eachword in ko if eachword not in stopword]
#토큰작업
ko = nltk.Text(ko)
# token이 만들어짐
ko.tokens
#단어개수를 뽑아줌
len(ko.tokens) 
#단어의 중복제거
len(set(ko.tokens))
#단어의 빈도수 
ko.vocab()
ko.vocab().most_common(10)

■ 다양한 method 
#특정단어 개수 세기
ko.count('국민')
#특정단어와 연관있는 단어(특정단어 side에 있는 단어)
ko.concordance('약속')
ko.concordance('문재인')

■ wordcloud install하기/ 실행하기
#Anaconda Prompt에 설치하기
pip install wordcloud
# 실행하기 (spyder에서 )
from wordcloud import WordCloud
#data 변수에 상위 30개 단어 담기
data = ko.vocab().most_common(30)
#wordcloud 만들기
wordcloud = WordCloud(font_path="c:\Windows\Fonts\malgunbd.ttf", background_color='white', width=1000, height=800).generate_from_frequencies(dict(data))
plt.figure(figsize=(10,10))
plt.imshow(wordcloud)
plt.axis("off")
plt.show()

# =============================================================================
# [문제185]동아일보 검색을 토대로 nlp분석
# =============================================================================

from bs4 import BeautifulSoup

#url가져오기
import urllib.request as req 

url_ai = 'http://news.donga.com/search?check_news=1&more=1&sorting=1&range=1&search_date=&query=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5'
ai = req.urlopen(url_ai)

#분석하기
soup_ai = BeautifulSoup(ai,"html.parser")
soup_ai


a_ai = soup_ai.select_one('.searchCont > div:nth-of-type(3) > div.t > p.tit > a')
a_ai

#url 불러오기
lst = []
for i in soup_ai.select('div.searchList > div.t > p.tit'):
    print(i.select_one('a')['href'])
    lst.append(i.select_one('a')['href'])
    
#본문 기사 정보 긁어오기 
lst   

cn = 0
txt = []
for i in lst:
    print(i)
    res = req.urlopen(i).read().decode('utf-8')
    soup = BeautifulSoup(res, 'html.parser')
    result = soup.select('div.article_txt')
    
    
    for i in result:
        #print(i.text)
       txt.append(i.text)
txt
    
new_txt = []

for i in range(0,15):
    new_txt.append(txt[i][0:txt[i].find('Copyright')])

#converting to list to string 1st way
news = ''
for i in new_txt :
    news +=i

news

#converting list to string 2nd way
str_ai =''.join(new_txt)
str_ai

■ twitter로 분석하기
from konlpy.tag import Twitter
twitter = Twitter()

#token작업 
ai_tokens = twitter.nouns(str_ai)
ai_tokens

# 단어의 수를 세기: nltk method 이용하기
ai = nltk.Text(ai_tokens)
# token이 만들어짐
ai.tokens
#단어개수를 뽑아줌
len(ai.tokens) 
#단어의 중복제거
len(set(ai.tokens))
#단어의 빈도수 
ai.vocab()


import matplotlib.pyplot as plt
from matplotlib import font_manager ,rc
font_name = font_manager.FontProperties(fname="c:\windows\Fonts\malgun.ttf").get_name()
rc('font',family=font_name)

# plot 만들기 
plt.figure(figsize=(12,6))
ai.plot(10) #상위 20개만 보여주기
plt.show()

#빈도 상위 10개 단어 보여주기 
ai.vocab().most_common(10)

■ 불용어(필요없는글자;stopword) 제거하기 
#리스트 변수에 불용어 만들기 
stopword=['.',',','(',')','의','것','등','또','고','수','곳','이','간엔','창','며','명','개','박','원', '때문', '더', '중', '은', '그', '건', '도', '를', '로','라며','위해']
#리스트 내장객체 생각해보기  (eachword가 stopword에만 없어야 ko안에서 eachwod를 리스트로 만들기)
ai = [eachword for eachword in ko if eachword not in stopword]
#토큰작업
ai = nltk.Text(ai)
# token이 만들어짐
ai.tokens
#단어개수를 뽑아줌
len(ai.tokens) 
#단어의 중복제거
len(set(ai.tokens))
#단어의 빈도수 
ai.vocab()
ai.vocab().most_common(1000)


■ wordcloud install하기/ 실행하기
#Anaconda Prompt에 설치하기
pip install wordcloud
# 실행하기 (spyder에서 )
from wordcloud import WordCloud
#data 변수에 상위 30개 단어 담기
data = ai.vocab().most_common(50)
#wordcloud 만들기
wordcloud = WordCloud(font_path="c:\Windows\Fonts\malgunbd.ttf", background_color='white', width=1000, height=800).generate_from_frequencies(dict(data))
plt.figure(figsize=(10,10))
plt.imshow(wordcloud)
plt.axis("off")
plt.show()



#[문제 185] 쌤답 - kkma사용
    #주의해야할 부분
        #기사형식에서 버려야 할 것을 버리고 string으로 저장 (1)
        #파일로 떨어뜨려 저장한 뒤, 파일로 읽어들여 분석하기 (2)

import urllib.request
from bs4 import BeautifulSoup

params = []
for i in range(1,50,15):
    list_url = "http://news.donga.com/search?p="+str(i)+"&query=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5&check_news=1&more=1&sorting=1&search_date=1&v1=&v2=&range=1"

    url = urllib.request.Request(list_url)
    res = urllib.request.urlopen(url, timeout=100).read().decode("utf-8")
    soup= BeautifulSoup(res, "html.parser")
    for link in soup.findAll('p', class_='tit'):
        params.append(link.find('a').get('href'))


txt= []
for i in params:
    #print(i)
    url = urllib.request.Request(i)
    res = urllib.request.urlopen(url).read().decode("utf-8")
    soup= BeautifulSoup(res, "html.parser")
    result = soup.find_all('div',{'class':'article_txt'})
    
    
    for i in result:
        #print(i.text)
       txt.append(i.text)


#기사형식에서 버려야 할 것을 버리고 string으로 저장 (1)
new_text =''
for i in range(0,60):
    new_text = new_text + txt[i][0:txt[i].find('Copyright')] + '\n'
    

import nltk
from konlpy.tag import Kkma
kkma = Kkma()

tokens_ko = kkma.nouns(new_text)
tokens_ko

ko = nltk.Text(tokens_ko)
len(ko.tokens)
len(set(ko.tokens))
ko.vocab()
ko.vocab().most_common(50)


#파일로 떨어뜨려 저장한 뒤, 파일로 읽어들여 분석하기 (2)
with open("c:/data/new_text.txt","w",encoding="utf-8") as file:
    for i in range(0,60):
        file.write(txt[i][0:txt[i].find('Copyright')])


with open("c:/data/new_text.txt","r",encoding="utf-8") as file:
    news = file.read()          #file.read(): 하나의 문서로 그대로 가져옴/ -> readlines으로 하면 안됨; list형식으로 가져오기 때문에 


import nltk
from konlpy.tag import Kkma
kkma = Kkma()

tokens_ko = kkma.nouns(news)
ko = nltk.Text(tokens_ko)
ko.vocab()



# =============================================================================
# wordcloud - 그림 넣기;  파일 참조 wordcloud.txt
# =============================================================================

#설치한 library 목록을 보여줌 
pip.exe list 

#공학쪽 library: scipy 
- scipy 확인하기 


from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

#UTF-8이 오류가 나서 ANSI 표준으로 바꿔 불러왔음 
with open("c:/data/moon.txt","r") as file:
	text = file.read()



from scipy.misc import imread

heart_mask = imread("c:/data/heart.jpg")

#공백 줄바꿈을 기준으로 Wordcloud를 만듦 
wordcloud = WordCloud(font_path = "c://Windows//Fonts//malgunbd.ttf", 
		stopwords=STOPWORDS,              #불용어 내부적으로 내장되어 있음; option; 
		background_color="white",
		width=1000,
		height=800,
		mask=heart_mask).generate(text)  #mask라는 변수에 heart_mask를 지정 

plt.figure(figsize=(10,10))
plt.imshow(wordcloud)
plt.axis("off")
plt.show()


# =============================================================================
# wordcloud2 - imageio.imread 로 이용하기
# =============================================================================
pip.exe list


from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

with open("c:/data/moon.txt","r") as file:
	text = file.read()


## from scipy.misc import imread 

## heart_mask = imread("c:/data/heart.jpg") # deprecated

import imageio

heart_mask = imageio.imread("c:/data/heart.jpg")


wordcloud = WordCloud(font_path = "c://Windows//Fonts//malgunbd.ttf", 
		stopwords=STOPWORDS,
		background_color="white",
		width=1000,
		height=800,
		mask=heart_mask).generate(text)

plt.figure(figsize=(10,10))
plt.imshow(wordcloud)
plt.axis("off")
plt.show()

# =============================================================================
# 웹페이지의 이미지를 컴퓨터에 저장
# =============================================================================

■ 웹페이지의 이미지를 컴퓨터에 저장

한겨례신문 - 더보기 - 만화 - 메인의 10월 2일 한겨레 그림판의 그림 긁어오기

from bs4 import BeautifulSoup
import urllib.request as req

url = "http://www.hani.co.kr/arti/cartoon/home01.html"
res = req.urlopen(url)
soup = BeautifulSoup(res, "html.parser")

lnk=soup.select_one('div.today-comic > a > img').get('src')

print(lnk)
http://img.hani.co.kr/imgdb/resize/2018/1001/53_1538392461_00503455_20181001.JPG


from urllib import request

request.urlretrieve(lnk,'c:/data/20181002.jpg')            #lnk위치의 파일을 c:/data에 20181002.jpg로 저장

Out[14]: ('c:/data/20181002.jpg', <http.client.HTTPMessage at 0x9de5b00>)
