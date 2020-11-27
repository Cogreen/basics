# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 09:52:16 2018

@author: stu
"""

# =============================================================================
# 정규표현식(Regular Expression) 
# =============================================================================

▣ 정규표현식(Regular Expression)

import re

source = "Data Science"

■ re.match
- boolean 형식의 값을 return문 
- 조건 제어문에서 사용하는 것이 유리하다.

# Da’라는 글자가 source에서 처음부터 어디까지 있는지 match하자
m = re.match('Da',source)

# 대소문자를 구분함 -> 현재 값: None
re.match('da',source)
print(re.match('da',source))

#
if m:
    print('패턴이 일치한다.')
else: 
    print('패턴이 불일치한다.')
    

#
if re.match('da',source):
    print("패턴이 일치한다.")
else:
    print("패턴이 불일치한다.")
    
# re.I : 대소문자 구분 하지 않기
if  re.match('da', source, re.I):
    print("패턴이 일치한다.")
else:
    print("패턴이 불일치한다.") 

#group, start, end, span에 대한 method 의미
source = "Data Science"
m = re.match('da', source, re.I)
if  m:
    print("패턴이 일치한다.")
    print(m.group())
    print(m.start())
    print(m.end())
    print(m.span())
else:
    print("패턴이 불일치한다.") 
    
■ re.match : 앞의 패턴을 찾는 것을 의미
#re.match에 대한 boolean return을 확인하기    
bool(re.match('D','Data'))
#[0-9]숫자의 패턴으로 되어있는지 확인하기
# *의 의미확인하기
bool(re.match('[0-9]th', '2th'))
bool(re.match('[0-9]th', '21th'))
bool(re.match('[0-9][0-9]th', '21th'))
bool(re.match('[0-9]*th', '21th'))
bool(re.match('[0-9]*th', '2th'))
bool(re.match('[0-9]*th', 'th'))
bool(re.match('[0-9]th', 'th'))
bool(re.match('[0-9]*th', '212th'))
#\d: [0-9]를 의미(숫자 패턴 확인)
bool(re.match('\d\dth', '21th'))
bool(re.match('\d*th', '21th'))

#메타문자
- a.b: .위치에 모든 문자 온다, aab, acb, aob
- .은 한글자 한글자를 의미한다. 
bool(re.match('D.','Data'))
bool(re.match('D...','Data'))
bool(re.match('D.b','Data'))
bool(re.match('D.t','Data'))
#[.]:.이 한글자 한글자가 아닌 dot .로 찾을 때는 대괄호로 사용하게 된다. 즉, dot을 문자로 의미하게 된다.
- a[.]b: .은 문자로 인식해서 찾는다. 
bool(re.match('D[.]','D.ata'))
# *: 앞의 패턴이 0번, 1번, 몇번이상 나올지 상관없다.
a*b: aaaaab, aab
bool(re.match('D*','Data'))
bool(re.match('D*a','Data'))
bool(re.match('D*a','DData'))
bool(re.match('A*','DData'))
bool(re.match('AA*','DData'))
# +: +앞에 글자가 최소 한번 이상 반복
a+b : +앞에 글자가 최소 한번 이상 반복
bool(re.match('c+','ccat'))
bool(re.match('c+','cat'))
bool(re.match('c+','at'))
bool(re.match('c*','at'))  #+와 *비교하기
#?: ?앞에 글자가 0번, 1번 반복되는 경우 (*, +, ?를 꼭 같이 고려하기)
a?b: ?앞에 글자가 0번, 1번 반복되는 경우  
bool(re.match('c?','ccat')) #cc가 두번 나온경우이지만 두번째 c도 있기 때문에 true로 반환
bool(re.match('c?','cat'))
bool(re.match('c?','at'))
bool(re.match('c?a','ccat')) #cc가 두번 나온경우
bool(re.match('c?a','cat')) 
bool(re.match('c?a','at'))
#a{2}b: a가 2번 반복 aab
bool(re.match('c{2}a', 'ccat'))
bool(re.match('c{2}a', 'cat'))
bool(re.match('c{2}a', 'cccat'))
#a{2,3}b: a가 2번 또는 3번 반복 aab, aaab
bool(re.match('c{2,3}a', 'ccat'))
bool(re.match('c{2,3}a', 'cat'))
bool(re.match('c{2,3}a', 'cccat'))
bool(re.match('c{2,3}a', 'ccccat'))
#a|b: a또는 b
bool(re.match('c|a', 'ccat'))
bool(re.match('c|a', 'cat'))
bool(re.match('c|a', 'aat')) 
bool(re.match('c|a', 'bat')) 
#[a-zA-Z]: 알파벳 모두
# [0-9]: 숫자 모두
# \d: 숫자 모두 [0-9]
# \D: 숫자가 아닌 것과 매치, [^0-9]
# \s: 공백문자와 매치
# \S: 공백문자가 아닌 것과 마치 
# \w: 문자, 숫자와 매치, [a-zA-Z0-9]
# \W: 문자, 숫자가 아닌 문자, [^a-zA-Z0-9]


source = "Data Science"
m = re.match('Science', source, re.I)
if  m:
    print("패턴이 일치한다.")
    print(m.group())
    print(m.start())
    print(m.end())
    print(m.span())
else:
    print("패턴이 불일치한다.") 
    
    
source = "Data Science"
m = re.match('\w* Science', source, re.I)
if  m:
    print("패턴이 일치한다.")
    print(m.group())
    print(m.start())
    print(m.end())
    print(m.span())
else:
    print("패턴이 불일치한다.") 
# .*: .은 임의의 문자 -> .가 여러개일경우
source = "Data Science"
m = re.match('.*Science', source, re.I)
if  m:
    print("패턴이 일치한다.")
    print(m.group())
    print(m.start())
    print(m.end())
    print(m.span())
else:
    print("패턴이 불일치한다.") 
# .+     
source = "Data Science"
m = re.match('.+Science', source, re.I)
if  m:
    print("패턴이 일치한다.")
    print(m.group())
    print(m.start())
    print(m.end())
    print(m.span())
else:
    print("패턴이 불일치한다.") 
# .? 
source = "Data Science"
m = re.match('.?Science', source, re.I)
if  m:
    print("패턴이 일치한다.")
    print(m.group())
    print(m.start())
    print(m.end())
    print(m.span())
else:
    print("패턴이 불일치한다.") 

■ re.search
- search는 전체를 대상으로 검색
- boolean형식으로 값을 return함 
(match는 앞의 패턴을 찾는 것이지만 search는 상관없이 전체를 대상으로 검색한다.)
#
bool(re.search('Science', source, re.I))

#
m = re.search('Science', source, re.I)
if  m:
    print("패턴이 일치한다.")
    print(m.group())
    print(m.start())
    print(m.end())
    print(m.span())
else:
    print("패턴이 불일치한다.") 
    

■ re.findall
- findall은 정규식에 일치하는 문자열을 리스트로 반환한다.

source = "Data Science"
# a라는 글자를 source에 있으면 찾기
re.findall('a', source)
# A라는 글자를 source에 있으면 찾기
re.findall('A', source)
# a라는 글자를 대소문자를 가리지 않고 source에 있으면 찾기
re.findall('A', source, re.I)

#a와 a다음 뒤에 글자 찾기
re.findall('a.', source)
#a와 a앞의 글자 찾기
re.findall('.a', source)
#0또는 1
re.findall('a.?', source)
#1이상 
re.findall('a.+', source)
#0이상
re.findall('a.*', source)
# 숫자만 찾아내기
re.findall('[0-9]', '오늘은 2018년 10월 5일 입니다.')
re.findall('\d', '오늘은 2018년 10월 5일 입니다.')
re.findall('[0-9]+', '오늘은 2018년 10월 5일 입니다.')
re.findall('\d+', '오늘은 2018년 10월 5일 입니다.')
# 문자만 찾아내기
re.findall('\D+', '오늘은 2018년 10월 5일 입니다.')
re.findall('[^0-9]+', '오늘은 2018년 10월 5일 입니다.')
re.findall('[a-zA-Z]+', '오늘은 2018년 10월 5일 입니다.') # 알파벳 문자이기 때문에 반환하는 것이 없음
re.findall('[가-힣]+', '오늘은 2018년 10월 5일 입니다.') #한글을 찾기 위해서는 [가-힇]를 사용하여 찾기

# =============================================================================
# 오후수업
# =============================================================================

source = "Data Science"

#replace: old -> new로 바꾸기: 미리보기이기 때문에 변수에 넣어주기
source = source.replace('Science', 'Scientist')

■ re.sub: old -> new로 바꾸기: 미리보기이기 때문에 변수에 넣어주기(적용)
- 메타문자들을 쓸 경우는 re.sub을 사용해서 바꿔주는 것이 용이 
- sub: 일치하는 패턴 대체하기 함수
source = re.sub('Scientist', 'Science', source )

■ re.split: 입력된 패턴을 구분자로 분리
 # : 콜론을 기준으로 split하겠다는 의미
re.split('[:]','python:progarmming')    
re.split('[\:]','python:programming')    
re.split('[,]','python,programming')    
#분리시킬 구분자를 나열하면 됨
re.split('[,:]','python,programming:R')   
re.split('[\,\:]','python,programming:R')   
#공백문자를 구분으로 분리하기
re.split('[ ]','python programming R')   
re.split('[\s]','python programming R')  
#,를 기준으로, 공백문자를 기준으로 분리하기
re.split('[,\s]','python,programming R')  
# \를 기준으로 구분하기
re.split('[\\\]','python\programming R') 


#주민등록번호가 있을 때 뒷부분을 *로 바꾸기
010101-1234567 -> 010101-******
#group: 교체시 그룹을 만들어 기존의 일부 데이터를 유지하며, 새로운 데이터에 적용하기
    #( ):를 통해 그룹 만들기 e.g. (\d{6})
    #\g<1>: 첫번째 그룹을 의미

re.sub('(\d{6})[-]\d{7}','\g<1>-*******','010101-1234567')

■ re.compile
- 정규식 표현식을 미리 compile한 것을 사용하기
p = re.compile(r"(\w+)\s+((\d+)[-]\d+[-]\d+)")
            (\w+): 첫번째 그룹 
            ((\d+)[-]\d+[-]\d+): 두번째 그룹
            (\d+): 세번째 그룹
            (\w+) 문자, 숫자
            \s+공백이 하나, 두개
p.sub("\g<1> \g<2>", "James 010-1234-1234")

# group의 순서가 바뀜 (이것이 없으면 위치를 바꾸고자 할때, split를 하고 변수에 넣어주고 인덱스를 통해 바꿔주는 작업을 해야한다.)
p.sub("\g<2> \g<1>", "James 010-1234-1234")

m = p.search("James 010-1234-1234")

m.group(0) #전체
m.group(1) #이름
m.group(2) #전화번호

# group의 이름을 임의로 만들 수 있음
p = re.compile(r"(\w+)\s+((\d+)[-]\d+[-]\d+)")
# (?P<name>\w+): 그룹 1, name이라는 그룹
# (?P<phone>(\d+)[-]\d+[-]\d+): 그룹2, phone이라는 그룹
p = re.compile(r"(?P<name>\w+)\s+(?P<phone>(\d+)[-]\d+[-]\d+)")
m = p.search("james 010-1234-1234")
m.group("name")
m.group("phone")

#
txt = "of the people, by then people, for the people"
re.findall('people', txt)
re.findall('of|by|for', txt)
re.findall('^of',txt) # ^은 시작의 의미  cf. [^0-9] :^은 not의 의미
re.findall('people$', txt) #$은 끝의 의미

#the 이전에 나오는 for를 찾는다. (the 문자 이전에 for가 있으면 보여주고 없으면 보여주지 않는다.)
re.findall('for (?=the)', txt)
#the 다음에 나오는 people을 찾는다. (the 문자 다음에 people이 있으면 보여주고 없으면 보여주지 않는다.)
re.findall('(?<=the) people', txt)


p = re.compile(r"(\w+)\s+((\d+)[-]\d+[-]\d+)")
p = re.compile(r"(\w+)\s+(\d+[-]\d+[-]\d+)")


p = re.compile(r"(\w+)\s+((\d+)[-]\d+[-]\d+)")
            (\w+): 첫번째 그룹 
            (\d+): 두번째 그룹
            (\w+) 문자, 숫자
            \s+공백이 하나, 두개
p.sub("\g<1> \g<2>", "James 010-1234-1234")

# =============================================================================
# group의 의미를 알기 위해 ()를 다시 설정하여 혼자 공부해 봄
# =============================================================================
# group의 순서가 바뀜 (이것이 없으면 위치를 바꾸고자 할때, split를 하고 변수에 넣어주고 인덱스를 통해 바꿔주는 작업을 해야한다.)
p.sub("\g<2> \g<1>", "James 010-1234-1234")

m = p.search("James 010-1234-1234")

m.group(0) #전체
m.group(1) #이름
m.group(2) #전화번호

p = re.compile(r"(?P<name>\w+)\s+(?P<phone>\d+[-]\d+[-]\d+)")
m = p.search("james 010-1234-1234")
m.group("name")
m.group("phone")


# =============================================================================
#  다시 수업으로 돌아가서
# =============================================================================

print("우리 행복하게 살자")
print('우리 "행복"하게 살자')
#\사용법: 문자로 인식하도록 하기 
print("우리 \"행복\"하게 살자")
#\: :만 사용하면 가끔 인식이 안될 수 있어서 \:를 사용하기도 함

정규식 표현식으로 나타내기 
txt = "Let's live happily"
p = re.compile('\w+')
p.findall(txt) #['Let', 's', 'live', 'happily']

p = re.compile('\w')
p.findall(txt)  #['L', 'e', 't', 's', 'l', 'i', 'v', 'e', 'h', 'a', 'p', 'p', 'i', 'l', 'y']

#'를 문자로 인식하기 때문에 앞에  \를 붙여 \'로 쓰도록 한다.
# [\']뒤에는 문자 하나만 나오면 되기 때문에 .을 사용하면 됨다.
p = re.compile('\w+[\'].')
p.findall(txt)  #["Let's"]
#굳이 \를 안해도 되는 경우는 ""를 사용하여 literal 문자로 나타내면 된다.
p = re.compile("\w+['].")
p.findall(txt)

p = re.compile('Physical | Computer') #둘 중에 하나 또는 둘 다 data를 바꿈
p.sub('Data', 'Physical Science and Computer Science') #replace함 
#p.subn: replace하면서 바뀐 정보에 대한 갯수를 return해줌 
p.subn('Data', 'Physical Science and Computer Science')


#group 다시 정확하게 공부
(정규식에서 tuple모양이 여기서는 group을 의미하다)
p = re.compile(r"(\w+)\s+((\d+)[-](\d+)[-](\d+))")
            r: literal 문자 안에 "를 사용할 경우 \을 또 해줘야 하기 때문에 계속 \를 사용하지 않고 사용하게 해줘도 된다는 의미로 쓰임 
            (\w+): 첫번째 그룹 
            (\d+): 두번째 그룹
            (\w+) 문자, 숫자
            \s+공백이 하나, 두개
p.sub("\g<1> \g<2>", "James 010-1234-1234")

# group의 순서가 바뀜 (이것이 없으면 위치를 바꾸고자 할때, split를 하고 변수에 넣어주고 인덱스를 통해 바꿔주는 작업을 해야한다.)
p.sub("\g<2> \g<1>", "James 010-1234-1234")

m = p.search("James 010-1234-1234")

m.group(0) #전체 (r"(\w+)\s+(\d+[-]\d+[-]\d+)")
m.group(1) #이름 (\w+)
m.group(2) #전화번호 (\d+[-]\d+[-]\d+)
m.group(3) #첫번째(\d+)
m.group(4) #두번째(\d+)
m.group(5) #세번째(\d+)

