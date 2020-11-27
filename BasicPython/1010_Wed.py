# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 09:45:17 2018

@author: stu
"""

cf. 변수함수가 모여있는 것이 class라고 할 수 있다.
class Person:
    hobbys = []                 #habbys:클래스 변수: 인스턴스간의 값이 공유
    def add_hobby(self, hobby):  #hobby:매개변수: add_hobby에서만 사용하는 변수
        self.hobbys.append(hobby) #self.hobbys 클래스 변수이기때문에 self이후에도 사용
        
#p1 인스턴스를 생성
p1 = Person()
#'노래부르기' hobby에 추가
p1.add_hobby("노래부르기")
print(p1.hobbys)

#p2 인스턴스 생성 
p2 = Person()
p2.add_hobby("글쓰기")
print(p2.hobbys)

#class 변수는 인스턴스 간에 공유가 되기 때문에, 클래스 변수를 잘 넣어야 한다. 
#위의 경우에는 클래스 변수로 넣으면 p1, p2에 계속 클래스 변수가 공유되어 쌓이기 때문에 hobby를 인스턴스 변수로 만들어야 한다. 

#클래스 변수 호출하는 방법 (#클래스 변수는 p1, p2나 상관없기 때문에 )
print(Person.hobbys)


#hobbys를 인스턴스 변수로 넣기 
class Person:
   def add_hobby(self, hobby): 
        self.hobbys = []   #hobbys는 인스턴스 변수 -> 인스턴스에서만 사용되는 변수로 사용됨
        self.hobbys.append(hobby)

p1 = Person()
p1.add_hobby("노래부르기") 
print(p1.hobbys)

p2 = Person()
p2.add_hobby("글쓰기")
print(p2.hobbys)


#? 다시 확인하기
#1) 클래스 변수인지, 인스턴스 변수인지
#2) add_hobby(self.hobby)/ self를 인스턴스 안에서만 사용하겠다 하더라도 class 변수로 사용될 경우 인스턴스에서만 사용되지 않는다.
class Person:
    def add_hobby(self, hobby): 
        self.hobbys = []   #list 변수이기때문에 출력하면 안됨 
        self.hobbys.append(hobby)
    def show(self):
        print("내 취미는 "+self.hobbys)

p1 = Person()
p1.add_hobby("노래부르기")
print(p1.hobbys)
p1.show() #Error: list변수이기 때문에 

p2 = Person()
p2.add_hobby("글쓰기")
print(p2.hobbys)


#list변수로 고치기 
class Person:
    def add_hobby(self, hobby): 
        self.hobbys = ""   
        self.hobbys = hobby
    def show(self):
        print("내 취미는 "+self.hobbys)

p1 = Person()
p1.add_hobby("노래부르기")
p1.show()

#인스턴스를 사용할 때 만들 때 값을 넣을지, 메소드를 사용할 때 값을 넣을지 고민해야 한다. 
#지금 여기서는 인스턴스를 만들 때 값을 넣을 수 없다.  --> __init__(초기생성자)가 필요하다.
class Person:
    def add_hobby(self, hobby): 
        self.hobbys = hobby
    def show(self):
        print("내 취미는 "+self.hobbys)

#초기 생성자 사용
#초기 생성자를 만들 때, 인스턴스화를 할 때 name을 꼭 입력값으로 받아야 함.
class Person:
    def __init__(self, name):
        self.name = name
        self.hobbys =[]
    def add_hobby(self, hobby): 
        self.hobbys.append(hobby)

#인스턴스는 이름만 넣고, 초기화 됨 
#이름을 넣고, self.name = name 리스트 변수 생성
#add.hobby 메소드를 사용할 때 값을 생성 
p1 = Person('홍길동')
p1.add_hobby('음반수집')
p1.add_hobby('노래부르기')
print(p1.hobbys)

p2 = Person('박찬호')
p2.add_hobby('글쓰기')
print(p2.hobbys)


# =============================================================================
# [문제_189]초기 생성자에는 이름, 주소, 급여를 입력값으로 받고 아래와 같이 출력되는 클래스를 생성하세요. 
인스턴스 생성될때 마다 건수를 출력해주세요.
# =============================================================================
사원수 : 1
이름 : 홍길동 , 주소 : 덴마크,  급여 : 1000

사원수 : 2
이름 : 홍아들 , 주소 : 노르웨이,  급여 : 2000

#sal을 숫자로 받음 
class Emp:
    cn = 0
    def __init__(self, name, addr, sal):
        self.name = name
        self.addr = addr
        self.sal = sal
        Emp.cn += 1
        print('사원수 : %d' %Emp.cn)
        print('이름 :'+self.name+', 주소:'+self.addr+', 급여: %d'%self.sal)

p1 = Emp('홍길동', '덴마크', 1000)
p2 = Emp('홍아들', '노르웨이', 2000)

#sal을 함수에서 str으로 변환해서 입력하기; 숫자로 입력가능 
class Emp:
    cn = 0
    def __init__(self, name, addr, sal):
        self.name = name
        self.addr = addr
        self.sal = sal
        Emp.cn += 1
        print('사원수 : %d' %Emp.cn)
        print('이름 :'+self.name+', 주소:'+self.addr+', 급여: '+str(self.sal))

p1 = Emp('홍길동', '덴마크', 1000)
p2 = Emp('홍아들', '노르웨이', 2000)

#sal을 string으로 받음
class Emp:
    cn = 0
    def __init__(self, name, addr, sal):
        self.name = name
        self.addr = addr
        self.sal = sal
        Emp.cn += 1
        print('사원수 : %d' %Emp.cn)
        print('이름 :'+self.name+', 주소:'+self.addr+', 급여: '+self.sal)

p1 = Emp('홍길동', '덴마크', '1000')
p2 = Emp('홍아들', '노르웨이', '2000')

#함수 추가했을 때 output 
class Emp:
    cn = 0
    def __init__(self, name, addr, sal):
        self.name = name
        self.addr = addr
        self.sal = sal
        Emp.cn += 1
    def add_emp(self):
        print('사원수 : %d' %Emp.cn)
        print('이름 :'+self.name+', 주소:'+self.addr+', 급여: '+self.sal)

p1 = Emp('홍길동', '덴마크', '1000')
p1.add_emp()
p2 = Emp('홍아들', '노르웨이', '2000')
p2.add_emp()


#쌤답
class Employee:
   
   empCn = 0    #class변수

   def __init__(self, name, addr, salary): #형식 매개변수임 (NOT 인스턴스 변수) #__init__안에 있는 것들은 인스턴스를 생성할 때 초기화 된다.
      self.name = name   #인스턴스변수
      self.addr = addr   #인스턴스변수
      self.salary = salary  #인스턴스변수
      Employee.empCn += 1   #class이름.변수이름이 코드해석에 편리함
   
   def printCount(self):                   # 메소드 안에는 꼭 self를 포함하도록 한다.
     print("사원수 : %d" %Employee.empCn)   #class 변수값 출력

   def printEmployee(self):                # 메소드 안에는 꼭 self를 포함하도록 한다.
      print( "이름 : {} , 주소 : {},  급여 : {}".format(self.name, self.addr, self.salary)) #인스턴스 변수는 self.을 사용하도록 한다.


emp1 = Employee("홍길동","덴마크", 1000)
emp1.printCount()
emp1.printEmployee()


emp2 = Employee("홍아들","노르웨이", 2000)
emp2.printCount()
emp2.printEmployee()


# =============================================================================
# [문제 190]

id_number1 = "010101-3234567"
id_number2 = "990202-2123456"

2001 01 01 남성
1999 02 02 여성

# =============================================================================

#방법 
#1)인덱스 기준으로
#2) -split하여 

#답1
# -를 기준으로 split하기 
def id_process(id):
    first, second = id.split("-")  #split하여 first, second로 받을 수 있음
    gender = second[0]
    
    if gender == "1" or gender =="2":
        year = "19"+first[0:2]   #first[:2]까지 slicing해도 됨   
    else:
        year = "20"+first[0:2]
    
    if gender == "2" or gender == "4":
        gender = "여성"
    else:
        gender = "남성"
    
    month = first[2:4]
    day = first[4:6]
    
    return year, month, day, gender

id_process(id_number1)
id_process(id_number2)    
     
#답2
def id(i):     
    if i[7]=="1": 
        print('19'+i[0:2]+' '+i[2:4]+' '+i[4:6] + '남성')
    elif i[7]=="2":
        print('19'+i[0:2]+' '+i[2:4]+' '+i[4:6], '여성')
    elif i[7]=="3":
        print('20'+i[0:2]+' '+i[2:4]+' '+i[4:6], '남성')
    elif i[7]=="4":
        print('20'+i[0:2]+' '+i[2:4]+' '+i[4:6], '여성')       


id_number1 = "010101-3234567"    
id(id_number1)
id(id_number2)


# =============================================================================
# 다시 수업으로
# =============================================================================
class Employee:
    empCount = 0        #class 변수
    raise_ratio = 1.1   #rasie_ratio는 클래스변수인가? 인스턴스 변수인가? -> 인스턴스로 만들어짐!
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1
        
    def showCount(self):
        print("전체 종업원의 수는 {}".format(Employee.empCount))
    
    def showEmp(self):
        print("이름 {}, 급여{}".format(self.name, self.salary))
    
    def raise_salary(self):
        print(self.raise_ratio)
        self.salary = int(self.salary * self.raise_ratio)

    
emp1 = Employee("홍길동", 1000)
emp1.showCount()
emp1.showEmp()
emp1.raise_salary()
emp1.showEmp()

emp1 = Employee("홍길동", 1000)
emp1.showCount()
emp1.showEmp()
emp1.raise_ratio = 1.2
emp1.raise_salary()
emp1.showEmp()

emp2 = Employee("박찬호", 2000)
emp2.showCount()
emp2.showEmp()
emp2.raise_salary()
emp2.showEmp()


#self.raise_ratio를 -> Employee.raise_ratio로 바꾸기 
class Employee:
    empCount = 0        
    raise_ratio = 1.1   
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1
        
    def showCount(self):
        print("전체 종업원의 수는 {}".format(Employee.empCount))
    
    def showEmp(self):
        print("이름 {}, 급여{}".format(self.name, self.salary))
    
    def raise_salary(self):
        print(Employee.raise_ratio)
        self.salary = int(self.salary * Employee.raise_ratio)

emp1 = Employee("홍길동", 1000)
emp1.showCount()
emp1.raise_salary()
emp1.showEmp()
Employee.raise_ratio = 1.2
emp1.raise_salary()
emp1.showEmp()

emp2 = Employee("박찬호", 2000)
emp2.showCount()
emp2.showEmp()
emp2.raise_salary()
emp2.showEmp()

# =============================================================================
# 오후 수업
# =============================================================================
class Person:
    hobbys = [] #클래스 변수처럼 선언 
    def __init__(self, name):
        self.name = name
    def add_hobby(self, hobby):
        self.hobbys.append(hobby)  #hobbys에 hobby를 추가함/self가 있어도 클래스 변수가 될 수 있다.
    def show_info(self):
        print(self.name, self.hobbys)

p1 = Person("홍길동")
p1.add_hobby("음반수집")
p1.show_info()

p2 = Person("박찬호")
p2.show_info()   
p2.add_hobby("글쓰기")
p2.show_info()

#hobbys =[]를 __init__에 넣으면 클래스 변수가 아니라 인스턴스 변수가 될 수 있다.
class Person:
    #hobbys = [] #클래스 변수처럼 선언 
    def __init__(self, name):
        self.name = name
        self.hobbys = [] 
    def add_hobby(self, hobby):
        self.hobbys.append(hobby)  #hobbys에 hobby를 추가함/self가 있어도 클래스 변수가 될 수 있다.
    def show_info(self):
        print(self.name, self.hobbys)

p1 = Person("홍길동")
p1.add_hobby("음반수집")
p1.show_info()

p2 = Person("박찬호")
p2.show_info()   
p2.add_hobby("글쓰기")
p2.show_info()


#raise_ratio 중심으로 살펴보기 
class Employee:
    raise_ratio = 1.1  #클래스변수처럼 선언되어있더라도 이 변수는 인스턴스 변수로 사용될 수 있다. 
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def emp_info(self):                 #인스턴스 메소드
        print("이름 : ",self.name,"급여 : ",self.salary)
    
    def rasie_salary(self):             #인스턴스 메소드
        self.salary = int(self.salary*self.raise_ratio)

emp1 = Employee("홍길동", 1000)
emp1.emp_info()
print(emp1.raise_ratio) 
emp1.raise_ratio = 1.2 #인스턴스 변수 -> 자기영역에서만 1.2로 사용됨
print(emp1.raise_ratio)  #인스턴스 변수
emp1.rasie_salary()
emp1.emp_info()

emp2 = Employee("박찬호", 2000)
emp2.emp_info()
print(emp2.raise_ratio)  #인스턴스변수
emp2.rasie_salary()      #1.1인상
emp2.emp_info()


#클래스 메소드: 모든 인스턴스가 그 메소드를 적용해서 사용하는 것
# raise_ratio를 변경시 다른 인스턴스에서도 계속 적용되도록 만들기
class Employee:
    raise_ratio = 1.1  
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def emp_info(self):                 
        print("이름 : ",self.name,"급여 : ",self.salary)
    
    def rasie_salary(self):             
        self.salary = int(self.salary*self.raise_ratio)
    @classmethod    #@classmethod: 바로 밑에는 클래스 메소드라는 지시자        
    def change_raise_ratio(cls, ratio): #클래스 메소드에서는 cls.매개변수를 만들어야 함
        cls.raise_ratio = ratio #cls.매개변수를 만들어야 함 / #classmethod를 이용하여 위의 raise_ratio=1.1의 변경작업을 함
        print("인상률", round((ratio-1)*100), "%")

#@classmethod: 바로 밑에는 클래스 메소드라는 지시자        
#cls: 클래스 메소드를 의미하는 매개변수(self대신)
#이용: 온라인 게임시 내가 죽었을 때 상대방도 내가 죽은 것으로 나와야하기 때문에 클래스 메소드로 적용하여야 한다.        
emp1 = Employee("홍길동", 1000)     #1
emp1.emp_info()                     #2
print(emp1.raise_ratio)             #3
emp1.change_raise_ratio(1.2)        #4      #내 인스턴스에서 rasie_ratio를 1.2로 변경함 (원래 인스턴스 메소드 변수였으니, cls.를 사용하면서 class 변수로 적용된다.)
print(emp1.raise_ratio)             #5
emp1.rasie_salary()
emp1.emp_info()
print(emp1.raise_ratio)             #11
Employee.change_raise_ratio(1.6)    #12
print(emp1.raise_ratio)             #13

emp2 = Employee("박찬호", 2000)     #6
emp2.emp_info()                     #7
print(emp2.raise_ratio)             #8  #홍길동에서 변경된 raise_ratio 1.2로 변경되어서 나옴 
emp2.rasie_salary()      
emp2.emp_info()

emp2.change_raise_ratio(1.5)        #9
print(emp2.raise_ratio)             #10 #나만 적용되는 것이 아니라 다른 인스턴스 안에서도 적용된다.
print(emp2.raise_ratio)             #14


인스턴스 메소드: 인스턴스를 통해 호출되고 인수값은 인스턴스 자신을 자동으로 전달하는 self를사용해야 한다. 

클래스 메소드: 클래스를 통해 호출되고 @classmethod 데코레이터로 정의하고 클래스 자신을 자동으로 전달하는 인자 cls사용 

스택틱 메소드: 인자를 받지 않는다. (인수값을 받지 않는다.), 함수를 그냥 모아놓을 때 사용하는 것이 좋다. 
(예를들어 math라는 class를 만들고 여러 수학함수를 만들어 놓을 때 그때마다 @staticmethod 를 사용하면 인자값을 넣지 않아도 함수로써 이용이 가능하다.)


class test:
    num = 0
    @staticmethod       #호출하면서 값을 넣는다. /굳이 인스턴스화를 안해도 된다. 
    def add(x,y):
        return x+y
    
t = test
#인스턴스를 통해서 호출
t.add(1,1)
# 클래스를 통해서 호출
test.add(10,20)


class test:
    num = 0            #num=0과 num=x+y의 num은 서로 다른 num이다. 
    @staticmethod    
    def add(x,y):
        num = x+y
        return num
    
t.add(1,2)
test.add(10,21)


# count_viva = classmethod(count_viva)는 @classmethod(데코레이터 classmethod)와 같다. 
##classmethod
#방법1) classmethod로 재적용한다. count_viva = classmethod(count_viva) 
#방법2) 데코레이터 classmethod를 사용한다. 
class Viva:
    cnt = 0                     #클래스 변수
    def __init__(self, name):
        self.name = name #self.name 인스턴스 변수
        print("{}님이 게임방에 들어왔습니다.".format(self.name))
        Viva.cnt += 1
    
    #@classmethod    
    def count_viva(cls):                #인스턴스 상관없이 적용되고 있음
        print("현재{}명이 남았습니다.".format(cls.cnt))  #cls.cnt는 class 변수 / 클래스이름.변수이름(Viva.cnt)라고 해도 된다.
    count_viva = classmethod(count_viva) #classmethod로 재적용 
    
    def __del__(self):  #__del__생성자: 소멸자  # __init__밑에 적용해도 된다. #소멸자는 del하면 돌아가게 된다.
        print("{}님이 게임방에서 나갔습니다.".format(self.name))
        Viva.cnt -=1
        
        
man1 = Viva("홍길동")   #1
man1.count_viva()       #2 #Error남 -> 확인해서 고쳐야함 ㅠㅠ
del man1                #5 #del 인스턴스이름 
man1.count_viva()       #7

man2 = Viva("박찬호")    #3
man2.count_viva()       #4
del man2                #6


class Viva:
    cnt = 0                     #클래스 변수
    def __init__(self, name):
        self.name = name #self.name 인스턴스 변수
        print("{}님이 게임방에 들어왔습니다.".format(self.name))
        Viva.cnt += 1
    
    @classmethod    
    def count_viva(cls):                #인스턴스 상관없이 적용되고 있음
        print("현재{}명이 남았습니다.".format(cls.cnt))  #cls.cnt는 class 변수 / 클래스이름.변수이름(Viva.cnt)라고 해도 된다.
    
    def __del__(self):  #__del__생성자: 소멸자  # __init__밑에 적용해도 된다. #소멸자는 del하면 돌아가게 된다.
        print("{}님이 게임방에서 나갔습니다.".format(self.name))
        Viva.cnt -=1

 
