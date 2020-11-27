# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 09:51:07 2018

@author: stu
"""
# =============================================================================
# 오전 수업
# =============================================================================

#
id_number1 = "010101-3123456"
id_number2 = "990101-2123456"

def id_process(id):
    gender = id[7]
    if gender == "1" or gender == "2":
        year = "19"+id[:2]
    else:
        year = "20"+id[:2]
    
    if gender == "2" or gender == "4":
        gender = "여성"
    else:
        gender = "남성"
    
    month = id[2:4]
    day = id[4:6]
    
    return year, month, day, gender

id_process(id_number1)
id_process(id_number2)   


#__str__: print라는 기능, 즉 인스턴스를 호출하게 되면 무조건 출력하게 됨 
#굳이 함수를 만들어 불러들여 출력하지 않아도 __str__을 통해 출력이 가능하다. 
class Person:
    
    def __init__(self, year, month, day, gender):
        self.year = year
        self.month = month
        self.day = day
        self.gender = gender 

    def __str__(self):
        return"{}년 {}월 {}일 성별은 {}입니다.".format(self.year, self.month, self.day, self.gender)

p = Person(2018, 10, 11, "남")
print(p)

#밑의 인수값을 넣어서 위의 클래스에서 정의된 함수를 통해서 return값을 출력하고 싶을 때 
id_number1 = "010101-3123456"
id_number2 = "990101-2123456"

#Error발생
p1 = Person(id_process(id_number1)) 
# *을 붙여 가변문자임을 명시한다. ; 함수앞에는 *을 꼭 넣어준다.
p1 = Person(*id_process(id_number1))
print(p1)


#클래스 메소드로 호출 하기
# 클래스 메소드 밖에서 클래스 변수를 선언하고자 한다면 cls.를 붙여야 한다. 
# 하지만    @classmethod안에서 선언되면 각각의 변수들에 굳이 cls.를 붙일 필요가 없다. 

class Person:
    
    def __init__(self, year, month, day, gender):
        self.year = year
        self.month = month
        self.day = day
        self.gender = gender 

    def __str__(self):
        return"{}년 {}월 {}일 성별은 {}입니다.".format(self.year, self.month, self.day, self.gender)
   
    @classmethod  #클래스 메소드로 바꾸기: 인스턴스 메소드로 사용하면 안된다. -> 이때는 클래스 메소드로 사용해야한다. 왜냐하면 모든 인스턴스에 메소드가 적용되기 위해서 / 클래스 메소드는 self대신 cls를 사용해야한다.
    def id_process(cls,id):                 #id_process(cls, id)
        gender = id[7]
        if gender == "1" or gender == "2":
            year = "19"+id[:2]
        else:
            year = "20"+id[:2]
        
        if gender == "2" or gender == "4":
            gender = "여성"
        else:
            gender = "남성"
        
        month = id[2:4]
        day = id[4:6]
        
        return cls(year, month, day, gender) #cls(변수들)
    
p1 = Person.id_process(id_number1)
print(p1)

p2 = Person.id_process(id_number2)
print(p2)



#상속
재사용의 방법

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("{}객체를 만드는 중".format(self.name))
    def show_info(self):
        print("이름은 {}, 나이는 {}세이다.".format(self.name, self.age))
        
p1 = Person("홍길동", 20)
p1.show_info()


# 중복되는 코드는 따로 class에 만들어 놓고 상속받으면 유용하다.
# 학생이라는 class는 Person이라는 class를 상속받음
class Student(Person):  #class Student(Person): Person이라는 class를 상속받음
    def __init__(self, name, age, hakbun): 
        Person.__init__(self, name, age)  #생성자에서도 Person의 class를 받고자 할 때 
        self.hakbun = hakbun
        
    def show_info(self): 
        Person.show_info(self) #Person 클래스에서의 함수 show_info도 사용하고자 할때
        print("학번은 {}입니다.".format(self.hakbun))

s1 = Student("홍길동", 20, 20181011)
s1.show_info()

# 
class Professor(Person):
    def __init__(self, name, age, years):
        Person.__init__(self, name, age)
        self.years = years
    
    def show_info(self):
        Person.show_info(self)
        print("근무연수가 {}년 입니다.".format(self.years))
        
p1 = Professor("정교수", 40, 10)
p1.show_info()


# =============================================================================
# [문제191] Person 클래스를 생성하세요. 생성자는 이름, 나이, 성별을 만드세요.
Person 클래스 에는 printMe 메소드를 생성하셔서 이름, 나이 성별을 출력합니다.

Employees클래스를 생성한후 Person상속받습니다.
생성자는 이름, 나이, 성별, 주소, 생일입니다.
단 이름, 나이, 성별은 person에서 상속받으세요.
Employees 클래스에 printMe를 재구성하셔서 주소, 생일을 출력하세요.


myPerson = Person("홍길동","10", "남")
myPerson.printMe()

myEmployee = Employee("송준기", "2", "남", "서울", "2016년 01월 01일")
myEmployee.printMe()



이름은 홍길동 ,  나이는 10살 이고, 성별은 남 입니다.
이름은 송준기 ,  나이는 2살 이고, 성별은 남 입니다.
집 주소는  서울  생일은  2016년 01월 01일 입니다. 
# =============================================================================

#답1
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def printMe(self):
        print("이름은 {}, 나이는 {}살 이고, 성별은 {}입니다.".format(self.name, self.age, self.gender))
        #print( + + + ), +로  만들경우 인스턴스를 만들 때 꼭 문자열("")로 만들어 줘야한다. 

myPerson = Person("홍길동","10", "남")
myPerson.printMe()

class Employee:
    def __init__(self, name, age, gender, addr, birth):
        Person.__init__(self, name, age, gender)
        self.addr = addr
        self.birth = birth
        
    def printMe(self):
        Person.printMe(self)
        print("집 주소는 {} 생일은 {} 입니다.".format(self.addr, self.birth))
        
myEmployee = Employee("송준기", "2", "남", "서울", "2016년 01월 01일")
myEmployee.printMe()


#print( + + + ), +로  만들경우 인스턴스를 만들 때 꼭 문자열("")로 만들어 줘야한다. 

# =============================================================================
# 수업 
# =============================================================================
# Person의 int의 매개변수를 그대로 사용하고자 할 때 pass를 그냥 써주면 된다.
class Emp(Person):
    pass

e = Emp("홍길동", 10, "남")
e.printMe()



# 상속은 여러개를 받을 수 있다. 여러개의 상속을 받을 경우 괄호 안에 상속할 클래스를 나열하면 된다. 
class Emp(Person1, Person2):
    
    
# =============================================================================
# [문제192] Add 클래스에 두수를 더하는 값을 리턴하는 add 메소드 생성
Multiply 클래스에 두수를 곱한값을 리턴하는 multiply 메소드 생성
Divide 클래스에 두수를 나눈값을 리턴하는 divide메소드 생성
Calculator클래스에는 Add, Multiply, Divide 상속받고 두수를 뺀값을 리턴하는 sub 메소드 생성하세요.

# =============================================================================

class Add:
    def add(self, x, y):
        result = 0
        self.x = x
        self.y = y
        self.result = x + y
        return self.result

 
class Multiply:
    def multiply(self, x, y):   
        result = 1
        self.x = x
        self.y = y
        self.result = x * y
        return self.result
        
class Divide:
    def divide (self, x, y):   
        result = 1
        self.x = x
        self.y = y
        self.result = x / y
        return self.result
        
class Calculator(Add, Multiply, Divide):
    def sub(self, x, y):
        result = 0
        self.x = x
        self.y = y 
        self.result = x-y
        return(self.result)
    

                

cal = Calculator()
print(cal.add(10,20))
print(cal.multiply(10,20))


#쌤답
class Add:
    def add(self, x, y):
        return x + y
 
class Multiply:
    def multiply(self, x, y):
        return x*y
        
class Divide:
    def divide(self, x, y):
        return x/y      
        
class Calculator(Add, Multiply, Divide):
    def sub(self, x, y):
        return x-y

cal = Calculator()
print(cal.add(10,20))
print(cal.multiply(10,20))

# =============================================================================
# 오후수업
# =============================================================================

#인스턴스 함수임 (self, x, y)
class Calculator:
    def add(self, x, y):
        return x + y
    
    def sub(self, x, y):
        return x-y
    
    def multiply(self, x, y):
        return x*y    

    def divide(self, x, y):
        return x/y  
    


Calculator.add(1,2)     #오류
#Calculator.add(1,2)가 error가 난다.
#인스턴스 메소드이기 때문에 인스턴스화를 먼저 해야한다.
c = Calculator()
c.add(1,2)

■ staticmethod
#클래스 메소드, 인스턴스 메소드 모두 적용될 수 있는 것은 스태틱 메소드이다. 
#1) 클래스이름.메소드 가능(어떤 인스턴스에 상관없이 같이 사용할 수 있음) 2)인스턴스이름.메소드 가능 -> 클래스 또는 인스턴스로 모두 접근(access)이 가능하다.
# self, cls를 넣으면 안된다.
class Calculator:
    @staticmethod
    def add(x, y):
        return x + y
    @staticmethod
    def sub(x, y):
        return x-y
    @staticmethod
    def multiply(x, y):
        return x*y    
    @staticmethod
    def divide(x, y):
        return x/y  


# =============================================================================
# 모듈 만들고 이용하기
# =============================================================================
■ 모듈 만들고 이용하기
#클래스 메소드로 사용 가능
Calculator.add(1,2)     
#인스턴스 메소드로 사용 가능 
c = Calculator()
c.add(1,2)

■ 모듈식으로 저장하기
- 내가 만든 클래스나 메소드를 모듈로 만들기 
- 예시> c:\data\cal.py로 저장하기

-설정 
파일 형식: 모든파일
파일확장자: .py
인코딩: utf-8 

- import하기
import sys
#path확인
sys.path
#path가 안걸려 있을 경우 추가하기
sys.path.append("c:\data")

#cal 모듈 import하기
import cal
#cal이라는 모듈안에 클래스와 메소드 확인하기 
dir(cal)

#calculator를 인스턴스화하기  :모듈이름.클래스이름
c=cal.Calculator()
c.add(1,2)

#바로 클래스 이름을 쓰고 싶을 때 (from 모듈 import *)
from cal import *
c = Calculator()

#잘 안됨 ㅠ
a = add(1,2)
a.add()


# 모듈 이름으로 불러들이기
PI = 3.141592
class Math:
    def cal(self, r):
        return PI*(r**2)

def mySum(i,j):
    return i+j

#if __name__ =="__main__":   이 조건문은 import할 때 if이하의 로직이 돌아가지 않는다.
if __name__ =="__main__":
    print(PI)
    m = Math()
    print(m.cal(10))
    print(mySum(PI,10))
    
# import 하기
import math_1
math_1.PI
math_1.mySum(1,2)


#모듈안에 무엇이 들어있는지 확인하기
dir(math_1)

print(math_1.PI)
m = math_1.Math()
m.cal(10)
math_1.mySum(math_1.PI,10)

from math_1 import *
print(PI)
m1 = Math()
m1.cal(10)
mySum(PI, 10)


# =============================================================================
# 다중상속
# =============================================================================
■ 다중상속

class mother:
    def talk(self):
        print("대화를 합니다.")

class father:
    def running(self):
        print("달리기를 합니다.")
        
class child(mother, father):
    def play(self):
        print("난 노는게 제일 좋아")
        
m = mother()
m.talk()
f = father()
f.running()
c = child()
c.talk()
c.running()
c.play()
#child가 무슨 상속을 받았는지 확인하기
print(child.__mro__)


class Person:
    country = "한국" #country는 클래스 변수이면서 인스턴스 변수가 될 수 있다.
    def __init__(self, name):
        self.name = name
    def myPrint(self):
        print(self.name + "은 " + self.country+"사람이다")

p1 = Person("홍길동")
p1.myPrint()

p2 = Person("제임스")
p2.country = "핀란드" #인스턴스가 다르기 때문에 다르게 적용된다.
p2.myPrint()

Person.country = "영국" #클래스 변수가 된다. 
p2.myPrint()
p1.myPrint()

#
class Person:
    country = "한국" #country는 클래스 변수이면서 인스턴스 변수가 될 수 있다.
    def __init__(self, name):
        self.name = name
    def myPrint(self):
        print(self.name + "은 " + self.country+"사람이다")

p1 = Person("홍길동")    #1
p1.myPrint()             #4

p2 = Person("제임스")    #2
p2.country = "핀란드"    #6  #인스턴스가 다르기 때문에 다르게 적용된다.
p2.myPrint()            #7

Person.country = "영국" #3 #클래스 변수가 된다. 
p2.myPrint()            #5
p1.myPrint()

#country를 한국으로 항상 상수처럼 사용하기 : __country 
class Person:
    __country = "한국" #country는 클래스 변수이면서 인스턴스 변수가 될 수 있다.
    def __init__(self, name):
        self.name = name
    def myPrint(self):
        print(self.name + "은 " + self.__country+"사람이다")

p1 = Person("홍길동")    #1
p1.myPrint()             #4

p2 = Person("제임스")    #2
p2.country = "핀란드"    #6  #인스턴스가 다르기 때문에 다르게 적용된다.
p2.myPrint()            #7

Person.country = "영국" #3 #클래스 변수가 된다. 
p2.myPrint()            #5
p1.myPrint()

