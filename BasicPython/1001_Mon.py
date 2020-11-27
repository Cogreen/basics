# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 09:49:43 2018

@author: stu
"""

from bs4 import BeautifulSoup

#html 가상으로 만들기

html="""
<html>
<body>
<div id = 'lecture1'>
<h1> 데이터 과학 </h1>
</div>
<div id = 'lecture2'>
<h1> 빅데이터분석 </h1>
<ul class = 'subject'>
<li> SQL </li>
<li> R </li>
<li> PYTHON </li>
</ul> 
</div>
</body>
</html>
"""

#분석기를 돌려야하고, 분석기는 저장해 둬야함 eg. soup

soup = BeautifulSoup(html, 'html.parser')


#h1 찾기: body는 생략가능 
##방법1
soup.html.div.h1.string                                                        
##방법2
soup.find('h1').string

#태그 모두 제거
soup.find('h1').get_text()
soup.find('h1').text

#변수에 h1 담기
h1 = soup.find('h1')
h1.string

#두번째 h1찾기
h2 = soup.find(id='lecture2')
h2.find('h1').string                                                            

#Python 찾기 (webpage에서 출력되는것;li목록이 다른 것에도 있을 것이라는 가정하에 뽑아내야함) 
#class_
soup.find('ul', class_='subject').string
#li가 여러개이기 때문에 get_text로 찾아야 함 -> 그러나 \n도 출력되기 때문에 다음 번과 같이 한다.
soup.find('ul', class_='subject').get_text()

ul = soup.find('ul', class_='subject')
for i in ul:
    print(i.string)
 
ul = soup.find('ul', class_='subject')                                          # 오류  
for i in ul:
    print(i.get_text())

for i in ul:                                                                   # 오류 
    print(i.text)
    
#find_all : 다 찾는 것  -> string으로는 찾아지지 않는다. : 따라서 get_text()를 이용해야함!
ul = soup.find_all('ul', class_='subject')
for i in ul:
    print(i.stirng)

ul = soup.find_all('ul', class_='subject')
for i in ul:
    print(i.get_text())

# 위와 유사한 method findAll
ul = soup.findAll('ul', class_='subject')
for i in ul:
    print(i.text)
    
# class 속성을 찾아야할 때는 꼭 class_로 넣어주거나 dictonary 모양으로 만들어 {'class':'subject'} 찾거나 하면 된다. (방법2가지)
ul = soup.find_all('ul', {'class':'subject'})
for i in ul:
    print(i.text)
    
    
■ css(cascading stylesheets)    
#stylesheets(eg. div..) 들에 대해서 편하게 분석하는 제공 툴 
□  select_one은 css 선택자 요소 하나를 추출   #find와 같은 역할을 한다. 

soup.select_one('div > h1').string      #>은 계층에 대한 표현

#두번째 h1을 찾기 -> id의 속성을 통해서 찾을 수 있음 
#div안에 id값을 표시할 때는 #(기호 샵)을 사용한다. 
soup.select_one('div#lecture1 > h1').string 

soup.select_one('div#lecture2 > h1').string 

                
# div.content 
-> .(점)은 그 안에 들어 있는 class를 의미한다. 


□ select는 css 선택자로 요소 여러개를 리스트로 추출한다. (기호의 의미 #:id, .:class를 의미)
s = soup.select('div#lecture2 > ul.subject > li')
for i in s:
    print(i.string)



■ 매번 url이 바뀔 경우에 crawling을 할 경우 
환율 정보 예시> 
https://finance.naver.com/marketindex/?tabSel=exchange#tab_section
https://finance.naver.com/marketindex


예를 들어 미국 환율만 뽑아 낼 경우 -> F12 -> 요소검사 -> span.value -> class가 value해당하는 string 값을 뽑아 내면 된다. 
<span class="value">1,111.80</span>

□url 내용을 가져오기 
from bs4 import BeautifulSoup
import urllib.request as req 

url = "https://finance.naver.com/marketindex"
res = req.urlopen(url)  #url에 있는 site내용을 가져옴 

#분석하기
soup = BeautifulSoup(res,"html.parser")
dollar = soup.select_one('div.head_info > span.value').string
print('USD/KRW', dollar)

□ copy> copy selector 으로 상위 정보와 함께 가져오기 ; 
1) #exchangeList > li.on > a.head.usd > div > span.value
2) soup.select_one을 통해서 span.vaule 뽑아내기 

1)    
#달러 찾기 
soup.select_one("#exchangeList > li.on > a.head.usd > div > span.value").string

#엔화 찾기
soup.select_one("a.head.jpy > div > span.value").string
soup.select_one("div.head_info.point_dn > span.value").string

#중국 원화 찾기
soup.select_one("a.head.cny > div > span.value").string


■ naver 실시간 검색
url1 = "https://datalab.naver.com/keyword/realtimeList.naver"
res = req.urlopen(url1)

soup = BeautifulSoup(res,"html.parser")
soup

막히네요.. 


#content > div > div.keyword_carousel > div > div > div:nth-child(1) > div > div > ul
ul = soup.find('ul', class_='rank_list')                                          # 오류  
for i in ul:
    print(i.text)


# =============================================================================
# 오후 수업 시작
# =============================================================================
html = """
<ul id = '조선왕'>
<li id = '태조'> '이성계' </li>
<li id = '정조'> '이방과' </li>
<li id = '태종'> '이방원' </li>
<li id = '세종'> '이도' </li>
<li id = '문종'> '이향' </li>
</ul>
"""

soup = BeautifulSoup(html, "html.parser")

#세종의 이름 뽑아내기; 세종의 id 속성 뽑아내기
soup.select_one("#세종").string
soup.select_one("#세종").text
soup.select_one("li#세종").string
soup.select_one("ul > li#세종").string
soup.select_one("#조선왕 #세종").string
soup.select_one("ul#조선왕 > li#세종").string
soup.select_one("li[id=세종]").string
#li:nth-of-type: li의 순서를 제한하여 id 속성 뽑아내기
soup.select_one("li:nth-of-type(4)").string
soup.select('li')

# list 형식으로 되어있는 text를 추출하기
for i in soup.select('li'):
    print(i.text)
    
soup.select('li')[0].string
soup.select('li')[3].string

#환율정보 nth-of-type 사용하기 (여러번 사용할 경우, 오류가 발생한다.-> 그땐 변수에 담아놓고 다시 시작하는 방법을 사용할 수 있다.)
url = "https://finance.naver.com/marketindex"
res = req.urlopen(url)
soup = BeautifulSoup(res,"html.parser")
l = soup.select_one('div.market1 > div.data > ul.data_lst > li:nth-of-type(1)')
l.select_one("span:nth-of-type(2)").string

#li:nth-of-type(2)
l = soup.select_one('div.market1 > div.data > ul.data_lst > li:nth-of-type(2)')
l.select_one("span:nth-of-type(2)").string

#li:nth-of-type(3)
l = soup.select_one('div.market1 > div.data > ul.data_lst > li:nth-of-type(3)')
l.select_one("span:nth-of-type(2)").string

#market2
l = soup.select_one('div.market2 > div.data > ul.data_lst > li:nth-of-type(1)')
l.select_one("span:nth-of-type(2)").string

#market3
l = soup.select_one('div.market3 > div.data > ul.data_lst > li:nth-of-type(1)')
l.select_one("span:nth-of-type(2)").string



# =============================================================================
# 개인실습: 네이버 부동산
# =============================================================================
url_reals = "https://land.naver.com/article/articleList.nhn?rletNo=97&rletTypeCd=A01&tradeTypeCd=A1"
real_state = req.urlopen(url_reals)
soup = BeautifulSoup(real_state, "html.parser")

#홀수만 매물 정보 검색가능
info = soup.select_one('tbody > tr:nth-of-type(1)')
info

price = info.select_one('td:nth-of-type(7)')
test = price.select_one('td > div> strong#')
test
                 
price.select_one('td > div > strong')


e.select_one('td:nth-of-type(7) > div > strong title')



# sale 타입
info.select_one('td:nth-of-type(1)')
info.select_one('td:nth-of-type(1) > div#inner')

# 특징
info.select_one('td:nth-of-type(2)')
# 단지정보 
info.select_one('td:nth-of-type(3)')
# 면적 
info.select_one('td:nth-of-type(4)')
# 동정보
info.select_one('td:nth-of-type(5)')
# 층수 정보
info.select_one('td:nth-of-type(6)')
# 중개업소 
info.select_one('td:nth-of-type(8)')


# =============================================================================
# 동아일보로 부터 인공지능 링크값 가져오기 
# =============================================================================
#contents > div:nth-child(9) > div > div:nth-child(2) > div.t > p.tit > a


url_ai = "http://news.donga.com/search?check_news=1&more=1&sorting=1&range=1&search_date=&query=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5"
ai = req.urlopen(url_ai)
soup = BeautifulSoup(ai, "html.parser")
soup

#
a = soup.select_one('.searchCont > div:nth-of-type(3) > div.t > p.tit > a')

#url 불러오기
lst = []
for i in soup.select('div.searchList > div.t > p.tit'):
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
     

# =============================================================================
# 설치하기 : konlpy 
# =============================================================================
Anaconda Prompt 
-설치 pip install konlpy 
- Java base 로 구현되어 있음 
- Java base 설치가 되어있어야 구현이 가능함 

- konlpy 실행이 안될 경우: pip install jpype1
- pip install jpype1 도 안될 경우: 밑의 step3개를 따르세요.
 
#step1
https://konlpy-ko.readthedocs.io/ko/v0.4.3/install/

#step2
https://www.lfd.uci.edu/~gohlke/pythonlibs/#jpype
JPype allows full access to Java class libraries. 

python 버전 확인 -> 3.6이기 때문에 / 운영체제 64bit이므로 
다운로드 : JPype1‑0.6.3‑cp36‑cp36m‑win_amd64.whl 
저장: c드라이브에 

#step3 
anaconda prompt을 관리자 권한으로 실행 
-> command line에서 cd c:\로 만들고 다시 설치 
-> dir *.whl # 파일이 있는지 확인

pip install JPype1‑0.6.3‑cp36‑cp36m‑win_amd64.whl

# =============================================================================
# konlpy 실행시키기
# =============================================================================
#java 경로 설정 
1) jdk의 위치 확인 후 
2) 시스템 고급 설정 > 환경변수
3) stu에 대한 사용자 변수 > 새로만들기
    -변수이름: JAVA_HOME
    -변수값: jdk 위치
4) 시스템 변수
    ;JAVA_HOME

#konlpy 실행 
from konlpy.tag import Twitter

twitter = Twitter()

malist = twitter.pos("아버지 가방에 들어가신다.", norm=True, stem=True)

print(malist)

pos: 형태소 분석
norm : 그래욬ㅋㅋㅋㅋ -> 그래요 로 바꿔줌
stem : 그렇다 원형을 찾아 준다

# 그래욬ㅋㅋㅋ 분석 
slang = twitter.pos('그래욬ㅋㅋㅋ', norm=True,  stem = True)
print(slang)

#txt분석 
txt = "텍스트 마이닝은 텍스트 형태의 데이터를 수학적 알고리즘에 기초하여 수집 , 처리 분석, 요약하는 연구 기법을 통칭하는 용어이다."

twitter.nouns(txt)
