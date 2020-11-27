# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 09:57:09 2018

@author: stu
"""

whoami
#session이 누구인지 확인하기
#창이 열려 있는 os계정이 보임 
'''[root@centos ~]# whoami
root'''

su - centos
#centos로 계정을 옮기

'''[root@centos ~]# su - centos
마지막 로그인: 화 11월 20 09:59:20 KST 2018 일시 pts/0
'''
su -
#root 계정으로 옮김, 이때 암호를 물어봄

'''[centos@centos ~]$ su -
암호:
마지막 로그인: 화 11월 20 09:58:50 KST 2018 일시 :0
'''

hostname
#호스트 이름 (서버이름)
#hadoop을 사용할 때 필요함 
'''[root@centos ~]# hostname
centos
'''

hostnamectl set-hostname dataserver
#호스트 이름 수정 (#server도 이름을 바꿀 수 있음)
# hostnamectl set-hostname dataserver: hostname을 dataserver이름으로 바꾸겠음(새로운 이름: dataserver)
'''[root@centos ~]# hostname
dataserver
'''

#cf. rebooting을 해야만 호스트이름이 바뀜

cd /etc
ls
cd
pwd
'''[root@centos ~]# pwd
/root
'''

#vi 편집기 사용하기
vi /etc/hosts
'''127.0.0.1   localhost localhost.localdomain localhost4 localhost4.localdomain4
::1         localhost localhost.localdomain localhost6 localhost6.localdomain6
192.168.56.101 centos
'''

ifconfig
#ipconfig: windows
#어댑터1: enp0s3 -> (Nat) dynamic하게 받음
#어댑터2: enp0s8 -> (host) 고정하여 사용하는 것이 좋음
virtual box > 설정 > 호스트 전용 네트워크 정보 > 최저 주소 한계 192.168.56.101/최고 주소 한계  192.168.56.254
# ip주소 하나를 써서, 그 하나를 가지고 공유기를 이용해서 public하게 사용함/ 따라서 이 주소는 여기 안에서만 사용하는 주소 임 
# 네트워크 > 어댑터2 > 

cd /etc/sysconfig/network-scripts
ls
'''[root@dataserver ~]# cd /etc/sysconfig/network-scripts
[root@dataserver network-scripts]# ls
ifcfg-enp0s3       ifdown-eth     ifdown-sit     ifup-ib     ifup-routes
ifcfg-enp0s8       ifdown-ib      ifdown-tunnel  ifup-ippp   ifup-sit
ifcfg-lo           ifdown-ippp    ifup           ifup-ipv6   ifup-tunnel
ifcfg-유선_연결_1  ifdown-ipv6    ifup-Team      ifup-isdn   ifup-wireless
ifdown             ifdown-isdn    ifup-TeamPort  ifup-plip   init.ipv6-global
ifdown-Team        ifdown-post    ifup-aliases   ifup-plusb  network-functions
ifdown-TeamPort    ifdown-ppp     ifup-bnep      ifup-post   network-functions-ipv6
ifdown-bnep        ifdown-routes  ifup-eth       ifup-ppp    test.txt
'''
#ifcfg-enp0s3: 첫번째 이더넷 
#ifcfg-enp0s8: 두번째 이더넷
    vi ifcfg-enp0s8
    #BOOTPROTO = none
    #ONBOOT = yes
    #NETMASK = 225.225.225.0 #고정임
    #IPADDR = 192.168.56.101 #바꿀 수 있음 (192.168.56 :사설이기 때문에 이부분은 고정이고/ 101: 이부분은 바꿀 수 있다.)


vi /etc/hosts
#192.168.56.110 dataserver 로 고치기
'''
127.0.0.1   localhost localhost.localdomain localhost4 localhost4.localdomain4
::1         localhost localhost.localdomain localhost6 localhost6.localdomain6
192.168.56.101 dataserver
'''

'''cf. vi 편집기
esc + u : undo 
ctrl + r : redo'''


esc + : + wq
#저장하고 나오기

reboot
#저장하고 reboot해야 활성화 됨


cf. 전체 설정 (복습)
장치 > 게스트이미지 cd 삽입 (마운트)
#윈도우와 공유폴더를 사용하기 위해 

설정 > 일반 > 고급 > 클립보두 공유(양방향) / 드래그앤 드롭(양방향)
#마우스를 윈도우와 linux를 왔다갔다 하게 만들기 위해


# =============================================================================
root로 접속> 

ls
# 현재 디렉토리 내용 확인

ls /home
# 홈에 무슨 내용이 있는지
ls /home/centos
# 홈 centos에서 무슨 내용있는지
ls -a
#현재 디렉토리 숨겨져 있는 파일 
'''[root@dataserver ~]# ls -a
.              .cache     .vboxclient-clipboard.pid    다운로드
..             .config    .vboxclient-display.pid      문서
.ICEauthority  .cshrc     .vboxclient-draganddrop.pid  바탕화면
.bash_history  .dbus      .vboxclient-seamless.pid     비디오
.bash_logout   .esd_auth  anaconda-ks.cfg              사진
.bash_profile  .local     initial-setup-ks.cfg         서식
.bashrc        .tcshrc    공개                         음악
'''

ls -l 
# permission에 대한 부분 (권한에 대한 부분)
# 권한은 3roTlr 
'''[root@dataserver ~]# ls -l
합계 8
-rw-------. 1 root root 1769 11월 19 17:07 anaconda-ks.cfg
-rw-r--r--. 1 root root 1800 11월 19 17:10 initial-setup-ks.cfg
drwxr-xr-x. 2 root root    6 11월 19 17:10 공개
drwxr-xr-x. 2 root root    6 11월 19 17:10 다운로드
drwxr-xr-x. 2 root root    6 11월 19 17:10 문서
drwxr-xr-x. 2 root root    6 11월 19 17:23 바탕화면
drwxr-xr-x. 2 root root    6 11월 19 17:10 비디오
drwxr-xr-x. 2 root root    6 11월 19 17:10 사진
drwxr-xr-x. 2 root root    6 11월 19 17:10 서식
drwxr-xr-x. 2 root root    6 11월 19 17:10 음악
'''
#drwxr(권한에 대한 정보: d-directgory/r-read/w-write/x-excute/)-xr-x: drw /  root(파일/디렉토리에 대한 소유자 이름) / root(그룹)
#drw :소유자 
#xr- :그룹(그 외의 사람들)
#- hypen은 아예 쓸 수 없게 만듦 







'''
ls : 현재 디렉토리 파일 목록
ls -a : 현재 디렉토리 숨김파일도 포함
ls -l : 현재 디렉토리 목록을 자세히 보여준다. 
'''

ls -l /etc/sysconfig/a*
#a가 들어간 파일을 모두 보여줌 
'''[root@dataserver ~]# ls -l /etc/sysconfig/a*
-rw-r--r--. 1 root root 403 11월  6  2016 /etc/sysconfig/atd
-rw-r--r--. 1 root root 430 11월 19 17:06 /etc/sysconfig/authconfig
-rw-r--r--. 1 root root 339 11월  6  2016 /etc/sysconfig/autofs
'''

cd /etc/sysconfig
cd
#홈 디렉토리로 옮겨감 
cd ~centos 
#cd ~유저이름 : 유저의 home directory로 옮겨감
pwd
'''[root@dataserver centos]# pwd
/home/centos
'''


touch test.txt
#크기가 0인 파일 생성
#크기가 0인 파일을 생성하거나 이미 파일이 존재한다면 파일의 최종수정시간 변경
ls -l test.txt
'''[root@dataserver ~]# ls -l test.txt
-rw-r--r--. 1 root root 0 11월 20 11:10 test.txt
'''
다시 touch test.txt 
'''[root@dataserver ~]# touch test.txt
[root@dataserver ~]# ls -l test.txt
-rw-r--r--. 1 root root 0 11월 20 11:11 test.txt
'''

rm test.txt
#파일 삭제
#파일을 삭제하면 다시 살릴 수 없다. 따라서 주의가 필요하다.
'''[root@dataserver ~]# rm test.txt
rm: remove 일반 빈 파일 `test.txt'? '''
rm -i test.txt #파일 삭제시 물어본다
rm -f test.txt #파일 삭제시 물어보지 않는다. 

# =============================================================================
# directory 생성 
# =============================================================================
mkdir data
#data라는 디렉토리가 생성됨

'''[root@dataserver ~]# cd data
[root@dataserver data]# pwd
/root/data
[root@dataserver data]# cd
[root@dataserver ~]# ls
anaconda-ks.cfg  initial-setup-ks.cfg  공개      문서      비디오  서식
data             test.txt              다운로드  바탕화면  사진    음악
'''

cd ..
pwd
ls
#가장 상위로 올라옴 
'''[root@dataserver ~]# cd ..
[root@dataserver /]# pwd
/
[root@dataserver /]# ls
1    boot  etc   lib    media  opt   root  sbin  sys  usr
bin  dev   home  lib64  mnt    proc  run   srv   tmp  var
'''
#home라는 기능은 디렉토리는 유저 이름의 집(공간)을 만들어주는 기능이다. 

cd /home 
ls 
'''[root@dataserver /]# cd /home
[root@dataserver home]# ls
centos
'''
pwd
'''[root@dataserver home]# pwd
/home
'''
cd
pwd
'''
[root@dataserver home]# cd
[root@dataserver ~]# pwd
/root
'''
# root로 돌아옴

mkdir -p /home/data
'''[root@dataserver ~]# mkdir -p /home/data
[root@dataserver ~]# cd /home/data
[root@dataserver data]# pwd
/home/data
'''
# -p : 이미 존재하는 디렉토리 안에 서브디렉토리를 만들고자 할때 -p를 사용한다. 

cd
# root디렉토리로 오기
ls
pwd

'''[root@dataserver data]# cd
[root@dataserver ~]# ls
anaconda-ks.cfg  initial-setup-ks.cfg  공개      문서      비디오  서식
data             test.txt              다운로드  바탕화면  사진    음악
[root@dataserver ~]# pwd
/root
'''

# =============================================================================
# directory 지우기 
# =============================================================================

rmdir data
#rmdir :data 디렉토리를 삭제함
ls
'''[root@dataserver ~]# rmdir data
[root@dataserver ~]# ls
anaconda-ks.cfg       test.txt  다운로드  바탕화면  사진  음악
initial-setup-ks.cfg  공개      문서      비디오    서식
'''

mkdir data1
#data1 생성
cd data1
#data1로 들어오기
pwd
'''[root@dataserver ~]# mkdir data1
[root@dataserver ~]# cd data1
[root@dataserver data1]# pwd
/root/data1
'''

touch test.txt
# test 텍스트 생성하기
ls
'''[root@dataserver data1]# touch test.txt
[root@dataserver data1]# ls
test.txt
'''

cd 

rmdir data1
#rmdir: data1 디렉토리 안에 파일이 존재하지 않을 경우에만 삭제할 수 있는 기능이다.
#아까 data가 삭제된 이유는 파일이 존재하지 않았기 때문에 삭제할 수 있었다.
'''[root@dataserver ~]# rmdir data1
rmdir: failed to remove `data1': 디렉터리가 비어있지 않음
'''

rm -r data1
# 디렉토리 안에 파일이 있어도 삭제할 수 있는 기능 
'''[root@dataserver ~]# rmdir data1
rmdir: failed to remove `data1': 디렉터리가 비어있지 않음
[root@dataserver ~]# rm -r data1
rm: descend into directory `data1'? y
rm: remove 일반 빈 파일 `data1/test.txt'? y
rm: remove 디렉토리 `data1'? y
'''

rm -rf data1
# 묻지 않고 바로 삭제하기 

# =============================================================================
# java설치
# =============================================================================
centos 공유폴더에서 jdk 있는지 확인하기 

터미널 열기 - root 에서 방화벽을 해지 해야한다. 

iptables -L
#방화벽 확인 
'''[root@dataserver ~]# iptables -L
Chain INPUT (policy ACCEPT)
target     prot opt source               destination         
ACCEPT     udp  --  anywhere             anywhere             udp dpt:domain
ACCEPT     tcp  --  anywhere             anywhere             tcp dpt:domain
ACCEPT     udp  --  anywhere             anywhere             udp dpt:bootps
ACCEPT     tcp  --  anywhere             anywhere             tcp dpt:bootps
ACCEPT     all  --  anywhere             anywhere             ctstate RELATED,ESTABLISHED
ACCEPT     all  --  anywhere             anywhere            
INPUT_direct  all  --  anywhere             anywhere            
INPUT_ZONES_SOURCE  all  --  anywhere             anywhere            
INPUT_ZONES  all  --  anywhere             anywhere            
DROP       all  --  anywhere             anywhere             ctstate INVALID
REJECT     all  --  anywhere             anywhere             reject-with icmp-host-prohibited

Chain FORWARD (policy ACCEPT)
target     prot opt source               destination         
ACCEPT     all  --  anywhere             192.168.122.0/24     ctstate RELATED,ESTABLISHED
ACCEPT     all  --  192.168.122.0/24     anywhere            
ACCEPT     all  --  anywhere             anywhere            
REJECT     all  --  anywhere             anywhere             reject-with icmp-port-unreachable
REJECT     all  --  anywhere             anywhere             reject-with icmp-port-unreachable
ACCEPT     all  --  anywhere             anywhere             ctstate RELATED,ESTABLISHED
ACCEPT     all  --  anywhere             anywhere            
FORWARD_direct  all  --  anywhere             anywhere            
FORWARD_IN_ZONES_SOURCE  all  --  anywhere             anywhere            
FORWARD_IN_ZONES  all  --  anywhere             anywhere            
FORWARD_OUT_ZONES_SOURCE  all  --  anywhere             anywhere            
FORWARD_OUT_ZONES  all  --  anywhere             anywhere            
DROP       all  --  anywhere             anywhere             ctstate INVALID
REJECT     all  --  anywhere             anywhere             reject-with icmp-host-prohibited

Chain OUTPUT (policy ACCEPT)
target     prot opt source               destination         
ACCEPT     udp  --  anywhere             anywhere             udp dpt:bootpc
OUTPUT_direct  all  --  anywhere             anywhere            

Chain FORWARD_IN_ZONES (1 references)
target     prot opt source               destination         
FWDI_public  all  --  anywhere             anywhere            [goto] 
FWDI_public  all  --  anywhere             anywhere            [goto] 
FWDI_public  all  --  anywhere             anywhere            [goto] 

Chain FORWARD_IN_ZONES_SOURCE (1 references)
target     prot opt source               destination         

Chain FORWARD_OUT_ZONES (1 references)
target     prot opt source               destination         
FWDO_public  all  --  anywhere             anywhere            [goto] 
FWDO_public  all  --  anywhere             anywhere            [goto] 
FWDO_public  all  --  anywhere             anywhere            [goto] 

Chain FORWARD_OUT_ZONES_SOURCE (1 references)
target     prot opt source               destination         

Chain FORWARD_direct (1 references)
target     prot opt source               destination         

Chain FWDI_public (3 references)
target     prot opt source               destination         
FWDI_public_log  all  --  anywhere             anywhere            
FWDI_public_deny  all  --  anywhere             anywhere            
FWDI_public_allow  all  --  anywhere             anywhere            
ACCEPT     icmp --  anywhere             anywhere            

Chain FWDI_public_allow (1 references)
target     prot opt source               destination         

Chain FWDI_public_deny (1 references)
target     prot opt source               destination         

Chain FWDI_public_log (1 references)
target     prot opt source               destination         

Chain FWDO_public (3 references)
target     prot opt source               destination         
FWDO_public_log  all  --  anywhere             anywhere            
FWDO_public_deny  all  --  anywhere             anywhere            
FWDO_public_allow  all  --  anywhere             anywhere            

Chain FWDO_public_allow (1 references)
target     prot opt source               destination         

Chain FWDO_public_deny (1 references)
target     prot opt source               destination         

Chain FWDO_public_log (1 references)
target     prot opt source               destination         

Chain INPUT_ZONES (1 references)
target     prot opt source               destination         
IN_public  all  --  anywhere             anywhere            [goto] 
IN_public  all  --  anywhere             anywhere            [goto] 
IN_public  all  --  anywhere             anywhere            [goto] 

Chain INPUT_ZONES_SOURCE (1 references)
target     prot opt source               destination         

Chain INPUT_direct (1 references)
target     prot opt source               destination         

Chain IN_public (3 references)
target     prot opt source               destination         
IN_public_log  all  --  anywhere             anywhere            
IN_public_deny  all  --  anywhere             anywhere            
IN_public_allow  all  --  anywhere             anywhere            
ACCEPT     icmp --  anywhere             anywhere            

Chain IN_public_allow (1 references)
target     prot opt source               destination         
ACCEPT     tcp  --  anywhere             anywhere             tcp dpt:ssh ctstate NEW

Chain IN_public_deny (1 references)
target     prot opt source               destination         

Chain IN_public_log (1 references)
target     prot opt source               destination         

Chain OUTPUT_direct (1 references)
target     prot opt source               destination  '''

iptables -F
#방화벽 해지하기 
iptalbes -L
'''[root@dataserver ~]# iptables -L
Chain INPUT (policy ACCEPT)
target     prot opt source               destination         

Chain FORWARD (policy ACCEPT)
target     prot opt source               destination         

Chain OUTPUT (policy ACCEPT)
target     prot opt source               destination         

Chain FORWARD_IN_ZONES (0 references)
target     prot opt source               destination         

Chain FORWARD_IN_ZONES_SOURCE (0 references)
target     prot opt source               destination         

Chain FORWARD_OUT_ZONES (0 references)
target     prot opt source               destination         

Chain FORWARD_OUT_ZONES_SOURCE (0 references)
target     prot opt source               destination         

Chain FORWARD_direct (0 references)
target     prot opt source               destination         

Chain FWDI_public (0 references)
target     prot opt source               destination         

Chain FWDI_public_allow (0 references)
target     prot opt source               destination         

Chain FWDI_public_deny (0 references)
target     prot opt source               destination         

Chain FWDI_public_log (0 references)
target     prot opt source               destination         

Chain FWDO_public (0 references)
target     prot opt source               destination         

Chain FWDO_public_allow (0 references)
target     prot opt source               destination         

Chain FWDO_public_deny (0 references)
target     prot opt source               destination         

Chain FWDO_public_log (0 references)
target     prot opt source               destination         

Chain INPUT_ZONES (0 references)
target     prot opt source               destination         

Chain INPUT_ZONES_SOURCE (0 references)
target     prot opt source               destination         

Chain INPUT_direct (0 references)
target     prot opt source               destination         

Chain IN_public (0 references)
target     prot opt source               destination         

Chain IN_public_allow (0 references)
target     prot opt source               destination         

Chain IN_public_deny (0 references)
target     prot opt source               destination         

Chain IN_public_log (0 references)
target     prot opt source               destination         

Chain OUTPUT_direct (0 references)
target     prot opt source               destination '''


java -version
#java 확인 
''''[root@dataserver ~]# java -version
openjdk version "1.8.0_102"
OpenJDK Runtime Environment (build 1.8.0_102-b14)
OpenJDK 64-Bit Server VM (build 25.102-b14, mixed mode)
'''
# oepnjdk를 사용하면 잘 안된다. centos에서 무료로 제공해주는 jdk임
# openjdk대신 oracle에서 만든 jdk(자바)를 사용하도록 한다. 
# 이를 위해서는 변경작업이 필요하다. 
# cf. 하둡을 사용하기 위해서는 jdk 6버전 이상을 사용해야 한다. 


cd /media/sf_centos/ 
#공유폴더는 media 폴더에 있고, sf는 무조건 들어간다. 그다음 _공유폴더이름을 사용해야한다. 
# window에 있는 내용이지만 linux에 있는 것 처럼 보이게 한다. 
'''[root@dataserver ~]# cd /media/sf_centos/
'''

ls jdk*
'''[root@dataserver sf_centos]# ls jdk*
jdk7u80-linux-x64.tar.gz
'''
#linux에서 압축파일은 tar파일임 

cp jdk-7u80-linux-x64.tar.gz /usr
'''[root@dataserver sf_centos]# cp jdk-7u80-linux-x64.tar.gz /usr
'''
# 공유폴더에 있는 파일을 usr 위치에 복사함 
# cp 복사할 파일 /파일을 복사할 위치

cd /usr
# usr 디렉토리로 이동
ls jdk*
'''[root@dataserver sf_centos]# cd /usr
[root@dataserver usr]# ls jdk*
jdk-7u80-linux-x64.tar.gz
'''
#복사가 잘 됐는지 확인하기 


tar xvfz jdk-7u80-linux-x64.tar.gz 
#압축풀기
# xvfz 설명
#    x : 묶음을 해제
#    v : 화면에 표시
#    f : 파일이름을 지정
#    z : gunzip이라는 압축프로그램을 사용 
#디렉토리 이름은 파일이름으로 하여 압축을 품
'''[root@dataserver usr]# tar xvfz jdk-7u80-linux-x64.tar.gz 
'''

ls
# 압축풀기 확인하기
# jdk-7u80-linux-x64.tar.gz 폴더 생성하여 압축 품
'''[root@dataserver usr]# ls
bin  games    jdk-7u80-linux-x64.tar.gz  lib    libexec  sbin   src
etc  include  jdk1.7.0_80                lib64  local    share  tmp
'''

cd jdk1.7.0_80/
ls
pwd
'''[root@dataserver usr]# cd jdk1.7.0_80/
[root@dataserver jdk1.7.0_80]# ls
COPYRIGHT    THIRDPARTYLICENSEREADME-JAVAFX.txt  db       lib      src.zip
LICENSE      THIRDPARTYLICENSEREADME.txt         include  man
README.html  bin                                 jre      release
[root@dataserver jdk1.7.0_80]# pwd
/usr/jdk1.7.0_80
'''
#linux에서 java 홈 생성: /usr/jdk1.7.0_80

cd 
# 상위 디렉토리로 가기
pwd
# 확인하기 
'''
[root@dataserver jdk1.7.0_80]# cd ..
[root@dataserver usr]# pwd
/usr
'''
 
# java home(자바홈)을 환경설정해야 함
cd
vi /etc/profile
'''[root@dataserver usr]# cd
[root@dataserver ~]# vi /etc/profile
'''
#booting을 할때마다 제일 먼저 보게 되는 파일임 
#대문자 G를 누르면 제일 밑으로 감
#unset에 오면 
#소문자 o를 넣어 행을 insert 함

export JAVA_HOME=/usr/jdk1.7.0_80
export PATH=$PATH:$JAVA_HOME/bin
export CLASS_PATH="."

esc + : + wq 
#write 끝내고 나옴
 
source /etc/profile
# source: source명령어는 profile을 적용함

java -version
'''[root@dataserver ~]# java -version
openjdk version "1.8.0_102"
OpenJDK Runtime Environment (build 1.8.0_102-b14)
OpenJDK 64-Bit Server VM (build 25.102-b14, mixed mode)
'''
#java도 설치했는데 안되는 이유는 순위에서 밀린 것이다. 

which java
'''[root@dataserver ~]# which java
/usr/bin/java
'''

update-alternatives --install "/usr/bin/java" "java" "/usr/jdk1.7.0_80/bin/java" 1
'''[root@dataserver ~]# update-alternatives --install "/usr/bin/java" "java" "/usr/jdk1.7.0_80/bin/java" 1
'''
#사용해야할 jdk를 등록시키는 작업
#기존사용한 것: /usr/bin/java
#바꿀 것: "/usr/jdk1.7.0_80/bin/java"

update-alternatives --config java
#jdk 변경하고자 할 때 사용함 
'''
[root@dataserver ~]# update-alternatives --config java

3 개의 프로그램이 'java'를 제공합니다.

  선택    명령
-----------------------------------------------
   1           java-1.7.0-openjdk.x86_64 (/usr/lib/jvm/java-1.7.0-openjdk-1.7.0.111-2.6.7.8.el7.x86_64/jre/bin/java)
*+ 2           java-1.8.0-openjdk.x86_64 (/usr/lib/jvm/java-1.8.0-openjdk-1.8.0.102-4.b14.el7.x86_64/jre/bin/java)
   3           /usr/jdk1.7.0_80/bin/java

현재 선택[+]을 유지하려면 엔터키를 누르고, 아니면 선택 번호를 입력하십시오: #3번 치고 enter
'''

java -version
# 설치한 java 버전이 나옴 
'''[root@dataserver ~]# java -version
java version "1.7.0_80"
Java(TM) SE Runtime Environment (build 1.7.0_80-b15)
Java HotSpot(TM) 64-Bit Server VM (build 24.80-b11, mixed mode)'''


# =============================================================================
# 프로토콜 버퍼 설치
# =============================================================================

#프로토콜 버퍼 설치
    #-구글에서 만든 오픈소스 직렬화 라이브러리
    #-이기종 서버간의 데이터 통신은 서로 다른 종류의 언어로 개발된 시스템간의 데이터를 전달하는 방식 
    #-text format, binary format 데이터를 이용한다.
        #-text format 방식은 데이터를 이해하기 쉽고, 각 언어별로 파서를 제공한다(complie). 단점은 데이터 자체가 크다. 따라서 파서의 성능은 떨어진다. 
        #-binary format 방식은 데이터 크기가 작다. 따라서 성능이 좋다. 단점은 바이너리 코드를 만들고 해독해야 하는 모듈을 만들어야 하는 부담이 있다.
        
# 하둡2에서는 데몬간의 데이터 통신을 위해 protocol buffer를 사용한다. 
   
cd /media/sf_centos/
ls protobuf*
'''[root@dataserver ~]# cd /media/sf_centos/
[root@dataserver sf_centos]# ls protobuf*
protobuf-2.5.0.tar.gz
'''

cp protobuf-2.5.0.tar.gz /usr/local
# copy하기
'''[root@dataserver sf_centos]# cp protobuf-2.5.0.tar.gz /usr/local
'''

cd /usr/local
ls protobuf*
# 복사한 파일 확인하기
'''[root@dataserver sf_centos]# cd /usr/local
[root@dataserver local]# ls protobuf*
protobuf-2.5.0.tar.gz'''

tar xvfz protobuf-2.5.0.tar.gz
# 압축풀기
'''[root@dataserver local]# tar xvfz protobuf-2.5.0.tar.gz
'''

ls
'''[root@dataserver local]# ls
bin  games    lib    libexec         protobuf-2.5.0.tar.gz  share
etc  include  lib64  protobuf-2.5.0  sbin                   src
'''
cd protobuf-2.5.0/
'''[root@dataserver local]# cd protobuf-2.5.0/
'''

ls
'''[root@dataserver local]# ls
bin  games    lib    libexec         protobuf-2.5.0.tar.gz  share
etc  include  lib64  protobuf-2.5.0  sbin                   src
[root@dataserver local]# cd protobuf-2.5.0/
[root@dataserver protobuf-2.5.0]# ^C
[root@dataserver protobuf-2.5.0]# ls
CHANGES.txt       config.h.in                   java
CONTRIBUTORS.txt  config.sub                    ltmain.sh
COPYING.txt       configure                     m4
INSTALL.txt       configure.ac                  missing
Makefile.am       depcomp                       protobuf-lite.pc.in
Makefile.in       editors                       protobuf.pc.in
README.txt        examples                      python
aclocal.m4        generate_descriptor_proto.sh  src
autogen.sh        gtest                         vsprojects
config.guess      install-sh
'''

./configure
#환경설정하기 
'''[root@dataserver protobuf-2.5.0]# ./configure
checking whether to enable maintainer-specific portions of Makefiles... yes
checking build system type... x86_64-unknown-linux-gnu
checking host system type... x86_64-unknown-linux-gnu
checking target system type... x86_64-unknown-linux-gnu
checking for a BSD-compatible install... /usr/bin/install -c
checking whether build environment is sane... yes
checking for a thread-safe mkdir -p... /usr/bin/mkdir -p
checking for gawk... gawk
checking whether make sets $(MAKE)... yes
checking for gcc... gcc
checking whether the C compiler works... yes
checking for C compiler default output file name... a.out
checking for suffix of executables... 
checking whether we are cross compiling... no
checking for suffix of object files... o
checking whether we are using the GNU C compiler... yes
checking whether gcc accepts -g... yes
checking for gcc option to accept ISO C89... none needed
checking for style of include used by make... GNU
checking dependency style of gcc... gcc3
checking for g++... g++
checking whether we are using the GNU C++ compiler... yes
checking whether g++ accepts -g... yes
checking dependency style of g++... gcc3
checking how to run the C++ preprocessor... g++ -E
checking for grep that handles long lines and -e... /usr/bin/grep
checking for egrep... /usr/bin/grep -E
checking for ANSI C header files... yes
checking for sys/types.h... yes
checking for sys/stat.h... yes
checking for stdlib.h... yes
checking for string.h... yes
checking for memory.h... yes
checking for strings.h... yes
checking for inttypes.h... yes
checking for stdint.h... yes
checking for unistd.h... yes
checking minix/config.h usability... no
checking minix/config.h presence... no
checking for minix/config.h... no
checking whether it is safe to define __EXTENSIONS__... yes
checking C++ compiler flags...... use default: -O2  -g -DNDEBUG
checking whether __SUNPRO_CC is declared... no
checking how to print strings... printf
checking for a sed that does not truncate output... /usr/bin/sed
checking for fgrep... /usr/bin/grep -F
checking for ld used by gcc... /usr/bin/ld
checking if the linker (/usr/bin/ld) is GNU ld... yes
checking for BSD- or MS-compatible name lister (nm)... /usr/bin/nm -B
checking the name lister (/usr/bin/nm -B) interface... BSD nm
checking whether ln -s works... yes
checking the maximum length of command line arguments... 1572864
checking whether the shell understands some XSI constructs... yes
checking whether the shell understands "+="... yes
checking how to convert x86_64-unknown-linux-gnu file names to x86_64-unknown-linux-gnu format... func_convert_file_noop
checking how to convert x86_64-unknown-linux-gnu file names to toolchain format... func_convert_file_noop
checking for /usr/bin/ld option to reload object files... -r
checking for objdump... objdump
checking how to recognize dependent libraries... pass_all
checking for dlltool... no
checking how to associate runtime and link libraries... printf %s\n
checking for ar... ar
checking for archiver @FILE support... @
checking for strip... strip
checking for ranlib... ranlib
checking command to parse /usr/bin/nm -B output from gcc object... ok
checking for sysroot... no
checking for mt... no
checking if : is a manifest tool... no
checking for dlfcn.h... yes
checking for objdir... .libs
checking if gcc supports -fno-rtti -fno-exceptions... no
checking for gcc option to produce PIC... -fPIC -DPIC
checking if gcc PIC flag -fPIC -DPIC works... yes
checking if gcc static flag -static works... no
checking if gcc supports -c -o file.o... yes
checking if gcc supports -c -o file.o... (cached) yes
checking whether the gcc linker (/usr/bin/ld -m elf_x86_64) supports shared libraries... yes
checking whether -lc should be explicitly linked in... no
checking dynamic linker characteristics... GNU/Linux ld.so
checking how to hardcode library paths into programs... immediate
checking whether stripping libraries is possible... yes
checking if libtool supports shared libraries... yes
checking whether to build shared libraries... yes
checking whether to build static libraries... yes
checking how to run the C++ preprocessor... g++ -E
checking for ld used by g++... /usr/bin/ld -m elf_x86_64
checking if the linker (/usr/bin/ld -m elf_x86_64) is GNU ld... yes
checking whether the g++ linker (/usr/bin/ld -m elf_x86_64) supports shared libraries... yes
checking for g++ option to produce PIC... -fPIC -DPIC
checking if g++ PIC flag -fPIC -DPIC works... yes
checking if g++ static flag -static works... no
checking if g++ supports -c -o file.o... yes
checking if g++ supports -c -o file.o... (cached) yes
checking whether the g++ linker (/usr/bin/ld -m elf_x86_64) supports shared libraries... yes
checking dynamic linker characteristics... (cached) GNU/Linux ld.so
checking how to hardcode library paths into programs... immediate
checking for ANSI C header files... (cached) yes
checking fcntl.h usability... yes
checking fcntl.h presence... yes
checking for fcntl.h... yes
checking for inttypes.h... (cached) yes
checking limits.h usability... yes
checking limits.h presence... yes
checking for limits.h... yes
checking for stdlib.h... (cached) yes
checking for unistd.h... (cached) yes
checking for working memcmp... yes
checking for working strtod... yes
checking for ftruncate... yes
checking for memset... yes
checking for mkdir... yes
checking for strchr... yes
checking for strerror... yes
checking for strtol... yes
checking zlib version... headers missing or too old (requires 1.2.0.4)
checking for the pthreads library -lpthreads... no
checking whether pthreads work without any flags... no
checking whether pthreads work with -Kthread... no
checking whether pthreads work with -kthread... no
checking for the pthreads library -llthread... no
checking whether pthreads work with -pthread... yes
checking for joinable pthread attribute... PTHREAD_CREATE_JOINABLE
checking if more special flags are required for pthreads... no
checking whether to check for GCC pthread/shared inconsistencies... yes
checking whether -pthread is sufficient with -shared... yes
checking whether what we have so far is sufficient with -nostdlib... no
checking whether -lpthread saves the day... yes
checking the location of hash_map... <tr1/unordered_map>
configure: creating ./config.status
config.status: creating Makefile
config.status: creating src/Makefile
config.status: creating protobuf.pc
config.status: creating protobuf-lite.pc
config.status: creating config.h
config.status: executing depfiles commands
config.status: executing libtool commands
=== configuring in gtest (/usr/local/protobuf-2.5.0/gtest)
configure: running /bin/sh ./configure --disable-option-checking '--prefix=/usr/local'  --cache-file=/dev/null --srcdir=.
checking for a BSD-compatible install... /usr/bin/install -c
checking whether build environment is sane... yes
checking for a thread-safe mkdir -p... /usr/bin/mkdir -p
checking for gawk... gawk
checking whether make sets $(MAKE)... yes
checking for gcc... gcc
checking whether the C compiler works... yes
checking for C compiler default output file name... a.out
checking for suffix of executables... 
checking whether we are cross compiling... no
checking for suffix of object files... o
checking whether we are using the GNU C compiler... yes
checking whether gcc accepts -g... yes
checking for gcc option to accept ISO C89... none needed
checking for style of include used by make... GNU
checking dependency style of gcc... gcc3
checking for g++... g++
checking whether we are using the GNU C++ compiler... yes
checking whether g++ accepts -g... yes
checking dependency style of g++... gcc3
checking build system type... x86_64-unknown-linux-gnu
checking host system type... x86_64-unknown-linux-gnu
checking how to print strings... printf
checking for a sed that does not truncate output... /usr/bin/sed
checking for grep that handles long lines and -e... /usr/bin/grep
checking for egrep... /usr/bin/grep -E
checking for fgrep... /usr/bin/grep -F
checking for ld used by gcc... /usr/bin/ld
checking if the linker (/usr/bin/ld) is GNU ld... yes
checking for BSD- or MS-compatible name lister (nm)... /usr/bin/nm -B
checking the name lister (/usr/bin/nm -B) interface... BSD nm
checking whether ln -s works... yes
checking the maximum length of command line arguments... 1572864
checking whether the shell understands some XSI constructs... yes
checking whether the shell understands "+="... yes
checking how to convert x86_64-unknown-linux-gnu file names to x86_64-unknown-linux-gnu format... func_convert_file_noop
checking how to convert x86_64-unknown-linux-gnu file names to toolchain format... func_convert_file_noop
checking for /usr/bin/ld option to reload object files... -r
checking for objdump... objdump
checking how to recognize dependent libraries... pass_all
checking for dlltool... no
checking how to associate runtime and link libraries... printf %s\n
checking for ar... ar
checking for archiver @FILE support... @
checking for strip... strip
checking for ranlib... ranlib
checking command to parse /usr/bin/nm -B output from gcc object... ok
checking for sysroot... no
checking for mt... no
checking if : is a manifest tool... no
checking how to run the C preprocessor... gcc -E
checking for ANSI C header files... yes
checking for sys/types.h... yes
checking for sys/stat.h... yes
checking for stdlib.h... yes
checking for string.h... yes
checking for memory.h... yes
checking for strings.h... yes
checking for inttypes.h... yes
checking for stdint.h... yes
checking for unistd.h... yes
checking for dlfcn.h... yes
checking for objdir... .libs
checking if gcc supports -fno-rtti -fno-exceptions... no
checking for gcc option to produce PIC... -fPIC -DPIC
checking if gcc PIC flag -fPIC -DPIC works... yes
checking if gcc static flag -static works... no
checking if gcc supports -c -o file.o... yes
checking if gcc supports -c -o file.o... (cached) yes
checking whether the gcc linker (/usr/bin/ld -m elf_x86_64) supports shared libraries... yes
checking whether -lc should be explicitly linked in... no
checking dynamic linker characteristics... GNU/Linux ld.so
checking how to hardcode library paths into programs... immediate
checking whether stripping libraries is possible... yes
checking if libtool supports shared libraries... yes
checking whether to build shared libraries... yes
checking whether to build static libraries... yes
checking how to run the C++ preprocessor... g++ -E
checking for ld used by g++... /usr/bin/ld -m elf_x86_64
checking if the linker (/usr/bin/ld -m elf_x86_64) is GNU ld... yes
checking whether the g++ linker (/usr/bin/ld -m elf_x86_64) supports shared libraries... yes
checking for g++ option to produce PIC... -fPIC -DPIC
checking if g++ PIC flag -fPIC -DPIC works... yes
checking if g++ static flag -static works... no
checking if g++ supports -c -o file.o... yes
checking if g++ supports -c -o file.o... (cached) yes
checking whether the g++ linker (/usr/bin/ld -m elf_x86_64) supports shared libraries... yes
checking dynamic linker characteristics... (cached) GNU/Linux ld.so
checking how to hardcode library paths into programs... immediate
checking for python... /usr/bin/python
checking for the pthreads library -lpthreads... no
checking whether pthreads work without any flags... no
checking whether pthreads work with -Kthread... no
checking whether pthreads work with -kthread... no
checking for the pthreads library -llthread... no
checking whether pthreads work with -pthread... yes
checking for joinable pthread attribute... PTHREAD_CREATE_JOINABLE
checking if more special flags are required for pthreads... no
checking whether to check for GCC pthread/shared inconsistencies... yes
checking whether -pthread is sufficient with -shared... yes
configure: creating ./config.status
config.status: creating Makefile
config.status: creating scripts/gtest-config
config.status: creating build-aux/config.h
config.status: executing depfiles commands
config.status: executing libtool commands
'''

make
make install
#설치완료 

protoc --version
#protocol 정보확인
'''[root@dataserver protobuf-2.5.0]# protoc --version
libprotoc 2.5.0
'''

# =============================================================================
# hadoop 계정 만들기 
# =============================================================================
# root계정에서는 oracle software를 (응용프로그램) 설치할 수 없다. 
# 따라서 hadoop이라는 계정을 만들어서 사용할 수 있도록 해줘야 한다. 

cat /etc/passwd
#현재 os에 만들어진 user들을 다 확인할 수 있다.
'''[root@dataserver protobuf-2.5.0]# cat /etc/passwd
root:x:0:0:root:/root:/bin/bash
bin:x:1:1:bin:/bin:/sbin/nologin
daemon:x:2:2:daemon:/sbin:/sbin/nologin
adm:x:3:4:adm:/var/adm:/sbin/nologin
lp:x:4:7:lp:/var/spool/lpd:/sbin/nologin
sync:x:5:0:sync:/sbin:/bin/sync
shutdown:x:6:0:shutdown:/sbin:/sbin/shutdown
halt:x:7:0:halt:/sbin:/sbin/halt
mail:x:8:12:mail:/var/spool/mail:/sbin/nologin
operator:x:11:0:operator:/root:/sbin/nologin
games:x:12:100:games:/usr/games:/sbin/nologin
ftp:x:14:50:FTP User:/var/ftp:/sbin/nologin
nobody:x:99:99:Nobody:/:/sbin/nologin
systemd-bus-proxy:x:999:997:systemd Bus Proxy:/:/sbin/nologin
systemd-network:x:192:192:systemd Network Management:/:/sbin/nologin
dbus:x:81:81:System message bus:/:/sbin/nologin
polkitd:x:998:996:User for polkitd:/:/sbin/nologin
abrt:x:173:173::/etc/abrt:/sbin/nologin
unbound:x:997:994:Unbound DNS resolver:/etc/unbound:/sbin/nologin
tss:x:59:59:Account used by the trousers package to sandbox the tcsd daemon:/dev/null:/sbin/nologin
libstoragemgmt:x:996:993:daemon account for libstoragemgmt:/var/run/lsm:/sbin/nologin
rpc:x:32:32:Rpcbind Daemon:/var/lib/rpcbind:/sbin/nologin
colord:x:995:992:User for colord:/var/lib/colord:/sbin/nologin
usbmuxd:x:113:113:usbmuxd user:/:/sbin/nologin
saslauth:x:994:76:Saslauthd user:/run/saslauthd:/sbin/nologin
geoclue:x:993:991:User for geoclue:/var/lib/geoclue:/sbin/nologin
setroubleshoot:x:992:989::/var/lib/setroubleshoot:/sbin/nologin
rtkit:x:172:172:RealtimeKit:/proc:/sbin/nologin
qemu:x:107:107:qemu user:/:/sbin/nologin
radvd:x:75:75:radvd user:/:/sbin/nologin
chrony:x:991:988::/var/lib/chrony:/sbin/nologin
ntp:x:38:38::/etc/ntp:/sbin/nologin
sssd:x:990:987:User for sssd:/:/sbin/nologin
rpcuser:x:29:29:RPC Service User:/var/lib/nfs:/sbin/nologin
nfsnobody:x:65534:65534:Anonymous NFS User:/var/lib/nfs:/sbin/nologin
pulse:x:171:171:PulseAudio System Daemon:/var/run/pulse:/sbin/nologin
gdm:x:42:42::/var/lib/gdm:/sbin/nologin
gnome-initial-setup:x:989:984::/run/gnome-initial-setup/:/sbin/nologin
avahi:x:70:70:Avahi mDNS/DNS-SD Stack:/var/run/avahi-daemon:/sbin/nologin
postfix:x:89:89::/var/spool/postfix:/sbin/nologin
sshd:x:74:74:Privilege-separated SSH:/var/empty/sshd:/sbin/nologin
tcpdump:x:72:72::/:/sbin/nologin
centos:x:1000:1000:centos:/home/centos:/bin/bash
vboxadd:x:988:1::/var/run/vboxadd:/bin/false
'''

head -1 /etc/passwd
# 제일 위에것 한개만 보인다.
'''[root@dataserver protobuf-2.5.0]# head -1 /etc/passwd
root:x:0:0:root:/root:/bin/bash
'''
#root:x:0:0:root:/root:/bin/bash
사용자이름:암호:사용자id:사용자가소속된그롭id:전체이름:홈디렉토리/기본쉘
    #root: 사용자 이름
    #x: 암호(안보여주고 있음)
    #0:사용자 ID (고유한 번호로 만들어줌)
    #0:사용자가 소속된 그룹의 ID
    #root: 전체이름
    #/root: 홈디렉토리 
    #/bin/bas: 기본쉘


tail -2 /etc/passwd
# 제일 밑에 것 두개만 보인다.
'''[root@dataserver protobuf-2.5.0]# tail -2 /etc/passwd
centos:x:1000:1000:centos:/home/centos:/bin/bash
vboxadd:x:988:1::/var/run/vboxadd:/bin/false
'''

useradd(adduser)
#유저생성
useradd user10
tail -2 /etc/passwd
#확인하기
'''[root@dataserver protobuf-2.5.0]# tail -2 /etc/passwd
vboxadd:x:988:1::/var/run/vboxadd:/bin/false
user10:x:1001:1001::/home/user10:/bin/bash
'''

userdel 
#사용자 삭제
userdel -r user10
tail -2 /etc/passwd
#확인하기 
'''[root@dataserver protobuf-2.5.0]# tail -2 /etc/passwd
centos:x:1000:1000:centos:/home/centos:/bin/bash
vboxadd:x:988:1::/var/run/vboxadd:/bin/false
''''


groupadd hadoop
#그룹 생성

cat /etc/group
#그룹 생성 확인하기
'''[root@dataserver protobuf-2.5.0]# cat /etc/group
root:x:0:
bin:x:1:
daemon:x:2:
sys:x:3:
adm:x:4:
tty:x:5:
disk:x:6:
lp:x:7:
mem:x:8:
kmem:x:9:
wheel:x:10:
cdrom:x:11:
mail:x:12:postfix
man:x:15:
dialout:x:18:
floppy:x:19:
games:x:20:
tape:x:30:
video:x:39:
ftp:x:50:
lock:x:54:
audio:x:63:
nobody:x:99:
users:x:100:
stapusr:x:156:
stapsys:x:157:
stapdev:x:158:
utmp:x:22:
utempter:x:35:
ssh_keys:x:999:
input:x:998:
systemd-journal:x:190:
systemd-bus-proxy:x:997:
systemd-network:x:192:
dbus:x:81:
polkitd:x:996:
cgred:x:995:
abrt:x:173:
unbound:x:994:
tss:x:59:
libstoragemgmt:x:993:
rpc:x:32:
colord:x:992:
dip:x:40:
usbmuxd:x:113:
saslauth:x:76:
geoclue:x:991:
libvirt:x:990:
setroubleshoot:x:989:
rtkit:x:172:
kvm:x:36:qemu
qemu:x:107:
radvd:x:75:
chrony:x:988:
ntp:x:38:
sssd:x:987:
rpcuser:x:29:
nfsnobody:x:65534:
pulse-access:x:986:
pulse-rt:x:985:
pulse:x:171:
gdm:x:42:
gnome-initial-setup:x:984:
avahi:x:70:
slocate:x:21:
postdrop:x:90:
postfix:x:89:
sshd:x:74:
tcpdump:x:72:
centos:x:1000:centos
vboxsf:x:983:
hadoop:x:1001:
'''

groupdel hadoop
# 그룹삭제

#다시 그룹 생성
groupadd hadoop
#하둡그룹 만들기 

# 유저생성
useradd -g hadoop -G vboxsf -m hadoop
'''[root@dataserver protobuf-2.5.0]# useradd -g hadoop -G vboxsf -m hadoop
'''
# 꼭 os그룹을 만들어놓고 user를 만들어 줘야 한다.
# -g hadoop : 1차그룹 (os 그룹)
# -G vboxsf : 2차 그룹 (공유폴더를 사용할 있도록 받아얗나다.; 이것은 virtual box에서만 사용가능하다.-공유폴더를 사용하게 해주는 os그룹)
# -m hadoop: hadoop이라는 이름으로 기본디렉토리를 생성 
    # -m :기본디렉토리를 만들기(home directory)
    # hadoop: 유저이름 

root만 공유폴더를 쓰는 것이 아니라 hadoop계정도 공유폴더를 사용할 수 있도록 
게스트 확장 이미지 삽입을 마운트 할 시 vboxsf


tail -1 /etc/passwd
# 유저 생성하기 확인 
'''[root@dataserver protobuf-2.5.0]# tail -1 /etc/passwd
hadoop:x:1001:1001::/home/hadoop:/bin/bash
'''

passwd hadoop
#password 생성
#비밀번호 설정 
# 예시) hadoop이라고 저장하기
'''[root@dataserver protobuf-2.5.0]# passwd hadoop
hadoop 사용자의 비밀 번호 변경 중
새  암호:
잘못된 암호: 암호는 8 개의 문자 보다 짧습니다
새  암호 재입력:
passwd: 모든 인증 토큰이 성공적으로 업데이트 되었습니다.
'''

# 로그인 정보에서 사용자바꾸기 
hadoop
centos 

# hadoop으로 로그인하기

# 공유폴더가 보임: 그 이유는 os로 공유폴더를 받았기 때문 
 
# 터미널 창 띄우기

pwd
'''[hadoop@dataserver ~]$ pwd
/home/hadoop
'''
#cf. -m : home을 만들어 줌 


cd /media/sf_centos/
ls hadoop*
'''[hadoop@dataserver ~]$ cd /media/sf_centos/
[hadoop@dataserver sf_centos]$ ls hadoop*
hadoop-2.7.2.tar.gz'''

cp hadoop-2.7.2.tar.gz /home/hadoop
# home디렉토리에 hadoop-2.7.2 파일을 복사하기 
[hadoop@dataserver sf_centos]$ cp hadoop-2.7.2.tar.gz /home/hadoop

cd
ls
#확인하기 
'''[hadoop@dataserver sf_centos]$ cd
[hadoop@dataserver ~]$ ls
hadoop-2.7.2.tar.gz  공개  다운로드  문서  바탕화면  비디오  사진  서식  음악
'''

tar xvfz hadoop-2.7.2.tar.gz 
# 압축풀기
'''[hadoop@dataserver ~]$ tar xvfz hadoop-2.7.2.tar.gz 
'''

ls
'''[hadoop@dataserver ~]$ ls
hadoop-2.7.2         공개      문서      비디오  서식
hadoop-2.7.2.tar.gz  다운로드  바탕화면  사진    음악
'''

vi .bashrc
#환경설정하기
#마지막 줄에 insert하기
'''[hadoop@dataserver ~]$ vi .bashrc
'''

export JAVA_HOME=/usr/jdk1.7.0_80
export HADOOP_HOME=/home/hadoop/hadoop-2.7.2
export PATH=$JAVA_HOME/bin:$HADOOP_HOME/bin:$HADOOP_HOME/sbin:$PATH
#어느 위치에든 사용하도록 하는 부분 path

esc + : + wq
#save하고 나오기

source .bashrc
#적용하기 
'''[hadoop@dataserver ~]$ source .bashrc
'''

java -version
#자바버전 확인하기
'''[hadoop@dataserver ~]$ java -version
java version "1.7.0_80"
Java(TM) SE Runtime Environment (build 1.7.0_80-b15)
Java HotSpot(TM) 64-Bit Server VM (build 24.80-b11, mixed mode)
'''

# =============================================================================
# SHH설정
# =============================================================================
SHH설정
- 공개키는 사용자 계정의 홈디렉토리에 있는 .ssh폴더에 생성된다. 

rm -rf .ssh
#공개키 삭제 (이전것이 있으면 삭제하기)
'''[hadoop@dataserver ~]$ rm -rf .ssh
'''

ssh-keygen
#공개키 생성
'''[hadoop@dataserver ~]$ ssh-keygen
Generating public/private rsa key pair.
Enter file in which to save the key (/home/hadoop/.ssh/id_rsa): 
'''
enter 

enter 

enter 
'''[hadoop@dataserver ~]$ ssh-keygen
Generating public/private rsa key pair.
Enter file in which to save the key (/home/hadoop/.ssh/id_rsa): 
Created directory '/home/hadoop/.ssh'.
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in /home/hadoop/.ssh/id_rsa.
Your public key has been saved in /home/hadoop/.ssh/id_rsa.pub.
The key fingerprint is:
69:75:01:25:95:7d:e0:1d:1f:82:a8:54:a8:df:db:11 hadoop@dataserver
The key's randomart image is:
+--[ RSA 2048]----+
|        o.++=+.+ |
|       o . o.oo.=|
|      o . . . ..o|
|     . . o E     |
|      . S   .    |
|       o . .     |
|          o .    |
|         . .     |
|                 |
+-----------------+
'''
# enter 3번 치면 공개키가 만들어진다. 

ssh-copy-id -i /home/hadoop/.ssh/id_rsa.pub hadoop@192.168.56.101 
#101은 아까 설정했던 수로 맞춘다.
#혹시 잊어먹었으면 ifconfig로 확인 
    #enp0s8: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
    #        inㅛㄷㄴt 192.168.56.101  netmask 255.255.255.0  broadcast 192.168.56.255
    #        inet6 fe80::3e8a:bb22:829a:f702  prefixlen 64  scopeid 0x20<link>
    #        ether 08:00:27:3f:4f:80  txqueuelen 1000  (Ethernet)
    #        RX packets 193  bytes 33632 (32.8 KiB)
    #        RX errors 0  dropped 0  overruns 0  frame 0
    #        TX packets 94  bytes 17715 (17.2 KiB)
    #        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0


'''[hadoop@dataserver ~]$ ssh-copy-id -i /home/hadoop/.ssh/id_rsa.pub hadoop@192.168.56.101
The authenticity of host '192.168.56.101 (192.168.56.101)' can't be established.
ECDSA key fingerprint is 88:18:12:3d:03:4b:f9:c1:0d:de:6c:4e:47:23:fb:34.
Are you sure you want to continue connecting (yes/no)? yes
'''
yes
'''/usr/bin/ssh-copy-id: INFO: attempting to log in with the new key(s), to filter out any that are already installed
/usr/bin/ssh-copy-id: INFO: 1 key(s) remain to be installed -- if you are prompted now it is to install the new keys
hadoop@192.168.56.101's password: 
'''
hadoop
'''Number of key(s) added: 1

Now try logging into the machine, with:   "ssh 'hadoop@192.168.56.101'"
and check to make sure that only the key(s) you wanted were added.
'''

ssh hadoop@192.168.56.101
#한번 설정해놓고 나면 다시는 물어보지 않는다. 
'''[hadoop@dataserver ~]$ ssh hadoop@192.168.56.101
Last login: Tue Nov 20 14:56:13 2018
'''

# 안되면 공개키 디렉토리를 삭제하고 다시 생성하고 다시 카피하고 테스트 하면 된다. (다시 앞으로 가서...)


# =============================================================================
# 환경구성하기
# =============================================================================

cd /home/hadoop/hadoop-2.7.2/etc/hadoop
'''[hadoop@dataserver ~]$ cd /home/hadoop/hadoop-2.7.2/etc/hadoop
'''
#============================
vi hadoop-env.sh
#환경구성하는 파일 
'''[hadoop@dataserver hadoop]$ vi hadoop-env.sh
'''

# The java implementation to use.
# export JAVA_HOME=${JAVA_HOME} 를 수정하기

export JAVA_HOME=/usr/jdk.1.7.0_80


# The directory where pid files are stored. /tmp by default.
# NOTE: this should be set to a directory that can only be written to by 
#       the user that will run the hadoop daemons.  Otherwise there is the
#       potential for a symlink attack.

# export HADOOP_PID_DIR=${HADOOP_PID_DIR} 를 

export HADOOP_PID_DIR=/home/hadoop/hadoop-2.7.2/pids 

로 수정

esc + : + wq
#저장하고 나오기

#============================
vi masters
'''[hadoop@dataserver hadoop]$ vi masters
'''
192.168.56.101
#enp0s8 주소값만 입력하기

esc + : + wq
#저장하고 나오기

#============================
vi slaves
'''[hadoop@dataserver hadoop]$ vi slaves
'''
192.168.56.101
#local host를 지우고 ip주소를 입력하기

esc + : + wq
#저장하고 나오기

# =============================================================================
# 하둡환결설정 txt따라하기 #cf. 절대경로는 타이핑하지 않는다. 한번 제대로 만들어 놓고 복사해서 사용한다.
# =============================================================================

cd /home/hadoop/hadoop-2.7.2/etc/hadoop

[hadoop@dataserver hadoop]$ vi hadoop-env.sh
export JAVA_HOME=/usr/jdk1.7.0_80
export HADOOP_PID_DIR=/home/hadoop/hadoop-2.7.2/pids

[hadoop@dataserver hadoop]$ vi masters
192.168.56.110
[hadoop@dataserver hadoop]$ vi slaves
192.168.56.110

[hadoop@dataserver hadoop]$ vi core-site.xml 

<configuration>
 <property>
  <name>fs.defaultFS</name>
  <value>hdfs://dataserver:9010</value> #호스트 이름(서버이름)
 </property>
</configuration>


[hadoop@dataserver hadoop]$ vi hdfs-site.xml 

<configuration>
 <property>
  <name>dfs.replication</name>
  <value>1</value>
 </property>
 <property>
  <name>dfs.namenode.name.dir</name>
  <value>/home/hadoop/data/dfs/namenode</value>
 </property>
 <property>
  <name>dfs.namenode.checkpoint.dir</name>
  <value>/home/hadoop/data/dfs/namesecondary</value>
 </property>
 <property>
  <name>dfs.datanode.data.dir</name>
  <value>/home/hadoop/data/dfs/datanode</value>
 </property>
 <property>
  <name>dfs.http.address</name>
  <value>dataserver:50070</value>
 </property>
 <property>
  <name>dfs.secondary.http.address</name>
  <value>dataserver:50090</value>
 </property>
</configuration>


[hadoop@dataserver hadoop]$ cp mapred-site.xml.template mapred-site.xml
[hadoop@dataserver hadoop]$ vi mapred-site.xml

<configuration>
 <property>
  <name>mapreduce.framework.name</name>
  <value>yarn</value>
 </property>
</configuration>

[hadoop@dataserver hadoop]$ vi yarn-site.xml 

<configuration>
 <property>
  <name>yarn.nodemanager.aux-services</name>
  <value>mapreduce_shuffle</value>
 </property>
 <property>
  <name>yarn.nodemanager.aux-services.mapreduce_suffle.class</name>
  <value>org.apache.hadoop.mapred.ShuffleHandler</value>
 </property>
 <property>
  <name>yarn.nodemanager.local-dirs</name>
  <value>/home/hadoop/data/yarn/nm-local-dir</value>
 </property>
 <property>
  <name>yarn.resourcemanager.fs.state-store.uri</name>
  <value>/home/hadoop/data/yarn/system/rmstore</value>
 </property>
 <property>
  <name>yarn.resourcemanager.hostname</name>
  <value>dataserver</value>
 </property>
 <property>
  <name>yarn.web-proxy.address</name>
  <value>0.0.0.0:8089</value>
 </property>
</configuration>



# =============================================================================
# 
# =============================================================================
cd

hdfs namenode -format
#hdfs namenode - format 처음 설치할때만 
# 나중에도 -format하게 되면 내용이 다 날아가버린다. 
'''	at org.apache.hadoop.conf.Configuration.loadResources(Configuration.java:2492)
	at org.apache.hadoop.conf.Configuration.getProps(Configuration.java:2405)
	at org.apache.hadoop.conf.Configuration.set(Configuration.java:1143)
	at org.apache.hadoop.conf.Configuration.set(Configuration.java:1115)
	at org.apache.hadoop.hdfs.server.namenode.NameNode.setStartupOption(NameNode.java:1353)
	at org.apache.hadoop.hdfs.server.namenode.NameNode.createNameNode(NameNode.java:1425)
	at org.apache.hadoop.hdfs.server.namenode.NameNode.main(NameNode.java:1554)
18/11/20 16:25:05 ERROR namenode.NameNode: Failed to start namenode.
java.lang.RuntimeException: org.xml.sax.SAXParseException; systemId: file:/home/hadoop/hadoop-2.7.2/etc/hadoop/core-site.xml; lineNumber: 26; columnNumber: 3; The markup in the document following the root element must be well-formed.
	at org.apache.hadoop.conf.Configuration.loadResource(Configuration.java:2645)
	at org.apache.hadoop.conf.Configuration.loadResources(Configuration.java:2492)
	at org.apache.hadoop.conf.Configuration.getProps(Configuration.java:2405)
	at org.apache.hadoop.conf.Configuration.set(Configuration.java:1143)
	at org.apache.hadoop.conf.Configuration.set(Configuration.java:1115)
	at org.apache.hadoop.hdfs.server.namenode.NameNode.setStartupOption(NameNode.java:1353)
	at org.apache.hadoop.hdfs.server.namenode.NameNode.createNameNode(NameNode.java:1425)
	at org.apache.hadoop.hdfs.server.namenode.NameNode.main(NameNode.java:1554)
Caused by: org.xml.sax.SAXParseException; systemId: file:/home/hadoop/hadoop-2.7.2/etc/hadoop/core-site.xml; lineNumber: 26; columnNumber: 3; The markup in the document following the root element must be well-formed.
	at org.apache.xerces.parsers.DOMParser.parse(Unknown Source)
	at org.apache.xerces.jaxp.DocumentBuilderImpl.parse(Unknown Source)
	at javax.xml.parsers.DocumentBuilder.parse(DocumentBuilder.java:150)
	at org.apache.hadoop.conf.Configuration.parse(Configuration.java:2480)
	at org.apache.hadoop.conf.Configuration.parse(Configuration.java:2468)
	at org.apache.hadoop.conf.Configuration.loadResource(Configuration.java:2539)
	... 7 more
18/11/20 16:25:05 INFO util.ExitUtil: Exiting with status 1
18/11/20 16:25:05 INFO namenode.NameNode: SHUTDOWN_MSG: 
/************************************************************
SHUTDOWN_MSG: Shutting down NameNode at dataserver/192.168.56.101
************************************************************/
'''
#이렇게 되면 일단 끝
#하드 디스크 설정 끝

# =============================================================================
#  데몬실행하기 
# =============================================================================

start-dfs.sh
'''[hadoop@dataserver ~]$ start-dfs.sh
Starting namenodes on [dataserver]
The authenticity of host 'dataserver (192.168.56.101)' can't be established.
ECDSA key fingerprint is 88:18:12:3d:03:4b:f9:c1:0d:de:6c:4e:47:23:fb:34.
Are you sure you want to continue connecting (yes/no)? 
'''
yes 

# =============================================================================
# 데몬들을 다 띄우기 (시스템 전원을 껐을 때 데몬들을 다시 다 띄워야 한다.)
# =============================================================================
start-yarn.sh
'''[hadoop@dataserver ~]$ start-dfs.sh
Starting namenodes on [dataserver]
The authenticity of host 'dataserver (192.168.56.101)' can't be established.
ECDSA key fingerprint is 88:18:12:3d:03:4b:f9:c1:0d:de:6c:4e:47:23:fb:34.
Are you sure you want to continue connecting (yes/no)? yes
dataserver: Warning: Permanently added 'dataserver' (ECDSA) to the list of known hosts.
dataserver: starting namenode, logging to /home/hadoop/hadoop-2.7.2/logs/hadoop-hadoop-namenode-dataserver.out
192.168.56.101: starting datanode, logging to /home/hadoop/hadoop-2.7.2/logs/hadoop-hadoop-datanode-dataserver.out
Starting secondary namenodes [dataserver]
dataserver: starting secondarynamenode, logging to /home/hadoop/hadoop-2.7.2/logs/hadoop-hadoop-secondarynamenode-dataserver.out
[hadoop@dataserver ~]$ start-yarn.sh
starting yarn daemons
starting resourcemanager, logging to /home/hadoop/hadoop-2.7.2/logs/yarn-hadoop-resourcemanager-dataserver.out
m192.168.56.101: starting nodemanager, logging to /home/hadoop/hadoop-2.7.2/logs/yarn-hadoop-nodemanager-dataserver.out
'''

mr-jobhistory-daemon.sh start historyserver
'''[hadoop@dataserver ~]$ mr-jobhistory-daemon.sh start historyserver
starting historyserver, logging to /homㅓ네e/hadoop/hadoop-2.7.2/logs/mapred-hadoop-historyserver-dataserver.out
'''

yarn-daemon.sh start proxyserver 
'''[hadoop@dataserver ~]$ yarn-daemon.sh start proxyserver
starting proxyserver, logging to /home/hadoop/hadoop-2.7.2/logs/yarn-hadoop-proxyserver-dataserver.out
'''

jps
'''[hadoop@dataserver ~]$ jps
20371 JobHistoryServer
20502 Jps
19438 NameNode
20056 NodeManager
19581 DataNode
20433 WebAppProxyServer
19913 ResourceManager
19751 SecondaryNameNode
'''




#데몬 종료하기
stop-yarn.sh
stop-dfs.sh
mr-jobhistory-daemon.sh stop historyserver


# =============================================================================
# 만약 하둡유저가 잘못됐다면... (user 지우기/ 지웠는데 유저가 활성화 되어있다고 하면 로그아웃하고 나와서 root에서부터 시작한다.)
# =============================================================================
userdel 
#사용자 삭제
userdel -r hadoop

#그룹생성
groupadd hadoop
cat /etc/group



