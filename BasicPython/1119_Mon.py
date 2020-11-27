# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 11:00:59 2018

@author: stu
"""

▣ linux 

cf. unix은 intel cpu를 사용하지 않고, unix에서 사용하는 cpu는 엄청 비싸다.

따라서 intel계열의 cpu을 사용할 수 있는 linux를 personal computer에서 사용할 수 있도록 만듦 

hardware, software를 어우를 수 있는 것이 kernal임 

redhat에서 CentOS를 ..?


설치


▣ virtual box 열기
file > menu 

    > 환경설정 > 입력  > 가상머신 
    호스트 키 조합: Ctrl + Alt  (나중에 linux에서 window로 빠져나올 때 사용, 보편적으로 Ctrl+Alt를 사용)
    
    > 환경설정 > 네트워크 > NAT 네트워크 > +(새네트워크 추가)
    cf. 가상머신에서 인터넷을 사용해야하기 때문에 NAT 네트워크를 추가해야한다.
    추가된 네트워크 오른쪽 마우스 클릭 > 편집 > ok
    
    > 환경설정 > 네트워크 > 호스트 전용 네트워크 > VirtualBox Host-Only Ethernet Adapter > 편집 >
    cf. 윈두오와 리눅스가 바깥쪽에서 의사소통해야할 때 사용해야하는 네트워크 (가상네트워크끼리 의사소통해야 하기 때문에 사용해야 함 )
    cf. 내 pc에서만 사용할 수 있는 private 주소임 
    cf. 최저 주소 한계와 최고 주소 한계 사이에서 랜덤으로 할당됨

cf. 새롭게 server 만들어야함 (가이드 모드에서 실행하는 것이 편함)
> 새로만들기 
- 이름: centos 입력
- 종류: linux
- 버전: Red Hat(64-bit)
 
cf. centos는 꼭 Red Hat 버전을 사용해야한다.  
cf. centos를 입력하면 종류와 버전이 자동적으로 할당된다.

> 다음 (메모리크기)
2048mb (2gb) 정도 메모리 할당하여 사용

> 다음
- 지금 새 가상 하드 디스크 만들기 > 만들기

> 다음
하드디스크 파일 종류 > VDI

> 다음
동적할당 
(dynamic하게 사용하겠다는 의미 )

> 다음
centos 
용량 30gb
(dynamic하게 사용량이 달라짐, 30gb라고 해서 30gb가 생성되지는 않는다.)

==========================
centos 생성됨 

> 일반 > centos 
또는 
> 설정 > 

일반 > 고급 
cf. 호스트 : 윈도우 / 게스트: 리눅스 
클립보드 공유 > 양방향
드래그 앤 드롭 > 양방향

> 시스템 
>플로피디스크 해제

>저장소 > 컨트롤러 > 속성 (cd그림 클릭) > 가상 광 디스크 파일 선택 > (c://centos를 찾아서 ios파일 선택 ) -> 이미지 정보가 나타남

> 오디오 > 해제 (필요없이 resource만 잡아먹기 때문에 해제함)

> 네트워크  
> 어댑터 1 > 네트워크 어댑터 사용하기 
> 어댑터 2 > 네트워크 어댑터 사용하기 (체크) >  다음에 연결됨(호스트 전용 어댑터) / >무작위 모드 (모두 허용) / 케이블 연결됨(체크)

> 공유폴더 
> 폴더 추가표시 > 폴더경로 (c:\centos) > 자동마운트(체크) /(읽기전용을 선택하면 다음에 쓸 수 없다.) 

cf. 폴더 경로는 윈도우와 리눅스에서 공유할 폴더를 선택하면 된다. 지금은 c:\centos가 된다.
cf. 윈도우 파일을 ftp로 굳이 넣지 않아도 됨  -> 윈도우 파일을 공유할 수 있음 

==========================
현재 centos 종료 되어있는데 > 시작하기(클릭)

> centosOS Linux7을 선택하거나 test하고 실행하기(이미지 확인하고 centos를 실행함)



==========================
CentOS > Welcome to CENTOS LINUX 7

한국어 
키보드 > 영어/ 한국어 (영어를 우선으로)
=========
소프트웨어
> gnome 데스크탑 선택  / 선택한 환경기능 > 개발용 도구 (선택)


시스템
설치대상 > 파디션 자동
kdump > 비활성
네트워크 및 호스트명 > 켬 > 호스트 이름(centos )
=========
root 암호 설정 
사용자 생성 > centos (이때 사용자 생성을 해줘야 나중에 편함 )


# =============================================================================
# 설치 완료 후 
# =============================================================================
> 약관 동의 
> 네트워크& 호스트 이름 > 이더넷 다 켬
> 설정완료 

# =============================================================================
# root로 접속
# =============================================================================

window의 ip를 통해 인터넷 접속


바탕화면 오른쪽 클릭 > 터미널 열기 

# 쓰다가 tab키를 누르면 자동 완성기능이 된다.
# (root로 열렸는지 확인하기)


# command line에서 명령어
# id 확인하기
id
# 
ifconfig
'''
enp0s3: nat netkwork정보
enp0s8:
    ip주소가 안보일 경우 >  연결을 켜면 됨
'''
#change directory
cd /etc/sysconfig/network-scripts
pwd

#directory(window에서 폴더개념)에서 무슨 내용이ㅊ 들어있는지 정보 확인하기
#파일 정보만 보기
ls
#좀 더 디테일하게 확인하기
ll 

#파일 정보에서 무슨 내용되어 있는지 미리보기
cat ifcfg-enp0s3
    #인터넷이 되려면 onboot="yes"라고 되어있어야 함
    onboot="yes" 

# copy 명령어 : cp 원본 새로운file
cp ifcfg-enp0s3 test.txt

#
ls

# 파일이 생성됐는지 확인하기
ls test.txt

# =============================================================================
# vi 편집기 사용하기
# =============================================================================

# vi편집기 사용하기 - linux와 hadoop을 사용하기 위해서 
# window의 메모장같은 역할을 함

# 메모장이 열림 /방향키 (예전에는 hjkl를 방향키로 사용함)
vi test.txt

'''
연습 

$: 그 행의 end키 역할
^: 그 홈의 home버튼과 같은 역할
del: 지우기
gg: 제일 앞으로 pointer가 옮겨감 
대문자 G:제일 끝행으로 pointer가 옮겨감
숫자5+ 대문자G: cursor가 5행으로 옮겨감
숫자1+ 대문자G: cursor가 1행으로 옮겨감
숫자3+ 대문자G: cursor가 3행으로 옮겨감
esc + :q! : 그냥 나가기 
지금까지 명령어 보기 :윗방향키 누르기
esc + : 5: cursor가 5행으로 옮겨감
esc: 뭔가 잘못됐다고 생각하면 무조건 esc키를 누름 

#커서가 어느 위치에 있는지에 따라 i를 쓸지 a를 쓸지 결정해야함
i(소문자): 입력함(bt사에서 t앞에서 )
a(소문자): 입력함(bt사에서 t뒤에서 )
I(대문자): 그 줄의 바로 앞에서 입력됨
A(대문자): 그 줄의 가장 뒤에 입력됨
O(대문자): 줄 앞에 줄을 만듦
o(소문자): 커서가 있는 다음줄에서 줄을 만듦
dd(소문자): 커서 한줄이 없어짐
x(소문자): 지워야될 문자를 하나씩 지워줌 (del과 같은 역할)
X(대문자): backspace처럼 지
r(소문자): 글자 하나 수정할 때 사용
cw :한단어를 수장할 때 사용
esc: insert해제
yy(소문자): 복사하기
p(소문자): cursor있는 다음에 붙여넣기
P(대문자): cursor있는 앞에 붙여넣기
#
esc + :wq: 저장하고 나가기
2 + dd(소문자): cursor가 있는 위치부터 두줄 지우기 
esc / no + enter : 'no'를 찾기 > n을 누르면 그다음 'no'를 찾기 
esc :q! :나가기 

'''

#실제상황 
vi ifcfg-enp0s3
#ONBOOT확인하기
ONBOOT = "YES" 로 바꾸기
#
vi ifcfg-enp0s8
# Dynamic하게 하는게 아니라 static하게 고정시키기 위해 
BOOTPROTO=dhcp 를 none으로 수정하기 (cw누르고 단어 없애고 none(소문자)을 입력)
+
esc
+
ONBOOT = yes(cw를 누르고 단어 없애기)
+
enter (행바꾸기)
+
NETMASK=225.225.225.0

#호스트 전용 네트워크 정도
IPADDR(IP address)
IPADDR = 192.168.56.101 #101이 아니더라도 101-254까지 안의 숫자만 사용하면 됨

#
esc + :wq

# 수정다하고 나오기
>적용하기
service network restart 

> ifconfig

# ifcfg-enp0s3: network 정보가 들어있음
# ifcfg-enp0s8: host 정보가 들어있음


#맨 위의  파일/머신/보기/입력/장치/도움말 중 
장치 > 게스트 확장 cd이미지 삽입 > 실행  > (끝나면) > enter 
#cf. gnome을 설정하지 않은 경우는 프로그램이 돌아가지 않는다. 

#rebooting하기 
터미널 열기 > reboot

#사용자 root 로 들어가기 
바탕화면에 sf_centos 가 만들어져 있음 > window에 있는 파일이 공유폴더에 공유됨 
#cf. 공유폴더가 생성되지 않았을 경우 > 자동마운트, 항상 사용하기 (version이 높을 경우)
# 명령프롬프트에서 ping 192. 168. 56. 101 으로 확인하기 


# 터미널 열기 
window와 linux 운영체제에서 드래그앤 드롭이 가능함(양방향으로 되어있어야함) -> (복사-붙여넣기)가능

#예시 복사하기 붙여넣기
[root@centos ~]# copy^C
[root@centos ~]# ^C

# 바탕화면 cd 없애고 싶으면 마우스 오른쪽 버튼을 눌러 없애기 하면 됨 

=================================
# 터미널 열기
# 실제 host 연결 

# 안에 내용 미리보기 
cat /etc/hosts 
'''
[root@centos ~]# cat /etc/hosts
127.0.0.1   localhost localhost.localdomain localhost4 localhost4.localdomain4
::1         localhost localhost.localdomain localhost6 localhost6.localdomain6 
'''

#
vi /etc/hosts
'''
127.0.0.1   localhost localhost.localdomain localhost4 localhost4.localdomain4
::1         localhost localhost.localdomain localhost6 localhost6.localdomain6
'''
# 실제 host와 이어주기 
192. 168. 56. 101 centos

#저장하기 
esc + :wq 

# 전원꺼짐 
init 0 

====================================
#cf.virtual box의 장점: 사용한 내용 부분을 그대로 저장하고 끝낼 수 있음 
'닫을 때 > 가상머신 닫기 > 현재시스템 상태 저장하기'


====================================



 

