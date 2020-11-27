# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 09:47:37 2018

@author: stu
"""

[참조 : https://docs.python.org/ko/3/library/exceptions.html]

# =============================================================================
# [문제193] 양의 정수값만 입력 받아서 나누기를 수행하는 positive_divide 함수를 생성하세요.
# =============================================================================

#답1
def positive_divide():            
    try:    
        numerator = int(input("분자 숫자를 입력하세요 :"))
        denominator = int(input("분모 숫자를 입력하세요 :"))
 
        if(denominator < 0):  
            raise ValueError
        return  numerator / denominator
    except ValueError:
        print('오류  - 음수로 나눌수 없습니다.', denominator)
    except ZeroDivisionError as error:
        print('오류 -  0으로 나눌수 없습니다.',error)
            
positive_divide()

#답2 
def positive_divide(): 
    
    numerator = int(input("분자 숫자를 입력하세요 :"))
    denominator = int(input("분모 숫자를 입력하세요 :"))
    
    try:
        if denominator > 0:      
            result = numerator/denominator
            return result
        
        elif denominator < 0:
            raise Exception("오류 - 음수로 나눌 수 없습니다. -2")
        
        elif denominator == 0:
            raise Exception("오류 - 0으로 나눌 수 없습니다. division by zero")
    except Exception as error:
        print(error)

#쌤답 
def  positive_divide():
    try:
      
        x = int(input(' 분자 숫자를 입력하세요 : '))
        y = int(input(' 분모 숫자를 입력하세요 : '))
        
        if(y < 0):  
            raise ValueError
        return  x / y
    except ValueError:                          #내장되어있는 error
        print('오류  - 음수로 나눌수 없습니다.', y)
    except ZeroDivisionError as error:          #내장되어있는 error
        print('오류 -  0으로 나눌수 없습니다.',error)


# 클래스를 통해서 사용자 exception처리가 가능하다 
class NegativeDivisionError(Exception):     #Excetpion을 처리하기 위한 class를 만들어 놓음  
    def __init__(self, value):
        self.value = value
        
def  positive_divide():
    try:
        # n = NegativeDivisionError             -> 인스턴스화 해서 사용한 것을 씀; 그러나 굳이 하지 않아도 되기 때문에 #처리함 
        
        x = int(input(' 분자 숫자를 입력하세요 : '))
        y = int(input(' 분모 숫자를 입력하세요 : '))
        
        if(y < 0):  
            raise NegativeDivisionError(y)
        return  x / y
    except NegativeDivisionError as error:      #class에서 만든 error값을 만들어 error값을 그대로  
        print('오류  - 음수로 나눌수 없습니다.', error)
    except ZeroDivisionError as error:
        print('오류 -  0으로 나눌수 없습니다.',error)
        
# =============================================================================
# [문제194] 한주간동안 걸음수를 요일별로 그래프를 그리세요.
#         단 막대그래프 함수를 생성해서 인수값으로 걸음수, 요일을 입력하면 그래프가 그려지도록하세요.
# =============================================================================

# class walkPlot:
#          
#     def __init__(self, step, day):
#         self.step = step
#         self.day = day
#      
#     def walk(self):
#         walk = {self.step: self.day}
#         return walk
#     
#     def plot(self):
#         plt.bar()
#         plt.
#         
#     
#    
#     def plot(self):
#          
# 
# day1 = walkPlot(3000, "월")
# day1.walk()
# 
# day2 = walkPlot(5000, "화")
#day2.walk()


#쌤답
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

def create_bar_chart(data, labels,bar):

    num_bars = len(data)

    positions = range(1, num_bars+1)
    if bar == 1:        
        plt.bar(positions, data, align='center')
        plt.xticks(positions, labels)   #기본은 1,2,3,4..로 나오지만 요일로 나오게 만들기 위해서 
        plt.xlabel('요일')  
        plt.ylabel('걸음수')
       
    else:
         plt.barh(positions, data, align='center')
         plt.yticks(positions, labels)
         plt.xlabel('걸음수')
         plt.ylabel('요일')
    

    plt.title('한주간 동안 걸음수') 
    plt.grid()
    plt.show()
    
if __name__=='__main__':
    step = [1090,2000,3000,4000,10000,50000,2000]
    labels = ['월','화','수','목','금','토','일']
    create_bar_chart(step,labels,2)

if __name__=='__main__':
    step = [1090,2000,3000,4000,10000,50000,2000]
    labels = ['월','화','수','목','금','토','일']
    create_bar_chart(step,labels,1)



# 클래스로 만들기 
import matplotlib.pylab as plt
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

class create_bar_chart:
    def __init__(self,data, labels, bar):
        self.data = data
        self.labels = labels
        self.bar = bar
        
    def create_bar_chart(self):
    
        num_bars = len(self.data)
    
        positions = range(1, num_bars+1)
        if self.bar == 1:
            plt.bar(positions, self.data, align='center')
            plt.xticks(positions, self.labels)
            plt.xlabel('요일')
            plt.ylabel('걸음수')
           
        else:
            plt.barh(positions, self.data, align='center')
            plt.yticks(positions, self.labels)
            plt.xlabel('걸음수')
            plt.ylabel('요일')
        
    
        plt.title('한주간 동안 걸음수') 
        plt.grid()
        plt.show()
    
if __name__=='__main__':
    step = [5000,6000,7500,10000,10000,20000,2000]
    labels = ['월','화','수','목','금','토','일']
    cbc = create_bar_chart(step,labels,1)
    cbc.create_bar_chart()


# =============================================================================
# 오후 수업
# =============================================================================
import collections

#Counter: 컨테이너 ['a','b','a','c','a','b'] 안에 있는 동일한 값의 자료가 몇개인지를 파악한다. (빈도수 체크)
#컨테이너라는 것은 자료형이라고 보면 된다. 
#결과 값은 dictionary형태로 key:value값응로 제공한다. 빈도수가 높은 것부터 진열된다. 
collections.Counter(['a','b','a','c','a','b'])

collections.Counter(['우리','나라','우리','대한민국','우리','행복'])

#update: 후에 추가해서 값을 출력할 수도 있다.
container = collections.Counter()
container.update('aaaabbbbbccczzzzzzz')
print(container)

#추가기능
container.update({'c':2, 'e':5}) #'c':는 sum 'e'는 추가가 됨
print(container)

for i in 'abcdefyz':
    print('%s : %d'%(i,container[i]))

#c는 dictionary형으로 만들어진다. 따라서 key와 c.items(), c.keys(), c.values()와 같은 메소드를 사용할 수 있다.
c = collections.Counter("hellow james")
print(c)
c.keys()
c.values()
c.items()

#dict_keys를 지우기
list(c.keys())
list(c.items())

# 글자하나씩 counting함 
ct = collections.Counter()
with open("c:\data\hello.txt", "r") as f: #객체는 f로 선언함
    for i in f:
        ct.update(i.rstrip().lower()) #영어는 대소문자를 구분하기 때문에, 소문자로 만들기 + 띄어쓰기 없애기

print(ct)

#상위 5위 이상 
for i, c in ct.most_common(5):
    print("%s : %d"%(i,c))
    

# =============================================================================
# 사용자 구축 사전 만들기 pip install customized_konlpy
# =============================================================================
# anaconda prompt에서 실행
pip install customized_konlpy

#
from konlpy.tag import Twitter

twitter = Twitter()

# 
txt = "텍스트 마이닝은 텍스트 형태의 데이터를 수학적 알고리즘에 기초하여 수집, 처리, 분석, 요약하는 연구기법을 통칭하는 용어이다."

#container 로 담아서 명사수 세기
collections.Counter(twitter.nouns(txt))

#사용자 구축사전  #add_dictionary는 지속되지 않기 때문에 add_dictionary()코드를 같이 가지고 돌려야 한다. 
from ckonlpy.tag import Twitter
twitter = Twitter()
twitter.add_dictionary('마이닝','Noun') 

#단어 추가한 후 container.Counter로 명사수 세기
collections.Counter(twitter.nouns(txt))


