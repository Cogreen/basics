# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 09:53:55 2018

@author: stu
"""

# =============================================================================
# 오전 수업
# =============================================================================
cf. 
package: global 변수를 편하기 사용하기 위해서 이용

module식 개발: 작은 단위로 개발해서 끼워맞는 작업


▣ class - variable, method 로 구성 
■ 구조적인 프로그램(structured language/ procedural language)
- 프로그램은 순서대로 흐르는 언어(전방참조만 가능함)
■ 객체지향 프로그램(object-oriented language)
- 필요한 프로그램을 호출해서 사용하는 언어 
- 

###############################################################################

▣ 절차(구조적) 지향 프로그램(procedural language )
    - c언어 
    - 물이 위에서 아래로 흐르는 것처럼 순차적인 순차적인 처리가 중요시 되며 프로그램 전체가 유기적으로 연결 되도록 만드는 프로그래밍 기법
    - 단점
        : 재사용할 수 없다. 
        : 확장성이 떨어진다.(overload기능을 할 수 없음)
        : 유지보수가 어렵다. 
        
#누적합 구하기
(글로벌 변수)        
adder(3)
adder(4)
결과는 7일 출력되도록 함수를 만드세요.

x=0
def adder(y):  
    global x
    x+=y
    return x

a
adder(3)
adder(4)


b
adder(5)
adder(5)

a와 b가 따로따로 adder의 누적합을 구하고자 하는데 절차지향 프로그램은 이 경우는 a,b와 상관없이 합이 누적된다. 그래서 a와 b에 대한 함수를 따로 따로 개발해야한다.
그러나 객체지향 프로그램을 이용하여 하나의 프로그램을 가지고 둘이서 따로따로 사용할 수 있는 효과를 줄 수 있음 

▣ 객체지향 프로그램(object oriented language)
    - java, c++, c#, python 
    (cf. r은 구조적 언어이며, script 언어이다.)
    - 구조적프로그래밍과 다르게 큰 문제를 작게 쪼개는 것이 아니라 먼저 작은 문제들을 해결할 수 있는 객체들을 만든 뒤 이 객체들을 조합해서 큰 문제를 해결하는 방법
    - 객체: 사물 개념 중에서 명사로 표현할 수 있는 것을 의미한다.
            사람, 건물 학생
    - 클래스: 객체를 설명해 놓은 것(객체의 설계도)
    - 인스턴스: 클래스를 메모리에 만들어서 사용하도록 하는 의미

객체 = 사람 
속성(Attribute, field) = 변수: 팔, 다리, 머리, 눈, 코 , 입, 이름, 키, 나이, 주민번호, 주소, 학번, 성적, 성격
=> 수치, 값으로 표현 
메소드(method) = 함수 : 기능의 프로그램 처리, 조작하는 것, 속성의 값을 변경하는 기능

#클래스를 표현하는 방법 
class Calculator:
    def __init__(self):
        self.result = 0
        
    def adder(self, num):
        self.result += num
        return self.result

# __init__: 초기화 시키는 method, 꼭 필수사항은 아님
# self 는 자기자신 (이 클래스를 사용하고 있는 자기 자신 )
# 초기화 시키는 작업
# class Calculator:
#    def __init__(self):
#        self.result = 0
        
# adder 에 대한 method 
#    def adder(self, num):
#       self.result += num
#        return self.result
        

#하나의 프로그램을 다르게 사용하고 있음 
#class를 만들었으니 인스턴스instance를 해야함 
<<홍길동>>        
cal1 = Calculator() # 인스턴스 
print(cal1.adder(3))
print(cal1.adder(4))
print(cal1.adder(2))

<<박찬호>>
cal2 = Calculator() # 인스턴스 
print(cal2.adder(5))
print(cal2.adder(5))
print(cal2.adder(1))

class myClass:
    pass   #함수, 클래스에서 아무 작업하지 않을 때 사용 

#pass : 아무것도 수행하지 않겠다.; 함수, 클래스에서 아무 작업하지 않을 때 사용 
    
class Person:
    name = '홍길동'
    age = 20
    
    def myPrint(self):
         print("이름은 {}".format(self.name))
         print("나이는 {}".format(self.age))
#   name = '홍길동'
    age = 20
    위의 두개는 global 변수 처럼 어떤 인스턴스에서도 공통적으로 사용됨

#self: 이 함수를 쓰고 있는 자기 자신을 의미  ()
        홍길동이 이것을 쓰면 홍길동이 쓰고 있다는 것을 의미
# cf. java, c에서는 self를 this로 사용함

# 클래스를 기반으로 인스턴스 생성
p1 = Person()

# 인스턴스화한 method를 사용해야 함 
p2 = Person()
p2.myName()
p2.myAge()

p3=Person()
p3.name = '박찬호'
p3.age = 30
p3.myName()
p3.myAge()
#내 인스턴스 안에서는 속성을 추가할 수 있다. 
p3.job = '프로그래머'
print('직업은',p3,job)

#내 인스턴스 안에서 만큼은 변경 작업이 가능하다. 
#class 장점: 재사용이 가능함

#
class Person:
    def __init__(self):
        self.info=""
    def showinfo(self, name, age):
        self.info += "이름 :" +name+","+" 나이:"+str(age)+"\n"

# self.info대입연산자 + self. 이름 + self.age  그리고 \n 밑으로 한 줄 내리기로 append하게 생성한다.(누적함) 
# str(age)를 쓰지 않으면 오류가 남: 왜냐하면 숫자는 문자랑 같이 사용할 수 없기 때문에 

# init 무조건 인스턴스할 때 생성하고 초기화시킴, 이 클래스에서만 사용할수 있는 변수를 만듦
    name = '홍길동'
    age = 20
와 달리 init은 local변수처럼 적용된다. init에서 생성한 변수는 꼭 self를 붙여야 한다. 

#Person()을 수행시키자 마자 init이 돌아가고 self.info=""가 생성된다. self.info는 null값으로 값을 선언함 
man = Person()
man.showinfo("최유진", 26)
man.showinfo("구동매", 25)
print(man.info)

#woman이라는 인스턴스가 만들어짐, 새로운 info가 선언됨   
woman = Person()
woman.showinfo("고애신", 20)
woman.showinfo("이양화", 21)
woman.showinfo("김현정", 23)
print(woman.info)

name = "제임스"
class myName:
    def mySet(self, setname):
        self.name = setname
    def myPrint(self):
        print(name)
        print(self.name)

p1 = myName()     
p1.mySet("홍길동")        
p1.myPrint()
#self.name: 내 클래스 안에 있는 변수를 쓰겠다는 의미
#name: 클래스 밖에 잇는 변수를 쓰겠다는 의미

class Employee:
    empCount = 0
    
    def __init__(self, name, salary):       # __init__(self) : __init__에 self는 꼭 써야 한다!
        self.name = name                    # 일반적으로 init에 지정해놓은 변수를 self.이름에 같이 사용한다. (self.n = name이라고 해도 되지만)
        self.salary = salary
        Employee.empCount += 1
    def displayCount(self):                 #displayCount(self): self를 꼭 써줘야 한다. -문법임
        print('전체 종업원수는 %d'%Employee.empCount)
    def displayEmployee(self):              #displayEmployee(self): self를 꼭 써줘야 한다. 
        print("이름: ", self.name, ", 급여: ", self.salary)
    
#(기존에는 변수에 호출한 다음 넣었으나)    
# init의 생성자에 변수가 나열되어있으면 class를 인스턴스화 할때 값은 꼭 넣어야 함
emp1 = Employee("홍길동", 1000)
emp1.displayCount()
emp1.displayEmployee()

#Employee.empCount(클래스이름.변수이름 ) :진정한 글로벌 변수가 됨, init은 초기화 되지만 글로벌 변수는 초기화 되지 않는다. 어떤 인스턴스간에 공통으로 사용되는 변수가 됨 
emp2 = Employee("제임스", 2000)
emp2.displayCount()
emp2.displayEmployee()

emp3 = Employee("박찬호", 3000)
emp3.displayCount()
emp3.displayEmployee()


#비교후기. employee.empCount -> self.empCount 로 바꿨을 경우
class Employee:
    empCount = 0
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.empCount += 1
    def displayCount(self):
        print('전체 종업원수는 %d'%self.empCount)
    def displayEmployee(self):
        print("이름:", self.name, ", 급여: ", self.salary)
 
# self.empCount는 empCount가 자기자신의 인스턴스만이 되게 된다.        
# emp1.displayCount()가 계속 1이 됨 
emp1 = Employee("홍길동", 1000)
emp1.displayCount()
emp1.displayEmployee()

emp2 = Employee("제임스", 2000)
emp2.displayCount()
emp2.displayEmployee()

emp3 = Employee("박찬호", 3000)
emp3.displayCount()
emp3.displayEmployee()


# =============================================================================
# 오후수업
# =============================================================================

# 클래스 만들고 -> 인스턴스 생성 -> 클래스 변수를 만듦 (Employee.name);class에서는 맨처음에 변수가 만들지 않았지만 이로 인해 변수가 생성됨 -> 
class Employee:
    pass

#똑같은 class를 사용하지만 인스턴스는 다르게 생성함을 보여준다. id가 다르게 출력되기 때문에 이를 확인할 수 있다.
emp1 = Employee()
emp2 = Employee()

print(id(emp1)) #id는 물리적 메모리 주소
print(id(emp2))

#__class__: 인스턴스의 class 정보확인하기(인스턴스가 어떤 class에 있는지 확인하기)
print(emp1.__class__)
print(emp2.__class__)

#class에 대한 메모리 정보는 같은 값으로 출력된다. 
print(id(emp1.__class__))
print(id(emp2.__class__))

print(id(Employee))

#클래스 변수가 만들어짐 (클래스 변수는 어떤 인스턴스 간에 사용할 수 있다.)
Employee.name = "홍길동"
emp1.name #클래스 변수를 사용
emp2.name #클래스 변수를 사용

emp1.name = "박찬호"
emp1.name #인스턴스 변수가 됨 

emp2.name #클래스 변수르 사용 (자기의 인스턴스가 없기 때문에 클래스 변수를 사용함)

emp1.salary = 2000  
emp1.salary         #인스턴스 변수
emp2.salary         #오류: 자기안에 인스턴스 변수가 없기 때문에


<<요약>>
- 클래스를 사용할 때는 인스턴스화 해야한다. 
- 무조건 처음 사용해야할 method는 __init__이다. : 인스턴스를 초기화시키기 위한 method -> 이는 입력값을 그대로 사용하기 위한 방법이다.
- self지시자로 선언된 변수가 없으면 값이 출력이 되지 않는다. (e.g., self.name = name 변수 선언을 함)
- 모든 인스턴스에서 사용하기 위해서는 class변수로 선언해야 한다. 

# =============================================================================
# [문제187] 생성자에 이름, 핸드폰번호, 메일, 주소 변수를 생성합니다. 
print_info 메소드를 생성한 후  출력하는 Contact 클래스를 생성하세요.
인스턴스는 set_contact 함수를 이용해서 만드시고 이름, 핸드폰번호,메일, 주소는 입력값으로 받아서 출력하세요.
# =============================================================================
생성자 : __init__

#답1 - 잘못됨 
class contact:
    def __init__(self):
        self.name = ""
        self.mobile = ""
        self.email = ""
        self.address = ""
    def print_info(self):
        self.name = input("이름을 입력하세요: ")
        self.mobile = input("핸드폰번호를 입력하세요: ")
        self.email = input("메일을 입력하세요: ")
        self.address = input("주소를 입력하세요: ")  
    def set_contact(self):
        print("이름:",self.name)
        print("핸드폰번호:",self.mobile)
        print("메일:",self.email)
        print("주소:",self.address)

#답2  - 잘못됨
class contact:   
    def __init__(self):
        pass
    def print_info(self):
        self.name = input("이름을 입력하세요: ")
        self.mobile = input("핸드폰번호를 입력하세요: ")
        self.email = input("메일을 입력하세요: ")
        self.address = input("주소를 입력하세요: ")    
    def set_contact(self):
        print("이름:",self.name)
        print("핸드폰번호:",self.mobile)
        print("메일:",self.email)
        print("주소:",self.address)        

emp1 = contact()
emp1.print_info()
emp1.set_contact()


#답2 수정
class contact:   
    def __init__(self,name, mobile, email, address):
        self.name = name
        self.mobie = mobile
        self.email = email
        self.address = address

    def print_info(self):
        print("이름: %d"%self.name)
        print("핸드폰번호: %d"%self.mobile)
        print("메일: %d"%self.email)
        print("주소: %d"%self.address)    
        
def set_contact():
    name = input("이름을 입력하세요: ")
    mobile = input("핸드폰번호를 입력하세요: ")
    email = input("메일을 입력하세요: ")
    address = input("주소를 입력하세요: ")    
    info = Contact(name, mobile, email, address)
    info.print_info()

set_contact()

'홍길동', '010-1000-1004', 'hong@aaa.com', '서울시 강남구 삼성로'

#쌤답 
class Contact:
    def __init__(self,name, pn, email, addr):
        self.name = name
        self.pn = pn
        self.email = email
        self.addr = addr

    def print_info(self):
        print("이름 : {} ".format(self.name))
        print("핸드폰번호 : {} ".format(self.pn))
        print("메일 : {} ".format(self.email))
        print("주소 : {} ".format(self.addr))


def set_contact():
    name = input("이름을 입력하세요 : ")
    pn = input("핸드폰번호를 입력하세요 : ")
    email = input("메일을 입력하세요 : ")
    addr = input("주소를 입력하세요 : ")
    conIns = Contact(name, pn, email, addr)
    conIns.print_info()

set_contact()


# =============================================================================
# [문제188] Contact 클래스 이용해서 입력 들어 온 값들을 c:/data/contact.db 에
	저장해서 관리하세요.
# =============================================================================


import sqlite3

conn = sqlite3.connect(":memory:")

c = conn.cursor()

c.execute("create table contact(name, pn, email, addr)")

class Contact:
    def __init__(self,name, pn, email, addr):
        self.name = name
        self.pn = pn
        self.email = email
        self.addr = addr

    def print_info(self):
        print("이름 : {} ".format(self.name))
        print("핸드폰번호 : {} ".format(self.pn))
        print("메일 : {} ".format(self.email))
        print("주소 : {} ".format(self.addr))

    def input(self):
        self.conn = sqlite3.connect('c:/data/contact.db')
        self.c = self.conn.cursor()
        self.c.execute("insert into contact(name, pn, mail, addr) values(?,?,?,?)",(self.name,self.pn,self.email,self.addr))
        self.c.execute('select * from contact')
        print(self.c.fetchall())
    
    def commit(self):
        self.conn.commit()
       
    def rollback(self):
        self.conn.rollback()
    def close(self):
        self.c.close()
        self.conn.close()


def set_contact():
    name = input("이름을 입력하세요 : ")
    pn = input("핸드폰번호를 입력하세요 : ")
    email = input("메일을 입력하세요 : ")
    addr = input("주소를 입력하세요 : ")
    conIns = Contact(name, pn, email, addr)
    conIns.print_info()
    conIns.input()
    conIns.commit()
    conIns.close()

set_contact()

c.execute("drop table contact")

c.close()
info.close()
import sys
import os.path
sys.data.append('c:\data')
from Contact import *

#c:\data 에 모든파일형식으로 하되 확장자를 .py로 해주기, encoding은 utf-8로 하기 (utf-8로 하지 않으면 불러들일 때 )
# pacakage이름.py로 저장