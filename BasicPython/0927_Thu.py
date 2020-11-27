# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 15:36:46 2018

@author: stu
"""

import sqlite3

# 메모리에다가 db를 구성
conn = sqlite3.connect(":memory:")

# conn에 cursor 생성
c = conn.cursor() 

c.execute("create table contact(name, mobile, email, address)")

c.execute("insert into contact(name, mobile, email, address) values('홍길동','010','100@','100')")

c.execute("select*from contact")

c.fetchone()

c.fetchone()

c.execute("insert into contact(name, mobile, email, address) values('박찬호','010','103','102')")

c.execute("select*from contact")

c.fetchone()

c.fetchone()

c.fetchall()

#영구히 저장되는 것이 아니라서 rollback 수행시 사라짐
conn.rollback()

#영구히 저장
conn.commit()


#커서닫기
c.close()
#connect(메모리)닫기
coon.close()

conn=sqlite3.connect(":memory:")

c = conn.cursor()
# 커서와 메모리를 close했기 때문에 안의 내용(table) 사라짐
c.exectue("select*from contact")

c.close()

conn.close()

# 파일로 떨어뜨리면 close한 이후에도 계속사용 가능
conn=sqlite3.connect("c:/data/insa.db")

c = conn.cursor()

c.execute("create table emp1(id integer, name text, sal integer)")

c.execute("insert into emp1(id,name,sal) values(1,'권아름',1000)")

c.execute("insert into emp1(id,name,sal) values(2,'박찬호',2000)")

c.execute("select * from emp1")

c.fetchall()

conn.commit()

c.close()

conn.close()

#
conn=sqlite3.connect("c:/data/insa.db")

c = conn.cursor()

#내가 만든 테이블 보기
c.execute("select name from sqlite_master where type='table'")

c.fetchall()

#PRAGMA table_info(테이블명) : 테이블의 정보 확인 (sql에서 desc)
c.execute("PRAGMA table_info(emp1)")

c.fetchall()
# values를 ?,?,?로 두고 후에 입력값 처리
c.execute("insert into emp1(id,name,sal) values(?,?,?)",(3,'나얼',3000))	

c.execute("select * from emp1")

c.fetchall()

#입력값 처리
insert_sql="insert into emp1(id,name,sal) values(?,?,?)"	
c.execute(insert_sql,(4,'윤건',4000))

c.execute("select * from emp1")

c.fetchall()


conn.commit()

c.execute("select * from emp1")

#fetchmany(4) : 4개만 보기
c.fetchmany(4)

c.execute("update emp1 set sal=6000 where id=1")

c.execute("select * from emp1 where id=1")

c.fetchone()

conn.rollback()

c.execute("select * from emp1 where id=1")

c.fetchone()

c.execute("delete from emp1 where id=2")

c.execute("select * from emp1")

c.fetchall()

#컬럼 추가
c.execute("alter table emp1 add column deptno integer")		

c.fetchall()

c.execute("select * from emp1")

c.fetchall()

c.execute("drop table emp1")

c.execute("create table emp(id integer,name text,sal integer,deptno integer)")

c.execute("insert into emp(id,name,sal,deptno) values(1,'홍길동',1000,10)")

c.execute("insert into emp(id,name,sal,deptno) values(2,'박찬호',2000,20)")

c.execute("insert into emp(id,name,sal,deptno) values(3,'나얼',3000,30)")

c.execute("insert into emp(id,name,sal,deptno) values(4,'윤건',4000,40)")

conn.commit()

c.execute("select * from emp")

c.fetchall()

c.execute("create table dept(deptno integer, dname text)")

c.execute("insert into dept(deptno,dname) values(10,'총무부')")

c.execute("insert into dept(deptno,dname) values(20,'영업1')")

c.execute("insert into dept(deptno,dname) values(30,'영업2')")

c.execute("insert into dept(deptno,dname) values(40,'분석팀')")

conn.commit()

c.execute("select * from dept")

c.fetchall()

c.execute("insert into emp(id,name,sal,deptno) values(5,'김건모',5000,null)")

c.execute("insert into dept(deptno,dname) values(50,'인사팀')")

conn.commit()

c.execute("select * from emp")

c.fetchall()

c.execute("select * from dept")

c.fetchall()

#join은 ANSI표준으로 지원함
c.execute("select emp.id,emp.name,emp.deptno,dept.dname from emp inner join dept on emp.deptno=dept.deptno")	

#emp.deptno가 null인 김건모는 출력되지 않음
c.fetchall()

