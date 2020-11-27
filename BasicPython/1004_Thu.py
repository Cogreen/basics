# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 09:51:04 2018

@author: stu
"""


# =============================================================================
# [문제186] http://www.skwyverns.com/Wyverns/Players/picther/picther_list.asp
이미지를 다운로드하세요.
# =============================================================================
#img가 full address로 안 보일 경우 

from bs4 import BeautifulSoup
import urllib.request as req

params = []
url = "http://www.skwyverns.com/Wyverns/Players/picther/picther_list.asp"
res = req.urlopen(url).read()
soup = BeautifulSoup(res, 'html.parser')
#전체 가져옴
lnk = soup.select('div.sell > div.sum > a > img')

#실제 물리적인 주소를 만드는 방법
for i in lnk:
    params.append('http://www.skwyverns.com' + i['src'])

type(params)

#파일 저장 
for p in params:
    splitStr = p.split('/')
    name = splitStr[len(splitStr)-1]
    fullPath = 'c:/sk_picther/' + name
    req.urlretrieve(p, fullPath)


#사용처에 대해 고민해보기 
select vs. select_one
find vs. find_all
###############################################################################

#성복이꺼 
    

from bs4 import BeautifulSoup
import urllib.request as req
from urllib import request

url = "http://www.skwyverns.com/Wyverns/Players/picther/picther_list.asp"
res = req.urlopen(url)
res

## 이미
head ='http://www.skwyverns.com'

soup = BeautifulSoup(res,'html.parser')

img=soup.select_one('#content > div > div.entrie_list > div.list_group')
                    
img = img.select('.sell > .sum > a > img')
img

cn=0
cn
name=''
for i in img:
    cn+=1
    print(i.attrs['src'])
    print(i.attrs['alt'])
    
    img_url=head+i.attrs['src']
    name=i.attrs['alt']
    
    request.urlretrieve(img_url,"c:/data/"+name+".jpg")
    

#아루미꺼
from bs4 import BeautifulSoup
import urllib.request as req

url = "http://www.skwyverns.com/Wyverns/Players/picther/picther_list.asp"
res = req.urlopen(url)
soup = BeautifulSoup(res, "html.parser")

src=[]
name=[]

for i in soup.select('div.sell > div.sum > a > img'):
    src.append('http://www.skwyverns.com'+i.get('src'))
    name.append(i.get('alt'))


from urllib import request

for i in range(len(src)):
    request.urlretrieve(src[i],'c:/data/skwyverns_{}.jpg'.format(name[i]))
    

# =============================================================================
# 오전수업
# =============================================================================
▣ selenium
- 웹브라우저를 컨트롤하여 웹 UI(User Interface)를 자동화하는 도구
- dynamic한 웹페이지를 웹크롤링하기 위한 도구 (user id/ user pw를 필요로 하는 경우)

■ selenium client 설치
pip install selenium

■ selenium driver를 설치 (control할 수 있는 driver)
firefox driver: https://github.com/mozilla/geckodriver/releases
chrome driver: https://sites.google.com/a/chromium.org/chromedriver/downloads
panthomsJS: http://phantomjs.org


■ 사용 
from selenium import webdriver
url = 'http://www.naver.com'

#phantomJS가 웹브라우저를 제어함
driver = webdriver.PhantomJS('c:/data/phantomjs.exe')
#3초동안 대기
driver.implicitly_wait(3)
driver.get(url)
#스크린샷 저장
driver.save_screenshot('c:/data/naver.png')
#나가기
driver.quit()


##login하여 쇼핑-장부구니같은 내용을 스크롤링하고 싶을 경우 

#step1 login을 하는 페이지를 첫페이지로 간다    
https://nid.naver.com/nidlogin.login

# 숨어서 로그인하게, -> 클릭이 필요함: 이를 짜야함 


# =============================================================================
# 오후 수업
# =============================================================================

from selenium import webdriver
from bs4 import BeautifulSoup

#입력창에 id와 pw넣기
user = "kimhj139"
mypass = "wmfrjdnsgkfn"

#driver
driver= webdriver.PhantomJS("c:/data/phantomjs.exe")
driver.implicitly_wait(3)
#접속해야 될 사이트에 접속하기
url_login = 'http://nid.naver.com/nidlogin.login'
driver.get(url_login)
# id를 입력하는  input 요소를 찾는다. 
# find_element_by_id(id): id속성으로 요소를 하나 추출한다.
inputid = driver.find_element_by_id("id")
#입력박스에 있는 텍스트 지우기; (이전에 혹시 inputid값이 있다면 지워주기)
inputid.clear()
#send_keys: 입력박스에 아이디 입력
inputid.send_keys(user)
#비밀번호 입력하는 input 요소를 찾는다.
inputpw = driver.find_element_by_id("pw")
#기존 input값에 pw가 있는 경우 지우기
inputid.clear()
#
inputpw.send_keys(mypass)

#로그인하기- 요소 선택을 통해서 로그인 부분을 찾기
<input type="submit" title="로그인" alt="로그인" value="로그인" class="btn_global" onclick="nclks('log.login',this,event)">
# find_element_by_css_selector(""): css선택자로 요소 하나 추출  (#class는 input.btn_global로 찾고, type에 submit을 넣어주기, 속성은 꼭 써줄 필요는 없으나 어떤 페이지에서는 class이름이 동일할 경우 type을 찾아 써줘야한다.)
loginbn = driver.find_element_by_css_selector("input.btn_global[type=submit]")

#로그인 버튼 클릭 하기: 아이디와 비밀번호 전송
loginbn.submit()



#예시- 네이버 페이> 쇼핑 > 디지털/가전 
#주소
driver.get("https://pay.naver.com/introduction/merchant/list?searchMerchantCategoryCode=50000003&searchTapType=merchant&searchSortType=payOrderCount&searchType=merchantName&searchKeyword=")
# 페이지의 element를 모두 가지고 옮
html = driver.page_source
#BeautifulSoup가 내용을 가져오지 못하기 때문에 panthomJS가 가져오는 역할을 한다.
soup = BeautifulSoup(html, "html.parser")
#태그 안에서 원하는 부분만 추출하기 
notice = soup.find_all('table', class_="tb_list tb_store")

for n in notice:
    print(n.text)
    
driver.quit()


#예시 - 쇼핑목록 가져오기
from selenium import webdriver
from bs4 import BeautifulSoup

#입력창에 id와 pw넣기
user = "kimhj139"
mypass = "wmfrjdnsgkfn"

#driver
driver= webdriver.PhantomJS("c:/data/phantomjs.exe")
driver.implicitly_wait(3)
#접속해야 될 사이트에 접속하기
url_login = 'http://nid.naver.com/nidlogin.login'
driver.get(url_login)
# id를 입력하는  input 요소를 찾는다. 
# find_element_by_id(id): id속성으로 요소를 하나 추출한다.
inputid = driver.find_element_by_id("id")
#입력박스에 있는 텍스트 지우기; (이전에 혹시 inputid값이 있다면 지워주기)
inputid.clear()
#send_keys: 입력박스에 아이디 입력
inputid.send_keys(user)
#비밀번호 입력하는 input 요소를 찾는다.
inputpw = driver.find_element_by_id("pw")
#기존 input값에 pw가 있는 경우 지우기
inputid.clear()
#
inputpw.send_keys(mypass)

#로그인하기- 요소 선택을 통해서 로그인 부분을 찾기
<input type="submit" title="로그인" alt="로그인" value="로그인" class="btn_global" onclick="nclks('log.login',this,event)">
# find_element_by_css_selector(""): css선택자로 요소 하나 추출  (#class는 input.btn_global로 찾고, type에 submit을 넣어주기, 속성은 꼭 써줄 필요는 없으나 어떤 페이지에서는 class이름이 동일할 경우 type을 찾아 써줘야한다.)
loginbn = driver.find_element_by_css_selector("input.btn_global[type=submit]")

#로그인 버튼 클릭 하기: 아이디와 비밀번호 전송
loginbn.submit()


#주소
driver.get("https://order.pay.naver.com/home")

# 페이지의 element를 모두 가지고 옮
html = driver.page_source

#BeautifulSoup가 내용을 가져오지 못하기 때문에 panthomJS가 가져오는 역할을 한다.
soup = BeautifulSoup(html, "html.parser")
#태그 안에서 원하는 부분만 추출하기 
notice = soup.find_all 
('#_rowLi20181002104236CHK2018100275436881 > div.p_inr')                
notice

                     
for n in notice:
    print(n.text)
    
driver.quit()

#_listContentArea > div:nth-child(2)

# =============================================================================
# chrome driver
# =============================================================================

from selenium import webdriver
from bs4 import BeautifulSoup

#입력창에 id와 pw넣기
user = "kimhj139"
mypass = "wmfrjdnsgkfn"

#driver
#driver= webdriver.PhantomJS("c:/data/phantomjs.exe")
driver = webdriver.Chrome("c:/data/chromedriver.exe")
driver.implicitly_wait(3)
#접속해야 될 사이트에 접속하기
url_login = 'http://nid.naver.com/nidlogin.login'
driver.get(url_login)
# id를 입력하는  input 요소를 찾는다. 
# find_element_by_id(id): id속성으로 요소를 하나 추출한다.
inputid = driver.find_element_by_id("id")
#입력박스에 있는 텍스트 지우기; (이전에 혹시 inputid값이 있다면 지워주기)
inputid.clear()
#send_keys: 입력박스에 아이디 입력
inputid.send_keys(user)
#비밀번호 입력하는 input 요소를 찾는다.
inputpw = driver.find_element_by_id("pw")
#기존 input값에 pw가 있는 경우 지우기
inputid.clear()
#
inputpw.send_keys(mypass)

#로그인하기- 요소 선택을 통해서 로그인 부분을 찾기
#<input type="submit" title="로그인" alt="로그인" value="로그인" class="btn_global" onclick="nclks('log.login',this,event)">
# find_element_by_css_selector(""): css선택자로 요소 하나 추출  (#class는 input.btn_global로 찾고, type에 submit을 넣어주기, 속성은 꼭 써줄 필요는 없으나 어떤 페이지에서는 class이름이 동일할 경우 type을 찾아 써줘야한다.)
loginbn = driver.find_element_by_css_selector("input.btn_global[type=submit]")



#로그인 버튼 클릭 하기: 아이디와 비밀번호 전송
loginbn.submit()



#예시- 네이버 페이> 쇼핑 > 디지털/가전 
#주소
driver.get("https://pay.naver.com/introduction/merchant/list?searchMerchantCategoryCode=50000003&searchTapType=merchant&searchSortType=payOrderCount&searchType=merchantName&searchKeyword=")
# 페이지의 element를 모두 가지고 옮
html = driver.page_source
#BeautifulSoup가 내용을 가져오지 못하기 때문에 panthomJS가 가져오는 역할을 한다.
soup = BeautifulSoup(html, "html.parser")
#태그 안에서 원하는 부분만 추출하기 
notice = soup.find_all('table', class_="tb_list tb_store")

for n in notice:
    print(n.text)
    
driver.quit()

# =============================================================================
# 다음 로그인 - 웹크롤러
# =============================================================================
from selenium import webdriver
from bs4 import BeautifulSoup

#입력창에 id와 pw넣기
user = "kimhj139"
mypass = "cnfqkf!7"

#driver
#driver= webdriver.PhantomJS("c:/data/phantomjs.exe")
driver = webdriver.Chrome("c:/data/chromedriver.exe")
driver.implicitly_wait(3)
#접속해야 될 사이트에 접속하기
url_login = 'https://logins.daum.net/accounts/loginform.do?url=https%3A%2F%2Fmember.daum.net%2Ffind%2Fid.do%3Faction%3Dhome'
driver.get(url_login)
# id를 입력하는  input 요소를 찾는다. 
# find_element_by_id(id): id속성으로 요소를 하나 추출한다.
inputid = driver.find_element_by_id("id")
#입력박스에 있는 텍스트 지우기; (이전에 혹시 inputid값이 있다면 지워주기)
inputid.clear()
#send_keys: 입력박스에 아이디 입력
inputid.send_keys(user)
#비밀번호 입력하는 input 요소를 찾는다.
inputpw = driver.find_element_by_id("pw")
#기존 input값에 pw가 있는 경우 지우기
inputpw.clear()
#
inputpw.send_keys(mypass)

#로그인하기- 요소 선택을 통해서 로그인 부분을 찾기
#<input type="submit" title="로그인" alt="로그인" value="로그인" class="btn_global" onclick="nclks('log.login',this,event)">
# find_element_by_css_selector(""): css선택자로 요소 하나 추출  (#class는 input.btn_global로 찾고, type에 submit을 넣어주기, 속성은 꼭 써줄 필요는 없으나 어떤 페이지에서는 class이름이 동일할 경우 type을 찾아 써줘야한다.)
loginbn = driver.find_element_by_css_selector("button.loginBtn[type=submit]")
# button
<button id="loginBtn" type="submit" class="btn_comm" onclick="_tiq.push(['__trackEvent', 'loginform_pc', 'login_daum']);">로그인</button>
#로그인 버튼 클릭 하기: 아이디와 비밀번호 전송
loginbn.submit()



#예시- 네이버 페이> 쇼핑 > 디지털/가전 
#주소
driver.get("https://pay.naver.com/introduction/merchant/list?searchMerchantCategoryCode=50000003&searchTapType=merchant&searchSortType=payOrderCount&searchType=merchantName&searchKeyword=")
# 페이지의 element를 모두 가지고 옮
html = driver.page_source
#BeautifulSoup가 내용을 가져오지 못하기 때문에 panthomJS가 가져오는 역할을 한다.
soup = BeautifulSoup(html, "html.parser")
#태그 안에서 원하는 부분만 추출하기 
notice = soup.find_all('table', class_="tb_list tb_store")

for n in notice:
    print(n.text)
    
driver.quit()

###############################################################################
# naver
<input type="submit" title="로그인" alt="로그인" value="로그인" class="btn_global" onclick="nclks('log.login',this,event)">
#태그 안에서 원하는 부분만 추출하기 
notice = soup.find_all('table', class_="tb_list tb_store")
###############################################################################


# =============================================================================
# 이미지 검색만 하기
# =============================================================================

#기본적인 step#################################################################
# 네이버> 검색 > 이미지
# 이미지 검색창을 알아야 함 
https://search.naver.com/search.naver?where=image&sm=tab_jum&query=


# 입력창 태그보기
# <input type="text" id="nx_query" name="query" class="box_window" maxlength="255" accesskey="s" value="" autocomplete="off" title="검색어 입력">

# img url
#<img src="https://search.pstatic.net/common/?src=http%3A%2F%2Fpost.phinf.naver.net%2FMjAxNzEyMDdfMjIy%2FMDAxNTEyNjQ0NDEyODAy.tWSXo2z5dNjQe_VMhffKFR7dwxrR4u7YypsOi7VYNrwg.c5EgFgAEWov-QJhwRRVXjPd_uvZHGCbQQtqrBNw2-b8g.JPEG%2FIJhr12cKveg86zwOBerfBe69yccY.jpg&amp;type=b400" class="_img" alt="아이언맨 슈트 총정리-마크1부터 48까지  | 포스트" onerror="var we=$Element(this); we.addClass('bg_nimg'); we.attr('alt','이미지준비중'); we.attr('src','data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7');" data-width="526" data-height="969" style="height: 150.654px; width: 81.7792px; left: 0px; top: 0px; zoom: 1; opacity: 1;">

#검색된 이미지를 더 많이 보기 위해서는 end key나, scroll bar를 내리거나, 밑의 화살키를 누르거나 하는 작업을 반복해서 해야 함 

import urllib.request as req
from bs4 import BeautifulSoup
from selenium import webdriver
#end key를 제어하는 모듈 
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome("c:/data/chromedriver.exe")

#이미지 검색해야할 창 
browser.get("https://search.naver.com/search.naver?where=image&sm=tab_jum&query=")
#id 속성으로 입력창 값을 찾음 # 입력창 태그보기
# <input type="text" id="nx_query" name="query" class="box_window" maxlength="255" accesskey="s" value="" autocomplete="off" title="검색어 입력">
elem = browser.find_element_by_id("nx_query")
#검색어 검색창에 검색어 넣기,+ 검색하기
elem.send_keys("아이언맨")
elem.submit()
#html tag 분석
brower.find_element_by....
#웹페이지에 있는 정보를 다 가져오기  => body만 가져온 다음 -> 이미지만 세세하게 들어

#body 태그 안에 있는 것을 기준으로 end 키를 내부적으로 돌리겠다.
browser.find_element_by_tag_name("body").send_keys(Keys.END)
#
time.sleep(5)
#end키를 한번 만 돌릴 경우 이미지를 다 볼 수 없기 때문에 반복문을 생성한다.
for i in range(1,2):
    browser.find_element_by_tag_name("body").send_keys(Keys.END)
    

# END키를 누르면 계속해서 tag가 바뀌게 됨

html = browser.page_source    
soup = BeautifulSoup(html, "html.parser")

#img를 찾아야 함
# <img src="https://search.pstatic.net/common/?src=http%3A%2F%2Fpost.phinf.naver.net%2FMjAxNzEyMDdfMjIy%2FMDAxNTEyNjQ0NDEyODAy.tWSXo2z5dNjQe_VMhffKFR7dwxrR4u7YypsOi7VYNrwg.c5EgFgAEWov-QJhwRRVXjPd_uvZHGCbQQtqrBNw2-b8g.JPEG%2FIJhr12cKveg86zwOBerfBe69yccY.jpg&amp;type=b400" class="_img" alt="아이언맨 슈트 총정리-마크1부터 48까지  | 포스트" onerror="var we=$Element(this); we.addClass('bg_nimg'); we.attr('alt','이미지준비중'); we.attr('src','data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7');" data-width="526" data-height="969" style="height: 196.568px; width: 106.702px; left: 0px; top: 0px; zoom: 1; opacity: 1;">

params = []

imglist = soup.find_all("img", class_="_img")

for im in imglist:
    params.append(im['src'])
    
params

a = 1
for p in params:
    req.urlretrieve(p, "c:/data/pictest/"+str(a)+".jpg")
    a += 1 
    
browser.quit()

###############################################################################
#스크롤 되다가 끊어지는 모양으로 나오게 될 경우 range값을 조정해본다. 
import urllib.request as req
from bs4 import BeautifulSoup
from selenium import webdriver
#end key를 제어하는 모듈 
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome("c:/data/chromedriver.exe")

#이미지 검색해야할 창 
browser.get("https://search.naver.com/search.naver?where=image&sm=tab_jum&query=")
#id 속성으로 입력창 값을 찾음 # 입력창 태그보기
# <input type="text" id="nx_query" name="query" class="box_window" maxlength="255" accesskey="s" value="" autocomplete="off" title="검색어 입력">
elem = browser.find_element_by_id("nx_query")
#검색어 검색창에 검색어 넣기,+ 검색하기
elem.send_keys("아이언맨")
elem.submit()

#body 태그 안에 있는 것을 기준으로 end 키를 내부적으로 돌리겠다.
browser.find_element_by_tag_name("body").send_keys(Keys.END)
#
time.sleep(5)

#time.sleep을 늘려서 모든 태그 주소값 가져와보기
for i in range(1,2):
    time.sleep(40)
    browser.find_element_by_tag_name("body").send_keys(Keys.END)
    time.sleep(40)
    
html = browser.page_source    
soup = BeautifulSoup(html, "html.parser")


params = []

imglist = soup.find_all("img", class_="_img")

for im in imglist:
    params.append(im['src'])
    

a = 1
for p in params:
    req.urlretrieve(p, "c:/data/pictest/"+str(a)+".jpg")
    a += 1 
    
    
browser.quit()

# =============================================================================
# google 이미지 웹크롤링
# =============================================================================
import urllib.request as req
from bs4 import BeautifulSoup
from selenium import webdriver
#end key를 제어하는 모듈 
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome("c:/data/chromedriver.exe")

browser.get("https://www.google.co.kr/imghp?hl=ko&tab=wi")

#id 속성으로 입력창 값을 찾음 # 입력창 태그보기
# naver: <input type="text" id="nx_query" name="query" class="box_window" maxlength="255" accesskey="s" value="" autocomplete="off" title="검색어 입력">
# google: <input class="gsfi" id="lst-ib" maxlength="2048" name="q" autocomplete="off" title="검색" type="text" value="" aria-label="검색" aria-haspopup="false" role="combobox" aria-autocomplete="list" dir="ltr" spellcheck="false" style="border: none; padding: 0px; margin: 0px; height: auto; width: 100%; background: url(&quot;data:image/gif;base64,R0lGODlhAQABAID/AMDAwAAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw%3D%3D&quot;) transparent; position: absolute; z-index: 6; left: 0px; outline: none;">
elem = browser.find_element_by_id("lst-ib")
#검색어 검색창에 검색어 넣기,+ 검색하기
elem.send_keys("아이언맨")
elem.submit()



#body 태그 안에 있는 것을 기준으로 end 키를 내부적으로 돌리겠다.
browser.find_element_by_tag_name("body").send_keys(Keys.END)

#
time.sleep(5)

#time.sleep을 늘려서 모든 태그 주소값 가져와보기
for i in range(1,2):
    time.sleep(5)
    browser.find_element_by_tag_name("body").send_keys(Keys.END)
    time.sleep(5)
    
html = browser.page_source    
soup = BeautifulSoup(html, "html.parser")


params = []

# naver: <img src="https://search.pstatic.net/common/?src=http%3A%2F%2Fpost.phinf.naver.net%2FMjAxNzEyMDdfMjIx%2FMDAxNTEyNjQ0NDE1NzE2.OPs8ezLyVGnCYm__ukqwZWmNvFTdpQKcKaVK6KeXJF4g.2NIe1RpaB-yuEshhbdJ75iqWaaWsDntQe-uXONbJfcog.JPEG%2FIQDWQKddg_ynSbDTKmWU42inVob8.jpg&amp;type=b400" class="_img" alt="아이언맨 슈트 총정리-마크1부터 48까지  | 포스트" onerror="var we=$Element(this); we.addClass('bg_nimg'); we.attr('alt','이미지준비중'); we.attr('src','data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7');" data-width="271" data-height="499" style="height: 177.154px; width: 96.2097px; left: 0px; top: 0px; zoom: 1; opacity: 1;">
#naver-  class="_img" 
# <img class="rg_ic rg_i" id="eYn1yvL47yOQmM:" jsaction="load:str.tbn" alt="아이언맨에 대한 이미지 검색결과" onload="typeof google==='object'&amp;&amp;google.aft&amp;&amp;google.aft(this)" src="data:image/jpeg;base64,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" style="width: 300px; height: 168px; margin-left: -2px; margin-right: -6px; margin-top: 2px;">


imglist = soup.find_all("img", class_="rg_ic rg_i")

for im in imglist:
    params.append(im['src'])
    
imglist


a = 1
for p in params:
    req.urlretrieve(p, "c:/data/pictest/"+str(a)+".jpg")
    a += 1 
    
    
browser.quit()