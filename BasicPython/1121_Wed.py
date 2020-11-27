# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 11:27:25 2018

@author: stu
"""

data양이 더 많아질 경우 이를 해결하는 방법에는 두가지 방법이 있다. 

# way1: scale up
scale up : 더 큰 server를 구축하는 작업 (비용이 많이 지출됨)

# way2: (scale out) -> hadoop을 사용
분산환경 
- 이 문제를 해결하기 위해 똑같은 사양의 server를 구매한 뒤, 네트워크로 묶는다.  
    -> 이를 하나인 것처럼 돌린다. -> 분산환경 구축  (grid infrastructure)
- intel cpu, linux os를 사용
- 각각의 cpu를 돌릴 수 있도록 control함 : Hadoop사용

# =============================================================================
# 학원에서 test 내용 
# =============================================================================
# virtual box 하나를 가지고 test함 

# hadoop 구축된 것을 데이터를 긁어오는 것

# =============================================================================
# 
# =============================================================================

mr-jobhistory-daemon.sh stop historyserver

▣ big data
- 서버 한 대로 처리할 수 없는 규모의 데이터(2012 John rauser, Amazon 수석 엔진니어)
- 기존 소프트웨어로 처리할 수 없는 규모의 데이터 (1TB 이상/ 1PT이상의 데이터)
- scale up : 하드웨어 증성
- scale out : 비슷한 사양의 서버로 분산처리 

▣ 하둡 분산형 파일시스템 (HDFS: Hadoop Distributed File System)
- 하둡은 대용량 데이터를 분산처리할 수 있는 자바기반의 오픈소스 프레임워크이다. 

구글이 쌓여지는 수많은 빅데이터(웹페이지,데이터.. )들을 구글에서도 처음에는 RDBMS(Oracle)에 입력하고 데이터를 저장하고 처리하려고 시도를 했으나 
너무 데이터가 많아서 실패를 하고 자체적으로 빅데이터를 처리할 기술을 개발하고 대외적으로 논문을 발표했다. 

이 논물을 더그커팅(야후 재직)이 읽고 자바로 구현을 했다.

RDBMS -------------------------------------------------Hadoop
(Oracle)  
실시간 데이터 처리                                     배치처리(READ), 무료, 분산처리

RDBMS
장점
- 데이터의 품질이 좋음(db를 생성하고, table, columnsize, column의 제약조건을 넣기 때문에): 데이터의 무결성이 좋
- 실시간 데이터 처리(실시간으로 데이터를 읽고 쓸 수 있다.)

Hadoop
- 데이터의 무결성이 좋지않음
- 배치처리 (READ)  (실시간으로 데이터를 읽기만 가능하다. 즉, 데이터를 실시간적으로 수정할 수 없다. 수정하기 위해서는 파일을 열어 데이터를 수정해야 한다.)
- 무료
- 분산처리 

■ 분산처리 : 여러대의 노드를 묶어서 마치 하나의 서버처럼 보이게 하고 여러 노드의 자원을 이용해서 데이터를 처리하기 때문에 처리하는 속도가 빠르다. 
(Grid 개념)

■ 실례
2008년, 뉴욕타임즈의 130년 분량의 신문기사 1100만 페이지를 하둡을 이용해서 하루만에 PDF로 변환했고 비용은 200만원 밖에 안들었다. 하둡이 아닌 일반 서버로 처리했다면 14년이 걸린다. 

# =============================================================================
# hdfs 사용하기
# =============================================================================
 


#데몬 종료하기
stop-yarn.sh
'''[hadoop@dataserver mapreduce]$ stop-yarn.sh
stopping yarn daemons
stopping resourcemanager
192.168.56.101: stopping nodemanager
192.168.56.101: nodemanager did not stop gracefully after 5 seconds: killing with kill -9
stopping proxyserver'''

stop-dfs.sh
'''[hadoop@dataserver mapreduce]$ stop-dfs.sh
Stopping namenodes on [dataserver]
dataserver: no namenode to stop
192.168.56.101: stopping datanode
Stopping secondary namenodes [dataserver]
dataserver: stopping secondarynamenode
'''

#먼저 데몬을 실행시킨다.

# =============================================================================
# 
# =============================================================================

#jsp를 했을 때 namenode와 datanode가 뜨지 않을 경우 vi hdfs-site.xml 를 확인
#cf. 디렉토리는 datanode에 만들어진다.
vi hdfs-site.xml
#datanode와 namenode
#하둡데몬시작에서 namenode -format을 하는 순간 namenode를 실행할 수 있는 storage를 만들어야 하는데, 이를 수행하는 순간 home/hadoop/data/dfs/namenode 와 home/hadoop/data/dfs/datanode가 만들어진다. 

#잘 만들어졌는데도 불구하고 namenode와 datanode가 실행되지 않을 경우
rm -rf data
#물어보지 않고 data를 다 지움 
'''[hadoop@dataserver ~]$ rm -rf data
'''

hdfs namenode -format
ls
'''[hadoop@dataserver ~]$ ls
data          hadoop-2.7.2.tar.gz  다운로드  바탕화면  사진  음악
hadoop-2.7.2  공개                 문서      비디오    서식
'''

start-dfs.sh
'''[hadoop@dataserver ~]$ start-dfs.sh
Starting namenodes on [dataserver]
dataserver: starting namenode, logging to /home/hadoop/hadoop-2.7.2/logs/hadoop-hadoop-namenode-dataserver.out
192.168.56.101: starting datanode, logging to /home/hadoop/hadoop-2.7.2/logs/hadoop-hadoop-datanode-dataserver.out
Starting secondary namenodes [dataserver]
dataserver: starting secondarynamenode, logging to /home/hadoop/hadoop-2.7.2/logs/hadoop-hadoop-secondarynamenode-dataserver.out
'''


#yarn: 데이터를 관리하는 기능
'''[hadoop@dataserver ~]$ start-yarn.sh
starting yarn daemons
starting resourcemanager, logging to /home/hadoop/hadoop-2.7.2/logs/yarn-hadoop-resourcemanager-dataserver.out
192.168.56.101: starting nodemanager, logging to /home/hadoop/hadoop-2.7.2/logs/yarn-hadoop-nodemanager-dataserver.out
'''

mr-jobhistory-daemon.sh start historyserver
'''[hadoop@dataserver ~]$ mr-jobhistory-daemon.sh start historyserver
historyserver running as process 4340. Stop it first.
'''
yarn-daemon.sh start proxyserver 
# 종료시에는 stop-yarn.sh를 종료시 같이 종료됨
'''[hadoop@dataserver ~]$ yarn-daemon.sh start proxyserver 
starting proxyserver, logging to /home/hadoop/hadoop-2.7.2/logs/yarn-hadoop-proxyserver-dataserver.out
'''

jps
'''[hadoop@dataserver ~]$ jps
14454 Jps
13641 SecondaryNameNode
13985 NodeManager
13341 NameNode
13846 ResourceManager
14265 JobHistoryServer
14408 WebAppProxyServer
'''


# namenode, datanode 디렉토리 
# =============================================================================
# 
# =============================================================================


# =============================================================================
# hdfs 사용하기
# =============================================================================
 
jps
#Datanode: Namenode에 있는 정보를 Datanode를 통해 할당 
#Namenode: 각 데이터가 어느 서버에 할당되었는지에 대한 정보: 네임노드가 집어넣어야할 데이터를 조정함 (일부는 a 서버로, 일부는 b서버로 할당하는 내용을 저장함) 


hdfs dfs -ls /
'''[hadoop@dataserver ~]$ hdfs dfs -ls /
Found 1 items
drwxrwx---   - hadoop supergroup          0 2018-11-20 16:37 /tmp
'''

hdfs dfs -mkdir /user
# -mkdri :direcory 생성
'''[hadoop@dataserver ~]$ hdfs dfs -mkdir /user
'''

hdfs dfs -ls /
'''[hadoop@dataserver ~]$ hdfs dfs -ls /
Found 2 items
drwxrwx---   - hadoop supergroup          0 2018-11-20 16:37 /tmp
drwxr-xr-x   - hadoop supergroup          0 2018-11-21 14:37 /user
'''

# os 에서는 볼수 없고 하둡에서만 볼 수 있는 directory 
# user 하둡영역에서만 볼 수있는(관리할 수 있는) directory

ls
'''[hadoop@dataserver ~]$ ls
data          hadoop-2.7.2.tar.gz  다운로드  바탕화면  사진  음악
hadoop-2.7.2  공개                 문서      비디오    서식
'''

hdfs dfs -mkdir /user/hadoop
#user라는 directory 안에 hadoop라는 subdirectory 만들기
# cf. 꼭 subdirectory를 만들필요는 없다. test용으로 지금 하고 있습니다.
'''[hadoop@dataserver ~]$ hdfs dfs -mkdir /user/hadoop
'''

hdfs dfs -ls -R /
#-ls만 쓰면 home에 있는 디렉토리만 확인할 수 있다.
#R까지 쓰면 안에 있는 디렉토리도 확인할 수 있다.
'''[hadoop@dataserver ~]$ hdfs dfs -ls -R /
drwxrwx---   - hadoop supergroup          0 2018-11-20 16:37 /tmp
drwxrwx---   - hadoop supergroup          0 2018-11-20 16:37 /tmp/hadoop-yarn
drwxrwx---   - hadoop supergroup          0 2018-11-20 16:37 /tmp/hadoop-yarn/staging
drwxrwx---   - hadoop supergroup          0 2018-11-20 16:37 /tmp/hadoop-yarn/staging/history
drwxrwx---   - hadoop supergroup          0 2018-11-20 16:37 /tmp/hadoop-yarn/staging/history/done
drwxrwxrwt   - hadoop supergroup          0 2018-11-20 16:37 /tmp/hadoop-yarn/staging/history/done_intermediate
drwxr-xr-x   - hadoop supergroup          0 2018-11-21 14:41 /user
drwxr-xr-x   - hadoop supergroup          0 2018-11-21 14:42 /user/hadoop
drwxr-xr-x   - hadoop supergroup          0 2018-11-21 14:45 /user/hadoop/conf
-rw-r--r--   1 hadoop supergroup       4241 2018-11-21 14:45 /user/hadoop/conf/hadoop-env.sh
'''

hdfs dfs -mkdir /user/hadoop/conf
'''[hadoop@dataserver ~]$ hdfs dfs -mkdir /user/hadoop/conf
'''


hdfs dfs -put /home/hadoop/hadoop-2.7.2/etc/hadoop/hadoop-env.sh conf/
#os에 있는 특정한 data를 hadoop에 올리는 작업 (hdfs dfs -mkdir /user/hadoop/conf 이 디렉토리로 올리고 싶음)
#이때 os명령어를 쓰면 안된다. 하둡명령어를 써야 한다.
# -put: os(로컬)에 있는 파일을 하둡파일시스템에 올리는 명령어
# eg) os에 있는 hadoop-env.sh파일을 하둡이라는 directory에 put함 
'''[hadoop@dataserver ~]$ hdfs dfs -put /home/hadoop/hadoop-2.7.2/etc/hadoop/hadoop-env.sh conf/
'''
# 혹시 오류났으면 파일정보, 디렉토리 정보가 잘못된 경우다. 


hdfs dfs -ls conf/
#파일이 올려졌는지 확인하기
'''[hadoop@dataserver ~]$ hdfs dfs -ls conf/
Found 1 items
-rw-r--r--   1 hadoop supergroup       4241 2018-11-21 14:45 conf/hadoop-env.sh
'''

hdfs dfs -cat conf/hadoop-env.sh
'''[hadoop@dataserver ~]$ hdfs dfs -cat conf/hadoop-env.sh
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Set Hadoop-specific environment variables here.

# The only required environment variable is JAVA_HOME.  All others are
# optional.  When running a distributed configuration it is best to
# set JAVA_HOME in this file, so that it is correctly defined on
# remote nodes.

# The java implementation to use.
export JAVA_HOME=/usr/jdk1.7.0_80

# The jsvc implementation to use. Jsvc is required to run secure datanodes
# that bind to privileged ports to provide authentication of data transfer
# protocol.  Jsvc is not required if SASL is configured for authentication of
# data transfer protocol using non-privileged ports.
#export JSVC_HOME=${JSVC_HOME}

export HADOOP_CONF_DIR=${HADOOP_CONF_DIR:-"/etc/hadoop"}

# Extra Java CLASSPATH elements.  Automatically insert capacity-scheduler.
for f in $HADOOP_HOME/contrib/capacity-scheduler/*.jar; do
  if [ "$HADOOP_CLASSPATH" ]; then
    export HADOOP_CLASSPATH=$HADOOP_CLASSPATH:$f
  else
    export HADOOP_CLASSPATH=$f
  fi
done

# The maximum amount of heap to use, in MB. Default is 1000.
#export HADOOP_HEAPSIZE=
#export HADOOP_NAMENODE_INIT_HEAPSIZE=""

# Extra Java runtime options.  Empty by default.
export HADOOP_OPTS="$HADOOP_OPTS -Djava.net.preferIPv4Stack=true"

# Command specific options appended to HADOOP_OPTS when specified
export HADOOP_NAMENODE_OPTS="-Dhadoop.security.logger=${HADOOP_SECURITY_LOGGER:-INFO,RFAS} -Dhdfs.audit.logger=${HDFS_AUDIT_LOGGER:-INFO,NullAppender} $HADOOP_NAMENODE_OPTS"
export HADOOP_DATANODE_OPTS="-Dhadoop.security.logger=ERROR,RFAS $HADOOP_DATANODE_OPTS"

export HADOOP_SECONDARYNAMENODE_OPTS="-Dhadoop.security.logger=${HADOOP_SECURITY_LOGGER:-INFO,RFAS} -Dhdfs.audit.logger=${HDFS_AUDIT_LOGGER:-INFO,NullAppender} $HADOOP_SECONDARYNAMENODE_OPTS"

export HADOOP_NFS3_OPTS="$HADOOP_NFS3_OPTS"
export HADOOP_PORTMAP_OPTS="-Xmx512m $HADOOP_PORTMAP_OPTS"

# The following applies to multiple commands (fs, dfs, fsck, distcp etc)
export HADOOP_CLIENT_OPTS="-Xmx512m $HADOOP_CLIENT_OPTS"
#HADOOP_JAVA_PLATFORM_OPTS="-XX:-UsePerfData $HADOOP_JAVA_PLATFORM_OPTS"

# On secure datanodes, user to run the datanode as after dropping privileges.
# This **MUST** be uncommented to enable secure HDFS if using privileged ports
# to provide authentication of data transfer protocol.  This **MUST NOT** be
# defined if SASL is configured for authentication of data transfer protocol
# using non-privileged ports.
export HADOOP_SECURE_DN_USER=${HADOOP_SECURE_DN_USER}

# Where log files are stored.  $HADOOP_HOME/logs by default.
#export HADOOP_LOG_DIR=${HADOOP_LOG_DIR}/$USER

# Where log files are stored in the secure data environment.
export HADOOP_SECURE_DN_LOG_DIR=${HADOOP_LOG_DIR}/${HADOOP_HDFS_USER}

###
# HDFS Mover specific parameters
###
# Specify the JVM options to be used when starting the HDFS Mover.
# These options will be appended to the options specified as HADOOP_OPTS
# and therefore may override any similar flags set in HADOOP_OPTS
#
# export HADOOP_MOVER_OPTS=""

###
# Advanced Users Only!
###

# The directory where pid files are stored. /tmp by default.
# NOTE: this should be set to a directory that can only be written to by 
#       the user that will run the hadoop daemons.  Otherwise there is the
#       potential for a symlink attack.
export HADOOP_PID_DIR=/home/hadoop/hadoop-2.7.2/pids
export HADOOP_SECURE_DN_PID_DIR=${HADOOP_PID_DIR}

# A string representing this instance of hadoop. $USER by default.
export HADOOP_IDENT_STRING=$USER
'''

cd /home/hadoop/hadoop-2.7.2/share/hadoop/mapreduce
# map: 분석하기 위해 서버에 흩어버리도록 하는 기능
# reduce: 흩어져 있는 것을 조합하는 기능
#map: wordcount를 셀 때 서버가 두개이면 1000페이지를 1-500페이지 / 501-1000페이지를 각각 서버에 나눠 흩어버림
#reduce: 분석후 모으는 작업을 함 
'''[hadoop@dataserver ~]$ cd /home/hadoop/hadoop-2.7.2/share/hadoop/mapreduce
'''



ls
#확인하기
'''[hadoop@dataserver mapreduce]$ ls
hadoop-mapreduce-client-app-2.7.2.jar
hadoop-mapreduce-client-common-2.7.2.jar
hadoop-mapreduce-client-core-2.7.2.jar
hadoop-mapreduce-client-hs-2.7.2.jar
hadoop-mapreduce-client-hs-plugins-2.7.2.jar
hadoop-mapreduce-client-jobclient-2.7.2-tests.jar
hadoop-mapreduce-client-jobclient-2.7.2.jar
hadoop-mapreduce-client-shuffle-2.7.2.jar
hadoop-mapreduce-examples-2.7.2.jar
lib
lib-examples
sources
'''
#hadoop-mapreduce-examples-2.7.2.jar: wordcount를 수행하는 java프로그램 

yarn jar hadoop-mapreduce-examples-2.7.2.jar wordcount conf output
# hadoop-mapreduce-examples-2.7.2.jar 프로그램에서 wordcount를 사용함 
# conf라는 directory안에 있는 data에 대해 wordcount한 결과를  output 이라는 디렉토리 안에 저장함
'''[hadoop@dataserver mapreduce]$ yarn jar hadoop-mapreduce-examples-2.7.2.jar wordcount conf output
18/11/21 14:56:01 INFO client.RMProxy: Connecting to ResourceManager at dataserver/192.168.56.101:8032
18/11/21 14:56:02 INFO input.FileInputFormat: Total input paths to process : 1
18/11/21 14:56:02 INFO mapreduce.JobSubmitter: number of splits:1
18/11/21 14:56:03 INFO mapreduce.JobSubmitter: Submitting tokens for job: job_1542766080985_0001
18/11/21 14:56:03 INFO impl.YarnClientImpl: Submitted application application_1542766080985_0001
18/11/21 14:56:03 INFO mapreduce.Job: The url to track the job: http://0.0.0.0:8089/proxy/application_1542766080985_0001/
18/11/21 14:56:03 INFO mapreduce.Job: Running job: job_1542766080985_0001
18/11/21 14:56:12 INFO mapreduce.Job: Job job_1542766080985_0001 running in uber mode : false
18/11/21 14:56:12 INFO mapreduce.Job:  map 0% reduce 0%
18/11/21 14:56:20 INFO mapreduce.Job:  map 100% reduce 0%
18/11/21 14:56:26 INFO mapreduce.Job:  map 100% reduce 100%
18/11/21 14:56:27 INFO mapreduce.Job: Job job_1542766080985_0001 completed successfully
18/11/21 14:56:27 INFO mapreduce.Job: Counters: 49
	File System Counters
		FILE: Number of bytes read=4535
		FILE: Number of bytes written=244603
		FILE: Number of read operations=0
		FILE: Number of large read operations=0
		FILE: Number of write operations=0
		HDFS: Number of bytes read=4359
		HDFS: Number of bytes written=3462
		HDFS: Number of read operations=6
		HDFS: Number of large read operations=0
		HDFS: Number of write operations=2
	Job Counters 
		Launched map tasks=1
		Launched reduce tasks=1
		Data-local map tasks=1
		Total time spent by all maps in occupied slots (ms)=4437
		Total time spent by all reduces in occupied slots (ms)=4197
		Total time spent by all map tasks (ms)=4437
		Total time spent by all reduce tasks (ms)=4197
		Total vcore-milliseconds taken by all map tasks=4437
		Total vcore-milliseconds taken by all reduce tasks=4197
		Total megabyte-milliseconds taken by all map tasks=4543488
		Total megabyte-milliseconds taken by all reduce tasks=4297728
	Map-Reduce Framework
		Map input records=98
		Map output records=519
		Map output bytes=6256
		Map output materialized bytes=4535
		Input split bytes=118
		Combine input records=519
		Combine output records=268
		Reduce input groups=268
		Reduce shuffle bytes=4535
		Reduce input records=268
		Reduce output records=268
		Spilled Records=536
		Shuffled Maps =1
		Failed Shuffles=0
		Merged Map outputs=1
		GC time elapsed (ms)=112
		CPU time spent (ms)=1230
		Physical memory (bytes) snapshot=315531264
		Virtual memory (bytes) snapshot=1717854208
		Total committed heap usage (bytes)=168497152
	Shuffle Errors
		BAD_ID=0
		CONNECTION=0
		IO_ERROR=0
		WRONG_LENGTH=0
		WRONG_MAP=0
		WRONG_REDUCE=0
	File Input Format Counters 
		Bytes Read=4241
	File Output Format Counters 
		Bytes Written=3462
'''

hdfs dfs -ls output
'''[hadoop@dataserver mapreduce]$ hdfs dfs -ls output
Found 2 items
-rw-r--r--   1 hadoop supergroup          0 2018-11-21 14:56 output/_SUCCESS
-rw-r--r--   1 hadoop supergroup       3462 2018-11-21 14:56 output/part-r-00000
'''

hdfs dfs -ls -R
'''[hadoop@dataserver mapreduce]$ hdfs dfs -ls -R
drwxr-xr-x   - hadoop supergroup          0 2018-11-21 14:45 conf
-rw-r--r--   1 hadoop supergroup       4241 2018-11-21 14:45 conf/hadoop-env.sh
drwxr-xr-x   - hadoop supergroup          0 2018-11-21 14:56 output
-rw-r--r--   1 hadoop supergroup          0 2018-11-21 14:56 output/_SUCCESS
-rw-r--r--   1 hadoop supergroup       3462 2018-11-21 14:56 output/part-r-00000
'''
#d가 없으면 directory가 아니라 file을 뜻함 



# =============================================================================
#  다시 확인할 때 선생님 순서 ctrl+1누르고 
# =============================================================================
#[hadoop@dataserver ~]$ hdfs dfs -ls /
#Found 1 items
#drwxrwx---   - hadoop supergroup          0 2018-11-21 15:49 /tmp
#[hadoop@dataserver ~]$ hdfs dfs -mkdir /user
#[hadoop@dataserver ~]$ hdfs dfs -mkdir /user/hadoop
#[hadoop@dataserver ~]$ hdfs dfs -mkdir /user/hadoop/conf
#[hadoop@dataserver ~]$ hdfs dfs -ls -R /
#drwxrwx---   - hadoop supergroup          0 2018-11-21 15:49 /tmp
#drwxrwx---   - hadoop supergroup          0 2018-11-21 15:49 /tmp/hadoop-yarn
#drwxrwx---   - hadoop supergroup          0 2018-11-21 15:49 /tmp/hadoop-yarn/staging
#drwxrwx---   - hadoop supergroup          0 2018-11-21 15:49 /tmp/hadoop-yarn/staging/history
#drwxrwx---   - hadoop supergroup          0 2018-11-21 15:49 /tmp/hadoop-yarn/staging/history/done
#drwxrwxrwt   - hadoop supergroup          0 2018-11-21 15:49 /tmp/hadoop-yarn/staging/history/done_intermediate
#drwxr-xr-x   - hadoop supergroup          0 2018-11-21 15:51 /user
#drwxr-xr-x   - hadoop supergroup          0 2018-11-21 15:51 /user/hadoop
#drwxr-xr-x   - hadoop supergroup          0 2018-11-21 15:51 /user/hadoop/conf
#[hadoop@dataserver ~]$ hdfs dfs -put /home/hadoop/hadoop-2.7.2/etc/hadoop/hadoop-env.sh conf/
#18/11/21 15:51:48 WARN hdfs.DFSClient: DataStreamer Exception
#org.apache.hadoop.ipc.RemoteException(java.io.IOException): File /user/hadoop/conf/hadoop-env.sh._COPYING_ could only be replicated to 0 nodes instead of minReplication (=1).  There are 0 datanode(s) running and no node(s) are excluded in this operation.
#	at org.apache.hadoop.hdfs.server.blockmanagement.BlockManager.chooseTarget4NewBlock(BlockManager.java:1547)
#	at org.apache.hadoop.hdfs.server.namenode.FSNamesystem.getNewBlockTargets(FSNamesystem.java:3107)
#	at org.apache.hadoop.hdfs.server.namenode.FSNamesystem.getAdditionalBlock(FSNamesystem.java:3031)
#	at org.apache.hadoop.hdfs.server.namenode.NameNodeRpcServer.addBlock(NameNodeRpcServer.java:724)
#	at org.apache.hadoop.hdfs.protocolPB.ClientNamenodeProtocolServerSideTranslatorPB.addBlock(ClientNamenodeProtocolServerSideTranslatorPB.java:492)
#	at org.apache.hadoop.hdfs.protocol.proto.ClientNamenodeProtocolProtos$ClientNamenodeProtocol$2.callBlockingMethod(ClientNamenodeProtocolProtos.java)
#	at org.apache.hadoop.ipc.ProtobufRpcEngine$Server$ProtoBufRpcInvoker.call(ProtobufRpcEngine.java:616)
#	at org.apache.hadoop.ipc.RPC$Server.call(RPC.java:969)
#	at org.apache.hadoop.ipc.Server$Handler$1.run(Server.java:2049)
#	at org.apache.hadoop.ipc.Server$Handler$1.run(Server.java:2045)
#	at java.security.AccessController.doPrivileged(Native Method)
#	at javax.security.auth.Subject.doAs(Subject.java:415)
#	at org.apache.hadoop.security.UserGroupInformation.doAs(UserGroupInformation.java:1657)
#	at org.apache.hadoop.ipc.Server$Handler.run(Server.java:2043)
#
#	at org.apache.hadoop.ipc.Client.call(Client.java:1475)
#	at org.apache.hadoop.ipc.Client.call(Client.java:1412)
#	at org.apache.hadoop.ipc.ProtobufRpcEngine$Invoker.invoke(ProtobufRpcEngine.java:229)
#	at com.sun.proxy.$Proxy9.addBlock(Unknown Source)
#	at org.apache.hadoop.hdfs.protocolPB.ClientNamenodeProtocolTranslatorPB.addBlock(ClientNamenodeProtocolTranslatorPB.java:418)
#	at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
#	at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:57)
#	at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
#	at java.lang.reflect.Method.invoke(Method.java:606)
#	at org.apache.hadoop.io.retry.RetryInvocationHandler.invokeMethod(RetryInvocationHandler.java:191)
#	at org.apache.hadoop.io.retry.RetryInvocationHandler.invoke(RetryInvocationHandler.java:102)
#	at com.sun.proxy.$Proxy10.addBlock(Unknown Source)
#	at org.apache.hadoop.hdfs.DFSOutputStream$DataStreamer.locateFollowingBlock(DFSOutputStream.java:1459)
#	at org.apache.hadoop.hdfs.DFSOutputStream$DataStreamer.nextBlockOutputStream(DFSOutputStream.java:1255)
#	at org.apache.hadoop.hdfs.DFSOutputStream$DataStreamer.run(DFSOutputStream.java:449)
#put: File /user/hadoop/conf/hadoop-env.sh._COPYING_ could only be replicated to 0 nodes instead of minReplication (=1).  There are 0 datanode(s) running and no node(s) are excluded in this operation.
#[hadoop@dataserver ~]$ hdfs dfs -ls conf/
#cat: `conf/haddop-env.sh': No such file or directory
#
#[hadoop@dataserver ~]$ cd /home/hadoop/hadoop-2.7.2/share/hadoop/mapreduce
#
#[hadoop@dataserver ~]$ yarn jar hadoop-mapreduce-examples-2.7.2.jar wordcount conf output
#
#

# =============================================================================
# 
# =============================================================================

hdfs dfs -ls output

hdfs dfs -cat output/part-r-00000 | tail -10

hdfs dfs -get output/part-r-00000 /home/wc_output
#get: get생성
#home디렉토리 안에 hadoop이라는 디렉토리안에 wc_output으로 생성
#part-r-00000 은 output안에 있는 것으로 맞춰야하기 때문에 변할 수 있다.

cd /home/hadoop/wc_output
ls
# 파일 생성 

cat /home/hadoop/wc_output


# =============================================================================
# 
# =============================================================================
공유폴더에 파일을 넣고
put 하둡에 파일을 올리고
wordcount를 세고 
get 하기 

